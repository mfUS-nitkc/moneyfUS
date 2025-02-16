from django.urls import path
from .views.user.index import UserView
from .views.user.login import LoginView
from .views.user.logout import LogoutView
from .views.user.self import UserSelfView
from .views.asset.index import AssetView
from .views.asset.category import UsageCategoryView
from .views.loan.lend import LendView
from .views.loan.index import LoanCheckoutView
from .views.loan.borrowed import BorrowedView
from .views.notify.index import NotifyView
from .views.notify.read import NotifyReadView
from .views.loan.remind import LoanRemindView
from .views.friend.index import FriendView
from .views.split.split import SplitView

urlpatterns = [
    path("user", UserView.as_view()),
    path("user/login", LoginView.as_view()),
    path("user/logout", LogoutView.as_view()),
    path("user/self", UserSelfView.as_view()),
    path("notify", NotifyView.as_view()),
    path("notify/<str:notify_id>", NotifyReadView.as_view()),
    path("asset", AssetView.as_view()),
    path("asset/category", UsageCategoryView.as_view()),
    path("loan/lend", LendView.as_view()),
    path("loan/borrowed", BorrowedView.as_view()),
    path("loan/checkout/<str:loan_id>", LoanCheckoutView.as_view()),
    path("loan/remind/<str:loan_id>", LoanRemindView.as_view()),
    path("friend", FriendView.as_view()),
    path("split", SplitView.as_view()),
]
