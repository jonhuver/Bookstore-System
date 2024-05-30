from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404
#from .forms import CustomUserCreationForm,RegistrationForm
from django.views.generic import TemplateView
#import pydantic
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from Users.models import Users
from .models import Book,BookClub,BookExchange,BookReview,FormatChoices,BookCategory,AgeChoices,Post,Comment
from.forms import BookReviewForm
from Bookstore.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required
    #..Bookstore.settings import MEDIA_URL
from datetime import datetime
from django.core.exceptions import ValidationError




from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Prefetch
from django.db.models import Avg
from django.views import View
from django.db.models import Sum,Count,Avg


from slick_reporting.views import ReportView, Chart
from slick_reporting.fields import ComputationField
from slick_reporting.fields import SlickReportField

#from slick_reporting.fields import GroupByColumn, SumColumn




class TotalBooksPerCategory(ReportView):

    report_model=Book

    #date_field = "publication_date"
    group_by ='category'#]#'#name__category' #['age','c']#"client__country"  # notice the double underscore
    columns = [
        "category",
        ComputationField.create(
            Count,
            "name",
            name="sum__value",
            verbose_name="Total Books Per Category",
        ),
    ]

    chart_settings = [

        Chart(
            "Total Books Per Category Bar Chart $",
            Chart.BAR,
            data_source=["sum__value"],
            title_source=["category"],
        ),




        Chart(

            "Total Books Per Category PIE CHART",

            
            Chart.PIE,  # A Pie Chart
            data_source=["sum__value"],
            title_source=["category"],
        ),
    ]





class TotalBooksPerAge(ReportView):

    report_model=Book

    #date_field = "publication_date"
    group_by ='age'#]#'#name__category' #['age','c']#"client__country"  # notice the double underscore
    columns = [
        "age",
        ComputationField.create(
            Count,
            "name",
            name="sum__value",
            verbose_name="Total Books Per Age",
        ),
    ]

    chart_settings = [

        Chart(
            "Total Books Per Age Bar Chart $",
            Chart.BAR,
            data_source=["sum__value"],
            title_source=["age"],
        ),




        Chart(

            "Total Books Per Age PIE CHART",

            
            Chart.PIE,  # A Pie Chart
            data_source=["sum__value"],
            title_source=["age"],
        ),
    ]







class BooksPerRating(ReportView):

    report_model=Book

    #date_field = "publication_date"
    group_by ='age'#]#'#name__category' #['age','c']#"client__country"  # notice the double underscore
    columns = [
        "age",
        ComputationField.create(
            Count,
            "name",
            name="sum__value",
            verbose_name="Total Books Per Age",
        ),
    ]

    chart_settings = [

        Chart(
            "Total Books Per Age Bar Chart $",
            Chart.BAR,
            data_source=["sum__value"],
            title_source=["age"],
        ),




        Chart(

            "Total Books Per Age PIE CHART",

            
            Chart.PIE,  # A Pie Chart
            data_source=["sum__value"],
            title_source=["age"],
        ),
    ]












   

@login_required
def add_book(request):

    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")

    else:
        redirect('login')

    if request.method == 'GET' or 'get':
        print("got a get request add  book")
        choices=FormatChoices.choices
        age_choices=AgeChoices.choices
        category_choices=BookCategory.choices
        ages=[age_choice[1] for age_choice in age_choices]
        
        categories=[category_choice[1] for category_choice in category_choices]
        formats= [choice[1] for choice in choices]
        #formats=choices
        
        context = ''
        return render(request, 'book.html',{"formats":formats,'ages':ages,'categories':categories})#, {'context': context}


