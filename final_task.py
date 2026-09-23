#Final assessment of the module Fundamentals of Computing
import tkinter as tk
from tkinter import *

#Link to my GitHub repository: https://github.com/MSedan/Hallam
#Data for the planets
#Mass is in kilograms, distance from the sun is in kilometers. For formatting I used the help of this page: https://www.geeksforgeeks.org/python/print-number-commas-1000-separators-python/
#Moons are capped at 5. 

class Planet:
       def __init__(self, name, mass, distance_from_sun, number_of_moons, names_of_moons):
              self.name = name
              self.mass = mass
              self.distance_from_sun = distance_from_sun
              self.number_of_moons = number_of_moons
              self.names_of_moons = names_of_moons
              
       def get_name(self):
              return self.name
       def get_mass(self):
              return self.mass
       def get_distance_from_sun(self):
              return self.distance_from_sun
       def get_number_of_moons(self):
              return self.number_of_moons
       def get_names_of_moons(self):      
              return self.names_of_moons

mercury = Planet("Mercury", 3.3011*10**23, 46000000, 0, [])
venus = Planet("Venus", 4.8675*10**24, 108000000, 0, [])
earth = Planet("Earth", 5.972168*10**24, 149600000, 1, ["Moon"])
mars = Planet("Mars", 6.4171*10**23, 230000000, 2, ["Phobos", "Deimos"])
jupiter = Planet("Jupiter", 1.8982*10**27, 778000000, 97, ["Io", "Europa", "Ganymede", "Callisto", "Themisto"])
saturn = Planet("Saturn", 5.6834*10**26, 1434000000, 274, ["Titan", "Rhea", "Pandora", "Prometheus", "Enceladus"])
uranus = Planet("Uranus", 8.6810*10**25, 2000000000, 29, ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"])
neptune = Planet("Neptune", 1.02409*10**26, 4500000000, 16, ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa"])

valid_planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

#Used W3Schools for a reminder on global variables https://www.w3schools.com/python/python_variables_global.asp
current_planet = None

#Function for user input
def get_entry(entry):
       planet = entry.get().lower().capitalize()
       return planet

#Function to check the input and move to frame 2
def check_if_planet(planet):
       global current_planet
       if planet in [p.get_name() for p in valid_planets]:
              show_frame2()
              current_planet = planet
              label_main_frame2.config(text = f"You have picked {current_planet}", fg="green", font="50")
       elif planet == "":
              error_label.config(text="Please enter a planet name.", fg="red")
       else:
              error_label.config(text=planet + " is not a planet or you have made a typo. Please try again.", fg="red")

#Get mass of the planet
def get_planet_mass(current_planet):
       for planet in valid_planets:
              if planet.get_name() == current_planet:
                     mass = planet.get_mass()
                     return mass

#Function to display mass
def display_mass():
       mass = get_planet_mass(current_planet)
       mass_label.config(text=f"The mass of {current_planet} is {mass:.3e} kg.")
       
#Function to get distance from the sun
def get_distance_from_sun(current_planet):
       for planet in valid_planets:
              if planet.get_name() == current_planet:
                     distance = planet.get_distance_from_sun()
                     return distance

#Function to display distance from the sun
def display_distance():
       distance = get_distance_from_sun(current_planet)
       distance_label.config(text=f"The distance of {current_planet} from the sun is {distance:,.0f} km.")

#Funtion to get number of moons
def get_number_of_moons(current_planet):
       for planet in valid_planets:
              if planet.get_name() == current_planet:
                     number_of_moons = planet.get_number_of_moons()
                     return number_of_moons
              
#Function to display number of moons
def display_number_of_moons():
       number_of_moons = get_number_of_moons(current_planet)
       number_moons_label.config(text=str(current_planet) + " has " + str(number_of_moons) + " moons.")

#Function to get names of moons
def get_names_of_moons(current_planet):
       for planet in valid_planets:
              if planet.get_name() == current_planet:
                     names_of_moons = planet.get_names_of_moons()
                     return names_of_moons
              
#Function to display names of moons
def display_names_of_moons():
       names_of_moons = get_names_of_moons(current_planet)
       if len(names_of_moons) > 1:
              names_moons_label.config(text="The names of the moons for " + str(current_planet) + " are: " + ", ".join(names_of_moons) + ".")
       elif  len(names_of_moons) == 0:
              names_moons_label.config(text=str(current_planet) + " has no moons.")
       elif len(names_of_moons) == 1:
              names_moons_label.config(text=str(current_planet) + "'s moon is " + str(names_of_moons) + ".")
       

#Functions to switch between frames
def show_frame2():
       frame1.pack_forget()
       frame2.pack()
       mass_label.config(text="")
       distance_label.config(text="")
       number_moons_label.config(text="")
       names_moons_label.config(text="")

def return_to_frame1():
       frame2.pack_forget()
       frame1.pack()
       error_label.config(text="")


#Used this page to help with Tkinter https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
#Creating the main window
window = Tk()
window.title("Solar system planets")
window.geometry("600x500")

#First frame
frame1 = tk.Frame(window)
frame1.pack()
label_main_frame1 = tk.Label(frame1, text = "Please type a planet you would like to learn about:", font="50")
label_main_frame1.pack(pady=20)
entry = tk.Entry(frame1, width = 40)
entry.pack(pady=10)
check_button = tk.Button(frame1, text = "Submit", command=lambda: check_if_planet(get_entry(entry)),
                         cursor = "hand2")
check_button.pack(pady=10)
error_label = tk.Label(frame1, text = "")
error_label.pack()

#Creating the second frame
frame2 = tk.Frame(window)
label_main_frame2 = tk.Label(frame2, text = "")
label_main_frame2.pack(pady=20)

#Buttons and labels for frame 2
#Used this page to help with Tkinter labels https://coderslegacy.com/python/tkinter-config/
button_mass = tk.Button(frame2, text = "Mass", command= lambda: display_mass(),
                         cursor = "hand2")
button_mass.pack(pady=10)
mass_label = tk.Label(frame2, text="")
mass_label.pack()

button_distance = tk.Button(frame2, text = "Distance from the sun", command= display_distance,
                         cursor = "hand2")
button_distance.pack(pady=10)
distance_label = tk.Label(frame2, text="")
distance_label.pack()

button_number_moons = tk.Button(frame2, text = "Number of moons", command= display_number_of_moons,
                            cursor = "hand2")
button_number_moons.pack(pady=10)
number_moons_label = tk.Label(frame2, text="")
number_moons_label.pack()

button_names_moons = tk.Button(frame2, text = "Name of moons", command= display_names_of_moons,
                          cursor = "hand2")
button_names_moons.pack(pady=10)
names_moons_label = tk.Label(frame2, text="")
names_moons_label.pack()

button_new_planet = tk.Button(frame2, text = "Choose a new planet",
                          cursor = "hand2", command= return_to_frame1)
button_new_planet.pack(pady=10)

button_exit = tk.Button(frame2, text = "Exit",
                          cursor = "hand2", command=window.quit)
button_exit.pack(pady=10)

window.mainloop()