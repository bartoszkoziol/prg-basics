import random

class Thermometer:
    def __init__(self):
        self.is_on=False
        self.temperature=0.0

    def turn_on(self):
        self.is_on=True
        print("Thermometer is now ON.")

    def turn_off(self):
        self.is_on=False
        print("Thermometer is now OFF.")
    
    def measure_temp(self):
        if self.is_on:
            self.temperature=round(random.uniform(34.0, 42.0), 1)
            print(f"Temperature: {self.temperature}C")
            if self.temp>=41.0:
                print("CRITICAL TEMPERATURE")     
            elif self.temp>=37.0:
                print("Fever")
            else:
                print("Normal temp")
        else:
            print("The thermometer is off. Turn it on first.")




        