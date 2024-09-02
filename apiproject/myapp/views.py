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
