from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('contact/',views.contact, name='contact'),
    path('register/',views.register,name='register'),
    path('details/<int:id>/',views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='abc'),
    path('employee/', views.employee, name='employee'),
    path('edit/<int:id>/',views.edit,name='edit'),
]