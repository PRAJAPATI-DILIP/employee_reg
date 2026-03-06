#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Emp1

from django.shortcuts import render
from .models import Emp1

def test(request):

    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_working = request.POST.get("emp_working")

        Emp1.objects.create(
            name=emp_name,
            emp_id=emp_id,
            phone=emp_phone,
            address=emp_address,
            department=emp_department
        )

    return render(request,"home.html")

'''e=Emp()
    e.name=emp_name
    e.emp_id=emp_id
    e.phone=emp_phone
    e.address=emp_address
    e.department=emp_department
    if emp_working is None:
        e.working=False
    else:
        e.working=True
    e.save(0) '''       

    #print("hello dilip")
    