import random                       #for random number generation       
import statistics                   #for mean and standard deviation
total_steps=int(input("Number of steps bee can move are:"))         #total steps the bee would move
iterations=int(input("Number of iterations you want:"))             #number of cases
displacement=[]                                                     #store direct distance from initial state to final state all cases 
step=[]                                                             #store distance of actual possible movement for all cases
for y in range(1,iterations+1):                                     #n iterations for finding expected value
    initial_x=random.randrange(0,101,1)	                            #random x and y coordinate are generated between 0 and 101 for initial position
    initial_y=random.randrange(0,101,1)	                            #of bee on a two dimentional coordinate system
    current_x=initial_x 
    current_y=initial_y
    for x in range(1,total_steps+1):                                #1 step bee is moving in arbitary direction of 6 possible directions
	    direction=random.randrange(1,7,1)
	    if direction==1:                                        #all possible cases in if-else conditions
                current_y+=1
	    elif direction==2:
                current_x+=(3**0.5)*0.5
                current_y+=0.5
	    elif direction==3:
                current_x+=(3**0.5)*0.5
                current_y-=0.5
	    elif direction==4:
                current_y-=1
	    elif direction==5:
                current_x-=(3**0.5)*0.5
                current_y-=0.5
	    elif direction==6:
                current_x-=(3**0.5)*0.5
                current_y+=0.5
    final_x=current_x                                           #store final positions
    final_y=current_y
    displacement.append(((initial_x-final_x)**2+(initial_y-final_y)**2)**(0.5))     #storing in array the direct distance using euclidean distance
    current_x=initial_x
    current_y=initial_y
    steps=0
    while abs(current_x-final_x)>=0.1 and abs(current_y-final_y)>=0.1:              #finding path where actual moment is possible
    	if current_x<final_x and current_y<final_y:                                 #dividing the direction in 4 quadrants
    		current_x+=(3**0.5)*0.5
    		current_y+=0.5
    		steps+=1
    	elif current_x<final_x and current_y>final_y:
    		current_x+=(3**0.5)*0.5
    		current_y-=0.5
    		steps+=1
    	elif current_x>final_x and current_y>final_y:
    		current_x-=(3**0.5)*0.5
    		current_y-=0.5
    		steps+=1
    	elif current_x>final_x and current_y<final_y:
    		current_x-=(3**0.5)*0.5
    		current_y+=0.5
    		steps+=1
    while abs(current_x-final_x)<0.1 and abs(current_y-final_y)>=0.1:           #moment along y axis
	    if current_y<final_y:
	    	current_y+=1
	    	steps+=1
	    elif current_y>final_y:
	    	current_y-=1
	    	steps+=1
    while abs(current_x-final_x)>=0.1 and abs(current_y-final_y)<0.1:           #moment along x axis
	    if current_x<final_x:
	        current_x+=(3**0.5)
	        steps+=2
	    elif current_x>final_x:
                current_x-=(3**0.5)
                steps+=2
    step.append(steps)                                                      #storing steps of particular iteration
mean_displacement=statistics.mean(displacement)                             #finding and displaying mean and standard deviation of both type of distances
mean_step=statistics.mean(step)
sd_displacement=statistics.stdev(displacement)
sd_step=statistics.stdev(step)
print("Straight line distance from initial position to final position.")
print("Mean:")
print(mean_displacement)
print("Standard deviation:")
print(sd_displacement)
print("Number of steps needed for movement.")
print("Mean:")
print (mean_step)
print("Standard deviation:")
print (sd_step)

