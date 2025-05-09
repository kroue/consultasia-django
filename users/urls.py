from django.urls import path
from .views import register_user, login_user  # Import your views

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),  # ✅ Add login route
]
