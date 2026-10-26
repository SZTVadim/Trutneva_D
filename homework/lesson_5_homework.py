fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last_element = fruits.pop()

fruits = ["яблоко", "банан", "апельсин", "банан"]
index_banana = fruits.index("банан")
count_banana = fruits.count("банан")

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

cubes = [x ** 3 for x in range(1, 9)]
min_cube = min(cubes)
max_cube = max(cubes)
print(min_cube, max_cube)

my_numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
filtered_numbers = [x for x in my_numbers if x > 10]
print(filtered_numbers)
my_numbers = sum(filtered_numbers)
print(my_numbers)

cities = ["москва", "санкт-петербург", "казань"]
cities = [city.title() for city in cities]
print(cities)
