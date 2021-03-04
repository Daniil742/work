import numpy as np
import matplotlib.pyplot as plt

# функция определения положения точки относительно прямой
def pointPosition(vertex1, vertex2, point):
    if ((point[0] - vertex1[0]) * (vertex2[1] - vertex1[1]) - (point[1] - vertex1[1]) * (vertex2[0] - vertex1[0]) > 0):
        return "Справа" # right или же точка находится справа, то что нам нужно
    elif ((point[0] - vertex1[0]) * (vertex2[1] - vertex1[1]) - (point[1] - vertex1[1]) * (vertex2[0] - vertex1[0]) < 0):
        return "Слева" # left или же точка находится слева, то что нам не нужно
    else:
        return "На прямой"


# функция определения положения точки относительно отрезка
def pointIn(vertex1, vertex2, point):
    x = np.array([vertex1[0] - point[0], vertex1[1] - point[1]])
    y = np.array([vertex2[0] - point[0], vertex2[1] - point[1]])    
    if (pointPosition(vertex1, vertex2, point) == "На прямой"):
        if ((np.dot(x, y)) <= 0):
            return "Лежит на отрезке"
        else:
            return "На прямой"
    elif (pointPosition(vertex1, vertex2, point)) == "Справа":
        return "Справа"
    else:
        return "Слева"

vector = [[1, 1], [2, 3]] # координаты концов отрезка
point = [1.5, 2]        # координаты точки

print(pointIn(vector[0], vector[1], point))

plt.plot([vector[0][0], vector[1][0]], [vector[0][1], vector[1][1]])
plt.plot(point[0], point[1], 'ro')

plt.axis('equal')

plt.show()
