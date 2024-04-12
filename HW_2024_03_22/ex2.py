def taxi_cost(distance: int, waiting_time: int=0) -> int | None:
    if distance < 0 or waiting_time < 0:
        return None
 
    taxi_fare = 80
    distance_cost = (distance / 150) * 6
    waiting_time_cost = waiting_time * 3
    result = taxi_fare + distance_cost + waiting_time_cost
 
    if distance == 0:
        return taxi_fare + 80 + waiting_time_cost
 
    return round(result)

print(taxi_cost(1500))
print(taxi_cost(2560))
print(taxi_cost(0, 5))
print(taxi_cost(42130, 8))
print(taxi_cost(-300))