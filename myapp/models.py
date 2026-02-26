from django.db import models

# Create your models here.

def group_image_path(instance, filename):
    group_name = instance.name.lower().replace(" ", "-")
    return f"products/{group_name}/{filename}"

class Group(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=20)
    des = models.TextField()
    image = models.ImageField(upload_to=group_image_path)


def product_image_path(instance, filename):
    # instance.category is a Group object
    group_name = instance.category.name.lower().replace(" ", "_")
    return f"products/{group_name}/{filename}"
    # for uploading images to grouped path folder

class Product(models.Model):

    def __str__(self):
        return  self.name
    name = models.CharField(max_length=20)
    price = models.FloatField()
    des = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to=product_image_path)
    category = models.ForeignKey(Group, on_delete=models.CASCADE)


class Order(models.Model):
    pass