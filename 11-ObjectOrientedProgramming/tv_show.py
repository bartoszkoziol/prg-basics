# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
   my_tv=TV()

   my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"])

  # Show TV status
   my_tv.show_status()

    # Turn TV on
   my_tv.turn_on()
   my_tv.show_status()


   my_tv.show_channels()

   my_tv.set_channel_no(4)
   my_tv.show_status()

   my_tv.set_channel_no(7)
   my_tv.show_status()


   my_tv.increase_volume()
   my_tv.show_status()

   my_tv.decrease_volume()
   my_tv.show_status()

    # Turn TV off
   my_tv.turn_off()
   my_tv.show_status()

if __name__ == "__main__":
    main()