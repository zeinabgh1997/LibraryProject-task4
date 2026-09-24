from django.shortcuts import render
from .sample_data import books, members, borrowings
from datetime import date
from django.shortcuts import redirect


# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    query= request.GET.get("q", "").strip().lower()
    filtered_books=books
    if query:
        filtered_books=[
           book for book in books
           if query in book["title"].lower()
           or query in book["author"].lower()      
        ]
    return render(request, "library/book_list.html", {"books": filtered_books , "query":query ,"members":members })

def member_list(request):
    return render(request, "library/member_list.html", {"members": members})

# #find a specific book
# def find_book(request,pk):
#     for item in books:
#         if pk == item["id"]:
#             return render(request,"library/book_list.html", {"books": [item]})
#     else :
#          return render(request, "library/book_list.html", {"books": []})
def find_book(book_id):
    for item in books:
        if book_id == item["id"]:
           return item
    else :
         return None


# #find a specific member
# def find_member(request,pk):
#     for item in members:
#         if pk == item["id"]:
#             return render(request,"library/member_list.html", {"members": [item]})
#     else :
#          return render(request, "library/member_list.html", {"members": []})        
def find_member(member_id):
    for item in members:
        if member_id == item["id"]:
           return item
    else :
         return None

# #borrow_book
def borrow_book(request, book_id, member_id):
    book=find_book(book_id)
    member=find_member(member_id)
    if request.method=="POST":
        if member :
            if book:
                if book["available"]== True:
                    book["available"]= False
                    book["borrow_count"] +=1
                    borrowings.append({
                        "book_id":book_id,
                        "member_id": member_id ,
                        "borrowed_at": date.today().isoformat(),
                        "returned_at":None,
                    })   
    return redirect("book_list")           

#return book
def return_book(request,book_id):
    book= find_book(book_id)
    if request.method == "POST":
        if book and book["available"]==False:
           book["available"]= True

        for item in reversed(borrowings):
            if item["book_id"] == book_id and item["returned_at"] is None:
                item["returned_at"] = date.today().isoformat()
                break
        return redirect("book_list")





#add
def add_book(request):
    if request.method == "POST":
        last_id = books[-1]["id"]
        New_id = last_id + 1 
        books.append({
            "id" : New_id,
            "title": request.POST["title"],
            "author": request.POST["author"],
            "year":int (request.POST["year"]),
            "available": True,
            "borrow_count": 0,
            })
    return redirect("book_list")    


       
  

#history 
def member_history(request, member_id):
    member=find_member(member_id)
    current_borrowings=[]
    return_borrowings=[]

    for item in borrowings:
        if item["member_id"]== member_id:
            if item["returned_at"] is None:
                current_borrowings.append(item)
            else:    
                return_borrowings.append(item)

    return render(request, "library/history.html", {
        "member": member,
        "current_borrowings":current_borrowings,
        "return_borrowings":return_borrowings,
        "books": books,
    })        


def all_history(request):
    current_borrowings = []
    return_borrowings = []

    for item in borrowings:
        if item["returned_at"] is None:
            current_borrowings.append(item)
        else:
            return_borrowings.append(item)

    return render(request, "library/all_history.html", {
        "current_borrowings": current_borrowings,
        "return_borrowings": return_borrowings,
        "books": books,
        "members": members,
    })

# Create statistics
def statistics(request):
    total_books= len(books)
    available_books = 0 
    borrowed_books = 0
    for item in books:
        if item["available"]== True:
            available_books+=1      
        else:
            borrowed_books+=1

    most_popular = max(books, key=lambda b: b["borrow_count"], default=None)        

    return render(request, "library/statistics.html", {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "total_members": len(members),
        "most_popular": most_popular,
    })

