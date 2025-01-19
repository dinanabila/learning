AMADEUS_API_KEY = ""
AMADEUS_API_SECRET = ""
AMADEUS_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_SEARCH_CITY_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities?"

import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_API_SECRET
        self._token = self._get_new_token() # buat dapetin token baru setiap di-run


    def _get_new_token(self):
        header_token = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body_token = {
            'grant_type': 'client_credentials',
            'client_id': AMADEUS_API_KEY,
            'client_secret': AMADEUS_API_SECRET
        }
        response_token = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=header_token, data=body_token)
        return response_token.json()['access_token']


    def dapetin_iata_code(self, kota):
        parameters_city_search = {
            "keyword": kota,
            "max": 1,
            "include": "AIRPORTS",
        }

        header = {"Authorization": f"Bearer {self._token}"}

        response_city_search = requests.get(
            url=AMADEUS_SEARCH_CITY_ENDPOINT, 
            params=parameters_city_search,
            headers=header
        )

        try:
            iata_code = response_city_search.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: Airport code untuk {kota} tidak ditemukan.")
            return "N/A"
        except KeyError:
            print(f"IndexError: Airport code untuk {kota} tidak ditemukan.")
            return "Tidak ditemukan"
        
        return iata_code