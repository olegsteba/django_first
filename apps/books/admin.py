from django.contrib import admin
from .models import Book, PublishingHouse, Author, BookInAuthor
"""
    list_display - какието атрибуты выводятся на экран
    list_display_links - какие атребуты будут ссылки
    search_fields - по каким поиск
    list_editable - какие поля можно изменить в таблице
    list_filter - по каким полям будет фильтрация
    fieldsets - страница с изменениями
"""


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'book_name', 'description',
        'id_publishing_house', 'date_creation',
        'date_add', 'is_deletes'
    )
    list_display_links = ('id', 'book_name')
    search_fields = ('book_name',)
    list_editable = ('is_deletes', )
    list_filter = ('id_publishing_house',)
    fieldsets = (
        (
            (None, {
                'fields': ('book_name', 'author', 'description', 'id_publishing_house', 'date_creation',)
            }),
        )
    )


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'publishing_house_name', 'address',
        'contact_phone', 'email', 'website_link',
        'date_add', 'is_deletes'
    )
    list_display_links = ('id', 'publishing_house_name')
    search_fields = ('publishing_house_name',)
    list_editable = ('is_deletes',)
    list_filter = ('address', 'is_deletes')
    fieldsets = (
        (
            (None, {
                'fields': ('publishing_house_name', 'address',)
            }),
            ('Контакты', {
                'fields': ('contact_phone', 'email', 'website_link',)
            }),
        )
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name',
        'father_name', 'country',
        'birthday', 'language',
        'date_add', 'is_deletes'
    )
    list_display_links = ('id', 'first_name',)
    search_fields = ('first_name', 'last_name',)
    list_editable = ('is_deletes',)
    list_filter = ('country', 'is_deletes', )

    inlines = [
       BookInAuthor,
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Author, AuthorAdmin)



