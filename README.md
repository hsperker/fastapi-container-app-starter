# FastAPI Container App Starter

A production-ready template for building and deploying FastAPI services in containers.

## Overview

This project provides a complete starter template for developing FastAPI applications with modern Python tooling. It's designed to help you quickly bootstrap new API services with best practices already in place.

## Features

- **FastAPI** - High-performance web framework for building APIs
- **Clean Architecture** - Organized project structure with separation of concerns
- **Type Safety** - Fully typed Python codebase with MyPy integration
- **Testing** - Pytest setup with sample unit and integration tests
- **Modern Python Tooling** - Uses [uv](https://github.com/astral-sh/uv) for faster package management and virtual environments
- **Development Mode** - Hot reloading support for rapid development
- **Production-Ready** - Container-optimized setup for deployment

## Getting Started

### Prerequisites

- Python 3.11
- [uv](https://github.com/astral-sh/uv)

### Setup

1. Clone this repository or use it as a template:
   ```bash
   git clone https://github.com/hsperker/fastapi-container-app-starter.git
   cd fastapi-container-app-starter
   ```

2. Run type checking to verify code quality:
   ```bash
   uv run mypy app tests
   ```
   
   Note: This command will automatically create a virtual environment and install the necessary dependencies.

3. Run tests to ensure everything is working properly:
   ```bash
   uv run pytest
   ```

4. Start the development server:
   ```bash
   uv run fastapi dev
   ```

## Project Structure

```
app/
├── __init__.py
├── main.py
├── api/             # API routes and schemas
├── core/            # Core business logic
└── infrastructure/  # Repositories

tests/
├── core/            # Unit tests for core functionality
└── integration/     # Integration tests
```

## API Documentation

When running the server, API documentation is automatically generated:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
