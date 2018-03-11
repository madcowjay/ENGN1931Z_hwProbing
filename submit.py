#Run this script at the end when you are ready to submit your homework to the autograder.

import hw_probing  # imports your hw_sniffing module
import requests

submissionFile=open('hw_probing.py','r')
postParams=hw_probing.yourSubmission()

with open('token','a+') as tokenFile:
	token=tokenFile.read();
	if len(token)<6: 
		tokenResponse=requests.post("https://script.google.com/macros/s/AKfycbyJeqzwq7MxtCExb5PVE_05E4soG4iNBrHf9-lZ6f52v9Lz5vo/exec",data={'requestingToken':1,'email':postParams["email"]});
		token=tokenResponse.text;
		tokenFile.write(token)

postParams["token"]=token
postParams["submission"]=submissionFile.read()
subResponse=requests.post("https://script.google.com/macros/s/AKfycbyJeqzwq7MxtCExb5PVE_05E4soG4iNBrHf9-lZ6f52v9Lz5vo/exec",data=postParams)
responseFile=open('submissionResponse.txt','wb')
responseFile.write(subResponse.text.encode('utf-8'))
print(subResponse.text)
