from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'comments', views.CommentsViewSet)
router.register(r'reviews', views.ReviewViewSet)


urlpatterns = []

urlpatterns += router.urls