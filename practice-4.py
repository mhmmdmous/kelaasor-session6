class Robot:
    def __init__(self, m = 0, n = 0, i = 0, j = 0):
        self.m = m
        self.n = n
        self.i = i
        self.j = j
    
    def update_position(self, di, dj):
        if self.m >= di and self.n >= dj :
            self.i = di
            self.j = dj
        else:
            print("its not correct move!")
    
    def move_right(self):
        if self.i<self.m and self.i>0:
            self.i += 1
            return self.i
        else:
            print("incorrect move!")
    def move_left(self):
        if self.i<self.m and self.i>0:
            self.i -= 1
            return self.i
        else:
            print("incorrect move!")
    def move_up(self):
        if self.j<self.n and self.j>0:
            self.j += 1
            return self.j
        else:
            print("incorrect move!")
    def move_down(self):
        if self.i<self.n and self.i>0:
            self.j -= 1
            return self.j
        else:
            print("incorrect move!")
r = Robot(5, 5, 2, 2)  
r.move_up()  
r.move_left()  
r.move_down()  
r.move_right()
r.move_right()
r.move_right()
r.move_right()  
r.move_right()
r.move_right()
r.move_up()  
print(r.i, r.j)       