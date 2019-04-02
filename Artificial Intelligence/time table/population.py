
from chromosome import Chromosome
import random



class Population:
    
    
    '''
    A population object contains a list of population of particular size
    In which each element contains a chromosome of n genes, n is number of courses
    Each gene is a time table of a particular course
    '''
    
    
    
    def __init__(self, size, timetables, mutation_rate):
             
        
        '''
        It inputs 
            - the size of population
            - number of timetables/courses present
            - mutation rate
        
        And creates the intial 0-generation population of time tables
        '''
        
        self.generations = 0
        self.fitness = 0
        self.population = []
        self.size = size
        self.mutation_rate = mutation_rate

        for i in range(self.size):
            self.population.append(Chromosome(timetables))
    
    
    
    
    def calculate_fitness(self):
        
        
        '''
        This function calculates fitness of whole of the population, 
        by calculating fitness of each of the chromosome
        '''
        
        
        for chromosome in self.population:
            chromosome.calculate_fitness()
            self.fitness += chromosome.fitness
            

    
    
    def generate(self):
        
        
        '''
        This function creates new generation by evaluating fitness of the 
        chromosomes of the previous ones
        '''

        #normalizing fitness of current generation
        sum = 0
        normalized = []
        for chromosome in self.population:
            sum += chromosome.fitness
        for chromosome in self.population:
            normalized.append(chromosome.fitness / sum)

        new_population = []

        for _ in self.population:
            parent = self.choose_parent(normalized)
            child = parent.crossover()
            child.mutate(self.mutation_rate)
            new_population.append(child)

        self.population = new_population.copy()
        self.generations += 1

    
    
    

    def choose_parent(self, normalized):
        
        
        '''
        In this function random parent is selected from whole of the population
        '''
        
        
        loc = 0
        randm = random.random()

        while randm > 0:
            randm -= normalized[loc]
            loc += 1
        loc -= 1
        return self.population[loc]

    
    
    
    
    
    def get_fittest(self):
        
        
        '''
        In this function the best chromosome of the population
        in a particular generation is being searched
        '''
        
        
        
        fittest_chromosome = self.population[0]
        for chromosome in self.population:
            if chromosome.fitness > fittest_chromosome.fitness:
                fittest_chromosome = chromosome
        return fittest_chromosome



    #TODO
    def isFinished(self):
        pass
