class Course:
    
    
    '''
    Course object contains
        -an id of course
        -course name
        -subjects associated with that course
    '''
    
    
    def __init__(self, course_id, course_name, subjects):
        self.id = course_id
        self.name = course_name
        self.subjects = subjects
