from django.contrib.auth import get_user_model
from django.db import models
from products import models as product_models
from seller_products import choices
from users import choices as user_choices


# Create your models here.


class SellerProduct(models.Model):
    product = models.ForeignKey(
        to='products.Product',
        on_delete=models.PROTECT,
        related_name='seller_products',
    )
    seller = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='seller_products',
        limit_choices_to={'user_type': user_choices.UserTypeChoices.Seller}
    )
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    amount_currency = models.CharField(
        max_length=3,
        choices=choices.CurrencyChoices.choices,
        default=choices.CurrencyChoices.KZT
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
