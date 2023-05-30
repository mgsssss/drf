from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .serializers import KospiSerializer
from .models import Kospi


class KospiList(APIView):
    
    def get(self, requst, format=None):
        kospi = Kospi.objects.all()
        serializer = KospiSerializer(kospi, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = KospiSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class KospiDetail(APIView):
    def get(self, request, pk, format=None):
        kospi = get_object_or_404(Kospi, id=pk)
        serializer = KospiSerializer(kospi)
        return Response(serializer.data)
    
    def put(self, request, pk):
        kospi = get_object_or_404(Kospi, id=pk)
        serializer = KospiSerializer(kospi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        kospi = get_object_or_404(Kospi, id=pk)
        kospi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)