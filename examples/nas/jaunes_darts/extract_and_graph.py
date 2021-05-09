import datetime
import re
import pytz
import copy
import numpy as np
import matplotlib.pyplot as plt
import argparse

def get_timestamp(line_str):
	time_re = re.search(r"^\[2.*\] INFO", line_str)
	time_re = re.search(r"^\[2.*\]", time_re.group(0))
	if time_re: 
		time_str = time_re.group(0)
		date_time_obj = datetime.datetime.strptime(time_str, '[%Y-%m-%d %H:%M:%S]')
	else: 
		print("ERROR, timestamp not found in str: "+str())

	# local = pytz.timezone("America/Los_Angeles")
	# local_dt = local.localize(date_time_obj, is_dst=None)
	# utc_dt = local_dt.astimezone(pytz.utc)
	date_time_obj = date_time_obj.replace(tzinfo=None)
	secs = (date_time_obj-datetime.datetime(1970,1,1)).total_seconds()
	return secs

def get_type(line_str):
	train_re = re.search(r".*Train: \[.*", line_str)
	valid_re = re.search(r".*Valid: \[.*", line_str)
	final_re = re.search(r".*Final Prec@1.*", line_str)
	if train_re:
		if final_re:
			return "final", "train_final"
		else:
			return "normal", "train_normal"
	if valid_re:
		if final_re:
			return "final", "valid_final"
		else:
			return "normal", "valid_normal"
	return "junk", "junk"



def process_finals(line_str):
	final_prec_re = re.search(r"\d\d\.\d\d\d\d", line_str)
	final_prec = float(final_prec_re.group(0))
	timestamp = get_timestamp(line_str)
	return [timestamp, final_prec]

def process_normals(line_str):
	# print("line_str: "+str(line_str))
	normal_loss_re = re.search(r"Loss \d\.\d\d\d", line_str)
	normal_loss_re = re.search(r"\d\.\d\d\d", normal_loss_re.group(0))
	loss = float( normal_loss_re.group(0))
	
	normal_prec_re1 = re.search(r"Prec@\(1,5\) \(\d\d\.\d%", line_str)
	normal_prec_re2 = re.search(r"Prec@\(1,5\) \(\d\.\d%", line_str)
	normal_prec_re3 = re.search(r"Prec@\(1,5\) \(\d\d\d\.\d%", line_str)
	if normal_prec_re1:
		normal_prec_re = re.search(r"\d\d\.\d", normal_prec_re1.group(0))
	elif normal_prec_re2:
		normal_prec_re = re.search(r"\d\.\d", normal_prec_re2.group(0))
	else: 
		normal_prec_re = re.search(r"\d\d\d\.\d", normal_prec_re3.group(0))
	
	prec = float(normal_prec_re.group(0))

	timestamp = get_timestamp(line_str)

	return [timestamp, prec, loss]



def gen_data(input_str):
	data = {}
	data["train_final"] = [[0,0]]
	data["train_normal"] = [[0,0,0]]
	data["valid_final"] = [[0,0]]
	data["valid_normal"] = [[0,0,0]]

	input_list = input_str.split("\\r\\n")

	for input_line in input_list:
		typ, subtyp = get_type(input_line)
		if typ == "final":
			data[subtyp].append(process_finals(input_line))
		if typ == "normal":
			data[subtyp].append(process_normals(input_line))

	# super strange indexing issues going on here. 
	# data2 = copy.deepcopy(data)
	first_secs = (data["train_normal"])[1][0]
	for subtyp in list(data.keys()):
		lst = data[subtyp]
		if len(lst) > 1:
			for idx in range(1, len(lst)):
				data_point = lst[idx]
				timestamp_secs = data_point[0]
				hours = (timestamp_secs  - first_secs)/3600
				lst[idx][0] = hours
				data[subtyp] = lst

		data[subtyp] = np.asarray((data[subtyp])[1:])
	return data



def process_file(file_path):
	with open(file_path, 'rb') as file:
		text = str(file.read())
	data = gen_data(text)
	return data

def gen_graphs(out_dir, resData, modelName):
	train_hours = resData["train_normal"][:, 0]
	test_hours = resData["valid_normal"][:, 0]
	train_loss = resData["train_normal"][:, 2]
	train_accuracy = resData["train_normal"][:, 1]
	test_loss = resData["valid_normal"][:, 2]
	test_accuracy = resData["valid_normal"][:, 1]
	gen_plot(out_dir, modelName+" Loss Vs GPU Hours", "Loss", "GPU Hours", train_loss, test_loss,  train_hours, test_hours)
	gen_plot(out_dir, modelName+" Accuracy Vs GPU Hours", "Accuracy", "GPU Hours", train_accuracy, test_accuracy, train_hours, test_hours)

def gen_plot(out_dir, plot_title, y_label, x_label, y1, y2, x1, x2):
	plt.plot(x1, y1, color='blue', label = "Train")
	plt.plot(x2, y2, color='orange', label = "Test")
	plt.title(plot_title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.legend()
	file_name = str(plot_title).replace(" ","")
	file_path = out_dir + file_name
	plt.savefig(file_path)
	plt.close()


parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="The text file to be processed and graphed")
parser.add_argument("model_name", help="The name for the graph")
parser.add_argument("out_dir", help="The output directory")
args = parser.parse_args()

# data = process_file("../examples/nas/darts/darts_final_retrain_90.txt")
# gen_graphs(data, "dank memer model")
data = process_file(args.input_file)
gen_graphs(args.out_dir, data, args.model_name)