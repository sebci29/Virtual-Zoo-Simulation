from ast import Index
from random import randint

animal_sick_chance = 10
animal_hungry_chance = 50
animals = []
health_conditions = ["Healthy", "Sick", "Hungry/Healthy", "Hungry/Sick"]

class Animal():
    def __init__(self, species, age, health_status, enclosure, id):
        self.species = species
        self.age = age
        self.health_status = health_status
        self.enclosure = enclosure
        self.id = id
        
    def species_update(self):
        self.species = input("New species classification: ")
        print("Species succesfully changed!")
    
    def age_update(self):
        self.age += 1
        
        sick_chance = randint(0,100)
        if sick_chance < animal_sick_chance:
            self.health_status = "Sick"
            print(f"ID: {self.id} - {self.species} is now sick")

        hunger_chance = randint(0,100)
        if hunger_chance < animal_hungry_chance:
            if self.health_status == health_conditions[0]:
                self.health_status = health_conditions[2]
                print(f"ID: {self.id} - {self.species} is now hungry")
            elif self.health_status == health_conditions[1]:
                self.health_status = health_conditions[3]
                print(f"ID: {self.id} - {self.species} is now hungry")
        return
            
    def feed_animal(self):
        if self.health_status == health_conditions[2]:
            self.health_status = health_conditions[0]
            print(f"ID: {self.id} - {self.species} is no longer hungry")
        elif self.health_status == health_conditions[3]:
            self.health_status = health_conditions[1]
            print(f"ID: {self.id} - {self.species} is no longer hungry")
        return
    
    def heal_animal(self):
        self.health_status = "Healthy"
        print(f"ID: {self.id} - {self.species} is now healthy")
    
    def enclosure_update(self):
        self.enclosure = input("New enclosure: ")
        print("Enclosure succesfully changed!")
    
    def save_animal(self, file_name):
        with open(file_name,"r+") as file:
            lines = file.readlines()
            for i,line in enumerate(lines):
                split_line = line.split(',')
                try:
                    if self.id == int(split_line[4].strip()):
                        lines[i] = f"{self.species},{self.age},{self.health_status},{self.enclosure},{self.id}\n"
                        return print("Animal saved succesfully!")
                except IndexError:
                    return print("ERROR: Invalid Animal")
            lines.append(f"{self.species},{self.age},{self.health_status},{self.enclosure},{self.id}\n")
            file.seek(0)
            file.truncate()
            file.writelines(lines)
            return print("Animal saved succesfully!")
        
    def display_animal(self):
        print(f"ID: {self.id.strip()} - {self.species} - Age (days): {self.age} - Condition: {self.health_status} - Enclosure: {self.enclosure}")

def load_animals(file_name):
    global animals
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            split_line = line.split(",")
            try:
                animals.append(Animal(split_line[0],int(split_line[1]),split_line[2],split_line[3],split_line[4]))
                continue
            except IndexError:
                print("ERROR: Invalid Animal")
                continue
