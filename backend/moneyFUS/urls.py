from django.urls import path
from .views.user.index import UserView
from .views.user.login import LoginView
from .views.asset.index import AssetView
from .views.asset.category import UsageCategoryView
from .views.lend.index import LendView, LendCheckoutView

urlpatterns = [
    path("user/login", LoginView.as_view()),
    path("user", UserView.as_view()),
    path("asset", AssetView.as_view()),
    path("asset/category", UsageCategoryView.as_view()),
    path("lend", LendView.as_view()),
    path("lend/checkout/<str:lend_id>", LendCheckoutView.as_view())
]
