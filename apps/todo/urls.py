from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskAPIViewSet,ToDoAllDeleteAPIViewSet

# from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register('tasks', TaskAPIViewSet, 'tasks')

urlspatterns = [
    path("delete/", ToDoAllDeleteAPIViewSet.as_view(), name='delete'),
]

urlpatterns = router.urls