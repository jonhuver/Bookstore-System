from .models import Book,BookClub,BookReview,BookExchange
from django import forms

class BookForm(forms.Form):

    # email = forms.EmailField()
    
    name = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    description = forms.TextInput()#  CharField(max_length=100)

    format=forms.CharField(max_length=100)

    price=forms.DecimalField(max_digits=10,decimal_places=2)

    publication_date=forms.DateField()
    cover_image=forms.ImageField()#




class BookReviewForm(forms.ModelForm):


    class Meta:
        model=BookReview
        #fields="__all__"

        fields=['book','rating','review_text']

