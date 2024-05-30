from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
#from django.contrib.auth import get_user_model
from Users.models  import Users
from django.contrib.auth.models import User,BaseUserManager
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from qr_code.qrcode.utils import QRCodeOptions
import qr_code,qrcode

class FormatChoices(models.TextChoices):
    #hardcover='Hardcover'
    #paperback='Paperback'
    pdf='pdf'
    ebook= 'E-Book'
    audiobook= 'Audiobook'




class BookCategory(models.TextChoices):

    
        religious='religion'
        general_knowledge= 'general knowledge'
        study= 'study'
        Science='scientific'
        Comic= 'comic'
        uplifting= 'motivational'
        long_story= 'novels'
        short_story= 'short stories'
        fiction= 'fiction'
    

class AgeChoices(models.TextChoices):
   
         young= 'kids'
         middle_age='teenagers'
         adults='adults'
         elderly= 'old'
         everyone= 'everyone'
 

    

    
class Book(models.Model):##

   
    #language

    name=models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    book_language=models.CharField(max_length=50,default='English')
    category=models.CharField(max_length=50,default=BookCategory.fiction ,choices=BookCategory.choices)
    age=models.CharField(max_length=50,default='everyone',choices=AgeChoices.choices)
    pages=models.PositiveIntegerField(default=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book covers/')
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_by=models.ForeignKey(Users, on_delete=models.CASCADE,default=1)
    #format_choices = [
       
    format = models.CharField(max_length=30, choices=FormatChoices.choices ,default=FormatChoices.pdf)

    book_file = models.FileField(upload_to='book_files/',null=True,blank=True)  # New fiel


    class Meta:
        # Define a unique constraint on the combination of position_type and location
        constraints = [
            models.UniqueConstraint(fields=['name', 'added_by','author'], name='unique_book_per_user')#one user one ballot per election
        ]


    def __str__(self):
        return self.name  # f"wriiten by{self.author}" 
    
    def get_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.name)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{self.name}_qr.png")

        
    




    
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Define a unique constraint on the combination of position_type and location
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='unique_review_per_user')#one user one ballot per election
        ]




class BookClub(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    members = models.ManyToManyField(Users, related_name='book_clubs',)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
    def join(self,user):

        self.members.add(user)


class Post(models.Model):
    title=models.CharField(max_length=50,null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    book_club = models.ForeignKey(BookClub, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}\'s post in {self.book_club.name}'
    

class Comment(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}\'s comment on {self.post}'


class BookExchange(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    #owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='owned_books')
    borrower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='borrowed_books', null=True, blank=True)
    date_borrowed = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    return_due_date = models.DateTimeField(null=True, blank=True,default=datetime.now()+timedelta(weeks=2))
    date_returned = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        # Define a unique constraint on the combination of position_type and location
        constraints = [
            models.UniqueConstraint(fields=['borrower', 'book'], name='unique_book_per_borrower')#one user one ballot per election
        ]
    

    def return_book(self):
        """
        Method to mark the book as returned.
        """
        self.is_returned = True
        self.date_returned = datetime.now()  # Import timezone from django.utils if not already imported
        self.save()


    def clean(self):
        

       if not self.is_returned and self.borrower:
            unreturned_books = self.borrower.borrowed_books.filter(is_returned=False).count()
            if unreturned_books >= 5:
                raise ValidationError({'borrower': 'You can only borrow a maximum of 5 books at a time.'})



    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model
        super().save(*args, **kwargs)

