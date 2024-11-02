from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts', views.post, name='posts-page'),
    path('post/<slug:slug>', views.single_post, name='post-detail-page'), #toplearn.com/post/newPost, as we got int, str we also have slug
]
