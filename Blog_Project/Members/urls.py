from django.urls import path
#from . import views
from .views import CreateUserForm

urlpatterns = [
    path('register/', CreateUserForm.as_view(), name="register"),
]
