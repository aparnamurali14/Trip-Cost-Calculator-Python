# Trip Cost Calculator

def hotel_cost(no_of_nights):

    # Calculate the total hotel cost. Hotel cost is $140 per night.
    
    hotel_cost_per_night=140
    total_hotel_cost=no_of_nights*hotel_cost_per_night
    return total_hotel_cost


def plane_ride_cost(city_name):

    # Return round-trip flight cost based on city name.

    if city_name=="Charlotte":
        return 183
    elif city_name=="Tampa":
        return 220
    elif city_name=="Pittsburgh":
        return 222
    elif city_name=="Los Angeles":
        return 475
    else:
        return 0                  # Default cost for unknown cities
    

def rental_car_cost(rental_days):

    # Calculate car rental cost with discounts. Base rate: $40 per day , Discount: $50 for 7+ days, $20 for 3-6 days

    base_rental_cost=rental_days*40
    if rental_days>=7:
        return base_rental_cost-50
    elif rental_days>=3:
        return base_rental_cost-20
    else:
        return base_rental_cost 
    

def trip_cost(city_name,no_of_nights,days,spending_money):

    # Calculate the total trip cost including hotel, flight, car rental, and spending money.

    hotel = hotel_cost(no_of_nights)
    flight = plane_ride_cost(city_name)
    car = rental_car_cost(days)

    total = hotel + flight + car + spending_money

    print("Hotel= $",hotel)
    print("Flight= $",flight)
    print("Car rental= $",car)
    print("Spending money= $",spending_money)
    
    return total

# User inputs

no_of_nights=int(input("Enter the number of nights"))
city_name=input("Enter the city name")
rental_days=int(input("Enter the number of rental days"))
spending_money = int(input("Enter the money spent: "))

# Calculate total trip cost

total_amount = trip_cost(city_name, no_of_nights,rental_days,spending_money)
print("\nTotal trip cost= $",total_amount)