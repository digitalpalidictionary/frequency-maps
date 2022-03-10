import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import os
import pickle
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

dpd_df = pd.read_csv("../csvs/dpd-full.csv", sep = "\t", dtype=str)
dpd_df_length =  len(dpd_df)

print(f"{timeis()} {yellow}mapmaker")
print(f"{timeis()} {yellow}----------------------------------------")

def test_map_same():
	print(f"{timeis()} {green}test if map has changed")

	global map_same
	new_map = pd.read_csv("map.csv", sep="\t", index_col=0)
	with open ("output/pickle tests/old map", "rb") as old_map_file:
		old_map = pickle.load(old_map_file)
	map_same = new_map.equals(old_map)

	if map_same != True:
		print(f"{timeis()} {red}map has changed")
	with open ("output/pickle tests/old map", "wb") as old_map_file:
		pickle.dump(new_map, old_map_file)

test_map_same()


def test_inflection_pattern_changed():
	print(f"{timeis()} {green}test if any inflection patterns have changed")

	global pattern_changed
	with open("output/pickle tests/pattern_changed", "rb") as pc_pickle:
		pattern_changed = pickle.load(pc_pickle)

	if len(pattern_changed) != 0:
		print(f"{timeis()} {red}{pattern_changed} {len(pattern_changed)}")

test_inflection_pattern_changed()


def test_stem_pattern_changed():
	print(f"{timeis()} {green}test if any stems or patterns have changed")

	global stem_pattern_changed
	with open("output/pickle tests/stem_pattern_differences", "rb") as pickle_file:
		stem_pattern_changed = pickle.load(pickle_file)

	if len(stem_pattern_changed) != 0:
		print(f"{timeis()} {red}{stem_pattern_changed} {len(stem_pattern_changed)}")

test_stem_pattern_changed()


def test_data_file_missing():
	print(f"{timeis()} {green}test if data file is missing")

	global data_file_missing
	data_file_missing = []
	for row in range(dpd_df_length): 
		headword = dpd_df.loc[row, "Pāli1"]
		pos = dpd_df.loc[row, "POS"]
		if not os.path.isfile(f"output/data/{headword}.csv") and pos != "idiom":
			data_file_missing.append(headword)

	if len(data_file_missing) != 0:
		print(f"{timeis()} {red}{data_file_missing} {len(data_file_missing)}")

test_data_file_missing()


def test_data_file_zero():
	print(f"{timeis()} {green}test if data file is 0 kb")

	global data_file_zero
	data_file_zero = []
	for row in range(dpd_df_length):
		headword = dpd_df.loc[row, "Pāli1"]
		pos = dpd_df.loc[row, "POS"]
		if headword not in data_file_missing and pos != "idiom":
			if os.path. getsize(f"output/data/{headword}.csv") == 0:
				data_file_zero.append(headword)

	if len(data_file_zero) != 0:
		print(f"{timeis()} {red}{data_file_zero} {len(data_file_zero)}")

test_data_file_zero()


def test_html_file_missing():
	print(f"{timeis()} {green}test if html file is missing")

	global html_file_missing
	html_file_missing = []
	for row in range(dpd_df_length):
		headword = dpd_df.loc[row, "Pāli1"]
		pos = dpd_df.loc[row, "POS"]
		if pos != "idiom":
			if not os.path.isfile(f"output/html/{headword}.html"):
				html_file_missing.append(headword)

	if len(html_file_missing) != 0:
		print(f"{timeis()} {red}{html_file_missing} {len(html_file_missing)}")

test_html_file_missing()


def test_delete_old_data_files():
	print(f"{timeis()} {green}deleting old data files ")

	global headwords_list
	headwords_list = dpd_df["Pāli1"].tolist()
	for root, dirs, files in os.walk("output/data", topdown=True):
		for file in files:
			file_clean = re.sub(".csv", "", file)
			if file_clean not in headwords_list:
				os.remove(f"output/data/{file}")
				print(f"{timeis()} {red}{file}")

test_delete_old_data_files()

def test_delete_old_html_files():
	print(f"{timeis()} {green}deleting old html files ")
	
	for root, dirs, files in os.walk("output/html", topdown=True):
		for file in files:
			file_clean = re.sub(".html", "", file)
			if file_clean not in headwords_list:
				os.remove(f"output/html/{file}")
				print(f"{timeis()} {red}{file}")

