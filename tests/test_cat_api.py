import pytest
import requests
from src.cat_api import CatFact


@pytest.fixture
def cat_fact():
    """
    Fixture to create an instance of the CatFact class.
    """
    yield CatFact()


def test_get_cat_fact_no_mock(cat_fact):
    """
    Test the get_cat_fact method of the CatFact class (No mocking or patching).
    """
    response = cat_fact.get_cat_fact()
    print(response)
    assert response["status_code"] == 200


def test_get_cat_fact_success(mocker, cat_fact):
    """
    Test the get_cat_fact method of the CatFact class (With Mocking and Patching).
    """
    # Mock response data, ensuring it matches the structure the real method would return
    mock_response_data = {
        "status_code": 200,
        "response": {
            "data": "Cats are amazing!"
        },  # Make sure this matches the actual response structure
    }

    # Use mocker to patch the get_cat_fact method of the CatFact class and get a reference to the mock
    mock_get_cat_fact = mocker.patch(
        "src.cat_api.CatFact.get_cat_fact", return_value=mock_response_data
    )

    # Call the method
    response = cat_fact.get_cat_fact()

    # Assert the mock was called once
    mock_get_cat_fact.assert_called_once()

    # Assert the expected response
    assert response == mock_response_data, "Expected mock response data not returned"


def test_get_cat_fact_success_stub(mocker):
     """
     Test the get_cat_fact method of the CatFact class (With Stubbing).
     """
     stub_response_data = {
        "status_code": 200,
        "response": {
            "data": "Cats are amazing!"
        },  # Make sure this matches the actual response structure
     }
     
     stub_get_cat_fact = mocker.stub(name='get_cat_fact')
     stub_get_cat_fact.return_value = stub_response_data

     # Call the method
     response = stub_get_cat_fact()
     assert response == stub_response_data

def test_get_cat_fact_success_monkeypatch(monkeypatch, cat_fact):
    """
    Test the get_cat_fact method of the CatFact class (With Monkeypatch).
    """
    def mock_return():
        return {
        "status_code": 200,
        "response": {
            "data": "Cats are amazing!"
        },  # Make sure this matches the actual response structure
     }
    
    monkeypatch.setattr(cat_fact, "get_cat_fact", mock_return)
    assert cat_fact.get_cat_fact() == mock_return()


