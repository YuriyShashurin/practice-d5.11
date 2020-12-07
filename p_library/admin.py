from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, DebtBooks

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'copy_count', 'publisher')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price','copy_count','publisher')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.full_name

    list_display = ('author_full_name','birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title','country')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(DebtBooks)
class DebtBooksAdmin(admin.ModelAdmin):
    pass
