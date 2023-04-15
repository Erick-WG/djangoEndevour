from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#importing our custom form.
from .forms import PostForm, EditForm
# importing out models
from .models import Category, Post
#importing our lazy folder
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']


class ArticleView(DetailView):
    model = Post
    template_name = "article.html"

# creating views from the browser.
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    # specifying the form fields. they can also be custom made.
    # fields = "__all__"

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"

    # specifying the form fields. they can also be custom made.
    fields = "__all__"

class UpdatePost(UpdateView):
    model = Post
    template_name = "update_post.html"
    form_class = EditForm
    #fields = ['title', 'title_tag', 'body']



class DeletePost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')







