import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestUser:
    def test_user_register(self, client):
        data = {
            "email": "test@example.com",
            "password": "test_password",
        }

        url = reverse("register")
        response = client.post(url, data=data)

        assert response.status_code == 201
