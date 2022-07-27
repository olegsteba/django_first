import re

from django.core.exceptions import ValidationError


def validation_book_name(book_name):
    if re.fullmatch(r"Книга .*", book_name):
        return book_name
    raise ValidationError(message="Не соответствует")


def validation_autor_name(autor_name):
    if re.match(r'[A-ZА-Я]', autor_name):
        return autor_name
    raise ValidationError('Название не должно начинаться с маленькой буквы')

def validation_autor_name(autor_name):
    if autor_name[0].islower():
        raise ValidationError('Название не должно начинаться с маленькой буквы')
