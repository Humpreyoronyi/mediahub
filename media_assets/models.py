from django.db import models
from django.conf import settings
import cloudinary 
from cloudinary.models import CloudinaryField

# Create your models here.
class MediaAssets(models.Model):
    CATEGORY_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="Uploaded and maintained by MediaHUB")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='image')
    media_file = CloudinaryField('media', resource_type='auto') # Cloudinary in use
    # relationship attribute  # Object relationship - 'has a' : one user can have many uploads

    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='media_assets')
    created_at = models.DateTimeField(auto_now_add=True) # Automatically capture the time when the record is inserted
    updated_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)

    # Always display media in order of creation
    class meta:
        ordering = ['-created_at']

    # Editing rights
    def can_edit(self, user):
        '''check if user has editing rights'''
        return user == self.uploaded_by or user.is_teacher() or user.is_superuser()
    
    # DElete rights
    def can_delete(self, user):
        '''check if user can delete'''
        return user == self.uploaded_by or user.is_teacher() or user.is_superuser()
    # Return the object name i.e media asset
    def __str__():
        return self.title
    
    
    
