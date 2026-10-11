import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.image as mpimg
import random
tab20 = plt.get_cmap("tab20").colors
cmap = ListedColormap([tab20[5], tab20[10], tab20[15], tab20[17]])
from PIL import Image

class Ride():
    def __init__(self, name, size, position, duration, park, capacity=8, animation_count=0):
        """
        Parameters:
        name: string, name of the ride
        size: tuple (width, height)
        position: tuple (x, y), location of ride
        duration: int, duration of the ride in timesteps
        capacity: int, maximum patrons allowed on 1 ride
        animation_count: int, counter for animation (starts at 0)
        """
        self.name = name
        self.size = size
        self.position = position
        self.duration = duration
        self.capacity = capacity
        self.animation_count = animation_count # increases only when running
        self.park = park

        # drop tower properties
        self.tower_x = 30
        self.tower_y = 60
        self.width_tower = 10
        self.height_tower = 25
        self.tower_colour = 'red'

        self.width_seat = 20
        self.height_seat = 5
        self.seat_x = 25
        self.seat_y = 70
        self.seat_colour = 'orange'
        self.direction = 1
        width_seat = 20
        height_seat = 5
        # Ride state management
        self.state = "idle" # either idle, running, loading
        self.ship_riders = [] # patrons on ship
        self.ferris_riders = [] # patrons on ferris wheel
        self.count = 0 # increases only for current state
        self.loading_time = 20 # timesteps taken to load patrons
        self.unloading_time = 15 # timesteps taken to unload
        
        self.waypoints = {
            'entrance': (94, 5),
            'ferris_wheel': (100, 40),
            'ferris_junction': (94, 30),
            'pirate_ship': (51, 30),
            'pirate_junction': (56, 35),
            'drop_junction': (56, 60),
            'exit': (124, 25)
        }
    def update_riders_ship(self, park):
        """
        Move patrons from ship queue to ship
        park: Park_Operations which has queue_ship
        """
        if self.state == "idle":
            while len(self.park.queue_ship) > 0 and len(self.ship_riders) < self.capacity:
                patron = self.park.queue_ship.pop(0) # Take 1st patron from queue 
                self.ship_riders.append(patron) # put 1st person on ride
                self.park.queue_ship.remove(patron)
                patron.state = "loading"
                print(f"{patron[0]} boarded {self.name}")
                for i, p in enumerate(self.park.queue_ship): # Update queue_position for the rest of patrons
                    p.queue_position = i


    def update_riders_ferris(self, park):
        """
        Move patrons from ship queue to ship
        """
        if self.state == "idle":
            while len(self.park.queue_ferris) > 0 and len(self.ferris_riders) < self.capacity:
                patron = self.park.queue_ferris.pop(0) # Take 1st patron from queue 
                self.ferris_riders.append(patron) # put 1st person on ride
                patron.state = "loading"
                print(f"{patron[0]} boarded {self.name}")
                for i, p in enumerate(self.park.queue_ferris): # Update queue_position for the rest of patrons
                    p.queue_position = i

    def start_ship(self):
        """
        Start ride if riders are loaded
        """
        if len(self.ship_riders) > 0:
            self.state = "running"
            self.time_remaining = self.duration
            print(f"{self.name} started with {len(self.ship_riders)} riders.")

    def start_ferris(self):
        """
        Start ride if riders are loaded
        """
        if len(self.ferris_riders) > 0:
            self.state = "running"
            self.time_remaining = self.duration
            print(f"{self.name} started with {len(self.ferris_riders)} riders.")

    def update_ship(self, park):
        """
        Update ship state each timestep
        """
        if self.state == "running":
            self.time_remaining -= 1
            self.animation_count += 1 # increase for animation
            if self.time_remaining <= 0:
                #self.finish_ship() # 1 round of ride finished
                self.state = "unloading"
        elif self.state == "idle":
            if len(park.queue_ship) > 0: # verify if there is still a queue
                self.state = "loading"
                self.update_riders_ship(park)
                #self.start_ship()

    def update_ferris(self, park):
        """
        Update ferris state each timestep
        """
        if self.state == "running":
            self.time_remaining -= 1
            self.animation_count += 1 # increase for animation
            if self.time_remaining <= 0:
                #self.finish_ferris() # 1 round of ride finished
                self.state = "unloading"
        elif self.state == "idle":
            if len(park.queue_ferris) > 0: # verify if there is still a queue
                self.state = "loading"
                self.update_riders_ferris(park)
                self.start_ferris()


    def plot_ship(self, plt, pos):
        """
        Plot boundary
        Plot and swing pirate ship
        """
        # plot ship inside of box
        xShip, yShip = self.position
        widthShip, heightShip = self.size
        x = np.array([xShip, xShip + widthShip, xShip + widthShip, xShip, xShip])
        y = np.array([yShip, yShip, yShip + heightShip, yShip + heightShip, yShip])
        plt.plot(x,y) # Plot Ship box
        frame_x = np.array([1, 2, 3, 4, 5, 4, 2])
        frame_y = np.array([1, 3, 5, 3, 1, 3, 3])
        #p.plot(frame_x,frame_y) # frame

        ship_x = np.array([1, 2, 4, 5, 3, 1, 2, 4, 5])
        ship_y = np.array([3, 2.5, 2.5, 3, 5, 3, 1.5, 1.5, 3])

        x_ship_scaled = (ship_x/5.5) * widthShip
        y_ship_scaled = (ship_y/5.5) * heightShip
        

        x_frame_scaled = (frame_x/4) * widthShip
        y_frame_scaled = (frame_y/4) * heightShip


        x_frame_translated = x_frame_scaled + ((1.7/4) * xShip)
        y_frame_translated = y_frame_scaled + ((2.45/4) * yShip)
        plt.plot(x_frame_translated, y_frame_translated,solid_capstyle="round", color='red')

        x_ship_translated = x_ship_scaled + ((3.6/4) * xShip)
        y_ship_translated = y_ship_scaled + ((4.5/4) * yShip)
        
        theta = np.radians(pos)
        
       
        # (32.7, 50) is like the nail fixing the ship to the frame
        x_move = (x_ship_translated - 32.7)*np.cos(theta) - (y_ship_translated - 50)*np.sin(theta) + 32.7
        y_move = (x_ship_translated - 32.7)*np.sin(theta) + (y_ship_translated - 50)*np.cos(theta) + 50
        plt.plot(x_move, y_move,solid_capstyle="round", color='blue')

    def drop_tower(self, p):
        """
        Plot boundary
        Plot and move drop tower
        """
        xShip, yShip = self.position
        widthShip, heightShip = self.size
        x = np.array([xShip, xShip + widthShip, xShip + widthShip, xShip, xShip])
        y = np.array([yShip, yShip, yShip + heightShip, yShip + heightShip, yShip])
        p.plot(x,y) # Plot drop tower box     

        
        tower = patches.Rectangle((self.tower_x, self.tower_y), self.width_tower, self.height_tower, color=self.tower_colour)
        p.gca().add_patch(tower)

        seat = patches.Rectangle((self.seat_x, self.seat_y), self.width_seat, self.height_seat, color=self.seat_colour)
        p.gca().add_patch(seat)

        if self.seat_y >= 80:
            self.direction = -1
        elif self.seat_y <= 70:
            self.direction = 1
        self.seat_y += 2 * self.direction # speed


    def plot_ferrisWheel(self, p, pos):
        """
        Plot boundary
        Plot and rotate ferris wheel
        """
        xShip, yShip = self.position
        widthShip, heightShip = self.size
        x = np.array([xShip, xShip + widthShip, xShip + widthShip, xShip, xShip])
        y = np.array([yShip, yShip, yShip + heightShip, yShip + heightShip, yShip])
        p.plot(x,y) # Plot Ferris Wheel box

        frame_x = np.array([1, 2, 3, 4, 5, 4, 2])
        frame_y = np.array([1, 3, 5, 3, 1, 3, 3])
       

        x_frame_scaled = (frame_x/6) * widthShip
        y_frame_scaled = (frame_y/6) * heightShip

        x_frame_translated = x_frame_scaled + ((8.1/8) * xShip)
        y_frame_translated = y_frame_scaled + ((5.7/8) * yShip)
        p.plot(x_frame_translated,y_frame_translated,solid_capstyle="round", color='magenta')

        pie = np.pi
        angle_rad = np.linspace(0, 2 * pie, 25) # 0 to 2 pi rad
        r = 20
        x_wheel = r * np.cos(angle_rad) # x pts
        y_wheel = r * np.sin(angle_rad) # y pts
        x_wheel_translated = x_wheel + ((9.2/8) * xShip) + (1/4 * xShip)
        y_wheel_translated = y_wheel + ((17/8) * yShip)

        p.plot(x_wheel_translated,  y_wheel_translated, color='r')
       
        range_angles = np.linspace(0, 2 * pie, 8, endpoint=False) # angles in rad from 0 to 360
        for i in range_angles:
            rad = pos + i
            x_line = (r * np.cos(rad)) + ((9.2/8) * xShip) + (1/4 * xShip)# x pts for line with translation
            y_line = (r * np.sin(rad)) + ((17/8) * yShip) # y pts for line with translation
            
            p.plot([91,  x_line], [86, y_line], color='green') # plot from centre to edge of wheel
            cabin_width = 6
            cabin_height= 5
            cabin =  plt.Rectangle((x_line - (cabin_width/2), y_line - (cabin_height/2)), cabin_width, cabin_height, color='g', linewidth=1)
        
            p.gca().set_aspect('equal', adjustable = 'box')
            p.gca().add_patch(cabin)
       

    
    
