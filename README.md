# Order Management System

A REST API for managing customers, products, and orders, built with Django and Django REST Framework.

## Features

- Customer profiles linked to Django's built-in auth system
- Product catalog with stock tracking
- Order creation with multiple line items and automatic total calculation
- Order status workflow: Pending → Confirmed → Shipped → Delivered / Cancelled
- Filtering and search on products and orders
- Django admin interface for internal management

## Tech Stack

- Python 3.11+
- Django 5
- Django REST Framework
- SQLite (default, dev) — swap in Postgres for production

## Project Structure

```
order-management-system/
├── manage.py
├── requirements.txt
├── orders_project/      # Django project settings & root URLs
└── orders/               # App: models, serializers, views, admin
```

## Setup & Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/order-management-system.git
cd order-management-system

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create an admin user
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` for the admin panel and `http://127.0.0.1:8000/api/` for the API root.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| GET/POST | `/api/customers/` | List / create customers |
| GET/PUT/DELETE | `/api/customers/{id}/` | Retrieve / update / delete a customer |
| GET/POST | `/api/products/` | List / create products (supports `?search=`) |
| GET/PUT/DELETE | `/api/products/{id}/` | Retrieve / update / delete a product |
| GET/POST | `/api/orders/` | List / create orders (supports `?status=`) |
| GET/PUT/DELETE | `/api/orders/{id}/` | Retrieve / update / delete an order |

## Example: Create an Order

```bash
curl -X POST http://127.0.0.1:8000/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{
        "customer": 1,
        "items": [
          {"product": 1, "quantity": 2, "unit_price": "19.99"},
          {"product": 2, "quantity": 1, "unit_price": "9.99"}
        ]
      }'
```

## Roadmap / Possible Extensions

- JWT authentication (SimpleJWT)
- Payment integration via the companion FastAPI Payment & Notification microservice
- Dockerfile + docker-compose for containerized deployment
- Automated tests (pytest-django)
- CI pipeline with GitHub Actions

## License

MIT
