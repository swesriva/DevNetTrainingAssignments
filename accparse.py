# Python program to read 
# json file 
  
  
import json 
  
# Opening JSON file 
f = open('data/db.json',) 
  
# returns JSON object as  
# a dictionary 
data1 = json.load(f) 
  
# Iterating through the json 
# list 
for i in data1: 
    print(data1) 
  
# Closing file 
f.close() 


import xml.etree.ElementTree as ET
tree = ET.parse('data/db.xml')
root = tree.getroot()

for child in root.iter():
    print(child.tag, child.attrib)
n=0
while(n<3):
    
    for x in root[n]:
        print(x.text)
    n=n+1
        

import yaml

with open(r'data\db.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    accounts_list = yaml.load(file, Loader=yaml.FullLoader)

    print(accounts_list)

