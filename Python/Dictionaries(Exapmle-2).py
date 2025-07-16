Library =[
    {
        "book_name": "IKIGAI",
        "book_cost": "$10",
        "book_author": "XYZ",
        "book_pages": "200"
    },
    {
        "book_name": "SAPIENS",
        "book_cost": "$8",
        "book_author": "ABC",
        "book_pages": "150"
    },
    {
        "book_name": "RICH DAD,POOR DAD",
        "book_cost": "$12",
        "book_author": "DEF",
        "book_pages": "190"
    },
    {
        "book_name": "MONEY",
        "book_cost": "$15",
        "book_author": "AAA",
        "book_pages": "300"
    }
]
for Book in Library:
    print(Book["book_name"])
    print(Book["book_cost"])
    print(Book["book_author"])
    print(Book["book_pages"])
    print("__________________")