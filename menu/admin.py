from django.contrib import admin
from .models import Tacos
from .models import Ingredient_tacos
from .models import Pizzas, Ingredient_pizza
from .models import Boissons
from .models import Contact


#affichage des listes de données dans django

#-----------------partie tacos-------------------------
class Tacos_list_admin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'show_ingredients', 'price', 'vegetarienne')

    def show_ingredients(self, obj):
        return ", ".join([ing.name for ing in obj.ingredients_taco.all()])
    show_ingredients.short_description = "Ingrédients_tacos"


admin.site.register(Tacos, Tacos_list_admin)
admin.site.register(Ingredient_tacos)


#-----------------partie pizza-------------------------
class PizzasAdmin(admin.ModelAdmin): 
    list_display = ('name', 'image_url', 'show_ingredients', 'price', 'vegetarienne') 
    
    def show_ingredients(self, obj): 
        return ", ".join([ing.name for ing in obj.ingredients_pizza.all()]) 
        show_ingredients.short_description = "Pizza_ingredients" 
        
admin.site.register(Pizzas, PizzasAdmin) 
admin.site.register(Ingredient_pizza)

#-----------------partie boisson---------------------------
class BoissonAdmin(admin.ModelAdmin): 
    list_display = ('name', 'image_url', 'price') 
    
admin.site.register(Boissons, BoissonAdmin) 

#-----------------partie contact----------------------------

class ContactAdmin(admin.ModelAdmin): 
    list_display = ('address', 'mobile', 'email') 
    
admin.site.register(Contact, ContactAdmin) 



# Register your models here.
