def hotel_cost(days):
    return 140* days


    

        
def rentalcar_cost(days):
    costs = 40* days
    if days >= 7:
        costs =-50
    elif days >= 3:
        costs =-20    

    return costs

def trip_cost(city,days):
    hc =hotel_cost(days)
    # prc =plane_ride_cost(city)
    rcc = rentalcar_cost(days)
    print(hc)
    # print(prc)
    print(rcc)
    
def plane_ride_cost(city):
    cities = {}
    cities = {
        "Charlotte": 183,
        "Tampa": 220,
        "Pittsburgh": 222,
        "Los Angeles": 475
    }
    print(cities)
    inp = input("please enter the city  ")
    for i in cities:
        if inp == i:
            ss =i.key
        else:
            break
    return ss    

inp2 = input("please enter the city")
inp1 = input("please enter the number of days")

trip_cost(inp2, inp1)
 
