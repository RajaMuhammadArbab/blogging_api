from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('posts/', views.PostListCreate.as_view()),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view()),
    path('comments/', views.CommentListCreate.as_view()),
    path('comments/<int:pk>/', views.CommentDestroy.as_view()),
]
