from datetime import datetime
import requests

class VasttrafikWrapper:
    baseurl = "https://ext-api.vasttrafik.se/pr/v4"
    authurl = "https://ext-api.vasttrafik.se/token"

    client_id = ""
    client_secret = ""
    token = ""
    access_token = ""

    gid_cache = {}

    def __init__(self, client_id, client_secret, token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

        response = requests.post(
            self.authurl, 
            data={"grant_type": "client_credentials"}, 
            headers={"Authorization": "Basic " + self.token}
        )

        self.access_token = response.json()["access_token"]

    def search_station(self, query):
        headers = {"Authorization": "Bearer " + self.access_token}
        params  = {"q": query, "limit": 5}
        url = self.baseurl + f"/locations/by-text"
        response = requests.get(url, headers=headers, params=params)
        results = response.json()["results"]

        stations = []
        for result in results:
            if "gid" in result:
                self.gid_cache[result["name"]] = result["gid"]
                stations.append((result["name"], result["gid"]))
        return stations