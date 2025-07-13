# FastAPI Boilerplate

A modern and well-structured boilerplate for rapidly developing robust APIs with FastAPI.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 🚀 Features

- Modular and scalable architecture
- PostgreSQL integration with SQLAlchemy ORM
- Data validation with Pydantic
- Automatic API documentation with Swagger/OpenAPI
- Containerization with Docker and Docker Compose
- Configuration management via environment variables
- Ready-to-use CRUD structure
- Custom error handling

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose (recommended)
- PostgreSQL (if running locally without Docker)

## 🛠️ Installation

### With Docker (recommended)

1. Clone this repository

   ```bash
   git clone https://github.com/yourusername/fastapi-boilerplate.git
   cd fastapi-boilerplate
   ```

2. Create a `.env` file in the project root

   ```bash
   cp .env.example .env
   ```

   Then modify the variables according to your configuration.

3. Launch the application with Docker Compose

   ```bash
   docker-compose up -d
   ```

4. The API is accessible at http://localhost:8000
   - Swagger documentation: http://localhost:8000/docs
   - ReDoc documentation: http://localhost:8000/redoc

### Without Docker (local development)

1. Clone this repository

   ```bash
   git clone https://github.com/yourusername/fastapi-boilerplate.git
   cd fastapi-boilerplate
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root

   ```bash
   cp .env.example .env
   ```

   Then modify the variables according to your configuration.

5. Initialize the database

   ```bash
   python -m scripts.init_db
   ```

6. Launch the application
   ```bash
   uvicorn main:app --reload
   ```

## 📁 Project Structure

```
fastapi-boilerplate/
├── core/                   # Core application
│   ├── crud/               # CRUD operations
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── database.py         # Database configuration
│   ├── exceptions.py       # Custom exceptions
│   ├── security.py         # Security features
│   └── settings.py         # Application configuration
├── scripts/                # Utility scripts
│   └── init_db.py          # Database initialization
├── tests/                  # Unit and integration tests
├── v1/                     # API version 1
│   ├── endpoints/          # API endpoints
│   └── api.py              # Main API v1 router
├── docker-compose.yml      # Docker Compose configuration
├── dockerfile              # Docker configuration
├── main.py                 # Application entry point
└── requirements.txt        # Python dependencies
```

## 🔄 API Endpoints

### Users

- `GET /v1/users/` - Retrieve all users
- `GET /v1/users/{user_id}` - Retrieve a user by ID
- `POST /v1/users/?user_name=string` - Create a new user
- `DELETE /v1/users/{user_id}` - Delete a user

## 🧩 Extending the Boilerplate

### Adding a New Model

1. Create a new model file in `core/models/`
2. Create a corresponding schema in `core/schemas/`
3. Implement CRUD operations in `core/crud/`
4. Create a new router in `v1/endpoints/`
5. Include the router in `v1/api.py`

## 🔒 Security

To implement authentication and authorization:

1. Complete the `core/security.py` file with authentication logic
2. Create models and schemas for tokens and authenticated users
3. Implement authentication endpoints
4. Use FastAPI dependencies to protect routes

## 🧪 Tests

Run tests with pytest:

```bash
pytest
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
