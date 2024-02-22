
def extraction(file):
    data = {
        "invoice_number": "INV-12345",
        "vendor_name": "Acme Corporation",
        "invoice_date": "2023-10-27",
        "due_date": "2023-11-10",
        "line_items": [
            {"description": "Product A", "quantity": 2, "unit_price": 10.00, "total": 20.00},
            {"description": "Service B", "quantity": 1, "unit_price": 50.00, "total": 50.00},
        ],
        "subtotal": 70.00,
        "tax": 7.00,
        "total": 77.00,
        }
        
    return data