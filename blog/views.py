from django.shortcuts import render
from django.http import HttpResponse

def get_index(request):
    context = {
        "title": "Главная страница",
        "my_list":[1, 2, 3, 4]
    }
    return render(request, "blog/index.html", context=context)

def get_about(request):
    return render(request, "blog/about.html", context=None)

def get_contacts(request):
    context = {
    "title" : "как то так"
    }
    return render(request, "blog/contacts.html", context=None)