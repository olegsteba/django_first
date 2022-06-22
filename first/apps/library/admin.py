from django.contrib import admin
from .models import Library, User, SeasonTicket
"""
    list_display - какието атрибуты выводятся на экран
    list_display_links - какие атребуты будут ссылки
    search_fields - по каким поиск
    list_editable - какие поля можно изменить в таблице
    list_filter - по каким полям будет фильтрация
    fieldsets - страница с изменениями
"""


class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        "id", "library_name", "address", "phone", "is_deletes",
    )
    list_display_links = ("id", "library_name",)
    search_fields = ("library_name",)
    list_editable = ("is_deletes",)
    list_filter = ()
    fieldsets = (
        (
            (None, {
                "fields": ("library_name", "address", "phone",)
                }
            ),
        )
    )



class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id", "first_name", "last_name", "father_name", "birthday", "is_deletes",
    )
    list_display_links = ("id", "first_name",)
    search_fields = ("first_name",)
    list_editable = ("is_deletes",)
    list_filter = ()
    fieldsets = (
        (
            (None, {
                "fields": ("first_name", "last_name", "father_name", "birthday",)
                }
            ),
        )
    )
    
    
class SeasonTicketAdmin(admin.ModelAdmin):
    list_display = (
        "id", "number", "date_create", "id_library", "id_user", "is_deletes",
    )
    list_display_links = ("id", "number",)
    search_fields = ("number",)
    list_editable = ("is_deletes",)
    list_filter = ()
    fieldsets = (
        (
            (None, {
                "fields": ("number",)
                }
            ),
            ('Реквизиты абонемента', {
                'fields': ("id_library", "id_user",)
                }
            ),
        )
    )
    
        
admin.site.register(Library, LibraryAdmin)    
admin.site.register(User, UserAdmin)
admin.site.register(SeasonTicket, SeasonTicketAdmin)
