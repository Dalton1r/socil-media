from django.db import models
from django.contrib.auth.models import Group
from accounting.models import CustomUser, AbstractUser


class GroupCustom(Group):
    title = models.CharField(max_length=30)
    group_image = models.ImageField(upload_to='media\gp_image', null=True, blank=True)
    bio = models.CharField(max_length=30, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'this group name {self.name} with this {self.title}'


class GroupMember(models.Model):
    group = models.ForeignKey(GroupCustom, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='user_groups', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_day = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='media\post_image', null=True, blank=True)
    gp = models.ManyToManyField(GroupCustom)
    status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.title} created by {self.user.email} for {self.gp.name} group'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} left a comment on {self.post.title}'


class BookmarkModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email} has {self.post.count()} bookmark on {self.post.name}'


class LikeModel(models.Model):
    # votes = (
    #     ('l', 'like'),
    #     ('dis', 'dislike')
    # )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # vote = models.CharField(max_length=10, choices=votes)

    vote = models.BooleanField(default=1, null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} {self.vote} the {self.post.title}'
