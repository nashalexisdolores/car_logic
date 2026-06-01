class car_logic:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__current_speed = 0

    def accelerate(self):
        self.__current_speed += 5

    def brake(self):
        if self.__current_speed >= 5:
            self.__current_speed -= 5
        else:
            self.__current_speed = 0

    def get_speed(self):
        return self.__current_speed

    def get_info(self):
        return f"{self.__year_model} {self.__make}"