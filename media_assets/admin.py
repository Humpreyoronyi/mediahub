# from django.contrib import admin
# from .models import MediaAssets

# # Register your model here
# @admin.register(MediaAssets)
# class MediaAssetsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category','uploaded_by','is_public','view_count', 'created_at' )
#     list_filter = ('category', 'is_public', 'created_at')
#     search_fields = ('title', 'description', 'uploaded_by__username')
#     '''
#     admin can only view read only fields can never edit
#     '''
#     # readonly_fields = ('created_by', 'updated_at', 'view_count')
#     data_hierarchy = 'created_at' #Data ordering

    
# # Register your models here.
from django.contrib import admin
from .models import MediaAssets
# Register your models here.
@admin.register(MediaAssets)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = ('title','category','uploaded_by','is_public',
    'views_count','created_at')
    list_filter = ('category','is_public','created_at')
    search_fields = ('title','description','uploaded_by__username')
    '''admin can only view read only fields can never edit'''
    # readonly_fields = ('created_by','updated_at','views_count')
    data_hierarchy = 'created_at' # data ordering 
