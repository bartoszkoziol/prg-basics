def ms_to_kmh(ms):
    kmh=ms*(3600/1000)
    return kmh
speed1=10
speed2=35

print(f"{speed1}m/s ={ms_to_kmh(speed1):.2f} km/h")
print(f"{speed2}m/s ={ms_to_kmh(speed2):.2f} km/h")