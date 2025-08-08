from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, Comment
from .serializers import RegisterSerializers, postSerializers, CommentSerializers
from .permission import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDestroy(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


