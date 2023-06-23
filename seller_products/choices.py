from django.db.models import TextChoices


class CurrencyChoices(TextChoices):
    USD = 'USD'
    KZT = 'KZT'
    RUB = 'RUB'
