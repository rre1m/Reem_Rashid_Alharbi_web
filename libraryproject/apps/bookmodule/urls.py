from django.urls import path
from . import views

urlpatterns = [
    # Lab 4
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    # Lab 3
    path('index2/<int:val1>/', views.index2),
]
