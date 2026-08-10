
import pytest
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


@pytest.mark.django_db
class TestURLs:

    def test_admin_url(self):
        """Test that the admin URL is correctly configured."""
        resolver = resolve("/admin/")
        assert resolver.url_name == "index"

    def test_token_obtain_url(self):
        """Test that the JWT token obtain URL is correctly configured."""
        resolver = resolve("/api/token/")
        assert resolver.func.view_class == TokenObtainPairView

    def test_token_refresh_url(self):
        """Test that the JWT token refresh URL is correctly configured."""
        resolver = resolve("/api/token/refresh/")
        assert resolver.func.view_class == TokenRefreshView

    def test_menu_url(self):
        """Test that the menu URL is correctly configured."""
        resolver = resolve("/menu/")
        assert resolver is not None

    def test_root_url(self):
        """Test that the root URL is correctly configured."""
        resolver = resolve("/")
        assert resolver is not None
