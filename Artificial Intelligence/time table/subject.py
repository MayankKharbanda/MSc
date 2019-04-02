class Subject:
    
    
    '''
    The subject object contains a
            -subject id
            -name of the subject
            -teacher who teaches that subject
            -total number of theory slots required for the subject in a week
            -total number of practical slots required for the subject in a week
    '''
    
    
    def __init__(self, subject_id, subject_name, teacher, theory_slots, practical_slots):
        self.id = subject_id
        self.name = subject_name
        self.teacher = teacher
        self.theory_slots = theory_slots
        self.practical_slots = practical_slots
