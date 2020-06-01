# Python program to read 
# json file 
  
  
import json 
  
# JSON string 
f = open('data/dnac_devices.json',) 
  
# returns JSON object as  
# a dictionary 
data1 = json.load(f) 
  
# Convert string to Python dict 


for i in data1['response']: 
    print (i["id"])
    print (i["type"])
    print (i["family"])
    print (i["softwareType"])
    print (i["managementIpAddress"])
    print()
  
# Closing file 
f.close()  

