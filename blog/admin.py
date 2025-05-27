from django.contrib import admin
from .models import Post, PostLike, PostComment, PostCommentLike
from .forms import PostAdminForm

# Register your models here.
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'count_view', 'count_comment', 'count_like', 'created_at')
    list_filter = ('user__username',)
    search_fields = ('user__username', 'user__email', 'title')
    form = PostAdminForm

    
    
@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user',)
    search_fields = ('post', 'user',)
    

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'parent', 'count_like', 'created_at',)
    search_fields = ('user', 'post',)
    
    
@admin.register(PostCommentLike)
class PostCommentLikeAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user',)
    search_fields = ('user',)