#Laura Davis
#27 April 2016
#This program will calculate the energy difference after of going green by 
#comparing energy bills from the year prior to making the switch and the year
#following the switch. It will aggregate two years' worth of data and 
#compute the savings.

#CGP145 Ch08 Lab-5 Going Green

def main():
	#declare variables
	endProgram = "no"
	notGreenCost = [0] * 12
	goneGreenCost = [0] * 12
	savings = [0] * 12
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

	while endProgram == "no":
		
		#function calls
		notGreenCost = getNotGreen(notGreenCost, months)
		goneGreenCost = getGoneGreen(goneGreenCost, months)
		savings = energySaved(notGreenCost, goneGreenCost, savings)
		displayInfo(notGreenCost, goneGreenCost, savings, months)
		
		endProgram = raw_input('Do you want to end program? (Enter no or yes) --> ')

#the getNotGreen function
def getNotGreen(notGreenCost, months):
	counter = 0
	while counter < 12:
		print ("Enter NOT GREEN energy costs for"),months[counter] + ":"
		notGreenCost[counter] = input("Enter now --> ")
		counter = counter + 1
	print ""
	return notGreenCost
	
#the getGoneGreen function
def getGoneGreen(goneGreenCost, months):
	counter = 0
	while counter < 12:
		print ("Enter GONE GREEN energy costs for"),months[counter] + ":"
		goneGreenCost[counter] = input("Enter now --> ")
		counter = counter + 1
	print ""
	return goneGreenCost

#the energySaved function
def energySaved(notGreenCost, goneGreenCost, savings):
	counter = 0
	while counter < 12:
		savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
		counter = counter + 1
	print ""
	return savings

#the displayInfo function		
def displayInfo(notGreenCost, goneGreenCost, savings, months):
	counter = 0
	while counter < 12:
		print "Information for",months[counter]
		print "Savings $",savings[counter]
		print "Not Green Costs $",notGreenCost[counter]
		print "Gone Green Costs $",goneGreenCost[counter]
		print ""
		counter = counter + 1

#calls main
main()

