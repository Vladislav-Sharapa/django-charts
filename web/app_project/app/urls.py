from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("date/", views.get_week, name='get_week'),
    path("add/", views.add_page, name= 'add_page'),
    path('add/add_data/', views.add_data),
]