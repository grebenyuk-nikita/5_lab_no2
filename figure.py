
class Figure:

    def __init__(self, points = []):
        self.__points = points

    def get_points(self):
        return self.__points

    def __repr__(self):
        pts_strs = list(map(str,self.__points))
        return f"Points: {pts_strs}".replace('[',']').replace("]","'").replace("'","")