@login_required
def add_book_post(request):

    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")

    else:
        redirect('login')
    if request.method == 'POST' or 'post':
        print("got a POST request for book page")
        try:
         username=Users.objects.get(username=user_data)

        except ObjectDoesNotExist:
            print('wrong user')
            redirect('login')
        pages=request.POST.get('pages')
        age=request.POST.get('age')
        category=request.POST.get('category')
        request.POST.get('name')
        name:str = request.POST.get('name')
        author:str = request.POST.get('author')
        description:str = request.POST.get('description')
        format:str = request.POST.get('format')
        price = request.POST.get('price')
        publication_date=request.POST.get('publication_date')
        uploaded_image = request.FILES['cover_image']                
        fs = FileSystemStorage()           
        imagename = fs.save(f"book covers/{uploaded_image.name}", uploaded_image)
        uploaded_file_url = fs.url(imagename)

        uploaded_book = request.FILES['book_file']                
        fs = FileSystemStorage()           
        bookname = fs.save(f"book_files/{uploaded_book.name}", uploaded_book)
        uploaded_book_url = fs.url(bookname)


        
        choices=FormatChoices.choices
        age_choices=AgeChoices.choices
        category_choices=BookCategory.choices

        print("choices", type(choices),choices)

        def getIndexOfTuple(l, index, value):
                for pos,t in enumerate(l):
                    if t[index] == value:
                        
                        print("position is",pos)
                        #print('t index', t[index])
                        return pos

    
                
        index_choice=getIndexOfTuple(choices, 1, format)

        index_choice_age=getIndexOfTuple(age_choices,1,age)

        index_choice_category=getIndexOfTuple(category_choices,1,category)

        print('selected book format',format)

        print ("index of {fomat} in tuple",index_choice)
        print ("{category} category index in   ",index_choice_category)



        print("uploaded file url",uploaded_file_url)

        print("index of {format} in original list",choices[index_choice][0])


        book_details=Book(name=name,author=author,description=description,format=choices[index_choice][0],added_by=username,
                        cover_image=uploaded_file_url,publication_date=publication_date,price=price,book_file=uploaded_book_url,
                        pages=pages,age=age_choices[index_choice_age][0] ,category=category_choices[index_choice_category][0]
                        )
    
       
        
        try:
           book_details.save(False)
           book_details.cover_image="book covers/"+uploaded_image.name
           book_details.book_file="book_files/"+uploaded_book.name
           book_details.save()
        except IntegrityError:
            
            return HttpResponse("you have already added this book")
        print(username,"bokkname")
        return HttpResponse(f"BOOKNAME {username}")


