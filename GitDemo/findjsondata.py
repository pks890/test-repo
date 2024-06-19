import json

file_path = "getalluserjson.json"

def searchdata(range):
    
   with open(file_path,'r') as newdata:
       data = json.load(newdata)
       print(data)  
       
range = "10.0.0.0/8"
result= searchdata(range)       

print(result)