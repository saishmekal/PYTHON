customers =[
    {
        "id": 101,
        "customer_name": "SAISH",
        "phone_number": "122-322",
        "customer_mail": "xyz@gmail.com",
        "premum_customer": True
    },
    {
        "id": 102,
        "customer_name": "ANUJ",
        "phone_number": "122-987",
        "customer_mail": "abc@gmail.com",
        "premum_customer": False
    }
]
for customer in customers:
    print(customer["id"])
    print(customer["customer_name"])
    print(customer["phone_number"])
    print(customer["customer_mail"])
    print("________________")