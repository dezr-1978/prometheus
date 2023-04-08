'''
Написати функцію maze_controller(mr), єдиним аргументом якої є вже ініціалізований (перевіряльником) об'єкт класу MazeRunner. Функція нічого не повертає, але в результаті її виконання робот має бути переведений в поле лабіринту, де знаходиться артефакт -- тобто після виклику функції maze_controller(maze_runner), метод об'єкту maze_runner.found() повинен повертати True.
Прямий доступ до зображення лабіринту заборонено.
Ваш розв'язок повинен містити лише функцію maze_controller і нічого крім неї. Жодного введення або виведення даних крім взаємодії з переданим об'єктом бути не повинно. Об'єкт керування роботом створюється та ініціалізується автоматичним перевіряльником поза межами вашої функції.
Як завжди, для коректної роботи тестувальника ваш код не повинен містити коментарів, кирилиці, перевірок на те, чи є програма головним модулем, підключення нестандартних модулів, функції exit().
Нагадуємо, що в загальний рейтинг зараховуються бали за останню використану спробу, незалежно від її порядкового номеру.
'''

def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '

class MazeRunner(object):
    
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print_maze(self.__maze, self.__x, self.__y)
        return True
    
    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self
    
    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self
    
    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]

def maze_controller(self):
        class Robo(object):
            def __init__(self, r, o=0, x=0, y=0):
                self.__r = r
                self.__o = o
                self.__kx, self.__ky = 0, 0
                self.__px, self.__py = None, None
                self.__s = 0
                self.__k = {(self.__kx,self.__ky): 1}
                self.__p = []

            def turn(self, d=0):
                if d<0:
                    for i in range(-1*d):
                        self.__r.turn_left()
                        self.__o = 3 if self.__o == 0 else self.__o - 1
                if d>0:
                    for i in range(d):
                        self.__r.turn_right()
                        self.__o = 0 if self.__o == 3 else self.__o + 1
                return self

            def go(self, real_step=True):
                px, py = self.__kx, self.__ky
                if self.__r.go():
                    if self.__o == 0:
                        self.__kx, self.__ky = self.__kx + 1, self.__ky
                    elif self.__o == 1:
                        self.__kx, self.__ky = self.__kx, self.__ky + 1
                    elif self.__o == 2:
                        self.__kx, self.__ky = self.__kx - 1, self.__ky
                    else:
                        self.__kx, self.__ky = self.__kx, self.__ky - 1

                    if real_step:
                        self.__s += 1
                        if len(self.__p)==0: self.__p.append((px,py))
                        if len(self.__k)==0: self.__k[(px,py)]==1
                        self.__p.append(self.xy())
                        self.__k[self.xy()] = 1 if not self.xy() in self.__k \
                            else self.__k.get(self.xy()) + 1
                    else:
                        if not self.xy() in self.__k:
                            self.__k[self.xy()] = 0

                    return True
                return False

            def step_back(self):
                self.turn(2)
                self.go(False)
                self.turn(2)
                return self

            def step(self):
                return self.__s

            def found(self):
                return self.__r.found()

            def xy(self):
                return (self.__kx, self.__ky)

            def path(self):
                return self.__p

            def knop(self):
                return self.__k

            def look_around(self):
                l = [99999999, 9999999, 9999999]

                if self.go(False):
                    l[0] = self.__k.get(self.xy())
                    self.step_back()
                self.turn(-1)

                if self.go(False):
                    l[1] = self.__k.get(self.xy())
                    self.step_back()
                self.turn(2)

                if self.go(False):
                    l[2] = self.__k.get(self.xy())
                    self.step_back()
                self.turn(-1)
                
                return l

        robo = Robo(self)

        while not robo.found():
            if robo.step()>2000: break
            x = robo.look_around()

            if x[0]==x[1]==x[2]==9999999:
                robo.turn(-2).go()

            elif x[0] == min(x):
                robo.go()

            elif x[1] == min(x):
                robo.turn(-1).go()

            elif x[2] == min(x):
                robo.turn(1).go()



maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 1'

maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}
maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 2'

maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 3'

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 4'

maze_example6 = {
    'm': [
        [1,0,1,0,1],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [1,0,1,0,1],
    ],
    's': (2,0),
    'f': (2,4)
}
maze_runner = MazeRunner(maze_example6['m'], maze_example6['s'], maze_example6['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 6'

maze_example7 = {
    'm': [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,1,0],
        [0,1,0,0,1,0,1,0],
        [0,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,1,0],
        [1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0],
    ],
    's': (3, 2),
    'f': (7, 0)
}
maze_runner = MazeRunner(maze_example7['m'], maze_example7['s'], maze_example7['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 7'

maze_example8 = {
    'm': [
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ],
    's': (0,1),
    'f': (0,3)
}
maze_runner = MazeRunner(maze_example8['m'], maze_example8['s'], maze_example8['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 8'

maze_example10 = {
    'm': [
        [1,0,0,0,1,0,0,1],
        [1,0,1,0,1,1,0,1],
        [1,0,1,0,0,0,0,1],
        [1,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,0],
        [1,0,1,0,1,0,1,0],
    ],
    's': (0, 3),
    'f': (7, 5)
}
maze_runner = MazeRunner(maze_example10['m'], maze_example10['s'], maze_example10['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 10'

maze_example5 = {
    'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 5'

maze_example9 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,1,0,1,0,0],
        [0,1,0,1,1,0,1,0,1,1,1],
        [0,1,0,0,1,0,1,0,0,0,0],
        [0,1,1,0,1,0,1,0,1,1,0],
        [0,1,0,0,1,0,1,0,1,0,0],
        [0,1,0,1,1,0,1,0,1,0,1],
        [0,1,0,0,1,0,1,0,1,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0, 5),
    'f': (2, 5)
}
maze_runner = MazeRunner(maze_example9['m'], maze_example9['s'], maze_example9['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 9'

maze_example11 = {
    'm': [
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,1,1,1,1,0],
        [0,1,0,1,0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0,1,1,1,0],
        [0,1,1,1,1,1,0,1,0,0,0],
        [0,1,0,0,1,1,0,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,1,0],
        [0,0,0,1,0,1,0,1,0,1,0],
        [0,0,0,0,0,1,0,0,0,0,0],
    ],
    's': (4, 8),
    'f': (9, 1)
}
maze_runner = MazeRunner(maze_example11['m'], maze_example11['s'], maze_example11['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 11'

maze_example12 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,1,0,0,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,1,1,0,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (6, 4),
    'f': (10, 5)
}
maze_runner = MazeRunner(maze_example12['m'], maze_example12['s'], maze_example12['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 12'

maze_example13 = {
    'm': [
        [0,1,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,1,0,1,0,1,0],
        [0,0,0,0,0,0,0,1,0,1,0],
        [0,1,0,1,1,1,0,1,0,1,0],
        [0,1,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,1,0],
    ],
    's': (10, 5),
    'f': (6, 4)
}
maze_runner = MazeRunner(maze_example13['m'], maze_example13['s'], maze_example13['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 13'

maze_example14 = {
    'm': [
        [1,0,1,1,1,0,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,1,1,1,0,0,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
    ],
    's': (10, 1),
    'f': (7, 7)
}
maze_runner = MazeRunner(maze_example14['m'], maze_example14['s'], maze_example14['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 14'

maze_example15 = {
    'm': [
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,0,1,0,1,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,0,1,0,1,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
    ],
    's': (1, 1),
    'f': (9, 9)
}
maze_runner = MazeRunner(maze_example15['m'], maze_example15['s'], maze_example15['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 15'

