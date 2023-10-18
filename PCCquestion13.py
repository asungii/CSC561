import random as Random
import numpy as np

class VitaminBottle:
    def __init__(self, num, hand_ct, hand_variance, red_preference):
        self.num = num
        self.num_red = num / 2
        self.num_blue = self.num - self.num_red
        self.hand_ct = hand_ct
        self.hand_variance = hand_variance
        self.red_preference = red_preference
    
    def updateNum(self):
        self.num = self.num_red + self.num_blue

    # PROBLEM: IT DOESN'T CONTINUE PAST BLUE = 1 AND RED = 0

    # note: i am using index 0 to refer to vitamins
    def pickVitamins(self):
        picked_vitamins = []
        picked_red = 0
        picked_blue = 0
        picked_vitamin_count = round(np.random.normal(8, 1.41421))

        # check if picked_vitamin_count is valid
        if picked_vitamin_count < 0:
            picked_vitamin_count = 0
        elif picked_vitamin_count > self.num:
            picked_vitamin_count = int(self.num)

        for i in range(picked_vitamin_count):
            selected_num = Random.randint(0, self.num - 1)
            if (selected_num < self.num_red):
                picked_vitamins.append("red")
                picked_red += 1
                self.num_red -= 1
                self.updateNum()
            else:
                picked_vitamins.append("blue")
                picked_blue += 1
                self.num_blue -= 1
                self.updateNum()
        
        if ("red" in picked_vitamins) and ("blue" in picked_vitamins):
            choice = Random.randint(0,9)
            # if blue is picked
            if choice == 0:
                self.num_blue += picked_blue - 1
                self.num_red += picked_red
                self.updateNum()
            # if red is picked
            else:
                self.num_red += picked_red - 1
                self.num_blue += picked_blue
                self.updateNum()
        elif ("blue" not in picked_vitamins):
            self.num_red += picked_red - 1
            self.num_blue += picked_blue
            self.updateNum()
        elif ("red" not in picked_vitamins):
            self.num_blue += picked_blue - 1
            self.num_red += picked_red
            self.updateNum()
        
        if (self.num < 0):
            return

        print(print(*picked_vitamins, sep = ", "))
        print("Blue: " + str(self.num_blue))
        print("Red: " + str(self.num_red))


vb = VitaminBottle(500, 8, 2, 0.9)
for i in range(1000):
    vb.pickVitamins()