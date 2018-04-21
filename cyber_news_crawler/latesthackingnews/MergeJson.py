import json

data = []
with open("./LHNdata_1_10.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_11_20.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_21_30.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_31_40.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_41_50.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_51_60.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_61_70.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_71_80.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_81_100.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./LHNdata_101_120.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)


with open('LHNdata_final.json', 'w') as f:
	json.dump(data, f)