from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("students/", views.list_students, name="list_students"),
    path('register_student/', views.register_student, name='register_student'),

]