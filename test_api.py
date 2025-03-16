import pytest
from fastapi.testclient import TestClient
from main import create_app
from database import Base, engine, get_db
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una aplicación de prueba
app = create_app()

# Crear un cliente de prueba
client = TestClient(app)

# Crear la base de datos de prueba
Base.metadata.create_all(bind=engine)

# Dependencia de prueba para obtener la base de datos
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Prueba para crear una tarea
def test_create_task():
    response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "This is a test task"
    assert response.json()["done"] == False

# Prueba para obtener todas las tareas
def test_get_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Prueba para obtener una tarea por ID
def test_get_task():
    # Crear una tarea primero
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    task_id = create_response.json()["id"]

    # Obtener la tarea por ID
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

# Prueba para actualizar una tarea
def test_update_task():
    # Crear una tarea primero
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    task_id = create_response.json()["id"]

    # Actualizar la tarea
    update_response = client.put(
        f"/api/tasks/{task_id}",
        json={"title": "Updated Task", "description": "This is an updated test task", "done": True},
    )
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Task"
    assert update_response.json()["description"] == "This is an updated test task"
    assert update_response.json()["done"] == True

# Prueba para eliminar una tarea
def test_delete_task():
    # Crear una tarea primero
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    task_id = create_response.json()["id"]

    # Eliminar la tarea
    delete_response = client.delete(f"/api/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == task_id

    # Verificar que la tarea ha sido eliminada
    get_response = client.get(f"/api/tasks/{task_id}")
    assert get_response.status_code == 404