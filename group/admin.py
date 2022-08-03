from django.contrib import admin
from group.models import LikeModel, BookmarkModel, Post, Comment

admin.site.register(LikeModel)
admin.site.register(BookmarkModel)
admin.site.register(Post)
admin.site.register(Comment)
