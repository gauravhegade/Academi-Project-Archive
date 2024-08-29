from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("marks/upload/", views.upload_marks, name="upload_marks"),
    path("marks/view/", views.view_marks, name="view_marks"),
    path("marks/search/", views.search, name="search"),
]
