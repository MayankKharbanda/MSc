# Importing required function made in func.py
import func
from func import Relation, FunctionalDependencySet

# Enter the set of attributes 
set_attributes = input("Enter Relation Attributes: ")
print(set_attributes)

# Enter the functional dependencies : SEPARATED BY ','
fdString = input("Functional Dependencies (LHS and RHS seperated by '->' and each FD seperated by ','): ")

# Splitting functional dependencies and assigning it to class functional dependency setand assigning to "fd" object
fd = FunctionalDependencySet([ fd for fd in fdString.split(',')])

# Making an object of class Relation 
relation = Relation(set_attributes, fd)
print("\n")

# Printing the relation 
print(relation.toString())
print("\n")

# Printing candidate key of relation
print('Candidate Keys:', relation.candidateKeys())

# Enter attributes whose closure is to find out
closureAtrributes = input("Attributes to find Closure: ")
print("Closure of", closureAtrributes, ":", relation.closureSet(closureAtrributes)) #Printing closure of given attribute

print("Relation is 1NF?", 'Yes' if func.isFirstNF(relation) else 'No')  # Checking if relation is in 1NF
print("Relation is 2NF?", 'Yes' if func.isSecondNF(relation) else 'No') # Checking if relation is in 2NF
print("Relation is 3NF?", 'Yes' if func.isThirdNF(relation) else 'No')  # Checking if relation is in 3NF
print("Relation is BCNF?", 'Yes' if func.isBCNF(relation) else 'No')    # Checking if relation is in BCNF

print("\nMinimal Cover :")
minimalCover =  func.minimalCover(attributes, fdString) # Finding minimal cover
print(minimalCover.toString())
