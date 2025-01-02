from django.urls import path
from . import views
from .views.asset.index import AssetView
from .views.asset.category import UsageCategoryView

urlpatterns = [
    path("user/login", views.user.login.LoginView.as_view()),
    path("user", views.user.index.UserView.as_view()),
    path("asset", AssetView.as_view()),
    path("asset/category", UsageCategoryView.as_view()),
]
