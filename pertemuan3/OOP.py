class Hero:
    name = "Martis"
    hp = 3000
    damage = 200
    defanse = 100 

    def __init__(self, name, hp, damage, defanse):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defancs = defanse

    def attack(self, target):
        target.hp = target.hp - self.damage
        print("Sisa HP ", target.name, "=", target.hp)

# inisialisasi class hero
hero1 = Hero("Sun", 2000, 300, 15)
hero2 = Hero("jonson", 3000, 50, 300)

hero1.attack(hero2)
hero2.attack(hero1)