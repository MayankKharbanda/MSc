import random

class Gene:
    
    
    
    '''
    Object of gene contains an instance of a time table of a particular class.
    It has two functions--
        1. Permutate -- It calls permutate function from timetable class.
        2. Mutate -- It calls swap function from timetable class with a mutation rate/2 probability
            mutation is divided by two as swap changes two slots simultaneously.
    '''
    
    
    
    def __init__(self, timetable):
        self.timetable = timetable

    def permutate(self):
        self.timetable.permutate()

    def mutate(self, mutation_rate):
        for i in range(len(self.timetable.slots)):
            if random.random() < mutation_rate / 2:
                self.timetable.swap(i)
