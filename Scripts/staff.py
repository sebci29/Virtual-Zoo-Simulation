import animals as anim

staff_list = []

class Staff_Member():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def save_staff(self, file_name):
        with open(file_name,"r+") as file:
            lines = file.readlines()
            for i,line in enumerate(lines):
                split_line = line.split(',')
                try:
                    if self.name == split_line[0]:
                        lines[i] = f"{self.name},{self.role}\n"
                        return print("Staff saved succesfully!")
                except IndexError:
                    return print("ERROR: Invalid Staff Member")
            lines.append(f"{self.name},{self.role}\n")
            file.seek(0)
            file.truncate()
            file.writelines(lines)
            return print("Staff saved succesfully!")

    def staff_feed(self):
        try:
            animal_fed = int(input("Select Animal to feed (ID): "))
        except ValueError:
            return print("ERROR: Invalid ID")
        for a,animal in enumerate(anim.animal_list):
            if animal_fed == animal.id:
                animal.feed_animal()
                print(f"{self.name} has fed {animal.species} (ID: {animal.id})")
                break
        return print("ERROR: Animal not found")

    def staff_heal(self):
        try:
            animal_healed = int(input("Select Animal to heal (ID): "))
        except ValueError:
            return print("ERROR: Invalid ID")
        for a,animal in enumerate(anim.animal_list):
            if animal_healed == int(animal.id):
                animal.heal_animal()
                print(f"{self.name} has healed {animal.species} (ID: {animal.id})")
                break
        return print("ERROR: Animal not found")


def load_staff(file_name):
    global staff_list
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            split_line = line.split(",")
            try:
                staff_list.append(Staff_Member(split_line[0],split_line[1].strip()))
            except IndexError:
                print("ERROR: Invalid staff member")
                continue
