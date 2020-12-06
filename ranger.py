import json
def rangemaker(name,start,end):
	with open('vals.json','r') as file:
		cur_data = json.loads(file.read())	
		lst = cur_data.get(name)#cur_data.get("squ")
		if len(lst)==0 or lst[0] not in range(start,end+1) or lst[-1] not in range(start,end+1):
			lst = list(range(start,end+1))
		return lst,cur_data

def write_range(name,lst,cur_data):
	with open('vals.json','w') as f:
		cur_data[name] = lst
		f.write(json.dumps(cur_data,indent=2))
