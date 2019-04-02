class TimeSlot:
    
    
    '''
    This class contains the duration of unit slot alloted to a subject in time table.
    A time slot has two parameters, one is course and another is subject.
    '''
    
    
    duration = 1    #duration of unit slot (in hours)

    
    
    def __init__(self, course = None, subject = None):
        self.course = course
        self.subject = subject