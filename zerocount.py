import os
import pandas as pd
import re

zero_list = []
counter = 0

for filename in os.listdir("output/data"):
	filename_clean = re.sub("\.csv", "", filename)
	if counter %5000==0:
		print(counter, filename_clean)
	
	df = pd.read_csv(f"output/data/{filename}", header=None)
	# print(df)
	if (df[1] == 0).all():
		zero_list.append(filename_clean)
	counter += 1

zero_list = sorted(zero_list)

with open("output/zerocount.csv", "w") as f:
	f.write(f"{len(zero_list)}\n")
	for zero in zero_list:
		f.write(f"{zero}\n")


		