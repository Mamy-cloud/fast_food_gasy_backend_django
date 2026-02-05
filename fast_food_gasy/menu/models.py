from django.db import models


#----------------------Liste des tacos------------------------------

class Ingredient_tacos(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tacos(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tacos_images/')
    ingredients_taco = models.ManyToManyField(Ingredient_tacos)
    price = models.FloatField(default=10)
    vegetarienne = models.BooleanField(default=False)

    class Meta: 
        db_table = "menu_tacos" 
        verbose_name = "Tacos" 
        verbose_name_plural = "Tacos"

    def __str__(self):
        return self.name


#----------------------Liste des pizzas------------------------------

class Ingredient_pizza(models.Model): 
    name = models.CharField(max_length=100) 

        
    def __str__(self): 
        return self.name 
    
class Pizzas(models.Model): 
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='pizza_images/') 
    ingredients_pizza = models.ManyToManyField(Ingredient_pizza, related_name="pizzas") 
    price = models.FloatField(default=10) 
    vegetarienne = models.BooleanField(default=False) 
    
    class Meta: 
        db_table = "menu_pizzas" 
        verbose_name = "Pizza" 
        verbose_name_plural = "Pizzas"
        
    def __str__(self): 
        return self.name 


#----------------------Liste des boissons------------------------------

class Boissons(models.Model): 
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='boisson_image/') 
    price = models.FloatField(default=10)     

    
    class Meta: 
        db_table = "menu_boissons" 
        verbose_name = "Boisson" 
        verbose_name_plural = "Boissons"

    def __str__(self): 
        return self.name 
    
#----------------------Liste des contacts----------------------------

class Contact(models.Model):
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=16)
    email = models.EmailField(max_length=60)
# Create your models here.
#---------------------relier supabase et railway-----------------------
class Photo(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()  # lien vers Supabase
    uploaded_at = models.DateTimeField(auto_now_add=True)
