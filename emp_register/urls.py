from django.contrib import admin
from django.urls import path
from employee.views import test   # ✅ Import function directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name='home'), 
       path('index/', test, name='index'),  # ✅ Use function directly
]