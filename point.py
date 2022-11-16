class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_cords(self, x, y):
        self.__x = x
        self.__y = y

    def get_cords(self):
        return (self.__x, self.__y)

    def __repr__(self):
        return f"({self.__x}, {self.__y})"
