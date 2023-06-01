class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def make_sound(self):
        return f"{self.name} makes a sound."

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}."


class Mammal(Animal):
    def __init__(self, name, age, species, fur_color, num_legs):
        super().__init__(name, age, species)
        self.fur_color = fur_color
        self.num_legs = num_legs

    def give_birth(self):
        return f"{self.name} gives birth."

    def nurse_young(self):
        return f"{self.name} nurses its young."


class Bird(Animal):
    def __init__(self, name, age, species, wing_span, beak_length):
        super().__init__(name, age, species)
        self.wing_span = wing_span
        self.beak_length = beak_length

    def fly(self):
        return f"{self.name} flies."

    def build_nest(self):
        return f"{self.name} builds a nest."


class Reptile(Animal):
    def __init__(self, name, age, species, scale_color, venom_type):
        super().__init__(name, age, species)
        self.scale_color = scale_color
        self.venom_type = venom_type

    def lay_eggs(self):
        return f"{self.name} lays eggs."

    def shed_skin(self):
        return f"{self.name} sheds its skin."


class Enclosure:
    def __init__(self, size, temperature):
        self.size = size
        self.temperature = temperature
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f"Enclosure with size {self.size} and temperature {self.temperature} has {len(self.animals)} animals."


class Zookeeper:
    def __init__(self, name, years_experience):
        self.name = name
        self.years_experience = years_experience

    def feed_animals(self):
        return f"{self.name} feeds the animals."

    def clean_enclosures(self):
        return f"{self.name} cleans the enclosures."


class Zoo:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.enclosures = []
        self.zookeepers = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def remove_enclosure(self, enclosure):
        self.enclosures.remove(enclosure)

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)

    def remove_zookeeper(self, zookeeper):
        self.zookeepers.remove(zookeeper)

    def __str__(self):
        return f"{self.name} Zoo is located in {self.location} and has {len(self.enclosures)} enclosures and {len(self.zookeepers)} zookeepers."


# Create instances of each animal class
mammal = Mammal("Lion", 5, "Panthera leo", "Golden", 4)
bird = Bird("Eagle", 3, "Aquila chrysaetos", 2.3, 6)
reptile = Reptile("Snake", 2, "Pythonidae", "Green", "Non-venomous")

# Call methods for each animal instance
print(mammal.eat())
print(mammal.give_birth())
print(bird.fly())
print(bird.build_nest())
print(reptile.lay_eggs())
print(reptile.shed_skin())

# Create an instance of the Enclosure class
enclosure = Enclosure(100, 25)

# Add animals to the enclosure
enclosure.add_animal(mammal)
enclosure.add_animal(bird)
enclosure.add_animal(reptile)

# Print information about the enclosure
print(enclosure)

# Create an instance of the Zookeeper class
zookeeper = Zookeeper("John", 10)

# Call methods for the zookeeper instance
print(zookeeper.feed_animals())
print(zookeeper.clean_enclosures())

# Create an instance of the Zoo class
zoo = Zoo("Amazing", "New York")

# Add enclosure and zookeeper to the zoo
zoo.add_enclosure(enclosure)
zoo.add_zookeeper(zookeeper)

# Print information about the zoo
print(zoo)
