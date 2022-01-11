class Car:

    count = 0

    def __init__(self, make, model, vin, mileage, price, features=[]):
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        self.features = features
        Car.count += 1

    def __del__(self):
        Car.count -= 1

    def getFeatures(self):
        features = ""
        for x in self.features:
            features += x + "\n"
        return features

    def display(self):
        return f"{self.make}, {self.model}, {self.vin}, {self.mileage}, {self.price} \n" \
        f"Features:\n" \
        f"{self.getFeatures()}"