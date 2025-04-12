from django.urls import path

# from .views import UserDetail, UserList
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', UserViewSet, basename='user')
urlpatterns = router.urls
# urlpatterns = [
#     # path('users/', UserList.as_view(), name='user-list'),
#     # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail')
# ]
