import os


def test_wsgi_application():
    """Test that the WSGI application is correctly initialized."""

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "fast_food_gasy.settings"
    )

    from fast_food_gasy.wsgi import application

    assert application is not None