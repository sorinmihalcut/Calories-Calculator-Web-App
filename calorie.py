from temperature import Temperature

class Calorie:
    """
    Represents amount of calories calculated with
    BNR = 10*weight + 6.25*height - 5*age - 10*temperature
    """
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature
        return result

if __name__ == '__main__':
    temperature = Temperature(country='italy', city='rome').get()
    calorie = Calorie(temperature= temperature, weight=70, height=175, age=32)
    print(calorie.calculate())