test_delete_old_html_files()

# make dfs and dicts

rootdir = "output/word count csvs/"

vinaya_pārājika_mūla = pd.read_csv(f"{rootdir}vinaya_pārājika_mūla.csv", sep = "\t", header=None)
vinaya_pārājika_aṭṭhakathā = pd.read_csv(f"{rootdir}vinaya_pārājika_aṭṭhakathā.csv", sep = "\t", header=None)
vinaya_pācittiya_mūla = pd.read_csv(f"{rootdir}vinaya_pācittiya_mūla.csv", sep = "\t", header=None)
vinaya_pārājika_ṭīkā = pd.read_csv(f"{rootdir}vinaya_pārājika_ṭīkā.csv", sep = "\t", header=None)
vinaya_pācittiya_aṭṭhakathā = pd.read_csv(f"{rootdir}vinaya_pācittiya_aṭṭhakathā.csv", sep = "\t", header=None)
vinaya_pācittiya_ṭīkā = pd.read_csv(f"{rootdir}vinaya_pācittiya_ṭīkā.csv", sep = "\t", header=None)
vinaya_cūḷavagga_aṭṭhakathā = pd.read_csv(f"{rootdir}vinaya_cūḷavagga_aṭṭhakathā.csv", sep = "\t", header=None)
vinaya_cūḷavagga_mūla = pd.read_csv(f"{rootdir}vinaya_cūḷavagga_mūla.csv", sep = "\t", header=None)
vinaya_mahāvagga_aṭṭhakathā = pd.read_csv(f"{rootdir}vinaya_mahāvagga_aṭṭhakathā.csv", sep = "\t", header=None)
vinaya_mahāvagga_mūla = pd.read_csv(f"{rootdir}vinaya_mahāvagga_mūla.csv", sep = "\t", header=None)
vinaya_parivāra_aṭṭhakathā = pd.read_csv(f"{rootdir}vinaya_parivāra_aṭṭhakathā.csv", sep = "\t", header=None)
vinaya_parivāra_mūla = pd.read_csv(f"{rootdir}vinaya_parivāra_mūla.csv", sep = "\t", header=None)
vinaya_aññā_ṭīkā = pd.read_csv(f"{rootdir}vinaya_aññā_ṭīkā.csv", sep = "\t", header=None)
sutta_dīgha_mūla = pd.read_csv(f"{rootdir}sutta_dīgha_mūla.csv", sep = "\t", header=None)
sutta_dīgha_aṭṭhakathā = pd.read_csv(f"{rootdir}sutta_dīgha_aṭṭhakathā.csv", sep = "\t", header=None)
sutta_dīgha_ṭīkā = pd.read_csv(f"{rootdir}sutta_dīgha_ṭīkā.csv", sep = "\t", header=None)
sutta_majjhima_mūla = pd.read_csv(f"{rootdir}sutta_majjhima_mūla.csv", sep = "\t", header=None)
sutta_majjhima_aṭṭhakathā = pd.read_csv(f"{rootdir}sutta_majjhima_aṭṭhakathā.csv", sep = "\t", header=None)
sutta_majjhima_ṭīkā = pd.read_csv(f"{rootdir}sutta_majjhima_ṭīkā.csv", sep = "\t", header=None)
sutta_saṃyutta_mūla = pd.read_csv(f"{rootdir}sutta_saṃyutta_mūla.csv", sep = "\t", header=None)
sutta_saṃyutta_aṭṭhakathā = pd.read_csv(f"{rootdir}sutta_saṃyutta_aṭṭhakathā.csv", sep = "\t", header=None)
sutta_saṃyutta_ṭīkā = pd.read_csv(f"{rootdir}sutta_saṃyutta_ṭīkā.csv", sep = "\t", header=None)
sutta_aṅguttara_mūla = pd.read_csv(f"{rootdir}sutta_aṅguttara_mūla.csv", sep = "\t", header=None)
sutta_aṅguttara_aṭṭhakathā = pd.read_csv(f"{rootdir}sutta_aṅguttara_aṭṭhakathā.csv", sep = "\t", header=None)
sutta_aṅguttara_ṭīkā = pd.read_csv(f"{rootdir}sutta_aṅguttara_ṭīkā.csv", sep = "\t", header=None)
sutta_khuddaka1_mūla = pd.read_csv(f"{rootdir}sutta_khuddaka1_mūla.csv", sep = "\t", header=None)
sutta_khuddaka1_aṭṭhakathā = pd.read_csv(f"{rootdir}sutta_khuddaka1_aṭṭhakathā.csv", sep = "\t", header=None)
sutta_khuddaka2_mūla = pd.read_csv(f"{rootdir}sutta_khuddaka2_mūla.csv", sep = "\t", header=None)
sutta_khuddaka2_aṭṭhakathā = pd.read_csv(f"{rootdir}sutta_khuddaka2_aṭṭhakathā.csv", sep = "\t", header=None)
sutta_khuddaka2_ṭīkā = pd.read_csv(f"{rootdir}sutta_khuddaka2_ṭīkā.csv", sep = "\t", header=None)
abhidhamma_dhammasaṅgaṇī_aṭṭhakathā = pd.read_csv(f"{rootdir}abhidhamma_dhammasaṅgaṇī_aṭṭhakathā.csv", sep = "\t", header=None)
abhidhamma_dhammasaṅgaṇī_mūla = pd.read_csv(f"{rootdir}abhidhamma_dhammasaṅgaṇī_mūla.csv", sep = "\t", header=None)
abhidhamma_dhammasaṅgaṇī_ṭīkā = pd.read_csv(f"{rootdir}abhidhamma_dhammasaṅgaṇī_ṭīkā.csv", sep = "\t", header=None)
abhidhamma_vibhāṅga_mūla = pd.read_csv(f"{rootdir}abhidhamma_vibhāṅga_mūla.csv", sep = "\t", header=None)
abhidhamma_dhātukathā_mūla = pd.read_csv(f"{rootdir}abhidhamma_dhātukathā_mūla.csv", sep = "\t", header=None)
abhidhamma_vibhāṅga_aṭṭhakathā = pd.read_csv(f"{rootdir}abhidhamma_vibhāṅga_aṭṭhakathā.csv", sep = "\t", header=None)
abhidhamma_vibhāṅga_ṭīkā = pd.read_csv(f"{rootdir}abhidhamma_vibhāṅga_ṭīkā.csv", sep = "\t", header=None)
abhidhamma_dhātukathā_aṭṭhakathā = pd.read_csv(f"{rootdir}abhidhamma_dhātukathā_aṭṭhakathā.csv", sep = "\t", header=None)
abhidhamma_dhātukathā_ṭīkā = pd.read_csv(f"{rootdir}abhidhamma_dhātukathā_ṭīkā.csv", sep = "\t", header=None)
abhidhamma_puggalapaññatti_mūla = pd.read_csv(f"{rootdir}abhidhamma_puggalapaññatti_mūla.csv", sep = "\t", header=None)
abhidhamma_kathāvatthu_mūla = pd.read_csv(f"{rootdir}abhidhamma_kathāvatthu_mūla.csv", sep = "\t", header=None)
abhidhamma_yamaka_mūla = pd.read_csv(f"{rootdir}abhidhamma_yamaka_mūla.csv", sep = "\t", header=None)
abhidhamma_paṭṭhāna_mūla = pd.read_csv(f"{rootdir}abhidhamma_paṭṭhāna_mūla.csv", sep = "\t", header=None)
abhidhamma_aññā_ṭīkā = pd.read_csv(f"{rootdir}abhidhamma_aññā_ṭīkā.csv", sep = "\t", header=None)
aññā_visuddhimagga = pd.read_csv(f"{rootdir}aññā_visuddhimagga.csv", sep = "\t", header=None)
aññā_visuddhimagga_ṭīkā = pd.read_csv(f"{rootdir}aññā_visuddhimagga_ṭīkā.csv", sep = "\t", header=None)
aññā_leḍī = pd.read_csv(f"{rootdir}aññā_leḍī.csv", sep = "\t", header=None)
aññā_buddha_vandanā = pd.read_csv(f"{rootdir}aññā_buddha_vandanā.csv", sep = "\t", header=None)
aññā_vaṃsa = pd.read_csv(f"{rootdir}aññā_vaṃsa.csv", sep = "\t", header=None)
aññā_byākaraṇa = pd.read_csv(f"{rootdir}aññā_byākaraṇa.csv", sep = "\t", header=None)
aññā_nīti = pd.read_csv(f"{rootdir}aññā_nīti.csv", sep = "\t", header=None)
aññā_pucchavisajjana = pd.read_csv(f"{rootdir}aññā_pucchavisajjana.csv", sep = "\t", header=None)
aññā_pakiṇṇaka = pd.read_csv(f"{rootdir}aññā_pakiṇṇaka.csv", sep = "\t", header=None)
aññā_sihaḷa = pd.read_csv(f"{rootdir}aññā_sihaḷa.csv", sep = "\t", header=None)

