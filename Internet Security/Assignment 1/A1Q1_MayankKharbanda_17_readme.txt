Walking Bee:

Files
Programming is done in python3(Ubuntu) which can be executed by running the 'A1Q1_MayankKharbanda_17.py' file in any IDE for python.


Understanding the problem
The motion of the bee in hexagonal grid is possible in six directions, with equal probability of 1/6 in each. It can be thought of that the directions are separated by 60-degree angles in the cartesian plane.
The directions are:
	1. 1 unit distance in positive y-axis.
	2. 1 unit distance in 30-degree anticlockwise direction.
	3. 1 unit distance in 30-degree clockwise direction.
	4. 1 unit distance in negative y-axis.
	5. 1 unit distance in 150-degree clockwise direction.
	6. 1 unit distance in 150-degree anticlockwise direction.
Challenges
	1. To find the method of changes in the co-ordinates of bee's location according to the direction being choosen.
	2. To find how to calculate the distance between initial and final position.

Understanding the algorithm
	Initialization:-
		lines--3-11
		number of steps the bee can move and number of iterations are being asked from the user.
		All the iterations are being stored in an array.
		Initial coordinates of bee are set through random function.
	Moving to next position:-
		lines--13-29
		First a random value from 1 to 6 is being generated.
		According to value of random value function there are 6 directions:-
			1. y is incremented by 1.
			2. x is incremented by cos30 and y is incremented by sin30.
			3. x is incremented by cos30 and y is decremented by sin30.
			4. y is decremented by 1.
			5. x is decremented by cos30 and y is incremented by sin30.
			6. x is decremented by cos30 and y is decremented by sin30.
			(angle is in degree)
	Calculating the final distance:-
		There are 2 ways to do this.
		line--32
		1.In this direct distance from initial position to final position is calculated using euclidean distance formula.
		lines--36-66
		2.In this the actual possible moment of bee is being calculated.
		lines--36-52
			i).Firstly the bee is moved diagonally in four possible directions (i.e.- 2,3,5,6 in the above discribed directions) so that the result is that the bee comes either vertically or horizontally in straight line to the final position.
		lines--53-59
			ii).The bee is moved along y axis if initial and final possition are vertically in straight line.
		lines--60-66
			iii).The bee is moved along x axis(Horizontal case) and steps are incremented by 2 and x coordinate by root(3) as the movement of bee would be zig-zag, like:-/\/\/\/\/\/\/\/\/\/\, so two steps are included at every iteration to decrease checking conditions.
	Calculation and display:
		lines--68-81
		mean and standard deviation is being calculated using statisics functions and result is displayed.
