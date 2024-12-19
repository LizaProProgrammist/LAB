import json
data = [
    {
        "name": "Adeel Solangi",
        "language": "Sindhi",
        "id": "V59OF92YF627HFY0",
        "bio": "Donec lobortis eleifend condimentum. Cras dictum dolor lacinia lectus vehicula rutrum. Maecenas quis nisi nunc. Nam tristique feugiat est vitae mollis. Maecenas quis nisi nunc.",
        "version": 6.1
    },
    {
        "name": "Afzal Ghaffar",
        "language": "Sindhi",
        "id": "ENTOCR13RSCLZ6KU",
        "bio": "Aliquam sollicitudin ante ligula, eget malesuada nibh efficitur et. Pellentesque massa sem, scelerisque sit amet odio id, cursus tempor urna. Etiam congue dignissim volutpat. Vestibulum pharetra libero et velit gravida euismod.",
        "version": 1.88
    },
]

def search_users(data, query):
    result = [user for user in data if user["name"].lower().startswith(query.lower())]
    with open("/mnt/data/out.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
    return result

filtered_users = search_users(data, "Ade")
filtered_users 
