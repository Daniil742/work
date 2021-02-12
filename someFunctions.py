# https://pandia.ru/text/79/489/58441.php
# положение точки относительно прямой,
# алгоритм не отличает лежит точка на прямой или на ее продолжении
# доделать этот случай
# так же случай приближенного вычисления
#      [[x1,   y1], [x2,   y2]]
line = [[1.0, 1.0], [1.0, 5.0]]
#       [x,     y]
point = [2.0, 4.0]

#print((point[0] - line[0][0]) * (line[1][1] - line[0][1]) - (point[1] - line[0][1]) * (line[1][0] - line[0][0]))


# в качестве агументов в функцию передаются 2 точки по координатам,
# являющиеся координатами начала и конца отрезка и координаты проверяемой точки

def pointPosition(vertex1, vertex2, point):
    if ((point[0] - vertex1[0]) * (vertex2[1] - vertex1[1]) - (point[1] - vertex1[1]) * (vertex2[0] - vertex1[0]) > 0):
        return True # right или же точка находится справа, то что нам нужно
    elif ((point[0] - vertex1[0]) * (vertex2[1] - vertex1[1]) - (point[1] - vertex1[1]) * (vertex2[0] - vertex1[0]) == 0):
        if ((vertex1[1] <= point[1] <= vertex2[1]) or
            (vertex1[1] >= point[1] >= vertex2[1]) or
            (vertex1[0] <= point[0] <= vertex2[0]) or
            (vertex1[0] >= point[0] >= vertex2[0])):
            return True
        else:
            return False
    else:
        return False # left или же точка находится слева, то что нам не нужно

# http://algolist.ru/maths/geom/belong/poly2d.php
# http://cyber-code.ru/tochka_v_treugolnike/
# для определения принадлежности точки треугольнику
# выясним положение точки относительно каждого ребра треугольника
# в порядке обхода по часовой стрелке, как в моем случае,
# точка будет находиться внутри треугольника, если
# положение относительно каждого ребра будет правым(положительным)
# или ноль если на грани(рассмотреть случай когда точка лежит на продолжении стороны)

# в качестве аргументов в функцию передаются 3 вершины по координатам
# и координаты проверяемой точки
# возвращает:
#  true - точка лежит внутри или на границе треугольника
#  false - точка лежит вне треугольника

triangle = [[1.0, 1.0], [2.0, 5.0], [4.0, 1.0]]
point1 = [0.0, 1.0]
def pointInTriangle(vertex1, vertex2, vertex3, point):
    return (pointPosition(vertex1, vertex2, point) and
            pointPosition(vertex2, vertex3, point) and
            pointPosition(vertex3, vertex1, point))

#print(pointInTriangle(triangle[0], triangle[1], triangle[2], point1))


# угол образован тремя точками,
# функция rotate предназначена для определения выпуклости заданного угла,
# иначе говоря для нахождения коэффициента поворота
# для этих целей подойдет функция pointPosition
# она отрабатывает точно так же как функция rotate
#
#
#
def rotate():
    pass



polygon1 = [[1, 1], [2, 2], [1, 3], [0, 2], [0, 4], [3, 4], [3, 1]]

def triangulate(polygon):
    while len(polygon) != 3:
        for i in range(len(polygon)):
            print(i, "      ", polygon)
            if (i + 2) < len(polygon):
                if (pointPosition(polygon[i], polygon[i + 1], polygon[i + 2]) == True):
                    polygon.remove(polygon[i + 1])
                else:
                    continue
            elif (i + 2) == len(polygon):
                if (pointPosition(polygon[i], polygon[i + 1], polygon[0]) == True):
                    polygon.remove(polygon[i + 1])
                else:
                    continue
            else:
                if (pointPosition(polygon[i], polygon[0], polygon[1]) == True):
                    polygon.remove(polygon[0])
                else:
                    continue
            break

#triangulate(polygon1)
print(pointPosition([2, 1], [2, 3], [2, 4]))
