from app import app 

def test_home():
    with app.test_client() as client:
        response = client.post("/store-weather-data")
        print(f"POST /store-weather-data status: {response.status_code}")
        response = client.get("/list-weather-files")
        print(f"GET /list-weather-files status: {response.status_code}")
        response = client.get("/weather-file-content/<file_name>")
        print(f"GET /weather-file-content/<file_name> status: {response.status_code}")
        print(f"Response body: {response.data}")
        assert response.status_code == 200
