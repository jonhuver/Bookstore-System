from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#from django.contrib.auth import get_user_model

from django.contrib.auth.models import User,BaseUserManager
from django.db import models


class Users(AbstractUser):
    #pass
    # add additional fields in here

    #user_contact = models.CharField(max_length=20,unique=True)
    is_logged_in=models.BooleanField(default=False)
   # objects=models.Manager()
    #custoomuser =models.Manager()
   

    class Meta:
     db_table ='users'


        
       # print(last_name)

           # def save(self, *args, **kwargs):
               # super().save(*args, **kwargs)


    def __str__(self):
        return self.username


    
class UsersManager(BaseUserManager):
    def create_user(self, email,password,username,first_name,last_name,is_logged_in=False): #id_no,id_image,user_image,
      #,user_contact:str
        """

        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
           # user_contact=user_contact,
            password=password #,
            #id_image=id_image,
            #id_no=id_no,
            #user_image=user_image

        )

        user.set_password(password)
        user.save(using=self._db)
        return user   
    
