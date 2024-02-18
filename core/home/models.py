from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class LensMaterial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='materials/')
    description = models.TextField()

    def __str__(self):
        return self.name

class LensCoating(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='coatings/')
    description = models.TextField()

    def __str__(self):
        return self.name

class LensIndex(models.Model):
    index = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.index

class LensFeatures(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='features/')
    description = models.TextField()

    def __str__(self):
        return self.name

class StockLens(models.Model):
    TYPE_CHOICES = (
        ('SV', 'SV'),
        ('KT', 'KT'),
        ('Progressive', 'Progressive'),
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    brand_name = models.CharField(max_length=100)
    lens_index = models.ForeignKey(LensIndex, on_delete=models.CASCADE)
    lens_material = models.ForeignKey(LensMaterial, on_delete=models.CASCADE)
    lens_coating = models.ForeignKey(LensCoating, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stock_lenses/')
    description = models.TextField()
    features = models.ManyToManyField(LensFeatures)

    def __str__(self):
        return f"{self.brand_name} - {self.type}"

class PowerRange(models.Model):
    lens_id = models.ForeignKey(StockLens, on_delete=models.CASCADE)
    DIA = models.CharField(max_length=20)
    power_range = models.CharField(max_length=50)
    price_srp = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.lens_id} - {self.DIA} - {self.power_range}"