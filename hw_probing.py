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

initialURL='https://script.google.com/macros/s/AKfycbw24E3r_y1Gq3IpFWUZtfx3chNr1uYgz8kKp6DgHx_4dOoKXlM/exec?'
email= "YOUR_EMAIL_GOES_HERE@brown.edu" #REPLACE THIS

supportedPIDs=[???]; #REPLACE THIS BY A LIST OF STRINGS
ambientAirTemperature=???; #REPLACE THIS BY THE TEMPERATURE IN DEGREE CELCIUS AS A FLOAT
controlModuleVoltage=[???]; #REPLACE THIS BY A LIST OF FLOATS

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'probing','supportedPIDs':json.dumps(supportedPIDs),'ambientAirTemperature':ambientAirTemperature,'controlModuleVoltage':json.dumps(controlModuleVoltage)}
	# Convert the lists into json strings, so that they can be parsed as javascript arrays