def download_file(request):

    if request.method=="post" or 'POST':
     user_data = request.session.get('user')
     if user_data:
            
            file_id = request.POST.get('file_id')
            print("book_id",file_id)
            uploaded_file = Book.objects.get(pk=file_id).book_file

            response = HttpResponse(uploaded_file.file, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
            return response  
     else:

         return redirect('login')   
            


@login_required
def add_book_review(request):

    #page with all books to be reviwed. selet book 

    #book rev returns review for  with book id

    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")

        if request.method == 'GET':
            print("got a get request add  book review")

            #form=BookReviewForm()
            books=Book.objects.all()
        # form=BookReview.objects.all()
            context = ''
            return render(request, 'bookReview.html',{"books":books})#, {'context': context}
        #/books/review/

def add_book_review_review(request):
        user_data = request.session.get('user')
        if user_data:
           print("user data",user_data)
           print("user data in request")
   
        

           if request.method == 'post' or "POST":
                print("got a post request add  book review")

                book_id=request.POST.get('books_id')

                print('submited book',book_id)
                
                rate=request.POST.get('rating')
                reviw_text=request.POST.get('review_text')
                id_book=request.POST.get('books_id')
                #print("book from user",bk)
                bok=Book.objects.get(id=book_id)#get instance of book from Book class\
                # print("bok",bok)
                useer=Users.objects.get(username=user_data)#get instance of user from Users using session data of logged in user 
                book_review=BookReview(book=bok,user=useer,rating=rate,review_text=reviw_text)
                try:          
                
                 book_review.save()
            # form=BookReview.objects.all()
                except IntegrityError:
                    return HttpResponse("You have already reviwed this book ") #render(request, 'bookReview.html',{"form":form})#, {'context': context}

                
                return HttpResponse("SUCCESFULLY REVIEWED THE BOOK") #render(request, 'bookReview.html',{"form":form})#, {'context': context}




def add_book_review_get_page(request):
        user_data = request.session.get('user')
        if user_data:
           print("user data",user_data)
           print("user data in request")
   
        

           if request.method == 'get' or "GET":
                print("got a post request add  book review")

                books_id=request.GET.get('books_id')

                print('book_id',books_id)

                return render(request,'review.html',{'books_id':books_id})
           

        

@login_required
def viewAvailableBooks(request):
    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")
        # Get the user object using the retrieved user ID
       # user = CustomUser.objects.get(username=user_data)

        if request.method == 'GET':
          print("got request to get available books")

          books = Book.objects.annotate(average_rating=Avg('reviews__rating')).prefetch_related(Prefetch('reviews', queryset=BookReview.objects.order_by('-date_posted')))

          for book in books:
            print(f"Book: {book.name}, Average Rating: {book.average_rating}")
            for review in book.reviews.all():
                print(f"Review by {review.user.username}: {review.review_text}")
            #books = Book.objects.all() 
          #books=Book.objects.filter().prefetch_related(Prefetch('reviews', queryset=BookReview.objects.order_by('-date_posted'))) 
          print(f"total books: {len(books)}")    
          return render(request, 'books.html',{"books":books})


@login_required
def borrow_book(request):
    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")

        if request.method == 'GET':
            print("got a get request borrow  book ")
            context = ''
            books = Book.objects.all()  
            print(f"total books: {len(books)}") 
            return render(request, 'bookExchange.html',{"books":books})


        if request.method == 'POST':
            print("got a post request borrow  book ")
            context = ''
            borrowed_book=request.POST.get("books_id")

            print("borrowed book",borrowed_book)
            user=Users.objects.get(username=user_data)
    
            book=Book.objects.get(id=borrowed_book)
            print("bookname",book.name)
            book_exchange=BookExchange(book=book,borrower=user,date_borrowed=datetime.now())


            try:

                book_exchange.save()
    # Yo
            except ValidationError as e:
                # Handle validation error
                error_dict = e.message_dict
                for field, errors in error_dict.items():
                    # Print or handle each field's errors
                    for error in errors:
                        print(f"{field}: {error}")

                        return HttpResponse(f"{field}: {error}")
                        
            return HttpResponse(f"successfully borrowed {borrowed_book}")
        #books = Book.objects.all()  
        #print(f"total books: {len(books)}") 
        #return render(request, 'bookExchange.html',{"books":books})
@login_required
def account_summarry(request):
    if request.method=="GET":
     user_data = request.session.get('user')
     if user_data:
        user=Users.objects.get(username=user_data)
        owned_books=Book.objects.filter(added_by=user).all()
        total_books=len(owned_books)
        borrowed_books=BookExchange.objects.filter(borrower=user).all()
        #annotate(average_rating=Avg('reviews__rating'))
        for borrowed_book in borrowed_books:
            print(f"{borrowed_book.book.name} {borrowed_book.date_borrowed} {borrowed_book.return_due_date} {borrowed_book.is_returned}")
        total_borrowed_books=len(borrowed_books)
        print(f"you have added {total_books}\n you have borrowed{ total_borrowed_books}")


        books=borrowed_books
        #return HttpResponse(f"you have added {total_books}\n you have borrowed{ total_borrowed_books}")

        return render(request,'borrowed.html',{'books':books})
     

     else:
         redirect('login')



def edit_books_get(request):

    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")
        book_owner=Users.objects.get(username=user_data)
        books=Book.objects.filter(added_by=book_owner).all()

        return render(request,'user_books.html',{'books':books})

    else:

     redirect('login')





def edit_books_post(request):

    user_data = request.session.get('user')
    if user_data:
        print("user data",user_data)
        print("user data in request")
        book_owner=Users.objects.get(username=user_data)
        books=Book.objects.filter(added_by=book_owner).all()

    if request.method=='POST' or 'post':

        if request.POST.get("delete_id"):
           books_id=request.POST.get("delete_id")
           print(' selected book_id',books_id)
           to_delete=Book.objects.get(id=books_id)

           to_delete.delete()

           return HttpResponse('successfully Deleted book') #render(request,'user_books.html',{'books':books})
        

        if request.POST.get("update_id"):
           book_id=request.POST.get("update_id")
           #if request.POST.get("update_id"):
           book=Book.objects.get(id=book_id)
           print('update book request',request.POST.get("update_id"))
           print("found",book.name)

           choices=FormatChoices.choices

           print ('book file type',type(book.book_file.name))
           print ('image file type',type(book.cover_image.name))

           formats=[choice[1] for choice in choices ]


           age_choices=AgeChoices.choices
           category_choices=BookCategory.choices
           ages=[age_choice[1] for age_choice in age_choices]
        
           categories=[category_choice[1] for category_choice in category_choices]

           
           return render(request,'edit_book.html',{'book':book,'formats':formats,'ages':ages,'categories':categories})

           #return HttpResponse('successfully updated book')

    else:

     redirect('login')


def update_book_update(request):
    user_data = request.session.get('user')
    if user_data:
        if request.method=='POST':
            name:str = request.POST.get('name')
            author:str = request.POST.get('author')
            description:str = request.POST.get('description')
            pages:int = request.POST.get('pages')
            category:str = request.POST.get('category')

            age:int = request.POST.get('age')
            format:str = request.POST.get('format')
            price = request.POST.get('price')
            publication_date=request.POST.get('publication_date')
            book_id=request.POST.get("update_id")
            book=Book.objects.get(id=book_id)

            if 'cover_image' in request.FILES:
                uploaded_image = request.FILES['cover_image']                
                fs = FileSystemStorage()           
                imagename = fs.save(f"book covers/{uploaded_image.name}", uploaded_image)
                uploaded_file_url = fs.url(imagename)
                book.cover_image=uploaded_file_url
                book.cover_image="book covers/"+uploaded_image.name

            if 'book_file' in request.FILES:
                uploaded_book = request.FILES['book_file']
                fs = FileSystemStorage()           
                bookname = fs.save(f"book_files/{uploaded_book.name}", uploaded_book)
                uploaded_book_url = fs.url(bookname)
                book.book_file=uploaded_book_url
                book.book_file="book_files/"+uploaded_book.name


            def getIndexOfTuple(l, index, value):
             for pos,t in enumerate(l):
                if t[index] == value:
                    return pos

            choices=FormatChoices.choices
            index_choice=getIndexOfTuple(choices, 1, format)

            age_choices=AgeChoices.choices
            category_choices=BookCategory.choices

            index_choice_age=getIndexOfTuple(age_choices,1,age)

            index_choice_category=getIndexOfTuple(category_choices,1,category)

            book.name=name
            book.author=author

            if (publication_date)!='':
              book.publication_date=publication_date
            book.description=description
            book.format=choices[index_choice][0]
            book.age=age_choices[index_choice_age][0]
            book.category=category_choices[index_choice_category][0]
            book.price=price
            book.pages=pages
            try:
                book.save(False)
                book.save()
            except IntegrityError:
                return HttpResponse("Error while updating book. Please consider changing the book details.")
            return HttpResponse("Successful update.")
        else:
            return HttpResponse("Invalid request method.")
    else:
        return HttpResponse("User not logged in.")

        

                    
            
def myreviews(request):
    user_data = request.session.get('user')
    if user_data:

        user=Users.objects.get(username=user_data)

    if request.method=='get' or 'GET':

        print('all revs')

        #books=Book.objects.filter().prefetch_related(Prefetch('reviews', queryset=BookReview.objects.order_by('-date_posted'))

           



#class BookCategoryCreateView(View):
@login_required
def BookCategoryCreateViewget( request):

    user_data = request.session.get('user')
    if user_data:
        if request.method=='get' or 'GET':
            user=Users.objects.get(username=user_data)

            choices=BookCategory.category_choices

            age_choices=BookCategory.age_choices

            print('age_choices',age_choices)

            
            categories=[choice[1] for choice in choices ]

            ages=[age_choice[1] for age_choice in age_choices ]

            books=Book.objects.filter(added_by=user)

            print('get request for category')
            #
            return render(request, 'book_category.html',{'books':books ,'categories':categories,'ages':ages})  # replace with your template name
        
@login_required
def BookCategoryCreateViewPost( request):

    user_data = request.session.get('user')
    if user_data:    

        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            books = request.POST.get('books_id')  # if books is a multiselect field
            age = request.POST.get('age')

            print('booksid',books)

            #for book_id in books:
            book = Book.objects.get(id=books)  # assuming Book model exists

            def getIndexOfTuple(l, index, value):
             for pos,t in enumerate(l):
                if t[index] == value:
                    return pos

            category_choices=BookCategory.category_choices
            age_choces=BookCategory.age_choices

            index_choice_age=getIndexOfTuple(age_choces, 1, age)
            index_choice_category=getIndexOfTuple(category_choices, 1, category_name)

            print('index of age','age',age ,'index',[index_choice_age][0])
            print('index of category','category',category_name ,'index',[index_choice_category][0])
                
            #categ=
            
            try:
              exists=''#'BookCategoryMembership. objects.get(book=book,book_category=[index_choice_category][0],age=[index_choice_age][0])
              if exists:
                  print('book already in category')
                  return HttpResponse('book already exists in category')
            except ObjectDoesNotExist:
                pass

            book_category = BookCategory(category_name=category_name, age=age)
            book_category.save()

            #membership = BookCategoryMembership(book=book, book_category=category_name, age=age)
            #membership.save()

            

            return HttpResponse(f'successfully added book to category {category_name}')
    else:
        return redirect('login')
    
    
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book,
        'qr_code_url': book.get_qr_code,  # Make sure this method returns the URL of the QR code image
    }
    return render(request, 'book_detail.html', context)


