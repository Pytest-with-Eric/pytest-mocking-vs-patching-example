import pytest
import requests
from unittest.mock import Mock
from src.cat_api import CatFact


@pytest.fixture
def cat_fact():
    """
    Fixture to create an instance of the CatFact class.
    """
    yield CatFact()


@pytest.fixture
def mock_response():
    yield {
        "status_code": 200,
        "response": {"data": "Cats are amazing!"},
    }


def test_get_cat_fact_no_mock(cat_fact):
    """
    Test the get_cat_fact method of the CatFact class (No mocking or patching).
    """
    response = cat_fact.get_cat_fact()
    assert response["status_code"] == 200


def test_get_cat_fact_mock(cat_fact, mock_response):
    """
    Test the get_cat_fact method of the CatFact class (With Mocking).
    """

    # Create a mock for the get_cat_fact method
    cat_fact.get_cat_fact = Mock(return_value=mock_response)

    # Call the method
    response = cat_fact.get_cat_fact()

    # Assert the mock was called once
    cat_fact.get_cat_fact.assert_called_once()

    # Assert the expected response
    assert response == mock_response


def test_get_cat_fact_patch(mocker, cat_fact, mock_response):
    """
    Test the get_cat_fact method of the CatFact class (with Patching).
    """

    # Use mocker to patch the get_cat_fact method of the CatFact class and get a reference to the mock
    mock_get_cat_fact = mocker.patch(
        "src.cat_api.CatFact.get_cat_fact", return_value=mock_response
    )

    # Call the method
    response = cat_fact.get_cat_fact()

    # Assert the mock was called once
    mock_get_cat_fact.assert_called_once()

    # Assert the expected response
    assert response == mock_response