class Terrain():
    def __init__ (self, boundary, size, entrance, exit, gif_file=None):
        """
        boundary: tuple, fences of the theme park (x, y)
        size: tuple, width and length of the theme park (x, y)
        entrance: tuple, entrance (x, y)
        exit: tuple, exit (x, y)
        gif_file: string, gif path
        """
        self.boundary = boundary
        self.size = size
        self.entrance = entrance
        self.exit = exit
        self.terrain_grid = self.generate_grid()

        self.background_gif = gif_file # gif file path
        self.gif_frames = [] # store all frames
        self.current_frame_index = 0 # shows current frame
        self.frame_delay = 3 # shows frame each 3 timestep

        if gif_file: # load gif
            self.load_gif_frames(gif_file)

    def load_gif_frames(self, filename):
        """
        Load all frames from gif
        """
        try: 
            gif = Image.open(filename)
            if hasattr(gif, 'n_frames'): # gets all frames of gif
                total_frames = gif.n_frames
            else:
                total_frames = 1

            for frame_num in range(total_frames):
                gif.seek(frame_num) # go to this frame
                frame = gif.convert('RGBA') 
                frame_array = np.array(frame)
                self.gif_frames.append(frame_array) # store frame

            print(f"Loaded {len(self.gif_frames)} frames")
        except FileNotFoundError:
            print(f"Error: GIF file '{filename}' not found.")
            self.gif_frames = []
        except Exception as e:
            print(f"Error loading GIF: {e}")
            self.gif_frames = []

    def update_frame(self, timestep):
        """
        Shows which GIF frame should be displayed
        """
        if len(self.gif_frames) > 0:
            total_frames = len(self.gif_frames)
            self.current_frame_index = (timestep // self.frame_delay) % total_frames

    def generate_grid(self):
        """
        Generate terrain grid with numbers representing different areas
        Grid shape: (130, 120) = (x_max, y_max)
        Indexing: grid[x, y] matches matplotlib coordinates

        Grid codes
        0 = grass (walkable)
        1 = fence (not walkable)
        2 = Ride area (not walkable)
        3 = path (walkable)
        """
        grid_x = 130 
        grid_y = 150
        grid = np.zeros((grid_x, grid_y)) # Shape matches (x_limit, y_limit)
        grid[:,:] = 1 # Everything brown, the fence
        grid[5:125,5:150] = 0 # grass
        grid[15:50, 20:50] = 2 # Background of pirate ship
        grid[65:115, 40:110] = 2 # Background of ferris wheel
        grid[15:55, 60:85] = 2 # background of drop down
        grid[93:98, 0:40] = 3 # path to ferris wheel
        grid[50:93, 30:35] = 3 # path to pirate ship
        grid[55:60, 35:60] = 3 # path to drop tower
        grid[111:119, 6:19] = 1 # tree
        grid[71:79, 6:19] = 1 # tree
        grid[6:124, 112:149] = 1   # sky
        
        return grid
    
    def is_walkable(self, x, y):
        """
        Verifies if position (x, y) is walkable ()
        Uses matplotlib coordinates directly - grid[x, y]

        Parameters:
        x: x-coordinate (0-130)
        y: y-coordinate (0-120)

        Returns True if position is movable (grass or path)
        """
        # Convert to integers for array indexing
        x_int = int(x)
        y_int = int(y)

        # Check bounds
        if 0 <= x_int < 130 and 0 <= y_int < 120:
            # fence[x, y] matches matplotlib (x, y)
            cell_value = self.terrain_grid[x_int, y_int] # Check if (x_int & y_int) match 0,1,2,3
            return cell_value in [0, 3] # In bounds
        
        return False # Out bounds (not walkable)
    def plot_terrain(self, p):
        """
        Stores pictures and gif, and display them on terrain
        """

        xpos, ypos= self.boundary
        width, height = self.size
        x = np.array([xpos, xpos + width, xpos + width, xpos, xpos])
        y = np.array([ypos, ypos, ypos + height, ypos + height, ypos])
        #p.plot(x,y) # Plot boundary
        
        # plot grid after transposing (width,height become height,width)
        p.imshow(self.terrain_grid.T, origin="lower", cmap=cmap)

        x_en, y_en = self.entrance
        #ax.add_patch(plt.Rectangle((x_en , y_en), 20, 5, color=tab20[5])) # entrance gate
        entrance_gate = mpimg.imread("gate.jpg")
        p.imshow(entrance_gate, extent=[x_en, x_en + 30, y_en, y_en + 10])

        exit = mpimg.imread("exit.jpg")
        p.imshow(exit, extent=[120, 130, 25, 55])

        tree = mpimg.imread("tree.png")
        p.imshow(tree, extent=[110, 120, 5, 20])
        p.imshow(tree, extent=[70, 80, 5, 20])


        flower = mpimg.imread("flowers_2.jpg")
        p.imshow(flower, extent=[20, 30, 6, 11])
        p.imshow(flower, extent=[40, 50, 6, 11])

        bush = mpimg.imread("bush.jpg")
        p.imshow(bush, extent=[6, 11, 6, 11])

        stairs = mpimg.imread("stairs.png")
        p.imshow(stairs, extent=[80, 98, 40, 62])

        if len(self.gif_frames) > 0:
            current_frame = self.gif_frames[self.current_frame_index]
            p.imshow(current_frame, extent=[5, 125, 111, 150], alpha=1, aspect='auto')


        #p.show()

       
        
class Patron():
    def __init__ (self, name, marker, position, park):
        """
        name: string, name of patron
        marker: shape used to represent the patron
        """
        self.patron = []
        self.name = name
        self.position = position
        self.marker = marker
        self.park = park
        # state management
        self.state = None
        self.target_waypoint = None # coordinates of chosen ride
        self.chosen_ride = None # ride chosen by patron
        self.queue_position = None # position in queue

        self.x = random.uniform(94, 94) # spawn patrons at entrance
        self.y = random.uniform(0, 10)
        #self.x, self.y = position

        # waypoints directory
        self.waypoints = {
            'entrance': (94, 5),
            'ferris_wheel': (100, 40),
            'ferris_junction': (94, 30),
            'pirate_ship': (51, 30),
            'pirate_junction': (56, 35),
            'drop_junction': (56, 60),
            'exit': (124, 25)   
        }
        

    def plot_patron(self, p):
        """Plot patron at entrance"""
        
        p.plot(self.x, self.y, marker=self.marker, color='blue')
       
    
    def step_change(self, terrain):
        """
        Update patron position
        Verifies terrain for walkability using direct coordinate access
        """
        if self.state == "roaming":
            # Random walk respecting terrain
            self.random_walk(terrain)
            distance = ((self.x - self.waypoints['exit'][0])**2 + (self.y - self.waypoints['exit'][1])**2)**0.5
            if distance < 5:
                self.park.despawn_patron(self)

        elif self.state == "riding_ship":
            # move to pirate ship
            self.move_toward_ride(self.waypoints['pirate_ship'])
            distance = ((self.x - self.waypoints['pirate_ship'][0])**2 + (self.y - self.waypoints['pirate_ship'][1])**2)**0.5
            if distance < 5:
                # Get in line if patron within 5 units
                self.park.make_queue_ship(self)
        elif self.state == "riding_ferris":
            # move to pirate ship
            self.move_toward_ride(self.waypoints['ferris_wheel'])
            distance = ((self.x - self.waypoints['ferris_wheel'][0])**2 + (self.y - self.waypoints['ferris_wheel'][1])**2)**0.5
            if distance < 5:
                # Get in line if patron within 5 units
                self.park.make_queue_ferris(self)
        elif self.state == "riding_tower":
            # move to pirate ship
            self.move_toward_ride(self.waypoints['drop_junction'])
            distance = ((self.x - self.waypoints['drop_junction'][0])**2 + (self.y - self.waypoints['drop_junction'][1])**2)**0.5
            if distance < 5:
                # Get in line if patron within 5 units
                self.park.make_queue_drop(self)

        elif self.state == "leaving":
            # Walk toward exit
            self.move_toward_ride(self.waypoints['exit'])
            distance = ((self.x - self.waypoints['exit'][0])**2 + (self.y - self.waypoints['exit'][1])**2)**0.5
            if distance < 5:
                self.park.despawn_patron(self)
    
    def random_walk(self, terrain):
        """
        Move patron randomly (roaming) while stay on walkable terrain
        Uses terrain.is_walkable() 
        """
        validmoves = [(3,0),(3,3),(-3,-3),(3,-3),(0,3),(0,0),(0,-3),
                      (-3,0),(-3,3)]     # list of valid moves
        move = random.choice(validmoves)       # randomly choose a move
        print((self.x, self.y), move)
        # need to update the position based on the move
        new_x = self.x + move[0]
        new_y = self.y + move[1]
       
        # Verify if new position is walkable (using matplotlib coordinates)
        if terrain.is_walkable(new_x, new_y):
            self.x = new_x
            self.y = new_y
        return (new_x, new_y)

    def move_toward_target(self, target, terrain):
        """
        Move 1 step toward target
        """
        target_x, target_y = target

        # Calculate direction
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx**2 + dy**2)**(0.5) # pythagoras theorem

        if distance < 1:
            # Reached target
            return True # stops walking
        
        step_size = 1
        # take 1 step in direction of target
        new_x = self.x + ((dx / distance) * step_size) 
        new_y = self.y + ((dy / distance) * step_size)

         # Verify if new position is walkable (using matplotlib coordinates)
        if terrain.is_walkable(new_x, new_y):
            # patron moves each time it is on path or grass
            self.x = new_x
            self.y = new_y

        return False # Has not reached target but moved 1 step closer
    
    def move_toward_ride(self, target):
        """
        Move 1 step toward target
        """
        target_x, target_y = target

        # Calculate direction
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx**2 + dy**2)**(0.5) # pythagoras theorem

        if distance < 1:
            # Reached target
            return True # stops walking
        
        step_size = 1
        # take 1 step in direction of target
        new_x = self.x + ((dx / distance) * step_size) 
        new_y = self.y + ((dy / distance) * step_size)

        self.x = new_x
        self.y = new_y

    
        

