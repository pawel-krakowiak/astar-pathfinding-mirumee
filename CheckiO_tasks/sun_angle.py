def sun_angle(time):
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    if hour < 6 or hour+(minute/100) > 18:
        return "I don't see the sun!"
        
    return round(((hour-6)*15)+(minute*0.25), 2)
    
    # 15,0* every hour
    # 0,25* every minute

