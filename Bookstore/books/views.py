from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.shortcuts import render
#from .forms import CustomUserCreationForm,RegistrationForm
from django.views.generic import TemplateView
#import pydantic
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from .models import Book
from Bookstore.settings import MEDIA_URL
    #..Bookstore.settings import MEDIA_URL


def add_book(request):

    if request.method == 'GET':
        print("got a get request add  book")
        context = ''
        return render(request, 'book.html')#, {'context': context}
    
    elif request.method == 'POST':
        print("got a POST request for book page")

        username:str = request.POST.get('name')
      # @ password:str = request.POST.get('password')
        name:str = request.POST.get('name')
        author:str = request.POST.get('author')
        description:str = request.POST.get('description')
        format:str = request.POST.get('format')
       # cover_image = request.POST.get('cover_image')
        price = request.POST.get('price')

        publication_date=request.POST.get('publication_date')

        uploaded_image = request.FILES['cover_image']
        #unique_filename =shortuuid.uuid()
        x=f"book covers"

        print("new location," ,x)
            # Save the image to a new location (e.g., 'media/book_covers/')
        fs = FileSystemStorage()
        #saved_path = fs.save(unique_filename, uploaded_image)
        imagename = fs.save(f"book covers\{ uploaded_image.name}", uploaded_image)
        uploaded_file_url = fs.url(imagename)

        print("uploaded file url",uploaded_file_url)


        book_details=Book(name=name,author=author,description=description,format=format,
                          cover_image=uploaded_file_url,publication_date=publication_date,price=price)
        
       
            # Save the filename in the database
        #book.cover_image = saved_path
      #  username:str = request.POST.get('name')
      #  username:str = request.POST.get('name')

 
        #book_details.save(False)
        #book_details.s   #bset_password(password)

        book_details.save(False)
        book_details.cover_image="book covers/"+imagename
        book_details.save()
        print(username,"bokkname")
        return HttpResponse(f"BOOKNAME {username}")

        
    



def add_book_revi(request):

    if request.method == 'GET':
        print("got a get request add  book review")
        context = ''
        return render(request, 'book.html')#, {'context': context}