@login_required
def return_book(request):

    user_data = request.session.get('user')
    if user_data:  

        if request.method=='POST' or 'post':


            books_id = request.POST.get('books_id')

            print('return book with id ',books_id)

            user=Users.objects.get(username=user_data)

            book_instance=BookExchange.objects.get(id=books_id)

            print (book_instance.book.name)
            book_instance.return_book()

            

            return HttpResponse('successfully returned book')
        
    else:

        return redirect('login')
            



@login_required
def join_book_club(request):

    book_club_id=request.POST.get('book_club_id')

    user_data = request.session.get('user')
    if user_data:  

        user=Users.objects.get(username=user_data)

        #request.user=
        


        book_club = get_object_or_404(BookClub, pk=book_club_id)
        original_total_members=len(book_club.members.all())

        print('original total members',original_total_members)

        book_club.join(user=user)

        total_members_now=len(book_club.members.all())

        print(' total new members',total_members_now)

        redirect('blog_detail', book_club_id=book_club.id)


        
       # return HttpResponse('total members',total_members_now) #redirect('book_club_detail', book_club_id=book_club.id)
    


def create_post(request, book_club_id):

    user_data = request.session.get('user')
    if user_data:  

        user=Users.objects.get(username=user_data)

        book_club = get_object_or_404(BookClub, pk=book_club_id)
        if request.method == 'POST':
            content = request.POST.get('content')
            title = request.POST.get('title')
            Post.objects.create(author=user, book_club=book_club, content=content,title=title)
            #return redirect('book_club_detail', book_club_id=book_club.id)
      #  return render(request, 'create_post.html', {'book_club': book_club})
            return HttpResponse('created post successful')
            



