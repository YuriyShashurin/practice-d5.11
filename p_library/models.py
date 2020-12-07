from django.db import models

class Author (models.Model):
    full_name = models.CharField(max_length=200)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    title = models.TextField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.title

#Создаем модель друга
class Friend(models.Model):
    full_name = models.TextField()


    def __str__(self):
        return self.full_name



class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # добавляем книге поле ManyToManyField, определяем промежуточную таблицу DebtBooks
    friends = models.ManyToManyField(
        Friend,
        through='DebtBooks'
    )

    def __str__(self):
        return self.title

#промежуточная таблица DebtBooks
class DebtBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, verbose_name='Друг')
    book_count = models.SmallIntegerField(default=0, verbose_name='Количество книг')

    def __str__(self):
        return '{} одолжил книгу {} в количестве {} штук'.format(self.friend, self.book, self.book_count)

