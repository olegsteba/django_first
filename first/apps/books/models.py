from django.contrib import admin
from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.ManyToManyField(
        "Author",
        related_name="books",
        verbose_name="Авторы",
    )
    description = models.TextField(verbose_name="Описане книги")
    id_publishing_house = models.ForeignKey(
        "PublishingHouse",
        on_delete=models.CASCADE,
        related_name="publishing_house_books",
        verbose_name="ID издательства",
        null=True,
        blank=True,
    )
    date_creation = models.DateField(verbose_name="Дата написания книги")
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_deletes = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class PublishingHouse(models.Model):
    publishing_house_name = models.CharField(max_length=300, verbose_name="Название издательства")
    address = models.CharField(max_length=1500, verbose_name="Адресс издательства")
    contact_phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    email = models.EmailField(max_length=254, verbose_name="Электронный адрес")
    website_link = models.URLField(max_length=255, verbose_name="Адрес сайта", null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_deletes = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return self.publishing_house_name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    father_name = models.CharField(max_length=100, verbose_name="Отчество", null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name="Страна")
    birthday = models.DateField(verbose_name="Дата рождения")
    language = models.JSONField(verbose_name="Языки на которыз писал автор")
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_deletes = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class BookInAuthor(admin.TabularInline):
    model = Book.author.through
