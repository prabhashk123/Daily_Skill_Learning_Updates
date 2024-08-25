import pytest

@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    print("Browser Products")
    
def testAddItemtoCart(setup):
    print("Add Item Successful")
    
def testRemoveItemtoCart(setup):
    print("Remove Item Successful")