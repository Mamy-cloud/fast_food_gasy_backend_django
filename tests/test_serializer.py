import pytest

from menu.models import Tacos, Pizzas, Boissons
from menu.serializers import (
    TacosSerializer,
    PizzaSerializer,
    BoissonSerializer,
)


@pytest.mark.django_db
class TestTacosSerializer:

    def test_tacos_serializer(self):
        tacos = Tacos.objects.create(
            name="Tacos Poulet",
            price=15000,
            vegetarienne=False,
        )

        serializer = TacosSerializer(tacos)

        assert serializer.data["name"] == "Tacos Poulet"
        assert serializer.data["price"] == 15000
        assert serializer.data["vegetarienne"] is False

    def test_tacos_serializer_contains_all_fields(self):
        tacos = Tacos.objects.create(
            name="Tacos Test",
        )

        serializer = TacosSerializer(tacos)

        expected_fields = {
            "id",
            "name",
            "image",
            "ingredients_taco",
            "price",
            "vegetarienne",
        }

        assert set(serializer.data.keys()) == expected_fields


@pytest.mark.django_db
class TestPizzaSerializer:

    def test_pizza_serializer(self):
        pizza = Pizzas.objects.create(
            name="Pizza Margherita",
            price=20000,
            vegetarienne=True,
        )

        serializer = PizzaSerializer(pizza)

        assert serializer.data["name"] == "Pizza Margherita"
        assert serializer.data["price"] == 20000
        assert serializer.data["vegetarienne"] is True

    def test_pizza_serializer_contains_all_fields(self):
        pizza = Pizzas.objects.create(
            name="Pizza Test",
        )

        serializer = PizzaSerializer(pizza)

        expected_fields = {
            "id",
            "name",
            "image",
            "ingredients_pizza",
            "price",
            "vegetarienne",
        }

        assert set(serializer.data.keys()) == expected_fields


@pytest.mark.django_db
class TestBoissonSerializer:

    def test_boisson_serializer(self):
        boisson = Boissons.objects.create(
            name="Coca Cola",
            price=5000,
        )

        serializer = BoissonSerializer(boisson)

        assert serializer.data["name"] == "Coca Cola"
        assert serializer.data["price"] == 5000

    def test_boisson_serializer_contains_all_fields(self):
        boisson = Boissons.objects.create(
            name="Coca Cola",
        )

        serializer = BoissonSerializer(boisson)

        expected_fields = {
            "id",
            "name",
            "image",
            "price",
        }

        assert set(serializer.data.keys()) == expected_fields


class TestSerializerValidation:

    def test_tacos_serializer_valid_data(self):
        data = {
            "name": "Tacos Poulet",
            "price": 15000,
            "vegetarienne": False,
        }

        serializer = TacosSerializer(data=data)

        assert serializer.is_valid()

    def test_pizza_serializer_valid_data(self):
        data = {
            "name": "Pizza Margherita",
            "price": 20000,
            "vegetarienne": True,
        }

        serializer = PizzaSerializer(data=data)

        assert serializer.is_valid()

    def test_boisson_serializer_valid_data(self):
        data = {
            "name": "Coca Cola",
            "price": 5000,
        }

        serializer = BoissonSerializer(data=data)

        assert serializer.is_valid()