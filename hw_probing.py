# Homework Probing Template Code
#
# Your goal is to:
#  - Find all the supported Mode 01 PIDs and store them as a list of strings.
#  - Query the ambient air temperature and return the value in degress Celcius as a float.
#  - Query the control module voltage and return the value in Volts for each responding ECU as a list of floats.
#
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script

##################################################################
### YOUR CODE TO FIND THE SUPPORTED PIDS AND QUERY THE VALUES
##################################################################

# import anything you might need here
import requests, json, re

initialURL='https://script.google.com/macros/s/AKfycbw24E3r_y1Gq3IpFWUZtfx3chNr1uYgz8kKp6DgHx_4dOoKXlM/exec?query='
email= "jason_webster@brown.edu"

#Part A - determien all valid PIDs
supportedPIDs  = []
encodedPIDs    = ""
individualPIDs = ""
partA_iters    = ['00', '20', '40', '60', '80', 'A0', 'C0', 'E0']

#loop thru all PID request levels and get hex encodings for supported PIDs
for i in range(len(partA_iters)):
	query = '0201' + partA_iters[i] + '5555555555'
	response = requests.get(initialURL + query).text
	encodedPIDs = encodedPIDs + response[6:14]

#loop thru encodedPIDs and convert to a binary string
for c in encodedPIDs:
	individualPIDs = individualPIDs + format(int(c, base=16), '04b')

#loop thru the binary string and add the corresponding hex value to the result arrray if supported
for j in range(len(individualPIDs)):
	if(individualPIDs[j]=='1'):
		supportedPIDs.append("%0.2X" % (j+1))

#Part B - determine the ambient air temperature
ambientAirTemperatureQuery    = '0201465555555555'  #from table on Wikipedia
ambientAirTemperatureResponse = requests.get(initialURL + ambientAirTemperatureQuery).text
# returns one byte and temp is A-40
ambientAirTemperature         = float(int(ambientAirTemperatureResponse[6:8], base=16))-40

#Part C - determine voltages in each ECU that responds
controlModuleVoltage         = []
controlModuleVoltageQuery    = '0201425555555555' #from table on Wikipedia
controlModuleVoltageResponse = requests.get(initialURL + controlModuleVoltageQuery).text
#returns two bytes per ECU and voltage = (256*A + B) / 1000
controlModuleVoltageA = re.findall('044142([0-9A-F]{2})', controlModuleVoltageResponse)
controlModuleVoltageB = re.findall('044142[0-9A-F]{2}([0-9A-F]{2})', controlModuleVoltageResponse)
for k in range(len(controlModuleVoltageA)):
	controlModuleVoltage.append((256*float(int(controlModuleVoltageA[k], base=16)) + float(int(controlModuleVoltageB[k], base=16)))/1000)

#supportedPIDs=[???]; #REPLACE THIS BY A LIST OF STRINGS
#ambientAirTemperature=[]; #REPLACE THIS BY THE TEMPERATURE IN DEGREE CELCIUS AS A FLOAT
#controlModuleVoltage=[]; #REPLACE THIS BY A LIST OF FLOATS

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'probing','supportedPIDs':json.dumps(supportedPIDs),'ambientAirTemperature':ambientAirTemperature,'controlModuleVoltage':json.dumps(controlModuleVoltage)}
	# Convert the lists into json strings, so that they can be parsed as javascript arrays
