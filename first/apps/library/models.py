from django.db import models


class Library(models.Model):
    library_name = models.CharField(max_length=100, verbose_name="Название библиотеки")
    address = models.CharField(max_length=1500, verbose_name="Адрес")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    is_deletes = models.BooleanField(default=False, verbose_name="Удалено")
    
    def __str__(self):
        return self.library_name
    
    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"
        

class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    father_name = models.CharField(max_length=100, verbose_name="Отчество", null=True, blank=True)
    birthday = models.DateField(verbose_name="Дата рождения")
    is_deletes = models.BooleanField(default=False, verbose_name="Удалено")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"    
    

class SeasonTicket(models.Model):
    number = models.CharField(max_length=100, verbose_name="Имя")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_deletes = models.BooleanField(default=False, verbose_name="Удалено")
    id_library = models.ForeignKey(
        "Library",
        on_delete=models.CASCADE,
        related_name="season_ticket_library",
        verbose_name="ID библиотеки",
        null=True,
        blank=True,
    )
    id_user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="season_ticket_user",
        verbose_name="ID Читателя",
        null=True,
        blank=True,
    )
        
    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"  
        unique_together = ("id_library", "id_user")
