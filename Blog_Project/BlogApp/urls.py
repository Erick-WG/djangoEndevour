from django.urls import path
#from . import views
from .views import HomeView, ArticleView, AddPostView, UpdatePost, DeletePost, AddCategoryView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    # The angle brackets are used to specify the data in the db
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('Create_post/', AddPostView.as_view(), name="add_post"),
    path('Create_Category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePost.as_view(), name = "delete_post"),

]
