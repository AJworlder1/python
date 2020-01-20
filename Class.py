class Death():
    age = 999999
    name = "Death"
    weight = 0

#--------------
class Egor_Bakunin():
    name = "Egor"
    cellPhone = "58801856"
    email = "kafder97@gmail.com"

#--------------
class Person:
    name = "Elatrin"
    money = 99999999

Elatrin = Person()
name = "Elatrin"
money = 99999999

#--------------
class Person:
    name = "Elatrin"
    money = 999999999

Elatrin = Person()
print(Elatrin.name,"has",money,"bits.")

#--------------
class Cat():

    def __init__ (self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def meow(self):
        print(self.name + " лёг спать...")
        print(self.name + " мурлычит...")

cot = Cat("Эдвин Кяяпа","Русый",13)
cot.meow()

#------------
class Monster():

    def __init__ (self, name, hp, age, race):
        self.name = name
        self.hp = hp
        self.age = age
        self.race = race

    def info(self):

        time.sleep(0.6)
        print( "Имя: " + self.name )
        time.sleep(0.8)
        print( "Возраст: " + str( self.age ) )
        time.sleep(0.7)
        print( "Здоровье: " + str( self.hp ) )
        time.sleep(0.8)
        print( "Расса: " +  self.race  )
        time.sleep(0.6)
        print()

    def fight(self):

        print(self.name + " Начал драку с: Омником!")
        time.sleep(0.6)
        self.hp -= 100
        print("Здоровье"+ self.name + " = " + str(self.hp))
                      
        if self.hp() <= "0":
            print("Вы умерли!")
            input("Нажите \"ENTER\ чтобы завершить процесс программы!")
            exit()
              
lox = Monster( "Элатрин",100,999,"Нефритовый Король" )
