
ms_to_kmh = lambda ms: ms*3.6
speeds=[10,35]

for speed in speeds:
    print(f"{speed}m/s = {ms_to_kmh(speed)}km/h")