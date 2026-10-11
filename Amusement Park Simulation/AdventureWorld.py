import matplotlib.pyplot as plt
import numpy as np
from ThemePark import *




frame_colour='red'
ship_colour='blue'
fill_ship = 'b'
wheel_colour = 'c'
line_colour = 'pink'
frame_wheel = 'm'




terrain = Terrain((0,0), (130, 120), (80,0), (30, 110), gif_file="partly_cloudy_sky_GIF.gif")
#patron = Patron("Alice", 'o')
#rides = [pirate_ship, ferris_wheel]
park = Park_Operations(terrain)
pirate_ship = Ride("Pirate Ship", (35, 30), (15, 20), duration=100, capacity = 8, park=park)
ferris_wheel = Ride("Ferris Wheel", (50, 70), (65, 40), duration=100, capacity=8, park=park)
drop_tower = Ride("Drop tower", (40, 25), (15, 60), duration=100, capacity = 8, park=park)


print("Welcome to Adventure World !")


num_patrons = input("Enter the number of patrons: ")
while not num_patrons.isdigit():
    num_patrons = input("Please enter the number of patrons correctly: ")

num_patrons = int(num_patrons)

for i in range(num_patrons):
    patron = park.spawn_patron() # Creates patron_i
    state = ""
    choice = ""
    choose_ride = ""

    while state not in ["a", "b"]:
        state = input("What do you want to do ?: a) roaming b) riding: ").strip().lower()
    if state == "a":
        patron.state = "roaming"

    elif state == "b":
        while choose_ride not in ["a", "b", "c"]:
            choose_ride = input("Which ride do you want ? - (a)- Pirate Ship (b)- Ferris Wheel (c)- Drop Tower: ").strip().lower()
        if choose_ride == "a":
            patron.state = "riding_ship"
        elif choose_ride == "b":
            patron.state = "riding_ferris" 
        elif choose_ride == "c":
            patron.state = "riding_tower" 
    
print("\n***Simulation starts***\n")


plt.ion()
for n in range(300):

    plt.clf() # clear previous windows
    plt.title(f"Adventure World")
    plt.xlim(0, 130)
    plt.ylim(0, 150)

    angle = 26 * np.sin(n * 0.2)
    rad = -n * 0.1
    terrain.update_frame(n) # update frame displayed
    terrain.plot_terrain(plt)
    park.ship_ride.plot_ship(plt, angle)
    park.ferris_ride.plot_ferrisWheel(plt, rad)
    drop_tower.drop_tower(plt)
    park.move_all_patrons() # movement, queue joining

    park.plot_all_patrons(plt)
    plt.draw()
    plt.pause(0.08)
    
    plt.show()
            



