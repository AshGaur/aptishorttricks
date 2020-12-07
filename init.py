import json

with open('accuracy.json','w') as f:
	f.write(json.dumps({"Attempted":0,"Correct":0,"Incorrect":0,"best":100000},indent=2))

with open('vals.json','w') as f:
	f.write(json.dumps({"squ":[],"cub":[],"per":[]},indent=2))

print("Intialization Successful !")
