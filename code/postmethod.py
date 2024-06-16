import json
import requests

base_url = "https://reqres.in/api"
#Auth token:
auth_token = "token....token value"

def post_request():
    url = base_url + "/users"
    print("post url:" +url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Aaryan",
        "email": "aaryan@gmail.com",
        "Job": "QA learner",
        "level": "bachelors"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response body:", json_str)
    user_id = json_data["id"]
    print("User is==", user_id)
    assert response.status_code == 201
    print("......Get user is done........ ")
    print("................................")
    return user_id

user_id = post_request()
