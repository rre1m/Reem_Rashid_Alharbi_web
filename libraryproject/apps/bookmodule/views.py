from django.shortcuts import render
from django.http import HttpResponse


# ---------------- Lab 3 ----------------
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1) + " Reem Rashid Alharbi, ID:421201722")


# ---------------- Lab 4 ----------------
def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, 'bookmodule/list_books.html')


def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


# ---------------- Lab 5 ----------------
def links_page(request):
    return render(request, 'bookmodule/lab5/links.html')


def text_formatting(request):
    return render(request, 'bookmodule/lab5/text_formatting.html')


def listing_page(request):
    return render(request, 'bookmodule/lab5/listing.html')


def tables_page(request):
    return render(request, 'bookmodule/lab5/tables.html')
