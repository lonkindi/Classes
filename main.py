class animals:
    name = ''
    weight = 0

    def feed(self):
        print(f"I'm {self.name}. Good! I am full!")

    def clean_up(self):
        print('Fine! I am clean!')

    def animal_sound(self, sound):
        old_str = "'>"
        print(f"{sound}! This is sound of {str(type(self)).replace(old_str, '')[17:]} {self.name}")


class goose(animals):
    def laid_egg(self):
        print(f'I am goose {self.name}. It is a my goose eggs.')


class cow(animals):
    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight

    def to_milk(self):
        print('Milk a cow.')


class sheep(animals):
    def shear(self):
        print('Get sheep wool.')


class chicken(animals):
    def laid_egg(self):
        print('It is a chicken eggs.')


class goat(animals):
    def to_milk(self):
        print('Milk a goat.')

    def shear(self):
        print('Get goat wool.')


class duck(animals):
    def laid_egg(self):
        print('It is a duck eggs.')


Goose1 = goose()
Goose1.name = 'Gray'
Goose1.weight = 9
Goose1.laid_egg()
Goose1.clean_up()
Goose1.animal_sound('G-g-g-g-g')

Goose2 = goose()
Goose2.name = 'White'
Goose2.weight = 11
Goose2.animal_sound('Ga-ga-ga')

Cow1 = cow('Buryonka', 240)
print(f'I am cow {Cow1.name}, my weight = {Cow1.weight} kg')
Cow1.to_milk()
Cow1.animal_sound('Muuuuuu')

Sheep1 = sheep()
Sheep1.name = 'Lamb'
Sheep1.weight = 30
Sheep1.animal_sound('Be-e-e-e-e-e')
Sheep1.shear()

Sheep2 = sheep()
Sheep2.name = 'Curly'
Sheep2.weight = 32
Sheep2.animal_sound('Be-be-be-be')
Sheep2.feed()

Chicken1 = chicken()
Chicken1.name = 'Co-co'
Chicken1.weight = 5
Chicken1.animal_sound('Cocococo')
Chicken1.laid_egg()

Chicken2 = chicken()
Chicken2.name = 'Kukareku'
Chicken2.weight = 4
Chicken2.animal_sound('Ku-ka-re-ku')
Chicken2.clean_up()

Goat1 = goat()
