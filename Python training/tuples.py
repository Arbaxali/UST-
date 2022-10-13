cart = () 
cart =("apple")
print(type(cart))
cities =("nagpur","pune","mumbai","bangalore")
print(cities)
cities_with_codes =(100,"nagppur",101,"pune",103,"bangalore")
profile =("parag",42,False,"M")
print(profile)

for city in cities:
    print(city)
print("last city of the cities",cities[-1])
print("2 city of the cities ",cities[1])
c1,c2,c3,c4 =cities
print(c1,c2,c3,c4)

print(cities.index("Mumbai"))
print(len(cities))