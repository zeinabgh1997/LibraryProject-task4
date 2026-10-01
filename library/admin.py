from django.contrib import admin
from .models import Book,Member, Borrowing
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author","year","available","borrow_count")
    search_fields=("title", "author")
    list_filter=("available", "year")
    list_editable=("available",)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields=("name", )

@admin.register(Borrowing)    
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("book", "member","borrowed_at","returned_at")
    search_fields=("book__title", "member__name" )
    list_filter=("borrowed_at", "returned_at")

