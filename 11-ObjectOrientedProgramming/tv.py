class TV:
    def __init__(self):
        self.is_on = False  # TV is initially off
        self.channel_no = 1  # Default channel
        self.channels = []  # No channels initially
        self.volume = 0  # Initial volume is 0

    def turn_on(self):
        self.is_on = True  # Turn the TV on

    def turn_off(self):
        self.is_on = False  # Turn the TV off

    def set_channel_no(self, new_channel_no):
        if self.is_on:
            if 1 <= new_channel_no <= len(self.channels):
                self.channel_no = new_channel_no
                print(f"Channel changed to {self.channel_no}: {self.channels[self.channel_no - 1]}")
            else:
                print("Invalid channel number.")
        else:
            print("TV is off. Turn it on first to change the channel.")

    def set_channels(self, channels_list):
        self.channels = channels_list  # Set the list of available channels
        print("Channels have been set.")

    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for i, channel in enumerate(self.channels, start=1):
                print(f"{i}. {channel}")
        else:
            print("No channels available. Please set the channels first.")

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no}: {self.channels[self.channel_no - 1]}")
            else:
                print(f"TV is on, but channel {self.channel_no} is out of range.")
            print(f"Volume: {self.volume}")
        else:
            print("TV is off")

    def increase_volume(self):
        if self.is_on and self.volume < 10:
            self.volume += 1
            print(f"Volume increased to {self.volume}")
        else:
            print("Volume cannot be increased further.")

    def decrease_volume(self):
        if self.is_on and self.volume>0:
            self.volume-=1
            print(f"Volume decreased to {self.volume}")
        else:
            print("Volume cannot be decreased further")