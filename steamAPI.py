import requests 
import json

def get_app_data(AppID):
    url = f"https://store.steampowered.com/api/appdetails?appids={AppID}"
    response = requests.get(url)
    data = response.json()
    return data

def get_top_games(list_type):
    url = f"https://steamspy.com/api.php?request={list_type}"
    response = requests.get(url)
    data = response.json()
    return data

top_forever = get_top_games("top100forever")
top_2weeks = get_top_games("top100in2weeks")
top_owned = get_top_games("top100owned")
all_games = {**top_forever, **top_2weeks, **top_owned}


def discount_filter():
    percent_filter = int(input("What's the minimum discount you want? (Intervals of 5): "))

    for appid, game_data in all_games.items():
        discount = int(game_data['discount'])
        if discount >= percent_filter:
            print(f"{game_data['name']} - {discount}% off")

discount_filter()