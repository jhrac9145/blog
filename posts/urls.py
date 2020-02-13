from django.urls import path
from django.views import debug

from . import views


urlpatterns = [
    path('postlist/', views.PostListView.as_view(), name='post_lists'),
]