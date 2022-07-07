from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to="thumbnail")
    book_url = models.URLField()

    def _str_(self):
        return self.name