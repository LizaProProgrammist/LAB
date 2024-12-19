residents = [] 
areas = []      

for i in range(12):
    print(f"Район {i + 1}:")
    population = float(input("Введите количество жителей (в тыс.): "))
    area = float(input("Введите площадь района (в км²): "))
    residents.append(population)
    areas.append(area)

total_population = sum(residents) * 1000  
total_area = sum(areas)  
average_density = total_population / total_area

print(f"Средняя плотность населения по области: {average_density:.2f} чел./км²")

