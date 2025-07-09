# Todo API

A RESTful API for task management built with FastAPI, SQLAlchemy, and MySQL. This application provides user authentication and CRUD operations for managing personal tasks.

## Features

- User registration and authentication with JWT tokens
- Task creation, reading, updating, and deletion
- Filter tasks by completion status (completed/pending)
- User-specific task management
- Password hashing with bcrypt
- Database ORM with SQLAlchemy
- Input validation with Pydantic

## Tech Stack

- **Framework**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt
- **Validation**: Pydantic
- **Server**: Uvicorn

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/FrankSkep/todo-api
cd todo-api
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory with the following variables:

    ```env
    DATABASE_URL=mysql://username:password@localhost/database_name
    SECRET_KEY=your_secret_key_here
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5. **Set up the database**
   
   Make sure you have MySQL installed and running, then create a database for the project.

## Running the Application

1. **Start the server**
    ```bash
    python main.py
    ```

2. **Access the API**
   - Server will run on: `http://127.0.0.1:8070`
   - Interactive API documentation: `http://127.0.0.1:8070/docs`
   - Alternative documentation: `http://127.0.0.1:8070/redoc`

## API Documentation

The API provides comprehensive documentation through FastAPI's automatic documentation generation:

- **Swagger UI**: Available at `/docs` endpoint