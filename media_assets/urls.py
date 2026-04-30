from django.urls import path
from . import views

# Create the namespace
app_name = 'media_assets'

urlpatterns = [
    # '' : root path : 8000/
    path('', views.dashboard_view, name='dashboard'),
    # users uploaded media files view
    path('my-media/', views.my_media_view, name='my_media'),
    # user upload media view
    path('upload/', views.upload_view, name='upload_media'),
    # media full detail view
    path('media/<int:pk>/', views.media_detail_view, name='media_detail'),
    # edit view
    path('media/<int:pk>/edit/', views.edit_media_view, name='edit_media'),
    # delete view
    path('media/<int:pk>/delete/', views.delete_media_view, name='delete_media'),
]