#
import json
#json dict
data1 = {
    'name':'OJ Simpson',
    'age': 30,
    'city':'New York',
    'interests':['running','swimming', 'eating'],
    'is_student': False
}
#Open data1 (data above), write as json_file
with open('data1.json','w') as json_file:
#Dump the data dict in the JSON file
    json.dump(data1,json_file,indent=4)
#All the lines are running correctly
print("You have successfully written to data1.json")