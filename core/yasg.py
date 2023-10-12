from django.urls import path
from drf_yasg import openapi
from drf_yasg.views  import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="accounts Documentation",
        default_version="V1",
        description="The EventOrganization API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alexakola4eva@gmail.com"),
        liscense = openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-documentation'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-documentation'),
]