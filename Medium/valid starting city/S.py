def validStartingCity(distances, fuel, mpg):
    fuelLeft = 0
    bestCityIndex = 0
    for cityIndex in range(len(distances)):
        fuelLeft += fuel[cityIndex]*mpg - distances[cityIndex]
    
        # If fuelLeft is negative, it means we can't start from the current cityIndex
        # so we set the next cityIndex as the bestCityIndex and reset fuelLeft to
        if fuelLeft < 0:
            bestCityIndex = cityIndex + 1
            fuelLeft = 0
    return bestCityIndex