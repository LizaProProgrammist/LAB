import pickle

phones = {
    "iPhone 14": {"USA": 999, "UK": 899, "Germany": 1099, "India": 1049, "China": 949, "Japan": 899, "Australia": 999, "Canada": 999},
    "Samsung Galaxy S23": {"USA": 799, "UK": 749, "Germany": 869, "India": 899, "China": 829, "Japan": 769, "Australia": 849, "Canada": 829},
    "Google Pixel 8": {"USA": 699, "UK": 649, "Germany": 749, "India": 729, "China": 719, "Japan": 699, "Australia": 749, "Canada": 749},
    "OnePlus 11": {"USA": 649, "UK": 599, "Germany": 699, "India": 659, "China": 639, "Japan": 619, "Australia": 679, "Canada": 689},
    "Xiaomi 13 Pro": {"USA": 599, "UK": 569, "Germany": 659, "India": 679, "China": 649, "Japan": 599, "Australia": 639, "Canada": 629},
    "Huawei P60": {"USA": 549, "UK": 519, "Germany": 619, "India": 599, "China": 579, "Japan": 529, "Australia": 589, "Canada": 579},
    "Sony Xperia 1": {"USA": 1199, "UK": 999, "Germany": 1249, "India": 1299, "China": 1149, "Japan": 1099, "Australia": 1199, "Canada": 1249},
}

print("Мобильные телефоны и их средние стоимости:")
average_costs = {}
for phone, prices in phones.items():
    avg_cost = sum(prices.values()) / len(prices)
    average_costs[phone] = avg_cost
    print(f"{phone}: {avg_cost:.2f} USD")

min_phone = min(average_costs, key=average_costs.get)
del phones[min_phone]
print(f"\nТелефон с минимальной средней стоимостью ({min_phone}) удален.")

max_avg_cost = max(average_costs.values())
print("\nТелефоны, стоимость которых отличается менее чем на 30% от максимальной:")
for phone, avg_cost in average_costs.items():
    if abs(avg_cost - max_avg_cost) / max_avg_cost < 0.3:
        print(f"{phone}: {avg_cost:.2f} USD")

print("\nТелефоны, стоимость которых в США выше, чем в Великобритании:")
for phone, prices in phones.items():
    if prices["USA"] > prices["UK"]:
        print(phone)

with open("data.pickle", "wb") as file:
    pickle.dump(phones, file)
print("\nСловарь сохранен в файл data.pickle.")

with open("data.pickle", "rb") as file:
    loaded_phones = pickle.load(file)
print("\nЗагруженный словарь из файла:")
print(loaded_phones)
