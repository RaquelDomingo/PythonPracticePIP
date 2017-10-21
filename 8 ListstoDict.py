def make_dict(name, favorite_animal):
    Dictionary = zip(name, favorite_animal)
    new_dict = dict(Dictionary)
    print new_dict


make_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])