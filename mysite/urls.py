from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intro.urls')),  # 홈페이지 루트 주소 연결
]
