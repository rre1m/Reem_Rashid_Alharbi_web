from django.urls import path
from . import views

urlpatterns = [
    # Lab 5
    path('html5/links', views.links_page, name="books.lab5_links"),
    path('html5/text/formatting', views.text_formatting, name="books.lab5_text_formatting"),
    path('html5/listing', views.listing_page, name="books.lab5_listing"),
    path('html5/tables', views.tables_page, name="books.lab5_tables"),
    # Lab 4
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    # Lab 3
    path('index2/<int:val1>/', views.index2),
    path("search", views.search, name="books.search"),
]