vinaya_pārājika_mūla_dict = dict(vinaya_pārājika_mūla.values.tolist())
vinaya_pārājika_aṭṭhakathā_dict = dict(vinaya_pārājika_aṭṭhakathā.values.tolist())
vinaya_pācittiya_mūla_dict = dict(vinaya_pācittiya_mūla.values.tolist())
vinaya_pārājika_ṭīkā_dict = dict(vinaya_pārājika_ṭīkā.values.tolist())
vinaya_pācittiya_aṭṭhakathā_dict = dict(vinaya_pācittiya_aṭṭhakathā.values.tolist())
vinaya_pācittiya_ṭīkā_dict = dict(vinaya_pācittiya_ṭīkā.values.tolist())
vinaya_cūḷavagga_aṭṭhakathā_dict = dict(vinaya_cūḷavagga_aṭṭhakathā.values.tolist())
vinaya_cūḷavagga_mūla_dict = dict(vinaya_cūḷavagga_mūla.values.tolist())
vinaya_mahāvagga_aṭṭhakathā_dict = dict(vinaya_mahāvagga_aṭṭhakathā.values.tolist())
vinaya_mahāvagga_mūla_dict = dict(vinaya_mahāvagga_mūla.values.tolist())
vinaya_parivāra_aṭṭhakathā_dict = dict(vinaya_parivāra_aṭṭhakathā.values.tolist())
vinaya_parivāra_mūla_dict = dict(vinaya_parivāra_mūla.values.tolist())
vinaya_aññā_ṭīkā_dict = dict(vinaya_aññā_ṭīkā.values.tolist())
sutta_dīgha_mūla_dict = dict(sutta_dīgha_mūla.values.tolist())
sutta_dīgha_aṭṭhakathā_dict = dict(sutta_dīgha_aṭṭhakathā.values.tolist())
sutta_dīgha_ṭīkā_dict = dict(sutta_dīgha_ṭīkā.values.tolist())
sutta_majjhima_mūla_dict = dict(sutta_majjhima_mūla.values.tolist())
sutta_majjhima_aṭṭhakathā_dict = dict(sutta_majjhima_aṭṭhakathā.values.tolist())
sutta_majjhima_ṭīkā_dict = dict(sutta_majjhima_ṭīkā.values.tolist())
sutta_saṃyutta_mūla_dict = dict(sutta_saṃyutta_mūla.values.tolist())
sutta_saṃyutta_aṭṭhakathā_dict = dict(sutta_saṃyutta_aṭṭhakathā.values.tolist())
sutta_saṃyutta_ṭīkā_dict = dict(sutta_saṃyutta_ṭīkā.values.tolist())
sutta_aṅguttara_mūla_dict = dict(sutta_aṅguttara_mūla.values.tolist())
sutta_aṅguttara_aṭṭhakathā_dict = dict(sutta_aṅguttara_aṭṭhakathā.values.tolist())
sutta_aṅguttara_ṭīkā_dict = dict(sutta_aṅguttara_ṭīkā.values.tolist())
sutta_khuddaka1_mūla_dict = dict(sutta_khuddaka1_mūla.values.tolist())
sutta_khuddaka1_aṭṭhakathā_dict = dict(sutta_khuddaka1_aṭṭhakathā.values.tolist())
sutta_khuddaka2_mūla_dict = dict(sutta_khuddaka2_mūla.values.tolist())
sutta_khuddaka2_aṭṭhakathā_dict = dict(sutta_khuddaka2_aṭṭhakathā.values.tolist())
sutta_khuddaka2_ṭīkā_dict = dict(sutta_khuddaka2_ṭīkā.values.tolist())
abhidhamma_dhammasaṅgaṇī_aṭṭhakathā_dict = dict(abhidhamma_dhammasaṅgaṇī_aṭṭhakathā.values.tolist())
abhidhamma_dhammasaṅgaṇī_mūla_dict = dict(abhidhamma_dhammasaṅgaṇī_mūla.values.tolist())
abhidhamma_dhammasaṅgaṇī_ṭīkā_dict = dict(abhidhamma_dhammasaṅgaṇī_ṭīkā.values.tolist())
abhidhamma_vibhāṅga_mūla_dict = dict(abhidhamma_vibhāṅga_mūla.values.tolist())
abhidhamma_dhātukathā_mūla_dict = dict(abhidhamma_dhātukathā_mūla.values.tolist())
abhidhamma_vibhāṅga_aṭṭhakathā_dict = dict(abhidhamma_vibhāṅga_aṭṭhakathā.values.tolist())
abhidhamma_vibhāṅga_ṭīkā_dict = dict(abhidhamma_vibhāṅga_ṭīkā.values.tolist())
abhidhamma_dhātukathā_aṭṭhakathā_dict = dict(abhidhamma_dhātukathā_aṭṭhakathā.values.tolist())
abhidhamma_dhātukathā_ṭīkā_dict = dict(abhidhamma_dhātukathā_ṭīkā.values.tolist())
abhidhamma_puggalapaññatti_mūla_dict = dict(abhidhamma_puggalapaññatti_mūla.values.tolist())
abhidhamma_kathāvatthu_mūla_dict = dict(abhidhamma_kathāvatthu_mūla.values.tolist())
abhidhamma_yamaka_mūla_dict = dict(abhidhamma_yamaka_mūla.values.tolist())
abhidhamma_paṭṭhāna_mūla_dict = dict(abhidhamma_paṭṭhāna_mūla.values.tolist())
abhidhamma_aññā_ṭīkā_dict = dict(abhidhamma_aññā_ṭīkā.values.tolist())
aññā_visuddhimagga_dict = dict(aññā_visuddhimagga.values.tolist())
aññā_visuddhimagga_ṭīkā_dict = dict(aññā_visuddhimagga_ṭīkā.values.tolist())
aññā_leḍī_dict = dict(aññā_leḍī.values.tolist())
aññā_buddha_vandanā_dict = dict(aññā_buddha_vandanā.values.tolist())
aññā_vaṃsa_dict = dict(aññā_vaṃsa.values.tolist())
aññā_byākaraṇa_dict = dict(aññā_byākaraṇa.values.tolist())
aññā_nīti_dict = dict(aññā_nīti.values.tolist())
aññā_pucchavisajjana_dict = dict(aññā_pucchavisajjana.values.tolist())
aññā_pakiṇṇaka_dict = dict(aññā_pakiṇṇaka.values.tolist())
aññā_sihaḷa_dict = dict(aññā_sihaḷa.values.tolist())

