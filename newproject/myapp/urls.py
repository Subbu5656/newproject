from django.urls import path
from myapp import views
urlpatterns = [
    path('home/', views.home),
    path('simple/', views.simple),
    path('employee/', views.employees),
    path('employee_save/', views.employee_save),
    path('average/', views.average),
    path('main/', views.Main),
]
