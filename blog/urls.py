from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    #path('', views.home, name = 'blog-home'),
    path('blog/', PostListView.as_view(), name = 'blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), #url pattern with variable
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
]

#blog/post_list.html
#<app>/<model>_<viewtype>.html
