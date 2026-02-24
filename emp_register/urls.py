from django.contrib import admin
from django.urls import path
from emp_register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test),
]