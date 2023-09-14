from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.users.permissions import PostPermission
from apps.users.models import User
from apps.users.serializers import UserRegisterSerializer, UserSerializer, UserDetailSerializer


class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = PostPermission

    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        elif self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return(PostPermission(),)
        return(AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)