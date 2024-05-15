class Hero :
    jumlah_hero = 0
    def __init__ (self,inputName,inputHealth,inputPower,inputArmor):
        self.name   = inputName
        self.health = inputHealth
        self.power  = inputPower
        self.armor  = inputArmor
        Hero.jumlah_hero +=1
    #Method without Return
    def siapa(self):
        print("My Name is "+ self.name)

    def healthUp (self,up):
        self.health += up
    def getHealth (self) :
        return self.health



hero1  = Hero('sniper',100,100,10)
hero2  = Hero('mario',50,50,50) 

hero1.siapa()
print()
hero2.siapa()
print()
hero1.healthUp(10)
print(hero1.getHealth())