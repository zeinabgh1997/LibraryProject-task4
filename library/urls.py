from library import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:book_id>/delete/", views.book_delete, name="book_delete"),
    path("books/<int:book_id>/borrow/<int:member_id>/", views.borrow_book, name="borrow_book"),
    path("books/<int:book_id>/return/", views.return_book, name="return_book"),
    # path("books/<int:pk>/" , views.find_book , name="find_book"),
    path("members/", views.member_list, name="member_list"),
    path("members/add/" , views.add_member , name="add_member"),
    path("history/", views.all_history, name="all_history"),
    path("history/<int:member_id>/", views.member_history, name="member_history"),
    # path("members/<int:pk>/" , views.find_member , name="find_member"),
    path("statistics/", views.statistics, name="statistics"),
    
 
]




