from django.db import models


# Create your models here.

# models
#     category
#         id
#         type
#         name
#     places
#         id
#         name
#         city
#         state
#         country
#         lat
#         long -> None
#         category_id -FK

class Category(models.Model):
    type = models.CharField(null=True, blank=True, max_length=200, verbose_name='Type information')
    name = models.CharField(max_length=200, verbose_name='Name of the category')

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name of the place')
    city = models.CharField(max_length=100, verbose_name='Name of the city')
    state = models.CharField(max_length=100, verbose_name='Name of the state')
    country = models.CharField(max_length=200, verbose_name='Name of the country')
    category = models.ForeignKey(Category, related_name='places')

    def __str__(self):
        return self.name
