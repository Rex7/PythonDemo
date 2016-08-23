# just a simple demo for class


class Weapon:

    def __init__(self, gun_range, capacity, weight, bullet_size, gun_type):
        self.gun_type = gun_type
        self.capacity = capacity
        self.weight = weight
        self.bullet_size = bullet_size
        self.gun_range = gun_range

    def display_gun(self):
        print("Gun Type:{0}\nMagazine Capacity :{1}\nWeight in gram:{2} gm\nBullet Size in millimeter:{3}\nGun Range:{4}"
              .format(self.gun_type, self.capacity, self.weight, self.bullet_size, self.gun_range))
gun=Weapon("long", 12,50, .44, "Rifle")
gun.display_gun()
