import pytest
from django.utils import timezone

from menu.models import (
    Ingredient_tacos,
    Tacos,
    Ingredient_pizza,
    Pizzas,
    Boissons,
    Contact,
    Photo,
)


@pytest.mark.django_db
class TestIngredientTacos:

    def test_create_ingredient_tacos(self):
        ingredient = Ingredient_tacos.objects.create(
            name="Poulet"
        )

        assert ingredient.name == "Poulet"
        assert str(ingredient) == "Poulet"


@pytest.mark.django_db
class TestTacos:

    def test_create_tacos(self):
        tacos = Tacos.objects.create(
            name="Tacos Poulet"
        )

        assert tacos.name == "Tacos Poulet"
        assert tacos.price == 10
        assert tacos.vegetarienne is False
        assert str(tacos) == "Tacos Poulet"

    def test_tacos_ingredients(self):
        tacos = Tacos.objects.create(
            name="Tacos Poulet"
        )

        ingredient1 = Ingredient_tacos.objects.create(
            name="Poulet"
        )

        ingredient2 = Ingredient_tacos.objects.create(
            name="Fromage"
        )

        tacos.ingredients_taco.add(
            ingredient1,
            ingredient2
        )

        assert tacos.ingredients_taco.count() == 2
        assert ingredient1 in tacos.ingredients_taco.all()
        assert ingredient2 in tacos.ingredients_taco.all()

    def test_tacos_database_table(self):
        assert Tacos._meta.db_table == "menu_tacos"

    def test_tacos_verbose_name(self):
        assert Tacos._meta.verbose_name == "Tacos"
        assert Tacos._meta.verbose_name_plural == "Tacos"


@pytest.mark.django_db
class TestIngredientPizza:

    def test_create_ingredient_pizza(self):
        ingredient = Ingredient_pizza.objects.create(
            name="Fromage"
        )

        assert ingredient.name == "Fromage"
        assert str(ingredient) == "Fromage"


@pytest.mark.django_db
class TestPizzas:

    def test_create_pizza(self):
        pizza = Pizzas.objects.create(
            name="Pizza Margherita"
        )

        assert pizza.name == "Pizza Margherita"
        assert pizza.price == 10
        assert pizza.vegetarienne is False
        assert str(pizza) == "Pizza Margherita"

    def test_pizza_ingredients(self):
        pizza = Pizzas.objects.create(
            name="Pizza Poulet"
        )

        ingredient1 = Ingredient_pizza.objects.create(
            name="Poulet"
        )

        ingredient2 = Ingredient_pizza.objects.create(
            name="Fromage"
        )

        pizza.ingredients_pizza.add(
            ingredient1,
            ingredient2
        )

        assert pizza.ingredients_pizza.count() == 2
        assert ingredient1 in pizza.ingredients_pizza.all()
        assert ingredient2 in pizza.ingredients_pizza.all()

    def test_ingredient_pizza_reverse_relation(self):
        pizza = Pizzas.objects.create(
            name="Pizza Test"
        )

        ingredient = Ingredient_pizza.objects.create(
            name="Fromage"
        )

        pizza.ingredients_pizza.add(ingredient)

        assert pizza in ingredient.pizzas.all()

    def test_pizza_database_table(self):
        assert Pizzas._meta.db_table == "menu_pizzas"

    def test_pizza_verbose_name(self):
        assert Pizzas._meta.verbose_name == "Pizza"
        assert Pizzas._meta.verbose_name_plural == "Pizzas"


@pytest.mark.django_db
class TestBoissons:

    def test_create_boisson(self):
        boisson = Boissons.objects.create(
            name="Coca Cola"
        )

        assert boisson.name == "Coca Cola"
        assert boisson.price == 10
        assert str(boisson) == "Coca Cola"

    def test_boisson_database_table(self):
        assert Boissons._meta.db_table == "menu_boissons"

    def test_boisson_verbose_name(self):
        assert Boissons._meta.verbose_name == "Boisson"
        assert Boissons._meta.verbose_name_plural == "Boissons"


@pytest.mark.django_db
class TestContact:

    def test_create_contact(self):
        contact = Contact.objects.create(
            address="Antananarivo",
            mobile="0340000000",
            email="contact@example.com",
        )

        assert contact.address == "Antananarivo"
        assert contact.mobile == "0340000000"
        assert contact.email == "contact@example.com"


@pytest.mark.django_db
class TestPhoto:

    def test_create_photo(self):
        photo = Photo.objects.create(
            title="Photo Fast Food",
            image_url="https://example.com/image.jpg",
        )

        assert photo.title == "Photo Fast Food"
        assert photo.image_url == "https://example.com/image.jpg"
        assert photo.uploaded_at is not None
        assert isinstance(photo.uploaded_at, timezone.datetime)
