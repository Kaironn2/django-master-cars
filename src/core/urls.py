from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from accounts.views import UserCreateView, UserLoginView, UserLogoutView
from cars.views import (
    CarDeleteView,
    CarDetailView,
    CarsView,
    CarUpdateView,
    NewCarView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('cars_list', permanent=False)),
    path('cars/', CarsView.as_view(), name='cars_list'),
    path('new_car/', NewCarView.as_view(), name='new_car'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
