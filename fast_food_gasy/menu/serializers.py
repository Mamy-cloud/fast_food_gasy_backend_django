from rest_framework import serializers
from .models import Tacos, Pizzas, Boissons

class TacosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tacos
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzas
        fields = '__all__'

class BoissonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boissons
        fields = '__all__'
