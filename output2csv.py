import os
import re
import csv
import pathlib
from natsort import natsorted

f = open('RunSummary.csv', mode='w')
data = ['Run', 'date', 'start time', 'stop time', 'brhoD1', 'brhoD2', 'brhoD3', 'brhoD4', 'brhoD5', 'brhoD6', 'brhoD7', 'brhoD8', 'header', 'ender', 'size', 'format', 'file']
writer = csv.writer(f)
writer.writerow(data)
f.close()

p_temp = pathlib.Path('.').glob('test*.dat')
for p1 in natsorted(p_temp):
	dir_path = r'.'
	file_path = os.path.join(dir_path, p1)

	with open(file_path) as f:
		lines = f.readlines()[1:153]

#Take a line with brho from a file and list it
	lines_strip = [line.strip() for line in lines ]
	list_brho = [line_s for line_s in lines_strip if '<brho>' in line_s]
	list_rnum = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Run Number' in line_s]
	list_start = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Start Time'in line_s]
	list_stop = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Stop Time' in line_s]
	list_header = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Header' in line_s]
	list_ender = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Ender' in line_s]
	list_date = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Date' in line_s]
	list_size = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Size' in line_s]
	list_format = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] Format' in line_s]
	list_file = [line_s for line_s in lines_strip if 'RIBFROOT-Info: [TArtFileDataSource] File' in line_s]

#Type list as str and retrieve numbers in the list.
	brho_str = ",".join(list_brho)
	rnum_str = ",".join(list_rnum)
	start_str = ",".join(list_start)
	stop_str = ",".join(list_stop)
	header_str =",".join(list_header)
	ender_str = ",".join(list_ender)
	date_str =",".join(list_date)
	size_str = ",".join(list_size)
	format_str = ",".join(list_format)
	file_str = ",".join(list_file)

	brho = re.findall(r"\d+\.\d+",brho_str)
	rnum = re.findall(r"\d+",rnum_str)

	timeafter = r'Time = (.*)'
	start = re.search(timeafter, start_str)
	stop = re.search(timeafter, stop_str)
	headerafter = r'Header = (.*)'
	header = re.search(headerafter, header_str)

	enderafter = r'Ender = (.*)'
	ender = re.search(enderafter, ender_str)

	dateafter = r'Date = (.*)'
	date = re.search(dateafter, date_str)

	sizeafter = r'Size = (.*)'
	size = re.search(sizeafter, size_str)

	formatafter = r'Format = (.*)'
	format0 = re.search(formatafter, format_str)

	fileafter = r'fileafter = (.*)'
	file0 = re.search(fileafter, file_str)

	print(brho)
	print(rnum)
	print(start.group(1))
	print(stop.group(1))
	print(header.group(1))
	print(size.group(1))
	print(date.group(1))
	#print(ender.group(1))
	print(format0.group(1))
	#print(file0.group(1))

#Data to csv
	f = open('RunSummary.csv','a')
	data = [rnum[0], date.group(1),  start.group(1), stop.group(1), brho[0], brho[1], brho[2], brho[3], brho[4], brho[5], brho[6], brho[7], header.group(1), ender, size.group(1), format0.group(1), file0]
	writer = csv.writer(f)
	writer.writerow(data)
	f.close()
