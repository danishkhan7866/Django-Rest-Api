from django.contrib import admin
from django.urls import path
from records import views
from userlog.views import RegistrationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forstudent/', views.Studentlist.as_view()),
    path('forteachers/', views.StudentlistCreate.as_view()),
    path('forsuperadmin/<int:pk>/', views.StudentRetrieveupdateDestroy.as_view()),
    path('auth/register/', views.RegistrationAPIView.as_view(), name ='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name ='Login'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name ='refreshtoken'),



]