def create_comment(request, post_id):
    user_data = request.session.get('user')
    if user_data:  

        user=Users.objects.get(username=user_data)
        post = get_object_or_404(Post, pk=post_id)
        if request.method == 'POST':
            content = request.POST.get('content')
            Comment.objects.create(author=user, post=post, content=content)
            #return redirect('post_detail', post_id=post.id)
            #render(request, 'club_base.html',)
            
        #return render(request, 'create_comment.html', {'post': post})
            return HttpResponse('commented succcessfully')
    

def book_club_detail(request, book_club_id):

    user_data = request.session.get('user')
    if user_data:  

        user=Users.objects.get(username=user_data)
        book_club = get_object_or_404(BookClub, pk=book_club_id)

        print('all members in this group',len(book_club.members.all()))

        if user not in book_club.members.all():
            print('you have not yet joined club')
            return redirect('home')
        posts = Post.objects.filter(book_club=book_club).prefetch_related('comments')
        #comments = post.comments.all()
        return render(request, 'club_base.html', {'book_club': book_club, 'posts': posts})
    

def book_club_list(request):
    if request.method=='get' or 'GET':

        print('get method to see clubs')

        user_data = request.session.get('user')
        if user_data:  

        

            user=Users.objects.get(username=user_data)

            book_clubs=BookClub.objects.all()

            return render(request,'book_club_list.html',{'book_clubs':book_clubs})
        



def create_book_club(request):
     user_data = request.session.get('user')
     if user_data:  

        

            user=Users.objects.get(username=user_data)
            if request.method == 'POST':
                name = request.POST.get('name')
                description = request.POST.get('description')
                book_club = BookClub(name=name, description=description, owner=user)
                book_club.save()
                book_club.members.add(user)
                return redirect('home')
            #return render(request, 'create_book_club.html')

            return HttpResponse('succesfully created group')
