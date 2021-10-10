import os
import tempfile

import pytest
from flask import Flask
from app import app as flask_app


def test_health():
    with flask_app.test_client() as test_client:
        response = test_client.get('/health')
        assert response.status_code == 200
        assert response.get_json().get('ok') is True
