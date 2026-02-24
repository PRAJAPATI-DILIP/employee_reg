from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    print("hello dilip")
    return render(request,"home.html",{})