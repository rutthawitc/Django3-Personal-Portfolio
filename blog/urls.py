from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog, name='blog-page'),
    path('<int:blog_id>', views.detail, name='blog-detail'),

]