dicts = [
vinaya_pārājika_mūla_dict,
vinaya_pārājika_aṭṭhakathā_dict,
vinaya_pārājika_ṭīkā_dict,
vinaya_pācittiya_mūla_dict,
vinaya_pācittiya_aṭṭhakathā_dict,
vinaya_pācittiya_ṭīkā_dict,
vinaya_mahāvagga_mūla_dict,
vinaya_mahāvagga_aṭṭhakathā_dict,
vinaya_cūḷavagga_mūla_dict,
vinaya_cūḷavagga_aṭṭhakathā_dict,
vinaya_parivāra_mūla_dict,
vinaya_parivāra_aṭṭhakathā_dict,
vinaya_aññā_ṭīkā_dict,
sutta_dīgha_mūla_dict,
sutta_dīgha_aṭṭhakathā_dict,
sutta_dīgha_ṭīkā_dict,
sutta_majjhima_mūla_dict,
sutta_majjhima_aṭṭhakathā_dict,
sutta_majjhima_ṭīkā_dict,
sutta_saṃyutta_mūla_dict,
sutta_saṃyutta_aṭṭhakathā_dict,
sutta_saṃyutta_ṭīkā_dict,
sutta_aṅguttara_mūla_dict,
sutta_aṅguttara_aṭṭhakathā_dict,
sutta_aṅguttara_ṭīkā_dict,
sutta_khuddaka1_mūla_dict,
sutta_khuddaka1_aṭṭhakathā_dict,
sutta_khuddaka2_mūla_dict,
sutta_khuddaka2_aṭṭhakathā_dict,
sutta_khuddaka2_ṭīkā_dict,
abhidhamma_dhammasaṅgaṇī_mūla_dict,
abhidhamma_dhammasaṅgaṇī_aṭṭhakathā_dict,
abhidhamma_dhammasaṅgaṇī_ṭīkā_dict,
abhidhamma_vibhāṅga_mūla_dict,
abhidhamma_vibhāṅga_aṭṭhakathā_dict,
abhidhamma_vibhāṅga_ṭīkā_dict,
abhidhamma_dhātukathā_mūla_dict,
abhidhamma_dhātukathā_aṭṭhakathā_dict,
abhidhamma_dhātukathā_ṭīkā_dict,
abhidhamma_puggalapaññatti_mūla_dict,
abhidhamma_kathāvatthu_mūla_dict,
abhidhamma_yamaka_mūla_dict,
abhidhamma_paṭṭhāna_mūla_dict,
abhidhamma_aññā_ṭīkā_dict,
aññā_visuddhimagga_dict,
aññā_visuddhimagga_ṭīkā_dict,
aññā_leḍī_dict,
aññā_buddha_vandanā_dict,
aññā_vaṃsa_dict,
aññā_byākaraṇa_dict,
aññā_pucchavisajjana_dict,
aññā_nīti_dict,
aññā_pakiṇṇaka_dict,
aññā_sihaḷa_dict
]

