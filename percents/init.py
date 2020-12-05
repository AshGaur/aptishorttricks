import json

with open('accuracy.json','w') as f:
	f.write(json.dumps({"Attempted":0,"Correct":0,"Incorrect":0,"best":100000},separators=(",",":")))

print("Accuracy Initialised")
