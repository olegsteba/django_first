# Generated by Django 4.0.5 on 2022-06-21 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('father_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('language', models.JSONField(verbose_name='Языки на которыз писал автор')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_deletes', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_house_name', models.CharField(max_length=300, verbose_name='Название издательства')),
                ('address', models.CharField(max_length=1500, verbose_name='Адресс издательства')),
                ('contact_phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
                ('website_link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Адрес сайта')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_deletes', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описане книги')),
                ('date_creation', models.DateField(verbose_name='Дата написания книги')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_deletes', models.BooleanField(default=False, verbose_name='Удалено')),
                ('author', models.ManyToManyField(to='books.author', verbose_name='Авторы')),
                ('id_publishing_house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publishing_house_books', to='books.publishinghouse', verbose_name='ID издательства')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]