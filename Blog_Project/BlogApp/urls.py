from django.urls import path, include
#from . import views
from .views import HomeView, ArticleView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    # The angle brackets are used to specify the data in the db
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
]
