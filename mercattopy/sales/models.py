from django.db import models
from django.core.exceptions import ValidationError
from catalog.models import Product




class Sale(models.Model):

    STATUS_CHOICES = [
        ('open', 'Aberta'),
        ('completed', 'Concluída'),
    ]

    date = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    def __str__(self):
        return f"Venda #{self.id}"


class SaleItem(models.Model):

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    def save(self, *args, **kwargs):


        if self.product.stock < self.quantity:
            raise ValidationError("Estoque insuficiente para esta venda.")


        self.unit_price = self.product.price


        self.subtotal = self.unit_price * self.quantity

        super().save(*args, **kwargs)


        self.product.stock -= self.quantity
        self.product.save()


        total = sum(item.subtotal for item in self.sale.items.all())
        self.sale.total = total
        self.sale.save()
