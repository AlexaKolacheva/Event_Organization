from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'events', views.EventViewSet)
# router.register(r'comments', views.CommentsViewSet)
router.register(r'participations', views.ParticipationViewSet)

urlpatterns = []

urlpatterns += router.urls
