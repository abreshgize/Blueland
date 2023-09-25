from distutils.command.upload import upload
from email.policy import default
from operator import mod
from django.db import models
from tinymce.models import HTMLField




class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "Images/Category", blank =True)
    desc = HTMLField(blank=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = "Images/Subcategory", blank =True)

    def __str__(self):
        return self.name


class Brand (models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    ref = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    subcat = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    main_image = models.ImageField(upload_to = "Images/Product")
    side_image = models.ImageField(upload_to = "Images/Product", blank=True, default="")
    desc = HTMLField(blank=True, verbose_name="Description")
    additional_information = HTMLField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    hot = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.ref}" if self.ref else f"{self.name}"

    class Meta:
        ordering = ['-id']

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "Images/Product")

    def __str__(self):
        return f"{self.product}'s image"


class Partners(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to = "Images/Partner_Logo")
    link = models.URLField(null=True)

    def __str__(self):
        return self.name


class Mission(models.Model):
    mission = HTMLField()
    vision = HTMLField()
    years = models.IntegerField(default=5)

class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "Images/Team")
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, )
    email = models.EmailField(blank=True,)

    def __str__(self):
        return self.name


class ContactUsMessages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f"message from {self.name}"






