import pytest
from rest_framework.test import APIClient
from rest_framework import status

from menu.models import (
    Tacos,
    Pizzas,
    Boissons,
)
from menu.views import (
    TacosAPI,
    PizzaAPI,
    BoissonAPI,
    TacosViewSet,
    PizzaViewSet,
    BoissonViewSet,
)


@pytest.mark.django_db
class TestIndexView:

    def test_index_view(self, client):
        """Test that the index page loads correctly."""

        response = client.get("/")

        assert response.status_code == status.HTTP_200_OK
        assert "tacos" in response.context
        assert "pizzas" in response.context
        assert "boissons" in response.context
        assert "contacts" in response.context


@pytest.mark.django_db
class TestTacosAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_get_tacos(self):
        """Test GET request for tacos."""

        Tacos.objects.create(
            name="Tacos Poulet",
            price=15000,
            vegetarienne=False,
        )

        response = self.client.get("/api/tacos/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == "Tacos Poulet"

    def test_get_empty_tacos(self):
        """Test GET request when there are no tacos."""

        response = self.client.get("/api/tacos/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == []

    def test_post_tacos(self):
        """Test POST request for creating a taco."""

        data = {
            "name": "Tacos Poulet",
            "price": 15000,
            "vegetarienne": False,
        }

        response = self.client.post(
            "/api/tacos/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == "Tacos Poulet"

        assert Tacos.objects.filter(
            name="Tacos Poulet"
        ).exists()

    def test_post_invalid_tacos(self):
        """Test POST request with invalid taco data."""

        data = {
            "price": 15000,
        }

        response = self.client.post(
            "/api/tacos/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestPizzaAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_get_pizzas(self):
        """Test GET request for pizzas."""

        Pizzas.objects.create(
            name="Pizza Margherita",
            price=20000,
            vegetarienne=True,
        )

        response = self.client.get("/api/pizzas/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == "Pizza Margherita"

    def test_post_pizza(self):
        """Test POST request for creating a pizza."""

        data = {
            "name": "Pizza Margherita",
            "price": 20000,
            "vegetarienne": True,
        }

        response = self.client.post(
            "/api/pizzas/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == "Pizza Margherita"

        assert Pizzas.objects.filter(
            name="Pizza Margherita"
        ).exists()


@pytest.mark.django_db
class TestBoissonAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_get_boissons(self):
        """Test GET request for drinks."""

        Boissons.objects.create(
            name="Coca Cola",
            price=5000,
        )

        response = self.client.get("/api/boissons/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == "Coca Cola"

    def test_post_boisson(self):
        """Test POST request for creating a drink."""

        data = {
            "name": "Coca Cola",
            "price": 5000,
        }

        response = self.client.post(
            "/api/boissons/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == "Coca Cola"

        assert Boissons.objects.filter(
            name="Coca Cola"
        ).exists()


class TestViewSetConfiguration:

    def test_tacos_viewset(self):
        """Test TacosViewSet configuration."""

        assert TacosViewSet.queryset.model == Tacos
        assert TacosViewSet.serializer_class.__name__ == "TacosSerializer"

    def test_pizza_viewset(self):
        """Test PizzaViewSet configuration."""

        assert PizzaViewSet.queryset.model == Pizzas
        assert PizzaViewSet.serializer_class.__name__ == "PizzaSerializer"

    def test_boisson_viewset(self):
        """Test BoissonViewSet configuration."""

        assert BoissonViewSet.queryset.model == Boissons
        assert BoissonViewSet.serializer_class.__name__ == "BoissonSerializer"