# make data csvs

print(f"{timeis()} {green}making data csvs")
pickle_dir = "../inflection generator/output/inflections/"
errorlog = []

for row in range(dpd_df_length): #dpd_df_length
	headword = dpd_df.loc[row, "Pāli1"]
	pos = dpd_df.loc[row, "POS"]
	pattern = dpd_df.loc[row, "Pattern"]
		
	if pos != "idiom" and (map_same == False or pattern in pattern_changed or headword in stem_pattern_changed or headword in data_file_missing or headword in data_file_zero or headword in html_file_missing):
		print(f"{timeis()} {row}/{dpd_df_length} {headword}")
	
		output_file = open(f"output/data/{headword}.csv", "w")

		try:
			with open(f"{pickle_dir}{headword}", "rb") as inflections_file:
				inflections = pickle.load(inflections_file)
				inflections = (inflections)
		except:
			print(f"{timeis()} {red}{headword} error! why!?")
			errorlog.append(headword)

		section =0
		for dict in dicts: 
			count = 0
			for inflection in inflections:
				if inflection in dict:
					count += dict.get(inflection)
		
			with open(f"output/data/{headword}.csv", "a") as output_file:
				output_file.write(f"{section},{count}\n")
		
			section += 1

		output_file.close()

if len(errorlog) != 0:
	print(f"{timeis()} {red}file read errors {errorlog} {len(errorlog)}")

