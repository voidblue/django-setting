from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="My API 문서",
        default_version='v1',
        description="My API 문서입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dev@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
