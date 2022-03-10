from bs4 import BeautifulSoup
from aksharamukha import transliterate
import os
import re
from datetime import datetime

def timeis():
	global blue
	global yellow
	global green
	global red
	global white

	blue = "\033[38;5;33m" #blue
	green = "\033[38;5;34m" #green
	red= "\033[38;5;160m" #red
	yellow = "\033[38;5;220m" #yellow
	white = "\033[38;5;251m" #white
	now = datetime.now()
	current_time = now.strftime("%Y-%m-%d %H:%M:%S")
	return (f"{blue}{current_time}{white}")

print(f"{timeis()} {yellow}convert cst4 to txt")
print(f"{timeis()} {yellow}----------------------------------------")

for filename in os.listdir("../Cst4/Xml"):
	print(f"{timeis()} {filename}")

	try:
		with open(os.path.join("../Cst4/Xml", filename), 'r', encoding= "UTF-16") as file:
			contents = file.read()
			soup = BeautifulSoup(contents,'xml')
			text_tags = soup.find_all('text')
				
			text_extract = ""

			for text_tag in text_tags:
				text_extract += text_tag.get_text() + "\n"
			
			text_translit = transliterate.process("autodetect", "IASTPali", text_extract)
			# text_translit = re.sub("ü", "u", text_translit)
			# text_translit = re.sub("ï", "i", text_translit)

			with open(f"../Cst4/txt/{filename}.txt", "w") as output_file:
				output_file.write(text_translit)

	except:	
		print(f"{timeis()} {red}{filename} failed!")
