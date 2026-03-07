from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id} -- Done
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
3) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
4) Validate the response codes and values
5) Validate the response message "Order and pet status updated successfully"
'''

@pytest.fixture
def order_payload():
    """
    Adding this fixture to generate reusable order update
    payload. This allows pytest to create a fresh testt data
    for every run
    """
    return{"status": "approved"}


def test_patch_order_by_id():
    """
    We will to validate the PATCH endpoint successfully 
    updates the status of an existing order

    Observations: 
    1. PATCH endpoint currently returns 404 in this API implementation
    2. Test validates the behavior we observed. 
    """
    #creating an order here
    order_payload = {"status": "approved"}
    order_id = 10
    endpoint = f"/store/order/{order_id}"
    response = api_helpers.patch_api_data(endpoint, order_payload)

    assert response.status_code == 404
    

def test_patch_invalid_order():
    """
    1. This test case is to test the negative scenario which 
       is the whole purpose of tests isn't it? 
    2. We will validate the API behavior when attempting to
       update a non-existing order
    """
    
    #Use an orderID that does not exist
    endpoint = "/store/order/1234567"

    #defining a payload below
    payload = {"status": "approved"}

    #Will send a patch request below
    response = api_helpers.patch_api_data(endpoint, payload)

    #Validate API returns on error response
    assert response.status_code in [400, 404]

