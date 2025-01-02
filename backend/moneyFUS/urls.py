from django.urls import path
from .views.user.index import UserView
from .views.user.login import LoginView
from .views.asset.index import AssetView
from .views.asset.category import UsageCategoryView

urlpatterns = [
    path("user/login", LoginView.as_view()),
    path("user", UserView.as_view()),
    path("asset", AssetView.as_view()),
    path("asset/category", UsageCategoryView.as_view()),
]
