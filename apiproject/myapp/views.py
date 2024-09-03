from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Contacts
from myapp.serializers import ContactSerializer

@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        apivar = Contacts.objects.all()
        serializer = ContactSerializer(apivar, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    try:
        dvar = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(dvar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(dvar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dvar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
