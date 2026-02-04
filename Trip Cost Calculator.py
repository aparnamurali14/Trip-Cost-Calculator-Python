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
    

def trip_cost(city_name,days,spending_money):

    # Calculate the total trip cost including hotel, flight, car rental, and spending money.

    total = hotel_cost(days)+ plane_ride_cost(city_name) + rental_car_cost(days) + spending_money

    print("Hotel= $",hotel_cost(days))
    print("Flight= $",plane_ride_cost(city_name))
    print("Car rental= $",rental_car_cost(days))
    print("Spending money= $",spending_money)
    
    return total

# User inputs

days=int(input("Enter the number of night stay in hotel"))
city_name=input("Enter the city name")
spending_money = int(input("Enter the money spent: "))

# Calculate total trip cost

total_amount = trip_cost(city_name,days,spending_money)
print("\nTotal trip cost= $",total_amount)