# flowit_test_app
## Getting started

* Create Python virtual env
* Activate virtual env
* Install your project requirements
* MacOS - Install pango with brew
* Linux - should have pango pre-installed
* Start server

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
brew install pango

python manage.py runserver

```

## What to do once inside

Open http://localhost:8000/

There you'll see links

### Employees
Let's you change the email of Employee no 1.
This Employee is hardcoded as the default Employee for orders.

### Products
A list of Products with editing capabilities of name and barcode.

A simple filter form with exact match.
The barcode image gets regenerated on save.

### Orders
A list of Orders.
A link to get the pdf.
A link to send an email containing the pdf to the hardcoded Employee.

A view to see the contents of an order and a simple filter form with exact match.
