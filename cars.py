# 1. Create a single class that implements all functionality.
class CarStuff:
    
# 2. Create a method for reading the car makes file.
    def readMakes(self):
        with open('data/car-makes.txt', "r") as makes:
            makesList = makes.readlines()
            for i, make in enumerate(makesList):
                # Stripping takes out the line break "\n"
                makesList[i] = make.strip()
            return makesList 

# 3. Create a method for reading the car models file.
    def readModels(self):
        with open('data/car-models.txt', "r") as models:
            modelsList = models.readlines()
            for i, model in enumerate(modelsList):
                modelsList[i] = model.strip().replace('=','')
            return modelsList
# 4. Create a method that invokes the previous two methods and generates a dictionary.
#   i. The dictionary keys will be the make names.
#   i. The value for each key will be a list of model names.
    def combiningCars(self):
        makes = self.readMakes()
        models = self.readModels()

        makes_models = dict()
        for make in makes:
            makes_models[make] = []


        for model in models:
            for make in makes_models.keys():
                if make.startswith(model[0]):
                    makes_models[make].append(model[2:])

        return makes_models

readItAll = CarStuff()
print(readItAll.combiningCars())
