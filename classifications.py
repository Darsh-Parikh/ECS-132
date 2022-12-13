import matplotlib.pyplot as plt
import math

custom_x = [[0.7, 2.8, 3.2, 2.2, 1.3, 0.7], [8.2, 10.9, 13.5, 9.9, 12.3, 6]]
custom_y = [[9.5, 8.6, 13.6, 9.9, 12.3, 8.54], [12.6, 4.4, 9.2, 10.43, 15.9, 3.8]]

X_MAX = 14 ; Y_MAX = 14
plt.ylim([0, Y_MAX])

class Set:
    x = [] ; y = []
    size = 0

    def generate_custom(self, set_id):
       self.x = custom_x[set_id - 1]
       self.y = custom_y[set_id - 1]
       self.size = len(custom_x[set_id - 1])

class Line:
    x = [] ; y = []
    m = 0.0 ; b = 0.0
    ExistingLines = []

    def __init__(self): Line.ExistingLines.append(self)
    
    def classify(self, s1 : Set, s2 : Set):
        p1_x = 0.0 ; p1_y = 0.0
        p2_x = 0.0 ; p2_y = 0.0
        distance = 99999999999999999999999999.9
        for i in range(s1.size):
            for j in range(s2.size):
                d = math.sqrt( (s1.x[i] - s2.x[j])**2 + (s1.y[i] - s2.y[j])**2 )
                if d < distance:
                    p1_x = s1.x[i] ; p1_y = s1.y[i]
                    p2_x = s2.x[j] ; p2_y = s2.y[j]
                    distance = d
        '''
        The vector P1->P2 is perpendicular to the line.
        The midpoint can be found using P1 & P2, and so a vector can be constructed
        from this point to the y-intercept. The dot product of P1->P2 and b->M
        can help find b.
        '''
        self.b = (p2_x**2 - p1_x**2 + p2_y**2 - p1_y**2) / (2 * (p2_y - p1_y))
        self.m = (p1_y + p2_y - 2*self.b) / (p1_x + p2_x)

    def generate_line(self, other_set = None):
        if (other_set != None):
            ...
        
        self.x = [0, X_MAX]     # ! find a better method
        self.y = list(map(lambda a: (self.m * a + self.b), self.x))

    def __repr__(self): return (f"Line = {self.m}x + {self.b}")

set1 = Set(); set1.generate_custom(1)
set2 = Set(); set2.generate_custom(2)
line1 = Line() ; line1.classify(set1, set2)
line1.generate_line()
plt.scatter(set1.x, set1.y, color='red')
plt.scatter(set2.x, set2.y, color='blue')
plt.plot(line1.x, line1.y, color="black")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()