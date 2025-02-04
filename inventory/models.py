from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    # Attributes
    weight = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    discount_levels = models.TextField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    packaging_info = models.TextField(blank=True, null=True)
    margin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    production_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Classification
    classification_code = models.CharField(max_length=50, blank=True, null=True)
    unit_of_measure = models.CharField(max_length=50, blank=True, null=True)

    # Location
    branch = models.CharField(max_length=100, blank=True, null=True)
    primary_location = models.CharField(max_length=100, blank=True, null=True)
    secondary_location = models.CharField(max_length=100, blank=True, null=True)

    # Tax & Reorder
    tax_info = models.TextField(blank=True, null=True)
    reorder_quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
