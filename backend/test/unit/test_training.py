import pytest
import unittest.mock as mock #Load the mocking library

from src.controllers.controller import Controller
from src.util.dao import DAO

from enum import Enum
from src.static.diets import Diet, from_string


from src.util.calculator import calculate_ingredient_readiness, calculate_readiness

### backend/src/static/diets.py
@pytest.mark.unit
def test_from_string_vegetarian():
    #Arrange: setup all preconditions of the test
    input = 'vegetarian'

    # Act: let the system under test perform an operation
    sut = from_string(input)
    # Assert: compare the system´s response to the expected response
    assert sut == Diet.VEGETARIAN

@pytest.mark.unit
def test_from_string_vegan():
    #Arrange: setup all preconditions of the test
    input = 'vegan'

    # Act: let the system under test perform an operation
    sut = from_string(input)
    # Assert: compare the system´s response to the expected response
    assert sut == Diet.VEGAN

@pytest.mark.unit
def test_from_string_normal():
    #Arrange: setup all preconditions of the test
    input = 'abcd'

    # Act: let the system under test perform an operation
    sut = from_string(input)
    # Assert: compare the system´s response to the expected response
    assert sut == Diet.NORMAL

### backend/src/util/calculator.py
@pytest.mark.unit
def test_calculate_readiness_1():
    # Arrange:
    recipe = {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }

    available_items = {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }

    # Act:
    readiness = calculate_readiness(recipe, available_items)

    # Assert:
    expected_readiness = (
        (500 / 500) +  # Flour
        (20 / 20) +    # Walnuts
        (1 / 1) +      # Yeast
        (10 / 10) +    # Salt
        (30 / 30)      # Vinegar
    ) / len(recipe)

    assert readiness == expected_readiness

@pytest.mark.unit
def test_calculate_readiness_partial_items():
    # Arrange:
    recipe = {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }

    available_items = {
        "Flour": 200,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 15
    }

    # Act:
    readiness = calculate_readiness(recipe, available_items)

    # Assert:
    expected_readiness = (
        (200 / 500) +  # Flour
        (20 / 20) +    # Walnuts
        (1 / 1) +      # Yeast
        (10 / 10) +    # Salt
        (15 / 30)      # Vinegar
    ) / len(recipe)

    assert readiness == expected_readiness

@pytest.mark.unit
def test_calculate_ingredient_readiness_return_1():
    #Arrange:
    available_amount = 90

    required_amount = 90

    # Act:
    readiness = calculate_ingredient_readiness(available_amount, required_amount)

    expected_readiness = available_amount/required_amount

    # Assert:
    assert readiness == expected_readiness

@pytest.mark.unit
def test_calculate_ingredient_readiness_return_0():
    #Arrange:
    available_amount = 90

    required_amount = 0

    # Act:
    readiness = calculate_ingredient_readiness(available_amount, required_amount)

    expected_readiness = 0

    # Assert:
    assert readiness == expected_readiness


### backend/src/controller/controller.py
@pytest.mark.unit
def test_create():
    # Arrange
    data = {'key', 'value'}
    newly_created_obj = {'_id': {'$oid': 'unique_id'}, 'key' : 'value'}

    mockedcontroller = mock.MagicMock(spec=DAO) # Mock the dependency
    mockedcontroller.create.return_value = newly_created_obj

    sut = Controller(mockedcontroller) # Inject the dependency

    # Act
    result = sut.create(data)

    # Assert
    mockedcontroller.create.assert_called_once_with(data)
    assert result == newly_created_obj

@pytest.mark.unit
def test_create_raises_exception():
    # Arrange
    data = {'key', 'value'}

    mockedcontroller = mock.MagicMock(spec=DAO) # Mock the dependency
    mockedcontroller.create.side_effect = Exception()

    sut = Controller(mockedcontroller) # Inject the dependency

    # Assert
    with pytest.raises(Exception):
        sut.create(data) #Act

@pytest.mark.unit
def test_get_success():
    #Arrange
    obj_id = '139643452963184'
    found_obj = {'_id': {'$oid': obj_id}, 'key': 'value'}

    mockedcontroller = mock.MagicMock(spec=DAO) # Mock the dependency
    mockedcontroller.findOne.return_value = found_obj

    sut = Controller(mockedcontroller) # Inject the dependency

    # Act
    result = sut.get(obj_id)

    # Assert
    mockedcontroller.findOne.assert_called_once_with(obj_id) #Assert that the mock was called exactly once
    assert result == found_obj
