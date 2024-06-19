import json

file_path = "data.json"

def searchdata():
 with open(file_path,'r') as newdata:
    fildata = json.load(newdata)
  
    for dataser in fildata:
        
        print(dataser["username"])
        
result = searchdata()

print(result)        
        
        
        