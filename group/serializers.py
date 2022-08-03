from rest_framework import serializers
from group.models import GroupCustom, GroupMember, Post, Comment, LikeModel, BookmarkModel
from accounting.models import CustomUser
from accounting.serializers import UserSerializer


class Groupserializer(serializers.ModelSerializer):
    owner = UserSerializer(many=True, read_only=True)

    class Meta:
        model = GroupCustom
        fields = ['bio', 'owner', 'title', 'group_image']


class Groupallserializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCustom
        fields = '__all__'


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class Groupmemberserializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'


class LikeModelserializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = '__all__'


class BookmarkModelserializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkModel
        fields = '__all__'
