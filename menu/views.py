from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
from .models import Tacos
from .models import Pizzas
from .models import Boissons
from .models import Contact

#-----------importation création API-------------------------#
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tacos, Pizzas, Boissons
from .serializers import TacosSerializer, PizzaSerializer, BoissonSerializer
#-------------------------------------------------------------


#--------------------------création vue de django-------------------------
def index(request):

    tacos = Tacos.objects.all()
    pizzas = Pizzas.objects.all()
    boissons = Boissons.objects.all()
    contact = Contact.objects.all()
    return render(request, 'menu/index.html', 
                  {'tacos': tacos,
                   'pizzas': pizzas,
                   'boissons': boissons,
                   'contacts': contact,
                   })




#------------------création API JSON------------------------
#API tacos
class TacosAPI(APIView):

    def get(self, request):
        tacos = Tacos.objects.all()
        serializer = TacosSerializer(tacos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TacosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#API pizza
class PizzaAPI(APIView):

    def get(self, request):
        pizzas = Pizzas.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
#API boissons
class BoissonAPI(APIView):

    def get(self, request):
        boissons = Boissons.objects.all()
        serializer = BoissonSerializer(boissons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoissonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
#-------------------auth JWT for API-------------------------------------------
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

class TacosViewSet(ModelViewSet):
    queryset = Tacos.objects.all()
    serializer_class = TacosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PizzaViewSet(ModelViewSet):
    queryset = Pizzas.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BoissonViewSet(ModelViewSet):
    queryset = Boissons.objects.all()
    serializer_class = BoissonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create your views here.
