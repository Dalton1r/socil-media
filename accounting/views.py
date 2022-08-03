from django.shortcuts import render
from accounting.models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounting.serializers import UserSerializer


@api_view(['GET'])
def apiaccountingoverview(request):
    overview = {
        'accounting-detail': 'detail of specific users',
        'accounting-list': 'list of all users in our site',
        'accounting-update': 'update of specific user by id',
        'accounting-create': 'create a user ',
        'accounting-delete': 'delete a user'

    }
    return Response(overview)


@api_view(['GET'])
def accountinglist(request):
    accountingobj = CustomUser.objects.all()
    serializerobj = UserSerializer(data=accountingobj, many=True)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['GET'])
def accountingdetail(request, pk):
    accountingobj = CustomUser.objects.get(id=pk)
    serializerobj = UserSerializer(data=accountingobj, many=False)
    if serializerobj.is_valid():
        return Response(serializerobj.data)


@api_view(['PUT'])
def accountingupdate(request, pk):
    accountingobj = CustomUser.objects.get(id=pk)
    serializerobj = UserSerializer(data=request.data, instance=accountingobj)
    if serializerobj.is_valid():
        return serializerobj.save()
    Response(serializerobj.data)


@api_view(['POST'])
def accountingcreate(request):
    serializerobj = UserSerializer(data=request.data)
    if serializerobj.is_valid():
        return serializerobj.save()

    Response(serializerobj.data)


@api_view(['DELETE'])
def accountingdelete(request, pk):
    accountingobj = CustomUser.objects.get(id=pk)
    accountingobj.delete()
    return Response('delete is suceesful')
