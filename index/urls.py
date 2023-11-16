from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("allforms", views.all_forms, name="allforms"),
    path("<int:id>", views.resume, name="resume"),
    path('list/',views.list,name="list"),

]
