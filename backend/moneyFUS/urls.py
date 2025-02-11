from django.urls import path
from .views.user.index import UserView
from .views.user.login import LoginView
from .views.asset.index import AssetView
from .views.asset.category import UsageCategoryView
from .views.loan.lend import LendView
from .views.loan.index import LoanCheckoutView

urlpatterns = [
    path("user/login", LoginView.as_view()),
    path("user", UserView.as_view()),
    path("asset", AssetView.as_view()),
    path("asset/category", UsageCategoryView.as_view()),
    path("lend", LendView.as_view()),
    path("lend/checkout/<str:loan_id>", LoanCheckoutView.as_view()),
]
