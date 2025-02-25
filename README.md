# Orchestro Intelligence
## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
  - [Core Components](#core-components)
- [Project Structure](#project-structure)
 - [Project Components Explained](#project-components-explained)
   - [Service Structure](#service-structure)
 - [Key Directories](#key-directories)
 - [Code Organization Principles](#code-organization-principles)
- [Technical Stack](#technical-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Development](#development)
 - [Single Executable Mode](#single-executable-mode)
 - [Microservices Mode](#microservices-mode)
- [Testing](#testing)
- [Deployment](#deployment)
 - [Docker Deployment](#docker-deployment)
- [API Documentation](#api-documentation)
 - [Sample Request](#sample-request)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview
Orchestro Intelligence is a modern logistics and supply chain management platform providing comprehensive solutions for shipment management, quotes calculation, tracking, and business operations. The platform supports both microservices and monolithic deployments.

## Architecture
The platform is built using a microservices architecture with the following key components:
  
### Core Components
- **Shipment Service**: Quote calculations and tracking
- **Pre-onboarding Service**: Pre-sales and PLD management
- **Onboarding Service**: Member and account management
- **Settlement Service**: Invoice and billing
- **Operations Service**: Analytics and reporting

## Project Structure

```
app-services-parent/
├── infinity/                        # Infinity service
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── content/        # Content feature
│   │   │       │   ├── controllers/
│   │   │       │   ├── models/
│   │   │       │   │   ├── request/
│   │   │       │   │   ├── response/
│   │   │       │   │   └── entities/
│   │   │       │   └── services/
│   │   │       └── tools/         # Tools feature
│   │   └── main.py
│   ├── env/
│   ├── requirements/
│   └── tests/
│       ├── conftest.py
│       ├── content/
│       │   ├── test_controllers/
│       │   ├── test_models/
│       │   └── test_services/
│       └── tools/
│           ├── test_controllers/
│           ├── test_models/
│           └── test_services/
│
├── pre_onboarding/                 # Pre-onboarding service
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── pre_sales/     # Pre-sales feature
│   │   │       │   ├── controllers/
│   │   │       │   ├── models/
│   │   │       │   └── services/
│   │   │       └── pld/           # PLD feature
│   │   └── main.py
│   ├── env/
│   ├── requirements/
│   └── tests/
│       ├── conftest.py
│       ├── pre_sales/
│       │   ├── test_controllers/
│       │   ├── test_models/
│       │   └── test_services/
│       └── pld/
│           ├── test_controllers/
│           ├── test_models/
│           └── test_services/
│
├── onboarding/                     # Onboarding service
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── member/        # Member feature
│   │   │       ├── account/       # Account feature
│   │   │       └── network/       # Network feature
│   │   └── main.py
│   ├── env/
│   ├── requirements/
│   └── tests/
│       ├── conftest.py
│       ├── member/
│       ├── account/
│       └── network/
│
├── settlement/                     # Settlement service
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── invoice/       # Invoice feature
│   │   │       ├── billing/       # Billing feature
│   │   │       └── tax/           # Tax feature
│   │   └── main.py
│   ├── env/
│   ├── requirements/
│   └── tests/
│       ├── conftest.py
│       ├── invoice/
│       ├── billing/
│       └── tax/
│
└── operations/                     # Operations service
    ├── app/
    │   ├── api/
    │   │   └── v1/
    │   │       ├── analytics/     # Analytics feature
    │   │       │   ├── controllers/
    │   │       │   ├── models/
    │   │       │   └── services/
    │   │       ├── feedback/      # Feedback feature
    │   │       └── reporting/     # Reporting feature
    │   └── main.py
    ├── env/
    ├── requirements/
    └── tests/
        ├── conftest.py
        ├── analytics/
        │   ├── test_controllers/
        │   ├── test_models/
        │   └── test_services/
        ├── feedback/
        └── reporting/

```

### Project Components Explained

#### Service Structure

```
service/
├── app/                      # Service application code
│   ├── api/                  # API layer
│   │   └── v1/              # API version
│   │       └── feature/     # Feature module (e.g., quote, analytics)
│   │           ├── controllers/  # Request handlers & routing
│   │           ├── models/       # Data models & validation
│   │           │   ├── request/  # Request DTOs 
│   │           │   ├── response/ # Response DTOs
│   │           │   └── entities/ # Domain entities
│   │           └── services/     # Business logic & operations
│   └── main.py              # Service entry point & configuration
├── env/                     # Environment configurations
│   ├── .env.dev            # Development settings
│   ├── .env.stage          # Staging settings  
│   └── .env.prod           # Production settings
├── requirements/            # Dependencies
│   ├── requirements.txt    # Production dependencies
│   └── requirements-dev.txt # Development dependencies
└── tests/                  # Service test suite
    ├── conftest.py         # Test fixtures & configuration
    └── feature/            # Feature-specific tests
        ├── test_controllers/ # API endpoint tests
        ├── test_models/     # Data model tests
        └── test_services/   # Business logic tests

```

### Key Directories
- **app/**: Monolithic application code and entry point
- **app-services-parent/**: Individual microservices, each self-contained
- **agents/**: Shared AI functionality and service-specific agents
- **common/**: Shared utilities and configurations
- **docker/**: Container configurations for both deployment modes
- **env/**: Environment configuration files
- **requirements/**: Dependency management

### Code Organization Principles
1. **Feature-based Structure**: Each feature (e.g., quote) has its own complete MVC structure
2. **Clear Separation**: Models, controllers, and services are separated
3. **Consistent Patterns**: Same structure across all services
4. **Independence**: Services can run individually or as part of the monolith
5. **Shared Resources**: Common code in agents/ and common/ directories

## Technical Stack
- **Framework**: FastAPI (Python 3.8+)
- **Database**: PostgreSQL
- **AgentsFramework**: Langgraph
- **VectorDB**: Chroma for short-term persistence, PG Vector for long-term persistence
- **Cache**: Redis
- **Containerization**: Docker
- **Testing**: pytest
- **Dependencies**: See requirements.txt

## Prerequisites
- Python 3.8+
- Docker and Docker Compose
- PostgreSQL
- Redis

## Installation
```bash
# Clone repository
git clone https://github.com/your-org/orchestro-intelligence.git
cd orchestro-intelligence

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements/requirements.txt
```

## Development
### Monolith Mode
In monolith mode, all services run as a single application on port 8080.
```bash
cd opn-intelligence

# Development environment
uvicorn app.main:app --reload --port 8080 --env-file env/.env.dev

# Staging environment
uvicorn app.main:app --reload --port 8080 --env-file env/.env.stage

# Production environment
uvicorn app.main:app --reload --port 8080 --env-file env/.env.prod

# Test endpoints
# Main health check
curl http://127.0.0.1:8080/api/v1/health

# Individual service health checks
curl http://127.0.0.1:8080/api/v1/shipment/health
curl http://127.0.0.1:8080/api/v1/onboarding/health
curl http://127.0.0.1:8080/api/v1/settlement/health
curl http://127.0.0.1:8080/api/v1/operations/health
curl http://127.0.0.1:8080/api/v1/pre_onboarding/health
curl http://127.0.0.1:8080/api/v1/infinity/health
```
### Microservice Mode
Each service runs independently and can be deployed on different ports.

```bash
# Deploy individual services with environments
# Shipment Service (Port 8001)
cd app-services-parent/shipment
pip install -r requirements/requirements.txt
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8001 --env-file env/.env.dev  # Development
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8001 --env-file env/.env.stage  # Staging
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8001 --env-file env/.env.prod  # Production

# Onboarding Service (Port 8002)
cd app-services-parent/onboarding
pip install -r requirements/requirements.txt
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8002 --env-file env/.env.dev

# Settlement Service (Port 8003)
cd app-services-parent/settlement
pip install -r requirements/requirements.txt
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8003 --env-file env/.env.dev

# Operations Service (Port 8004)
cd app-services-parent/operations
pip install -r requirements/requirements.txt
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8004 --env-file env/.env.dev

# Pre-onboarding Service (Port 8005)
cd app-services-parent/pre_onboarding
pip install -r requirements/requirements.txt
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8005 --env-file env/.env.dev

# Infinity Service (Port 8006)
cd app-services-parent/infinity
pip install -r requirements/requirements.txt
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 8006 --env-file env/.env.dev

# Test endpoints
# Shipment Service
curl http://127.0.0.1:8001/api/v1/shipment/health

# Onboarding Service
curl http://127.0.0.1:8002/api/v1/onboarding/health

# Settlement Service
curl http://127.0.0.1:8003/api/v1/settlement/health

# Operations Service
curl http://127.0.0.1:8004/api/v1/operations/health

# Pre-onboarding Service
curl http://127.0.0.1:8005/api/v1/pre_onboarding/health

# Infinity Service
curl http://127.0.0.1:8006/api/v1/infinity/health
```

### Port Override
Override default ports by modifying the uvicorn --port argument:

```bash
# Example: Running shipment service on port 9001
DEPLOYMENT_MODE=microservice uvicorn app.main:app --reload --port 9001 --env-file env/.env.dev

# Test the overridden port
curl http://127.0.0.1:9001/api/v1/shipment/health
```
## Testing
### Monolithic Tests (Root Level)
```bash
cd opn-intelligence

# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run coverage report
pytest --cov=app --cov-report=html

# Run specific service tests from monolith
pytest app-services-parent/shipment/tests/
pytest app-services-parent/operations/tests/

# Run environment-specific tests
pytest --env-file env/.env.dev
pytest --env-file env/.env.stage
```

### Microservice Tests
```bash
# Navigate to specific service
cd app-services-parent/shipment

# Run all service tests
pytest

# Run with coverage for service
pytest --cov=app

# Generate HTML coverage report
pytest --cov=app --cov-report=html

# Run specific feature tests
pytest tests/quote/
pytest tests/quote/test_controllers/
pytest tests/quote/test_services/

# Run environment-specific tests
pytest --env-file env/.env.dev
pytest --env-file env/.env.stage

# Run with test marks
pytest -m "unit"
pytest -m "integration"
```
### Common Test Options
```bash
# Run tests with output
pytest -v

# Run tests with print statements
pytest -s

# Run specific test file
pytest tests/quote/test_controllers/test_quote_controller.py

# Run specific test function
pytest tests/quote/test_controllers/test_quote_controller.py::test_calculate_quote_success

# Run tests in parallel
pytest -n auto

# Run tests with log output
pytest --log-cli-level=INFO
```

## Deployment
### Docker Deployment
```bash
# Monolithic
docker-compose -f docker/docker-compose.monolith.yml up

# Microservices
docker-compose up
```
### Service URLs
- Monolithic Service: `http://localhost:8000`
- Shipment Service: `http://localhost:8001`
- Pre-onboarding Service: `http://localhost:8002`
- Onboarding Service: `http://localhost:8003`
- Settlement Service: `http://localhost:8004`
- Operations Service: `http://localhost:8005`

### Environment Configuration
Different environments are supported through environment files:
- Development: `.env.dev`
- Staging: `.env.stage`
- Production: `.env.prod`
  
## API Documentation
Access Swagger documentation at:
- Monolithic: `http://localhost:8000/docs`
- Individual Services: `http://localhost:8001/docs`

### Sample Request
```bash
curl -X POST "http://localhost:8001/api/v1/shipment/quote/calculate" \
-H "Content-Type: application/json" \
-d '{
    "origin": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "country": "USA",
        "postal_code": "10001"
    },
    "destination": {
        "street": "456 Market St",
        "city": "Los Angeles",
        "state": "CA",
        "country": "USA",
        "postal_code": "90007"
    },
    "packages": [
        {
            "weight": 10.5,
            "length": 20.0,
            "width": 15.0,
            "height": 12.0,
            "description": "Electronics"
        }
    ],
    "service_level": "express"
}'
```

## Troubleshooting
Common issues and solutions:
- Port conflicts: Check and kill processes using required ports
- Database connection: Verify PostgreSQL service and credentials
- Environment variables: Ensure proper .env file configuration

## Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License
Refer to project LICENCE file for details.

## Support
- Email: support@orchestro.ai
- Documentation: `/docs`
