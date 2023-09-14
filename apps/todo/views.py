from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer

class TaskAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'title', 'description', 'is_completed']
    search_fields = ['user__username', 'title', 'description']
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ToDoPermission(), )
        return (AllowAny(), )
    
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class ToDoAllDeleteAPIViewSet(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    
    def delete(self, request, *args, **kwargs):
        todo = Task.objects.filter(user=request.user)
        todo = delete()
        return Response({'delete' : 'Все  удалены'}) 