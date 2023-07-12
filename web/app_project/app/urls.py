from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("date/", views.get_week, name='get_week'),
    path("add/", views.add_page, name= 'add_page'),
    path('add/add_data/', views.add_data),
    path("chart/bar/<str:week>/", views.get_bar_data, name='bar_chart'),
    path("chart/line/<str:week>/", views.get_line_data, name='line_chart'),
    path("chart/pie/<str:week>/", views.get_pie_data, name='pie_chart'),
    path("chart/area/<str:week>/", views.get_area_data, name='area_chart')
]