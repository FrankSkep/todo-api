import pytest
from fastapi.testclient import TestClient
from main import create_app
from database import Base, engine, get_db
from sqlalchemy.orm import sessionmaker

# Database configuration for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a test application
app = create_app()

# Create a test client
client = TestClient(app)

# Create the test database
Base.metadata.create_all(bind=engine)

# Test dependency to get the database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Test to create a task
def test_create_task():
    response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "This is a test task"
    assert response.json()["done"] == False

# Test to get all tasks
def test_get_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test to get a task by ID
def test_get_task():
    # Create a task first
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    task_id = create_response.json()["id"]

    # Get the task by ID
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

# Test to update a task
def test_update_task():
    # Create a task first
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    task_id = create_response.json()["id"]

    # Update the task
    update_response = client.put(
        f"/api/tasks/{task_id}",
        json={"title": "Updated Task", "description": "This is an updated test task", "done": True},
    )
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Task"
    assert update_response.json()["description"] == "This is an updated test task"
    assert update_response.json()["done"] == True

# Test to delete a task
def test_delete_task():
    # Create a task first
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "This is a test task", "done": False},
    )
    task_id = create_response.json()["id"]

    # Delete the task
    delete_response = client.delete(f"/api/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == task_id

    # Verify that the task has been deleted
    get_response = client.get(f"/api/tasks/{task_id}")
    assert get_response.status_code == 404