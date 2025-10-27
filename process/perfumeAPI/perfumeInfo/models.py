from django.db import models

# Create your models here.
class perfumeCategory(models.Model):
    category = models.CharField(max_length=20, null=False, blank=False, unique=True)

class perfumeInfo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    brand = models.CharField(max_length=100)
    brandJp = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(
        perfumeCategory,
        related_name = "perfumes",
        blank = False,
    )