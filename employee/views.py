#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    emp_name=request.POST.get("emp_name")
    emp_id=request.POST.get("emp_id")
    print(emp_name)
    print(emp_id)


    #print("hello dilip")
    return render(request,"home.html")