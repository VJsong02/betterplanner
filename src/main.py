from vasttrafikwrapper import VasttrafikWrapper
import json

if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    vasttrafik = VasttrafikWrapper(config["client_id"], config["client_secret"], config["token"])
