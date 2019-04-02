from random import shuffle
from timeslot import TimeSlot
import random


class TimeTable:
    
    
    '''
    The class TimeTable is an instance of actual time table.
    It contains:-
            - number of days in a week a course would be taught
            - number of hours in a day the classes would be arranged
    '''
    
    
    days_per_week = 5
    hours_per_day = 8
    num_of_slots_per_day = hours_per_day // TimeSlot.duration       #duration of unit time slots that could be alloted to each lecture.
    num_of_slots_per_week = num_of_slots_per_day * days_per_week

    
    
    '''
    Time table is assigned to a particular course
    all the slots are assigned as first cum first serve
    remaining slots are filled by none 
    '''
    
    
    def __init__(self, course):
        
        assert course is not None
        
        self.course = course
        self.slots = [TimeSlot(self.course) for x in range(0,TimeTable.num_of_slots_per_week)]  #None value has been assigned to the all the possible slots in above statement
        
        
        
        '''
        Each subject's theory and practical slots are summed up and checked if 
        there are enough slots left in a week interval to be alloted 
        '''
        
        occupied_slots = 0
        for subject in self.course.subjects:
            slots_required = int(subject.theory_slots + subject.practical_slots)
            assert slots_required < len(self.slots) - occupied_slots
            for i in range(slots_required):
                self.slots[occupied_slots + i] = TimeSlot(self.course, subject)
            occupied_slots += slots_required

    
    
    '''
    permutate-
        This function outputes a permutated timetable randomly.
    swap-
        This function swaps ith slot with a random slot in the time table.
    '''
    
    
    
    def permutate(self):
        shuffle(self.slots)

    
    
    def swap(self, x):
        y = x
        while y == x:
            y = random.randint(0, len(self.slots) - 1)
        self.slots[x], self.slots[y] = self.slots[y], self.slots[x]