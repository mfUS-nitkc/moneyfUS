from django.urls import path
from . import views

urlpatterns = [
    path("user/login", views.user.login.LoginView.as_view()),
    path("user", views.user.register.RegisterView.as_view())
]
