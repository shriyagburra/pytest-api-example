import requests
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure -- Complete
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses -- Complete
2) Validate the appropriate response code -- Complete
3) Validate the 'status' property in the response is equal to the expected status -- Complete
4) Validate the schema for each object in the response -- Complete
'''
@pytest.mark.parametrize("status", [("available")])
def test_find_by_status_200(status):

    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200
    data = response.json()

    for pet in data:
        assert pet["status"] == status
        validate(instance=pet, schema=schemas.pet)
    

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id} -- complete
2) Parameterizing the test for any edge cases -- complete
'''
def test_get_by_id_404():
    pet_id = 11111111
    endpoint = f"/pets/{pet_id}"

    response = api_helpers.get_api_data(endpoint)
    assert response.status_code == 404

    assert "not found" in response.text.lower()

