from django.shortcuts import render
from django.http import HttpResponse

# about/ -> "About"


# request = объект класса  HtttpResponse который формирует из запроса от клиента на наш сервер 

def hello(request):

    return HttpResponse("Hello", headers = {"Name": "Alex"}, status = 500)

def get_about(request):
    return HttpResponse("как-то так1")

def get_contacts(request):
    return HttpResponse("как-то так")
