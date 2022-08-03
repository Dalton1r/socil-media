from group.models import GroupCustom, Post, Comment, BookmarkModel, LikeModel, GroupMember
from rest_framework.decorators import api_view
from rest_framework.response import Response
from group.serializers import Groupserializer, Groupallserializer, Postserializer, Commentserializer, \
    LikeModelserializer, Groupmemberserializer, BookmarkModelserializer


@api_view(['GET'])
def overviewlist(request):
    overview = {
        'group-list': 'list of all group',
        'group-detail': 'detail of specific group',
        'group-update': 'update of specific group',
        'group-create': 'create your own group',
        'group-delete': 'delete your own group',
        'post-list': 'list of all post',
        'post-detail': 'detail of specific post',
        'post-update': 'update of specific post',
        'post-create': 'create your own post',
        'post-delete': 'delete your own post',
        'commnet-list': 'list of all commnet',
        'commnet-detail': 'detail of specific commnet',
        'commnet-update': 'update of specific commnet',
        'commnet-create': 'create your own commnet',
        'commnet-delete': 'delete your own commnet',
        'groupmember-list': 'list of all groupmember',
        'groupmember-detail': 'detail of specific groupmember',
        'groupmember-update': 'update of specific groupmember',
        'groupmember-create': 'create your own groupmember',
        'groupmember-delete': 'delete your own groupmember',
        'bookmark-list': 'list of all bookmark',
        'bookmark-detail': 'detail of specific bookmark',
        'bookmark-update': 'update of specific bookmark',
        'bookmark-create': 'create your own bookmark',
        'bookmark-delete': 'delete your own bookmark',
        'like-list': 'list of all like',
        'like-detail': 'detail of specific like',
        'like-update': 'update of specific like',
        'like-create': 'create your own like',
        'like-delete': 'delete your own like',

    }
    return Response(overview)


@api_view(['GET'])
def grouplist(request):
    grouplistobj = GroupCustom.objects.all()
    serializerobj = Groupallserializer(data=grouplistobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def groupdetail(request, pk):
    groupobj = GroupCustom.objects.get(id=pk)
    serializerobj = Groupserializer(data=groupobj, many=False)
    return Response(serializerobj.data)


@api_view(['PUT'])
def groupupdate(request, pk):
    groupobj = GroupCustom.objects.get(id=pk)
    serializerobj = Groupallserializer(data=request.data, instance=groupobj)
    if serializerobj.is_valid():
        serializerobj.save()
    return Response(serializerobj.data)


@api_view(['POST'])
def groupcreate(request):
    serializerobj = Groupallserializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def groupdelete(request, pk):
    groupobj = GroupCustom.objects.get(id=pk)
    groupobj.delete()
    return Response('delete is suceesful')


@api_view(['GET'])
def postlist(request):
    postobj = Post.objects.all()
    serializerobj = Postserializer(data=postobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def postdetail(request, pk):
    postobj = Post.objects.get(id=pk)
    serializerobj = Postserializer(data=postobj, many=False)
    return Response(serializerobj.data)


@api_view(['PUT'])
def postupdate(request, pk):
    postobj = Post.objects.get(id=pk)
    serializerobj = Postserializer(data=request.data, instance=postobj)
    if serializerobj.is_valid():
        serializerobj.save()
    return Response(serializerobj.data)


@api_view(['POST'])
def postcreate(request):
    serializerobj = Postserializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def postdelete(request, pk):
    postobj = Post.objects.get(id=pk)
    postobj.delete()
    return Response('delete is suceesful')


@api_view(['GET'])
def commnetlist(request):
    commntobj = Comment.objects.all()
    serializerobj = Commentserializer(data=commntobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def commnetdetail(request, pk):
    commntobj = Comment.objects.get(id=pk)
    serializerobj = Commentserializer(data=commntobj, many=False)
    return Response(serializerobj.data)


@api_view(['PUT'])
def commnetupdate(request, pk):
    commntobj = Comment.objects.get(id=pk)
    serializerobj = Commentserializer(data=request.data, instance=commntobj)
    if serializerobj.is_valid():
        serializerobj.save()
    return Response(serializerobj.data)


@api_view(['POST'])
def commnetcreate(request):
    serializerobj = Commentserializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def commnetdelete(request, pk):
    commntobj = Comment.objects.get(id=pk)
    commntobj.delete()
    return Response('delete is suceesful')


@api_view(['GET'])
def likelist(request):
    likeobj = LikeModel.objects.all()
    serializerobj = LikeModelserializer(data=likeobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def likedetail(request, pk):
    likeobj = LikeModel.objects.get(id=pk)
    serializerobj = LikeModelserializer(data=likeobj, many=False)
    return Response(serializerobj.data)


@api_view(['PUT'])
def likeupdate(request, pk):
    likeobj = LikeModel.objects.get(id=pk)
    serializerobj = LikeModelserializer(data=request.data, instance=likeobj)
    if serializerobj.is_valid():
        serializerobj.save()
    return Response(serializerobj.data)


@api_view(['POST'])
def likecreate(request):
    serializerobj = LikeModelserializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def likedelete(request, pk):
    likeobj = LikeModel.objects.get(id=pk)
    likeobj.delete()
    return Response('delete is suceesful')


@api_view(['GET'])
def bookmarklist(request):
    bookmarkobj = BookmarkModel.objects.all()
    serializerobj = BookmarkModelserializer(data=bookmarkobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def bookmarkdetail(request, pk):
    bookmarkobj = BookmarkModel.objects.get(id=pk)
    serializerobj = BookmarkModelserializer(data=bookmarkobj, many=False)
    return Response(serializerobj.data)


@api_view(['PUT'])
def bookmarkupdate(request, pk):
    bookmarkobj = BookmarkModel.objects.get(id=pk)
    serializerobj = BookmarkModelserializer(data=request.data, instance=bookmarkobj)
    if serializerobj.is_valid():
        serializerobj.save()
    return Response(serializerobj.data)


@api_view(['POST'])
def bookmarkcreate(request):
    serializerobj = BookmarkModelserializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def bookmarkdelete(request, pk):
    bookmarkobj = BookmarkModel.objects.get(id=pk)
    bookmarkobj.delete()
    return Response('delete is suceesful')


@api_view(['GET'])
def groupmemberlist(request):
    groupmemberobj = GroupMember.objects.all()
    serializerobj = Groupmemberserializer(data=groupmemberobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def groupmemberdetail(request, pk):
    groupmemberobj = GroupMember.objects.get(id=pk)
    serializerobj = Groupmemberserializer(data=groupmemberobj, many=False)
    return Response(serializerobj.data)


@api_view(['PUT'])
def groupmemberupdate(request, pk):
    groupmemberobj = GroupMember.objects.get(id=pk)
    serializerobj = Groupmemberserializer(data=request.data, instance=groupmemberobj)
    if serializerobj.is_valid():
        serializerobj.save()
    return Response(serializerobj.data)


@api_view(['POST'])
def groupmembercreate(request):
    serializerobj = Groupmemberserializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def groupmemberdelete(request, pk):
    groupmemberobj = GroupMember.objects.get(id=pk)
    groupmemberobj.delete()
    return Response('delete is suceesful')
