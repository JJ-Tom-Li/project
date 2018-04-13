import json

data = []
with open("./HRdata_1_10.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_11_20.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_21_30.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_31_40.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_41_50.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_51_60.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_61_70.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_71_80.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_81_100.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_101_120.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_121_140.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_141_160.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_161_180.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)
with open("./HRdata_181_185.json",'r') as load_f:
	load_dict = json.load(load_f)
data.extend(load_dict)


with open('HRdata_final.json', 'w') as f:
	json.dump(data, f)