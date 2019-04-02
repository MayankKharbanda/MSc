author: Samayak Ahuja - Roll no:31
	Abhishek Sen - Roll no:3
	Mayank Kharbanda - Roll:17
Name of Antivirus: SAM antivirus
-------------------------------------------------------------------------------------------------------------------------------
Class: Evaluation : used to evaluate mathematical and logical expressions
	Member Variables:
		bufferVariables[]: stores the variable names in string format as and when interpreted in the code of the target file
		bufferValues[]: stores the corresponding values of the variables
	Member Functions:
		findValue(mathematicalExpression): it recieves a mathematical expression and solves it using binary expression tree
		checkEquations(sequenceOfOperations): it recieves a sequence of operations and evualates them using findValue() function
		checkCondition(condition): it recieves a logical condition as string and evualates whether it is True or False
Functions:
	isConverging( sequenceOfOperations, loopVar, intendedValue, evaluation_object): this function recieves the following
											1)sequence of operations inside the loop
											2)loop variable
											3)intended value of loop variable
											4)an object of the Evaluation class which contains all the variables and the values which were
											  introdeuced before the loop starts
										: Using the above values it executeds the sequence of operations inside the loop ones and checks whether the
										  loop variable is converging on the intended value, that is whether the gap between the value of the loop 
										  variable and intended value is reducing after one iteration or not. 
										  if it converges True is returned otherwise False.
	convergence(path): recieves the path of the file in which to check and returns if the loops present it it is finite or infinite
			   conditions for infite loop: 1) if loop condition is true before execuion of loop and if loop variable does not converge on its intended value(checked using isConverging())
			   condition for finite loop :1) if loop condition is false before execution of loop
						      2) if loop condition is true before execuion of loop and if loop variable does converge on its intended value(checked using isConverging())
	
	isBufferOverflow(path):recieves the path of the file and returnes whether any access beyond the scope of the array is taking place

 	isVirus(path):: recieves a path of the file and returnes if bufferOverflow is hapening using isBufferOverflow() or if infinite loop is present using convergence()
	
	main(): takes the path of the directory as input and lists the possible viruses in the directory using isVirus function()
	