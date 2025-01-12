import requests
import config

headers = {
    "Authorization": f"Bearer {config.BRAWL_KEY}"
}

url = f"https://api.brawlstars.com/v1/"


def get_player_data(battle_tag):
    battle_tag = battle_tag.replace("#", "%23")
    response = requests.get(url + f"players/{battle_tag}", headers=headers)
    if response.status_code == 200:
        player_data = response.json()
        player_info = ""
        player_info += f"Имя: {player_data['name']}\n"
        player_info += f"Баттлтэг: {player_data['battleTag']}\n"
        return player_info
    else:
        print("Error:", response.status_code, response.text)
        return f"Ошибка {response.status_code}: {response.text}"


def brawler_info(battle_tag, brawler_name):
    battle_tag = battle_tag.replace("#", "%23")
    response = requests.get(url + f"players/{battle_tag}", headers=headers)
    if response.status_code == 200:
        player_data = response.json()
        brawler = player_data["brawlers"]
        for brawler in brawler:
            if brawler["name"] == brawler_name.upper():
                brawler_info = ""
                brawler_info += f"Имя: {brawler['name']}\n"
                brawler_info += f"Уровень: {brawler['power']}\n"
                brawler_info += f"Ранг: {brawler['rank']}\n"
                brawler_info += f"Трофеи: {brawler['trophies']}\n"
                return brawler_info
        return "Brawler с таким именем не найден. Пиши на английском. Пример: Shelly"
    else:
        print("Error:", response.status_code, response.text)
        return f"Ошибка {response.status_code}: {response.text}"


if __name__ == "__main__":
    print(brawler_info("#9JJ0LG2U0", "colt"))