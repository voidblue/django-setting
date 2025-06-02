"""
URL configuration for djangosetting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#프로젝트 전체의 라우팅 설정

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.controller.user_view_set import UserViewSet
from api.controller.review_view_set import ReviewViewSet
from api.controller.swagger import schema_view

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register(r'users', UserViewSet) #itemviewset 과 item이라는 router 등록
router.register(r'reviews', ReviewViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # Swagger/OpenAPI 문서 URL
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # access 재발급
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

