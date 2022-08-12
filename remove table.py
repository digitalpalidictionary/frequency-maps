import os
import re

data_dir = "output/html/"
for filename in os.listdir(data_dir):
	f= open(f"{data_dir}{filename}", "r")
	file_data = f.read()
	f.close()
	if re.findall('no exact matches', file_data):
		search_string = re.compile("<style>.+$", re.DOTALL)
		# search_string = re.compile("ḹheading")
		file_data = re.sub(search_string, '', file_data)
		f= open(f"{data_dir}{filename}", "w")
		f.write(file_data)
		f.close()
