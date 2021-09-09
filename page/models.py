from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    d_o_b = models.DateField()


class Cand(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Category(models.Model):
    category_book = models.CharField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)  
 
