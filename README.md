## Running Tests

Activate the virtual environment:

```bash
source backend/venv/bin/activate

Run all tests :
cd backend
pytest -v

Expected output 
======================== 6 passed ========================

```
## Features

- JWT Authentication
- Password Hashing (bcrypt)
- Role-Based Access Control (Admin/User)
- User Registration & Login
- Protected Endpoints
- PostgreSQL Database
- SQLAlchemy ORM
- Pydantic Validation
- Automated API Tests with Pytest