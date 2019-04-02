
import pandas as pd
import re
import os
import sys
import warnings



from teacher import Teacher
from subject import Subject
from course import Course
from timetable import TimeTable
from population import Population





def read_data():
    
    
    
    '''
    this function is used to read data from a csv file which has data of type
                subject	    teacher	  theory	       lab
                MCA-101	       NK	       2	           3

    '''

    
    
    
    path="data.csv"
    data_frame = pd.read_csv(path)



    #initializing teachers

    teachers = data_frame['teacher'].unique()
    for i, teacher in enumerate(teachers):
        teachers[i] = Teacher(i, teacher)   #converting teachers list of strings into list of objects  

    
    #displaying teachers
    
    for teacher in teachers:
        print(teacher.id, teacher.name)



    #initializing subjects

    subjects = data_frame['subject']
    for i, row in enumerate(data_frame.values):
        teacher = None
        for p in teachers:
            if p.name == row[1]:
                teacher = p
                break
        theory_slots = row[2]
        practical_slots = row[3]
        subjects[i] = Subject(i, row[0], teacher, theory_slots, practical_slots)
        #subject objects list with each subject having the teacher theory and practical hours. 

    
    #displaying subjects
    
    for subject in subjects:
        print(subject.id, subject.name, subject.teacher.name, subject.theory_slots, subject.practical_slots)
    
    
    
    ##initialize course

    #TODO : dynamically calculate unique_courses
    unique_courses = ['MCA-1','MCA-3','MCS-1','MCS-3']
    courses = []
    for i, course in enumerate(unique_courses):
        reg = r'^' + re.escape(course)
        subs = [sub for sub in subjects if re.match(reg, sub.name)]
        courses.append(Course(i, course, subs))

    
    #displaying courses
    
    for course in courses:
        print(course.id, course.name, [subject.name for subject in course.subjects])



    #initializing timetables by assigning courses as it is
    
    timetables = []
    for course in courses:
        timetables.append(TimeTable(course))
        
    
    #displaying timetables

    for timetable in timetables:
        print(timetable.course.name, [slot.subject.name \
            for slot in timetable.slots if slot.subject is not None] + 
                  [slot.subject for slot in timetable.slots if slot.subject is None])


    return teachers, subjects, unique_courses, courses, timetables, path





def executor():
    
    
    
    '''
    This is the main function from where all the processes are being handled
        - first data is being read from the file
        - a population is being created
        - different generations have been evolved
        - fittest is servived
    '''
    
    
    
    teachers, subjects, unique_courses, courses, timetables, path = read_data()
    
    
    population_size = 251
    no_of_generations = 10000
    mutation_rate = 0.01
    fittest_chromosomes = []

    
    
    population = Population(population_size, timetables, mutation_rate)
    for i in range(no_of_generations):
        population.calculate_fitness()
        fittest_chromosomes.append(population.get_fittest())
        population.generate()
        if i % 100 == 0:
            print(f"Generation {i} of {no_of_generations} completed") 
    print(f"Generation {no_of_generations} of {no_of_generations} completed") 
   
   
    
    final_chromosome = fittest_chromosomes[0]
    for chromosome in fittest_chromosomes:
        if chromosome.fitness > final_chromosome.fitness:
            final_chromosome = chromosome

    
    
    print("Genetic Algorithm completed!")
    final_chromosome.output(os.path.dirname(path))


if __name__ == "__main__":
    
    
    #ignoring warnings
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    

    executor()