# generate html files

print(f"{timeis()} {green}generating html files")
template = pd.read_csv("map.csv", sep="\t", index_col=0)

for row in range(dpd_df_length): #dpd_df_length
	headword = dpd_df.loc[row, "Pāli1"]
	pos = dpd_df.loc[row, "POS"]
	pattern = dpd_df.loc[row, "Pattern"]
	
	if pos != "idiom" and (map_same == False or pattern in pattern_changed or headword in stem_pattern_changed or headword in data_file_missing or headword in data_file_zero or headword in html_file_missing):
		print(f"{timeis()} {row}/{dpd_df_length} {headword}")

		try:
			data = pd.read_csv(f"output/data/{headword}.csv", sep=",", index_col=0, header=None, dtype=int)
		except:
			print(f"{headword}.csv doesn't exist. why!?")
			continue

		vinaya_pārājika_mūla.csv = data.iloc[0,0]
		vinaya_pārājika_aṭṭhakathā.csv = data.iloc[1,0]
		vinaya_pārājika_ṭīkā.csv = data.iloc[2,0]
		vinaya_pācittiya_mūla.csv = data.iloc[3,0]
		vinaya_pācittiya_aṭṭhakathā.csv = data.iloc[4,0]
		vinaya_pācittiya_ṭīkā.csv = data.iloc[5,0]
		vinaya_mahāvagga_mūla.csv = data.iloc[6,0]
		vinaya_mahāvagga_aṭṭhakathā.csv = data.iloc[7,0]
		vinaya_cūḷavagga_mūla.csv = data.iloc[8,0]
		vinaya_cūḷavagga_aṭṭhakathā.csv = data.iloc[9,0]
		vinaya_parivāra_mūla.csv = data.iloc[10,0]
		vinaya_parivāra_aṭṭhakathā.csv = data.iloc[11,0]
		vinaya_aññā_ṭīkā.csv = data.iloc[12,0]
		sutta_dīgha_mūla.csv = data.iloc[13,0]
		sutta_dīgha_aṭṭhakathā.csv = data.iloc[14,0]
		sutta_dīgha_ṭīkā.csv = data.iloc[15,0]
		sutta_majjhima_mūla.csv = data.iloc[16,0]
		sutta_majjhima_aṭṭhakathā.csv = data.iloc[17,0]
		sutta_majjhima_ṭīkā.csv = data.iloc[18,0]
		sutta_saṃyutta_mūla.csv = data.iloc[19,0]
		sutta_saṃyutta_aṭṭhakathā.csv = data.iloc[20,0]
		sutta_saṃyutta_ṭīkā.csv = data.iloc[21,0]
		sutta_aṅguttara_mūla.csv = data.iloc[22,0]
		sutta_aṅguttara_aṭṭhakathā.csv = data.iloc[23,0]
		sutta_aṅguttara_ṭīkā.csv = data.iloc[24,0]
		sutta_khuddaka1_mūla.csv = data.iloc[25,0]
		sutta_khuddaka1_aṭṭhakathā.csv = data.iloc[26,0]
		sutta_khuddaka2_mūla.csv = data.iloc[27,0]
		sutta_khuddaka2_aṭṭhakathā.csv = data.iloc[28,0]
		sutta_khuddaka2_ṭīkā.csv = data.iloc[29,0]
		abhidhamma_dhammasaṅgaṇī_mūla.csv = data.iloc[30,0]
		abhidhamma_dhammasaṅgaṇī_aṭṭhakathā.csv = data.iloc[31,0]
		abhidhamma_dhammasaṅgaṇī_ṭīkā.csv = data.iloc[32,0]
		abhidhamma_vibhāṅga_mūla.csv = data.iloc[33,0]
		abhidhamma_vibhāṅga_aṭṭhakathā.csv = data.iloc[34,0]
		abhidhamma_vibhāṅga_ṭīkā.csv = data.iloc[35,0]
		abhidhamma_dhātukathā_mūla.csv = data.iloc[36,0]
		abhidhamma_dhātukathā_aṭṭhakathā.csv = data.iloc[37,0]
		abhidhamma_dhātukathā_ṭīkā.csv = data.iloc[38,0]
		abhidhamma_puggalapaññatti_mūla.csv = data.iloc[39,0]
		abhidhamma_kathāvatthu_mūla.csv = data.iloc[40,0]
		abhidhamma_yamaka_mūla.csv = data.iloc[41,0]
		abhidhamma_paṭṭhāna_mūla.csv = data.iloc[42,0]
		abhidhamma_aññā_ṭīkā.csv = data.iloc[43,0]
		aññā_visuddhimagga.csv = data.iloc[44,0]
		aññā_visuddhimagga_ṭīkā.csv = data.iloc[45,0]
		aññā_leḍī.csv = data.iloc[46,0]
		aññā_buddha_vandanā.csv = data.iloc[47,0]
		aññā_vaṃsa.csv = data.iloc[48,0]
		aññā_byākaraṇa.csv = data.iloc[49,0]
		aññā_pucchavisajjana.csv = data.iloc[50,0]
		aññā_nīti.csv = data.iloc[51,0]
		aññā_pakiṇṇaka.csv = data.iloc[52,0]
		aññā_sihaḷa.csv = data.iloc[53,0]

		map = template

		map.iloc[0,0] = vinaya_pārājika_mūla.csv
		map.iloc[0,1] = vinaya_pārājika_aṭṭhakathā.csv
		map.iloc[0,2] = vinaya_pārājika_ṭīkā.csv

		map.iloc[1,0] = vinaya_pācittiya_mūla.csv
		map.iloc[1,1] = vinaya_pācittiya_aṭṭhakathā.csv
		map.iloc[1,2] = vinaya_pācittiya_ṭīkā.csv
				
		map.iloc[2,0] = vinaya_mahāvagga_mūla.csv
		map.iloc[2,1] = vinaya_mahāvagga_aṭṭhakathā.csv
				
		map.iloc[3,0] = vinaya_cūḷavagga_mūla.csv
		map.iloc[3,1] = vinaya_cūḷavagga_aṭṭhakathā.csv
				
		map.iloc[4,0] = vinaya_parivāra_mūla.csv
		map.iloc[4,1] = vinaya_parivāra_aṭṭhakathā.csv
				
		map.iloc[5,2] = vinaya_aññā_ṭīkā.csv
				
		map.iloc[6,0] = sutta_dīgha_mūla.csv
		map.iloc[6,1] = sutta_dīgha_aṭṭhakathā.csv
		map.iloc[6,2] = sutta_dīgha_ṭīkā.csv
				
		map.iloc[7,0] = sutta_majjhima_mūla.csv
		map.iloc[7,1] = sutta_majjhima_aṭṭhakathā.csv
		map.iloc[7,2] = sutta_majjhima_ṭīkā.csv
				
		map.iloc[8,0] = sutta_saṃyutta_mūla.csv
		map.iloc[8,1] = sutta_saṃyutta_aṭṭhakathā.csv
		map.iloc[8,2] = sutta_saṃyutta_ṭīkā.csv
				
		map.iloc[9,0] = sutta_aṅguttara_mūla.csv
		map.iloc[9,1] = sutta_aṅguttara_aṭṭhakathā.csv
		map.iloc[9,2] = sutta_aṅguttara_ṭīkā.csv
				
		map.iloc[10,0] = sutta_khuddaka1_mūla.csv
		map.iloc[10,1] = sutta_khuddaka1_aṭṭhakathā.csv
				
		map.iloc[11,0] = sutta_khuddaka2_mūla.csv
		map.iloc[11,1] = sutta_khuddaka2_aṭṭhakathā.csv
		map.iloc[11,2] = sutta_khuddaka2_ṭīkā.csv
				
		map.iloc[12,0] = abhidhamma_dhammasaṅgaṇī_mūla.csv
		map.iloc[12,1] = abhidhamma_dhammasaṅgaṇī_aṭṭhakathā.csv
		map.iloc[12,2] = abhidhamma_dhammasaṅgaṇī_ṭīkā.csv
				
		map.iloc[13,0] = abhidhamma_vibhāṅga_mūla.csv
		map.iloc[13,1] = abhidhamma_vibhāṅga_aṭṭhakathā.csv
		map.iloc[13,2] = abhidhamma_vibhāṅga_ṭīkā.csv

		map.iloc[14,0] = abhidhamma_dhātukathā_mūla.csv
		map.iloc[14,1] = abhidhamma_dhātukathā_aṭṭhakathā.csv
		map.iloc[14,2] = abhidhamma_dhātukathā_ṭīkā.csv
				
		map.iloc[15,0] = abhidhamma_puggalapaññatti_mūla.csv		
		map.iloc[16,0] = abhidhamma_kathāvatthu_mūla.csv
		map.iloc[17,0] = abhidhamma_yamaka_mūla.csv
		map.iloc[18,0] = abhidhamma_paṭṭhāna_mūla.csv
		map.iloc[19,2] = abhidhamma_aññā_ṭīkā.csv
				
		map.iloc[20,1] = aññā_visuddhimagga.csv
		map.iloc[20,2] = aññā_visuddhimagga_ṭīkā.csv
				
		map.iloc[21,2] = aññā_leḍī.csv
		map.iloc[22,2] = aññā_buddha_vandanā.csv
		map.iloc[23,2] = aññā_vaṃsa.csv
		map.iloc[24,2] = aññā_byākaraṇa.csv
		map.iloc[25,2] = aññā_pucchavisajjana.csv
		map.iloc[26,2] = aññā_nīti.csv
		map.iloc[27,2] = aññā_pakiṇṇaka.csv
		map.iloc[28,2] = aññā_sihaḷa.csv

		map.fillna(0, inplace=True)
		
		with open(f"output/html/{headword}.html","w") as f:
			f.write(template.style.background_gradient(axis=None, low=0, vmin=0, cmap='Blues').render())
