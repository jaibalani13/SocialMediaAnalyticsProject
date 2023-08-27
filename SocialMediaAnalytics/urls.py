from django.contrib import admin
from django.urls import path
from .views import SocialMediaPostCreateView, SocialMediaPostAnalysisView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/', SocialMediaPostCreateView.as_view(), name='post-create'),
    path('api/v1/posts/<int:pk>/analysis/', SocialMediaPostAnalysisView.as_view(), name='post-analysis'),

]
