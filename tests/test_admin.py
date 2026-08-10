
import pytest
from django.contrib import admin

from menu.models import (
    Tacos,
    Ingredient_tacos,
    Pizzas,
    Ingredient_pizza,
    Boissons,
    Contact,
)

from menu.admin import (
    Tacos_list_admin,
    PizzasAdmin,
    BoissonAdmin,
    ContactAdmin,
)


@pytest.mark.django_db
class TestAdmin:

    def test_tacos_is_registered(self):
        """Test that Tacos is registered in Django admin."""
        assert Tacos in admin.site._registry

    def test_ingredient_tacos_is_registered(self):
        """Test that Ingredient_tacos is registered in Django admin."""
        assert Ingredient_tacos in admin.site._registry

    def test_pizzas_is_registered(self):
        """Test that Pizzas is registered in Django admin."""
        assert Pizzas in admin.site._registry

    def test_ingredient_pizza_is_registered(self):
        """Test that Ingredient_pizza is registered in Django admin."""
        assert Ingredient_pizza in admin.site._registry

    def test_boissons_is_registered(self):
        """Test that Boissons is registered in Django admin."""
        assert Boissons in admin.site._registry

    def test_contact_is_registered(self):
        """Test that Contact is registered in Django admin."""
        assert Contact in admin.site._registry

    def test_tacos_admin_configuration(self):
        """Test the Tacos admin configuration."""
        admin_instance = admin.site._registry[Tacos]

        assert isinstance(admin_instance, Tacos_list_admin)
        assert admin_instance.list_display == (
            "name",
            "image",
            "show_ingredients",
            "price",
            "vegetarienne",
        )

    def test_pizzas_admin_configuration(self):
        """Test the Pizzas admin configuration."""
        admin_instance = admin.site._registry[Pizzas]

        assert isinstance(admin_instance, PizzasAdmin)
        assert admin_instance.list_display == (
            "name",
            "image",
            "show_ingredients",
            "price",
            "vegetarienne",
        )

    def test_boissons_admin_configuration(self):
        """Test the Boissons admin configuration."""
        admin_instance = admin.site._registry[Boissons]

        assert isinstance(admin_instance, BoissonAdmin)
        assert admin_instance.list_display == (
            "name",
            "image",
            "price",
        )

    def test_contact_admin_configuration(self):
        """Test the Contact admin configuration."""
        admin_instance = admin.site._registry[Contact]

        assert isinstance(admin_instance, ContactAdmin)
        assert admin_instance.list_display == (
            "address",
            "mobile",
            "email",
        )

    def test_tacos_show_ingredients(self):
        """Test that Tacos ingredients are correctly displayed."""
        admin_instance = admin.site._registry[Tacos]

        tacos = Tacos.objects.create(
            name="Tacos Test",
            price=10000,
            vegetarienne=False,
        )

        ingredient1 = Ingredient_tacos.objects.create(
            name="Poulet"
        )

        ingredient2 = Ingredient_tacos.objects.create(
            name="Fromage"
        )

        tacos.ingredients_taco.add(ingredient1, ingredient2)

        result = admin_instance.show_ingredients(tacos)

        assert result == "Poulet, Fromage"

    def test_pizza_show_ingredients(self):
        """Test that Pizza ingredients are correctly displayed."""
        admin_instance = admin.site._registry[Pizzas]

        pizza = Pizzas.objects.create(
            name="Pizza Test",
            price=15000,
            vegetarienne=False,
        )

        ingredient1 = Ingredient_pizza.objects.create(
            name="Fromage"
        )

        ingredient2 = Ingredient_pizza.objects.create(
            name="Jambon"
        )

        pizza.ingredients_pizza.add(ingredient1, ingredient2)

        result = admin_instance.show_ingredients(pizza)

        assert result == "Fromage, Jambon"