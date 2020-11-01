from django.urls import path
from flashcardapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app_page', views.app_page, name='app_page'),
    path('addition', views.addition, name='addition'),
    path('subtraction', views.subtraction, name='subtraction'),
    path('multiplication', views.multiplication, name='multiplication'),
    path('division', views.division, name='division'),
]