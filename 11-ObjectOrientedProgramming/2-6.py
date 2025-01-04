class Phone():
    def __init__(self, battery_level, network_connection, storage_space):
        self.battery_level=battery_level
        self.network_connection=network_connection
        self.storage_space=storage_space

    def charge(self, amount):
        self.battery_level+=amount
        print(f"Charging phone. Battery level is now {self.battery_level}%.")\
    
    def make_call(self, phone_number):
        if self.network_connection:
            print(f"Calling {phone_number}...")
        else:
            print("No network connection available.")
            
    def install_app(self, app_size):
        if self.storage_space>=app_size:
            self.storage_space-=app_size
            print(f"App installed. {self.storage_space}MB of storage remaining.")
        else:
            print("Not enough storage.")

my_phone=Phone(50, True, 1000)

my_phone.charge(20)
my_phone.make_call("123-456-789")
my_phone.install_app(200)

print(f"Battery: {my_phone.battery_level}%")
print(f"Network Connection: {'Connected' if my_phone.network_connection else 'Disconnected'}")
print(f"Storage Space: {my_phone.storage_space}MB")