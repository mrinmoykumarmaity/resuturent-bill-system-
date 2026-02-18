# Hotel Billing / Restaurant System

This is a simple restaurant billing application with both command‑line and web interfaces.

## Features

- **Menu management** with ability to add/remove items (code extensible).
- **Order object** tracks items and quantities, computes subtotal/total, applies simple discount rules and prints receipts.
- **Command‑line interface** for taking orders interactively.
- **Flask web interface** with menu display, cart, and checkout.

## Getting Started

### Prerequisites

```bash
python -m venv venv        # or use your preferred env
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### CLI

```bash
python hotel_billing_application.py
```

### Web

Start the Flask application by running the package as a module from the project root:

```bash
# from project/ directory
venv\\Scripts\\activate  # if you created a venv
python -m restaurant.app
# open http://127.0.0.1:5000 in your browser
```

## Structure

```
project/
├─ hotel_billing_application.py  # CLI entry point
├─ requirements.txt
├─ README.md
└─ restaurant/
   ├─ __init__.py
   ├─ menu.py
   ├─ order.py
   ├─ app.py                    # Flask app
   ├─ templates/
   │   ├─ base.html
   │   ├─ menu.html
   │   ├─ cart.html
   │   └─ checkout.html
   └─ static/                   # optional styles/resources
```

## Running Tests

```bash
pip install -r requirements.txt  # ensures pytest is available
pytest
```

## Future Improvements

- Persist orders to a database.
- Add user authentication.
- Enhance web layout with CSS/Bootstrap.
- Export receipts as PDF.
- Add discounts, tax calculations, inventory tracking.
