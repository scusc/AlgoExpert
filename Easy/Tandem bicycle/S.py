def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    numTeams = len(redShirtSpeeds)
    if numTeams ==1:
        return max(redShirtSpeeds[0], blueShirtSpeeds[0])
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reversed = fastest)
    maxSpeed = 0
    for i in range(numTeams):
        maxSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    
    return maxSpeed
