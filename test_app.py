from app import app 

def test_home():
    with app.test_client() as client: 
        
        response=client.post("/store-weather-data")
        response=client.get("/list-weather-files")
        response=client.get("/weather-file-content/<file_name>")
        
        assert response.status_code == 200