class Park_Operations():
    """
    Manages all patron and ride operations in park
    """
    def __init__(self, terrain):
        self.terrain = terrain
        self.patrons_list = [] # List of all active patrons
        self.rides = [] # list of all rides
        self.queue_ship = []
        self.queue_ferris = []
        self.queue_drop = []
        self.queue_position = None 
        self.waypoints = {
            'entrance': (94, 5),
            'ferris_wheel': (100, 40),
            'ferris_junction': (94, 30),
            'pirate_ship': (51, 30),
            'pirate_junction': (56, 35),
            'drop_junction': (56, 60),
            'exit': (124, 25)
        }
        self.spawn_count = 0
        self.total_spawned = 0
        self.ship_ride = Ride("Pirate Ship", (35, 30), (15, 20), duration=100, park=self)
        self.ferris_ride = Ride("Ferris Wheel", (50, 70), (65, 40), duration=100, park=self)
    def spawn_patron(self):
        """Spawn patron"""
        self.total_spawned += 1
        name = f"Patron_{self.total_spawned}"

        # Spawn at entrance
        #x, y = self.waypoints['entrance']
        new_patron = Patron(name, 'o', self.waypoints['entrance'], self)
        self.patrons_list.append(new_patron)
        print(f"{name} entered the park.")
        return new_patron
        #return self.patrons_list
    def make_queue_ship(self, patron):
        """
        Make queue for pirate ship (add patron to queue)
        """
        
        if patron not in self.queue_ship[:]:
            self.queue_ship.append(patron)
            patron.state = "queuing"
            patron.queue_position = len(self.queue_ship) - 1 # gives index of patron in line
            print(f"{patron.name} joined pirate ship at position{len(self.queue_ship)}")

            
            # horizontal queue
            
            queue_x = self.waypoints['pirate_ship'][0] + (patron.queue_position * 3) # 3 units apart
            queue_y = self.waypoints['pirate_ship'][1]  
            patron.x = queue_x
            patron.y = queue_y
            return (patron.x, patron.y)
    def make_queue_ferris(self, patron):
        """
        Make queue for ferris wheel (add patron to queue)
        """
        if patron not in self.queue_ferris[:]:
            self.queue_ferris.append(patron)
            patron.state = "queuing"
            patron.queue_position = len(self.queue_ferris) - 1 # gives index of patron in line
            print(f"{patron.name} joined ferris wheel at position{len(self.queue_ferris)}")

            # vertical queue
            queue_x = self.waypoints['ferris_wheel'][0]
            queue_y = self.waypoints['ferris_wheel'][1] - (patron.queue_position * 3) # 3 units apart
            patron.x = queue_x
            patron.y = queue_y
            return (patron.x, patron.y)
    def make_queue_drop(self, patron):
        """
        Make queue for drop tower (add patron to queue)
        """
        if patron not in self.queue_drop[:]:
            self.queue_drop.append(patron)
            patron.state = "queuing"
            patron.queue_position = len(self.queue_drop) - 1 # gives index of patron in line
            print(f"{patron.name} joined drop tower at position{len(self.queue_drop)}")

            # vertical queue
            queue_x = self.waypoints['drop_junction'][0]
            queue_y = self.waypoints['drop_junction'][1] - (patron.queue_position * 3) # 3 units apart
            patron.x = queue_x
            patron.y = queue_y
            return (patron.x, patron.y)
    def move_all_patrons(self):
        """
        Update movement of all patrons in list for one timestep
        """
        for patron in self.patrons_list[:]:
            # change patron position
            patron.step_change(self.terrain)
            
            if patron.state == "leaving":
                distance_from_exit = ((patron.x - self.waypoints['exit'][0])**2 + (patron.y - self.waypoints['exit'][1])**2)**0.5

                if distance_from_exit < 3:
                    self.despawn_patron(patron)

    def update_all_rides(self):
        """
        Update both rides 
        """
        self.ship_ride.update_ship(self)
        self.ferris_ride.update_ferris(self)
    def despawn_patron(self, patron):
            """
            Despawn patron
            """
            if patron in self.patrons_list:
                self.patrons_list.remove(patron)
                print(f"{patron.name} exited the park.")

    def plot_all_patrons(self, p):
        """
        Plot all active patrons
        """
        for patron in self.patrons_list:
            patron.plot_patron(p)

    



