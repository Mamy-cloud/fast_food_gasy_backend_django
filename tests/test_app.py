
from django.apps import apps

from menu.apps import MenuConfig


def test_menu_app_config():
    """Test that the Menu application configuration is correct."""

    assert MenuConfig.name == "menu"
    assert MenuConfig.default_auto_field == "django.db.models.BigAutoField"


def test_menu_app_is_installed():
    """Test that the menu application is installed in Django."""

    config = apps.get_app_config("menu")

    assert config.name == "menu"
    assert isinstance(config, MenuConfig)
