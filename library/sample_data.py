
books=[
    {
        "id": 1,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K.Rowling",
        "year": 1997,
        "available": True ,
        "borrow_count": 2
    },
    {
        "id":2,
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K.Rowling",
        "year": 1999,
        "available": True ,
        "borrow_count": 5
        
    },
    {
        "id":3,
        "title": "Harry Potter and the Prisoner of Azkaban",
        "author": "J.K.Rowling",
        "year": 1999,
        "available": False ,
        "borrow_count": 5
    },
    {
        "id":4,
        "title": "Harry Potter and the Golbet of Fire",
        "author": "J.K.Rowling",
        "year":2000,
        "available": True ,
        "borrow_count": 8
    },
    {
        "id":5,
        "title": "Harry Potter and the Order of the Phoenix",
        "author": "J.K.Rowling",
        "year":2003 ,
        "available": True ,
        "borrow_count": 1   
        
    }
    ,
    {
        "id":6,
        "title": "Harry Potter and the Half-Blood Prince",
        "author": "J.K.Rowling",
        "year":2005 ,
        "available": True ,
        "borrow_count": 7   
            
    } ,
    {
        "id":7,
        "title": "Harry Potter and the Deathly Hallows",
        "author": "J.K.Rowling",
        "year":2007  ,
        "available": False ,
        "borrow_count": 3           
    },
    {
       "id":8,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year":1813,
        "available": True ,
        "borrow_count": 5
    },
    {
       "id":9,
       "title": "The Alchemist",
       "author" : "Paulo coelho" ,
       "year": 1988,
       "available": True ,
       "borrow_count": 0
    },
    {
       "id":10,
       "title":"1984",
       "author":"George Orwell",
       "year":1949,
       "available": True ,
       "borrow_count": 6
    }
]

members = [
        {
            "id": 1,
            "name": "Ali",
            "email": "ali@example.com"
        },
        {
            "id": 2,
            "name": "Sara",
            "email": "sara@example.com"
        },
        {
            "id": 3,
            "name": "Reza",
            "email": "reza@example.com"
        },
        {
            "id": 4,
            "name": "Zeinab",
            "email": "zeinab@example.com"
        },
        {
            "id": 5,
            "name": "Ahmad",
            "email": "ahmad@example.com"
        }
    ]

borrowings = [
    {
        "book_id": 3,
        "member_id": 1,
        "borrowed_at": "2026-09-05",
        "returned_at": None
    },
    {
        "book_id": 1,
        "member_id": 2,
        "borrowed_at": "2026-09-10",
        "returned_at": "2026-09-15"
    },
    {
        "book_id": 2,
        "member_id": 3,
        "borrowed_at": "2026-09-12",
        "returned_at": None
    },
    
]
