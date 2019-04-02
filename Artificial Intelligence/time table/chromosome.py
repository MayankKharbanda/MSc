from gene import Gene
import copy
import csv
import os



class Chromosome:
    
    
    
    '''
    It has an object containing all the time tables of the courses
    '''
    
    
    def __init__(self, timetables):
        self.fitness = 1
        self.genes = []
        for timetable in timetables:
            gene = Gene(timetable)
            gene.permutate()
            self.genes.append(gene)

    
    def calculate_fitness(self):
        
        
        '''
        This function calculate the fitness of the chromosome.
        constraint - 1
        lectures and practicals of a class on "same" day should be together
        constraint - 2
        teacher takes only one class in a slot across all timetables
        '''
        
        #to avoid divide by zero error
        self.fitness = 1
        
         #C-1
        slots_per_day = self.genes[0].timetable.num_of_slots_per_day
        
        '''
        partitioning the slots in days
        eliminating none
        then checking longest streak and adding it to fitness
        '''
        
        
        
        for gene in self.genes:
            
            slots_in_a_day__n = [gene.timetable.slots[i:i+slots_per_day] for i in range (0,len(gene.timetable.slots),slots_per_day)]                        
            slots_in_a_day__n = [[i for i in x if i.subject is not None] for x in slots_in_a_day__n]    
            lectures_day_list__n = [[i.subject.id for i in slot] for slot in slots_in_a_day__n]
            lectures_day_set__n = []
            for subjects in lectures_day_list__n:
                lectures_day_set__n.append(set(subjects))




            for i, lectures_day_list in enumerate(lectures_day_list__n):
                lectures_day_set = lectures_day_set__n[i]
                for subject in lectures_day_set:
                    appearance = [0]
                    streak = False
                    count = 0
                    for subject_list in lectures_day_list:
                        if subject_list == subject and streak:
                            count += 1
                        elif subject_list == subject and not streak:
                            streak = True
                            count += 1
                        elif subject_list != subject and streak:
                            streak = False
                            appearance.append(count)
                            count = 0
                        if subject_list == lectures_day_list[len(lectures_day_list) - 1] and streak:
                            appearance.append(count)


                    self.fitness += max(appearance)
        #C-2
        no_of_slots = len(self.genes[0].timetable.slots)
        no_of_conflicts = 0
        
        
        respective_slots = list(zip(*[t.timetable.slots for t in self.genes]))
        
        for i, timeslot in enumerate(respective_slots):
            #if timeslots in a tuple are none
            if all(v is None for v in timeslot):
                continue
            #if timeslots in a tuple are not none
            timeslot_without_none = [x for x in timeslot if x is not None]
            teachers_list = [x.subject.teacher.id 
                    for x in timeslot_without_none if x.subject is not None]
            teachers_set = set(teachers_list)
            if len(teachers_list) != len(teachers_set):
                no_of_conflicts += 1

        self.fitness += no_of_slots - no_of_conflicts


       
    
    
    
    '''
    crossover
        - just copies the chromosome as it is from parent to child
    mutate
        - it mutates every gene of chromosome with a given rate
    output
        - displays output in a csv file
    '''
    
    
    def crossover(self):
        return copy.copy(self)

    
    def mutate(self, mutation_rate):
        for gene in self.genes:
            gene.mutate(mutation_rate)
  
    
    def output(self, directory):
        dirPath = os.path.join(directory, "timetables")
        os.makedirs(dirPath, exist_ok=True)
        print("Writing data to separate files in",dirPath)
        for gene in self.genes:
            tt_slots = gene.timetable.slots
            filePath = os.path.join(dirPath, tt_slots[0].course.name + ".csv")
            dataList = [slot.subject.name+"-"+slot.subject.teacher.name 
                    if slot.subject is not None else "Empty"
                    for slot in tt_slots ]
            slotsPerDay = gene.timetable.num_of_slots_per_day 
            dataListByDay = [dataList[i:i+slotsPerDay]
                    for i in range(0, len(dataList), slotsPerDay)]
            with open(filePath, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(dataListByDay)
        #todo: theory and practical class should be written

