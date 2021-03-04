#https://ru.wikipedia.org/wiki/Пересечение_прямых
#https://gospodaretsva.com/urok-32-peresekayutsya-li-dva-otrezka.html

import numpy as np
import matplotlib.pyplot as plt

# функция определения положения точки относительно прямой
def pointPosition(vertex1, vertex2, point):
    if ((point[0] - vertex1[0]) * (vertex2[1] - vertex1[1])
        - (point[1] - vertex1[1]) * (vertex2[0] - vertex1[0]) > 0):
        return "Справа" # right или же точка находится справа, то что нам нужно
    elif ((point[0] - vertex1[0]) * (vertex2[1] - vertex1[1])
          - (point[1] - vertex1[1]) * (vertex2[0] - vertex1[0]) < 0):
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


# функция определяющая положения отрезков
def lineInLine(point1, point2, point3, point4):
    if (pointIn(point1, point2, point3) == "Лежит на отрезке" and pointIn(point1, point2, point4) == "Лежит на отрезке"):
        return "2 в 1"
    elif (pointIn(point3, point4, point1) == "Лежит на отрезке" and pointIn(point3, point4, point2) == "Лежит на отрезке"):
        return "1 в 2"
    elif (pointIn(point1, point2, point4) == "Лежит на отрезке" and pointIn(point3, point4, point1) == "Лежит на отрезке"):
        return "Снизу1"
    elif (pointIn(point1, point2, point3) == "Лежит на отрезке" and pointIn(point3, point4, point1) == "Лежит на отрезке"):
        return "Снизу2"
    elif (pointIn(point1, point2, point3) == "Лежит на отрезке" and pointIn(point3, point4, point2) == "Лежит на отрезке"):
        return "Сверху1"
    elif (pointIn(point1, point2, point4) == "Лежит на отрезке" and pointIn(point3, point4, point2) == "Лежит на отрезке"):
        return "Сверху2"
    else:
        return "1 точка"
    

# функция отпределения пересечения отрезков
def peresLines(point1, point2, point3, point4):
    vector34 = [point4[0] - point3[0], point4[1] - point3[1]] #координаты векторов
    vector31 = [point1[0] - point3[0], point1[1] - point3[1]]
    vector12 = [point2[0] - point1[0], point2[1] - point1[1]]
    vector13 = [point3[0] - point1[0], point3[1] - point1[1]]
    vector32 = [point2[0] - point3[0], point2[1] - point3[1]]
    vector14 = [point4[0] - point1[0], point4[1] - point1[1]]
    v1 = vector34[0] * vector31[1] - vector34[1] * vector31[0]
    v2 = vector34[0] * vector32[1] - vector34[1] * vector32[0]
    v3 = vector12[0] * vector13[1] - vector12[1] * vector13[0]
    v4 = vector12[0] * vector14[1] - vector12[1] * vector14[0]
    if (((v1 * v2 < 0) and (v3 * v4 < 0))
        or pointIn(point1, point2, point3) == "Лежит на отрезке"
        or pointIn(point1, point2, point4) == "Лежит на отрезке"
        or pointIn(point3, point4, point1) == "Лежит на отрезке"
        or pointIn(point3, point4, point2) == "Лежит на отрезке"):
        return "Пересекаются"
    else:
        return "Не пересекаются"


# функция нахождения точки пересечения отрезков
def pointPeres(point1, point2, point3, point4):
    if (lineInLine(point1, point2, point3, point4) == "2 в 1"):
        return [point3, point4]
    elif (lineInLine(point1, point2, point3, point4) == "1 в 2"):
        return [point1, point2]
    elif (lineInLine(point1, point2, point3, point4) == "Снизу1"):
        return [point1, point4]
    elif (lineInLine(point1, point2, point3, point4) == "Снизу2"):
        return [point1, point3]
    elif (lineInLine(point1, point2, point3, point4) == "Сверху1"):
        return [point2, point3]
    elif (lineInLine(point1, point2, point3, point4) == "Сверху2"):
        return [point2, point4]
    else:
        if peresLines(point1, point2, point3, point4) == "Пересекаются":
            D = ((point1[0] - point2[0]) * (point3[1] - point4[1])
                 - (point1[1] - point2[1]) * (point3[0] - point4[0]))
            px = ((point1[0] * point2[1] - point1[1]
                   * point2[0]) * (point3[0] - point4[0]) - (point1[0] - point2[0])
                   * (point3[0] * point4[1] - point3[1] * point4[0])) / D
            py = ((point1[0] * point2[1] - point1[1] * point2[0])
                  * (point3[1] - point4[1]) - (point1[1] - point2[1])
                  * (point3[0] * point4[1] - point3[1] * point4[0])) / D
            return [px, py]
        else:
            return "Не пересекаются"

# менять line1 и line2
line1 = [[0, 0], [4, 4]] # координаты началаи конца первого отрезка
line2 = [[1, 1], [3, 3]] # координаты началаи конца второго отрезка

print(peresLines(line1[0], line1[1], line2[0], line2[1]))
point = pointPeres(line1[0], line1[1], line2[0], line2[1])
print("point = ", point)

plt.plot([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]])
plt.plot([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]])

if (point == "Не пересекаются"):
    pass
elif (type(point[0]).__name__ == 'float'):
    plt.plot(point[0], point[1], 'ro')
elif (type(point[0]).__name__ == 'list'):
    plt.plot(point[0][0], point[0][1], 'ro')
    plt.plot(point[1][0], point[1][1], 'ro')

plt.axis('equal')
plt.show()

