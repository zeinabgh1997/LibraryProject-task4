from django.shortcuts import render , get_object_or_404 , redirect
# from .sample_data import books, members, borrowings
from datetime import date
from .models import Book,Member,Borrowing
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    query = request.GET.get("q","").strip()
    books = Book.objects.all()
    members=Member.objects.all()
    if query: 
        books=books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
            )
     

    return render(request, "library/book_list.html", {"books": books , "members": members })

def member_list(request):
    query = request.GET.get("q","").strip()
    members = Member.objects.all()
    if query:
        members=members.filter(
            name__icontains=query
        )
    return render(request, "library/member_list.html", {"members": members})


def add_book(request):
    if request.method == "POST":         
        Book.objects.create(             
            title= request.POST["title"],             
            author= request.POST["author"],             
            year= request.POST["year"],        
            )        
        return redirect ("book_list")     
    return render (request ,"library/book_list.html")

def add_member(request):
    if request.method=="POST":
        Member.objects.create(
            name= request.POST["name"],
            email=request.POST["email"],
        )
        return redirect("member_list")
    return render(request,"library/member_list.html")

def book_edit(request,book_id):
    book=get_object_or_404(Book,id=book_id )
    if request.method == "POST":
        book.title= request.POST["title"]
        book.author= request.POST["author"]
        book.year= request.POST["year"]
        book.save()
        return redirect ("book_list" ) 
    return render (request ,"library/book_list.html" , {"book": book})

def book_delete(request,book_id):
    book= get_object_or_404(Book,id=book_id)
    if request.method =="POST":
        book.delete()
        return redirect ("book_list") 
    return render (request ,"library/book_list.html" , {"book": book})


# #borrow_book
def borrow_book(request, book_id, member_id):
    book=get_object_or_404(Book, id=book_id)
    member=get_object_or_404(Member , id=member_id)
    if request.method=="POST":
        if book.available== True:
            book.available= False
            book.borrow_count +=1
            book.save()
            Borrowing.objects.create(
                book=book,
                member=member ,
                borrowed_at= date.today()   
                )   
    return redirect("book_list")           

#return book
def return_book(request,book_id):
    borrowing = Borrowing.objects.filter(
    book_id=book_id,
    returned_at__isnull=True
).order_by("-borrowed_at").first()

    if borrowing:
        borrowing.returned_at = date.today()
        borrowing.save()

        borrowing.book.available = True
        borrowing.book.save()

    return redirect("book_list")


       
  

#history 
def member_history(request, member_id):
    member=get_object_or_404(Member, id=member_id)

    history =member.borrowings.all()
    active =member.borrowings.filter(returned_at__isnull=True)
    returned= member.borrowings.filter(returned_at__isnull=False)

    return render(request, "library/history.html", {
        "member": member,
        "history":history,
        "active":active,
        "returned":returned,
        
    })        


def all_history(request):
    current_borrowings = Borrowing.objects.filter(returned_at__isnull=True)
    return_borrowings = Borrowing.objects.filter(returned_at__isnull=False)
    books = Book.objects.all()
    members = Member.objects.all()

    return render(request, "library/all_history.html", {
        "current_borrowings": current_borrowings,
        "return_borrowings": return_borrowings,
        "books": books,
        "members": members,
    })

# Create statistics
def statistics(request):
    total_books= Book.objects.count()
    available_books = Book.objects.filter(available=True).count() 
    borrowed_books = Book.objects.filter(available=False).count()

    most_popular = Book.objects.order_by("-borrow_count").first()
    total_members= Member.objects.count()   

    return render(request, "library/statistics.html", {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "total_members":total_members,
        "most_popular": most_popular,
    })

