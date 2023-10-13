from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'events', views.EventViewSet)
# router.register(r'comments', views.CommentsViewSet)
router.register(r'participations', views.ParticipationViewSet)

urlpatterns = []

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
