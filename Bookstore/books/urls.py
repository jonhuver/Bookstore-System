from django.urls import path

from.views import add_book,viewAvailableBooks,borrow_book,account_summarry,add_book_review,add_book_post,download_file
from .views import edit_books_get,edit_books_post,update_book_update,add_book_review_review,add_book_review_get_page

from.views import BookCategoryCreateViewget,BookCategoryCreateViewPost,TotalBooksPerCategory,TotalBooksPerAge

from .views import return_book


from .views import book_club_list,book_club_detail,join_book_club,create_comment,create_post,create_book_club

urlpatterns = [
    
    


     path("add/",add_book, name="addbook"),#render login view as function #function based views
     path("add/book/",add_book_post, name="addbookPost"),
     path("edit/",edit_books_get, name="EditBooksGet"),
     path("update/",edit_books_post, name="EditBooksPost"),

     path("update/book/",update_book_update, name="UpdateBook") ,
     path("view/",viewAvailableBooks, name="viewBooks"),
     path("borrow/",borrow_book, name="borrowBooks"),
     path("summary/",account_summarry, name="accountSummary"),


     path("reviews/",add_book_review, name="bookReview"),
     path("reviews/book/",add_book_review_get_page,name='ReviewPage'),#add_book_review_review, name="bookReviewReview"),
     path("reviews/book/review/",add_book_review_review,name='ReviewPageRev'),
     path("borrowed/return/",return_book,name='return-book'),

     

     path("download/",download_file, name="downloadFile"),
     


     path("category/" ,BookCategoryCreateViewget,name='bookcategory-new'),
     path("category/add",BookCategoryCreateViewPost,name='bookcategory-new-add'),


     path("reports/", TotalBooksPerAge.as_view(), name="bookingsReports"),

    path("categories/", TotalBooksPerCategory.as_view(), name="bookingsReportsTests"),

    
#path("", views.blog_index, name="blog_index"),
   # path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
   # path("category/<category>/", views.blog_category, name="blog_category"),
    #urls for book clubs
   
    path('clubs/',book_club_list,name='get-book-clubs'),

    path("clubs/join/",join_book_club,name='join_book_club'),#join-club'
  
    path('clubs/<int:book_club_id>/',book_club_detail,name='blog_detail'),

   path('clubs/comments/<int:post_id>/',create_comment,name='create_comment'),

    path('clubs/posts/<int:book_club_id>/',create_post,name='create_post'),


    path('club/create/',create_book_club,name='create_book_club'),


    
]