from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + "  |  " + str(self.author) # remember to pass in the author object as a string


# Getting the absolute url path, in this case for the redirect when post is created from the browser.
    def get_absolute_url(self):
        #return reverse ('article', args=(str(self.id)))
        return reverse ('home')











