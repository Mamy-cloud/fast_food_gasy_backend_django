from rest_framework import serializers
from .models import Tacos, Pizzas, Boissons, Contact
from .models import Ingredient_tacos, Ingredient_pizza

#---------------------permet d'afficher les listes d'ingrédients-----------------
class IngredientTacosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_tacos
        fields = ['id', 'name']

class IngredientPizzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_pizza
        fields = ['id', 'name']
#--------------------------------------------------------------------------------

class TacosSerializer(serializers.ModelSerializer):
    ingredients_taco = IngredientTacosSerializer(many=True, read_only=True)
    class Meta:
        
        model = Tacos
        fields = ['id', 'name', 'image_url', 'price', 'vegetarienne', 'ingredients_taco']



class PizzaSerializer(serializers.ModelSerializer):
    ingredients_pizza = IngredientPizzasSerializer(many=True)
    class Meta:
        
        model = Pizzas
        fields = ['id', 'name', 'image_url', 'price', 'vegetarienne', 'ingredients_pizza']

class BoissonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boissons
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
