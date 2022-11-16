from point import *
class Segment:

    def __init__(self, start_point=Point(), end_point=Point(), error=0.1):
        self.__start_point = start_point.get_cords()
        self.__end_point = end_point.get_cords()
        self.__error = error
        self.__A = self.__start_point[1] - self.__end_point[1]
        self.__B = self.__end_point[0] - self.__start_point[0]
        self.__C = self.__start_point[0] * self.__end_point[1] - self.__end_point[0] * self.__start_point[1]


    def get_all_segment_points(self):
        k = (self.__end_point[1] - self.__start_point[1])/(self.__end_point[0] - self.__start_point[0])
        b = self.__start_point[1] - k * self.__start_point[0]
        self.__list_of_points = []
        x1 = float(min(self.__start_point[0], self.__end_point[0]))
        y1 = float(min(self.__start_point[1], self.__end_point[1]))
        x2 = float(max(self.__start_point[0], self.__end_point[0]))
        y2 = float(max(self.__start_point[1], self.__end_point[1]))
        runningX = x1
        runningY = y1
        while runningX <= x2:
            while runningY <= y2:
                if abs(runningY - (k * runningX + b)) <= self.__error:
                    self.__list_of_points.append(Point(runningX, runningY))
                runningY += 0.1
            runningX += 0.1
            runningY = y1

        return self.__list_of_points


    def get_segment_points(self):
        return(self.__start_point, self.__end_point)

    def get_equation(self):
        return [self.__A, self.__B, self.__C]

    def get_segmentDOT(self, cord = 0, axis = 'x'):
        if axis == 'x': i = 0
        else: i = 1
        if cord < min(self.__start_point[i], self.__end_point[i]) or\
        cord > max(self.__start_point[i], self.__end_point[i]):
            return None
        if axis == 'x':
            x = cord
            y = -1 * (self.__C + self.__A * x) / self.__B
            return y
        else:
            y = cord
            x = -1 * (self.__C + self.__B * y) / self.__A
            return x

    def __repr__(self):
        return f"Points of segment: {self.__start_point}, {self.__end_point}"
