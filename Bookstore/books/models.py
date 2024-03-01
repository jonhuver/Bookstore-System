from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#from django.contrib.auth import get_user_model
from Users.models  import Users
from django.contrib.auth.models import User,BaseUserManager
from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book covers/')
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    format_choices = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('ebook', 'E-Book'),
        ('audiobook', 'Audiobook')
    ]
    format = models.CharField(max_length=20, choices=format_choices)


    def __str__(self):
        return f"{self.name } wriiten by{self.author}"




    
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)




class BookClub(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    members = models.ManyToManyField(Users, related_name='book_clubs')

    


class BookExchange(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='owned_books')
    borrower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='borrowed_books', null=True, blank=True)
    date_borrowed = models.DateTimeField(null=True, blank=True)
    return_due_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
