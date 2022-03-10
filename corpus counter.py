import nltk
import re
import pandas as pd
import os
from datetime import datetime

nltk.download('punkt')

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

print(f"{timeis()} {yellow}corpus counter")
print(f"{timeis()} ----------------------------------------")


rootdir = "../Cst4/txt"
master_dict = {}

# vinaya

vinaya_pārājika_mūla = ["vin01m.mul.xml.txt"]
vinaya_pārājika_aṭṭhakathā = ["vin01a.att.xml.txt"]
vinaya_pārājika_ṭīkā = ["vin01t1.tik.xml.txt", "vin01t2.tik.xml.txt"]

master_dict["vinaya_pārājika_mūla"] = vinaya_pārājika_mūla
master_dict["vinaya_pārājika_aṭṭhakathā"] = vinaya_pārājika_aṭṭhakathā
master_dict["vinaya_pārājika_ṭīkā"] = vinaya_pārājika_ṭīkā

vinaya_pācittiya_mūla = ["vin02m1.mul.xml.txt"]
vinaya_pācittiya_aṭṭhakathā = ["vin02a1.att.xml.txt"]
vinaya_pācittiya_ṭīkā = ["vin02t.tik.xml.txt"]

master_dict["vinaya_pācittiya_mūla"] = vinaya_pācittiya_mūla
master_dict["vinaya_pācittiya_aṭṭhakathā"] = vinaya_pācittiya_aṭṭhakathā
master_dict["vinaya_pācittiya_ṭīkā"] = vinaya_pācittiya_ṭīkā

vinaya_mahāvagga_mūla = ["vin02m2.mul.xml.txt"]
vinaya_mahāvagga_aṭṭhakathā = ["vin02a2.att.xml.txt"]

master_dict["vinaya_mahāvagga_mūla"] = vinaya_mahāvagga_mūla
master_dict["vinaya_mahāvagga_aṭṭhakathā"] = vinaya_mahāvagga_aṭṭhakathā

vinaya_cūḷavagga_mūla = ["vin02m3.mul.xml.txt"]
vinaya_cūḷavagga_aṭṭhakathā = ["vin02a3.att.xml.txt"]

master_dict["vinaya_cūḷavagga_mūla"] = vinaya_cūḷavagga_mūla
master_dict["vinaya_cūḷavagga_aṭṭhakathā"] = vinaya_cūḷavagga_aṭṭhakathā

vinaya_parivāra_mūla = ["vin02m4.mul.xml.txt"]
vinaya_parivāra_aṭṭhakathā = ["vin02a4.att.xml.txt"]

master_dict["vinaya_parivāra_mūla"] = vinaya_parivāra_mūla
master_dict["vinaya_parivāra_aṭṭhakathā"] = vinaya_parivāra_aṭṭhakathā

vinaya_aññā_ṭīkā = ["vin04t.nrf.xml.txt", "vin05t.nrf.xml.txt", "vin06t.nrf.xml.txt", "vin07t.nrf.xml.txt", "vin08t.nrf.xml.txt", "vin09t.nrf.xml.txt", "vin10t.nrf.xml.txt", "vin11t.nrf.xml.txt", "vin12t.nrf.xml.txt", "vin13t.nrf.xml.txt"]

master_dict["vinaya_aññā_ṭīkā"] = vinaya_aññā_ṭīkā

# sutta

# dīgha

sutta_dīgha_mūla = ["s0101m.mul.xml.txt", "s0102m.mul.xml.txt", "s0103m.mul.xml.txt"]
sutta_dīgha_aṭṭhakathā = ["s0101a.att.xml.txt", "s0102a.att.xml.txt", "s0103a.att.xml.txt"]
sutta_dīgha_ṭīkā = ["s0101t.tik.xml.txt", "s0102t.tik.xml.txt", "s0103t.tik.xml.txt", "s0104t.nrf.xml.txt", "s0105t.nrf.xml.txt"]

master_dict["sutta_dīgha_mūla"] = sutta_dīgha_mūla
master_dict["sutta_dīgha_aṭṭhakathā"] = sutta_dīgha_aṭṭhakathā
master_dict["sutta_dīgha_ṭīkā"] = sutta_dīgha_ṭīkā

# majjhima

sutta_majjhima_mūla = ["s0201m.mul.xml.txt", "s0202m.mul.xml.txt", "s0203m.mul.xml.txt"]
sutta_majjhima_aṭṭhakathā = ["s0201a.att.xml.txt", "s0202a.att.xml.txt", "s0203a.att.xml.txt"]
sutta_majjhima_ṭīkā = ["s0201t.tik.xml.txt", "s0202t.tik.xml.txt", "s0203t.tik.xml.txt"]

master_dict["sutta_majjhima_mūla"] = sutta_majjhima_mūla
master_dict["sutta_majjhima_aṭṭhakathā"] = sutta_majjhima_aṭṭhakathā
master_dict["sutta_majjhima_ṭīkā"] = sutta_majjhima_ṭīkā

# saṃyutta

sutta_saṃyutta_mūla = ["s0301m.mul.xml.txt", "s0302m.mul.xml.txt", "s0303m.mul.xml.txt", "s0304m.mul.xml.txt", "s0305m.mul.xml.txt"]
sutta_saṃyutta_aṭṭhakathā = ["s0301a.att.xml.txt", "s0302a.att.xml.txt", "s0303a.att.xml.txt", "s0304a.att.xml.txt", "s0305a.att.xml.txt"]
sutta_saṃyutta_ṭīkā = ["s0301t.tik.xml.txt", "s0302t.tik.xml.txt", "s0303t.tik.xml.txt", "s0304t.tik.xml.txt", "s0305t.tik.xml.txt"]

master_dict["sutta_saṃyutta_mūla"] = sutta_saṃyutta_mūla
master_dict["sutta_saṃyutta_aṭṭhakathā"] = sutta_saṃyutta_aṭṭhakathā
master_dict["sutta_saṃyutta_ṭīkā"] = sutta_saṃyutta_ṭīkā

# aṅguttara

sutta_aṅguttara_mūla = ["s0401m.mul.xml.txt", "s0402m1.mul.xml.txt", "s0402m2.mul.xml.txt", "s0402m3.mul.xml.txt", "s0403m1.mul.xml.txt", "s0403m2.mul.xml.txt", "s0403m3.mul.xml.txt", "s0404m1.mul.xml.txt", "s0404m2.mul.xml.txt", "s0404m3.mul.xml.txt", "s0404m4.mul.xml.txt"]
sutta_aṅguttara_aṭṭhakathā = ["s0401a.att.xml.txt", "s0402a.att.xml.txt", "s0403a.att.xml.txt", "s0404a.att.xml.txt"]
sutta_aṅguttara_ṭīkā = ["s0401t.tik.xml.txt", "s0402t.tik.xml.txt", "s0403t.tik.xml.txt", "s0404t.tik.xml.txt"]

master_dict["sutta_aṅguttara_mūla"] = sutta_aṅguttara_mūla
master_dict["sutta_aṅguttara_aṭṭhakathā"] = sutta_aṅguttara_aṭṭhakathā
master_dict["sutta_aṅguttara_ṭīkā"] = sutta_aṅguttara_ṭīkā

# khuddaka1
# early Sutta Nipata, Itivuttaka, Dhammapada, Therigatha (Theragatha), Udana and Jataka

sutta_khuddaka1_mūla = ["s0502m.mul.xml.txt", "s0503m.mul.xml.txt", "s0504m.mul.xml.txt", "s0505m.mul.xml.txt", "s0508m.mul.xml.txt", "s0509m.mul.xml.txt", "s0513m.mul.xml.txt", "s0514m.mul.xml.txt"]
sutta_khuddaka1_aṭṭhakathā = ["s0502a.att.xml.txt", "s0503a.att.xml.txt", "s0504a.att.xml.txt", "s0505a.att.xml.txt", "s0508a1.att.xml.txt", "s0508a2.att.xml.txt", "s0509a.att.xml.txt", "s0513a1.att.xml.txt", "s0513a2.att.xml.txt", "s0513a3.att.xml.txt", "s0513a4.att.xml.txt", "s0514a1.att.xml.txt", "s0514a2.att.xml.txt", "s0514a3.att.xml.txt"]

master_dict["sutta_khuddaka1_mūla"] = sutta_khuddaka1_mūla
master_dict["sutta_khuddaka1_aṭṭhakathā"] = sutta_khuddaka1_aṭṭhakathā

# khuddaka2
# late Khuddakapatha, Vimanavatthu, Petavatthu, Niddesa, Patisambhida, Apadana, Buddhavamsa, Cariyapitaka , Netti, Milinda, Peṭakopadesa 

sutta_khuddaka2_mūla = ["s0501m.mul.xml.txt", "s0506m.mul.xml.txt", "s0507m.mul.xml.txt", "s0510m1.mul.xml.txt", "s0510m2.mul.xml.txt", "s0511m.mul.xml.txt", "s0512m.mul.xml.txt", "s0515m.mul.xml.txt", "s0516m.mul.xml.txt", "s0517m.mul.xml.txt", "s0519m.mul.xml.txt", "s0518m.nrf.xml.txt", "s0520m.nrf.xml.txt"]
sutta_khuddaka2_aṭṭhakathā = ["s0501a.att.xml.txt", "s0506a.att.xml.txt", "s0507a.att.xml.txt", "s0510a.att.xml.txt", "s0511a.att.xml.txt", "s0512a.att.xml.txt", "s0515a.att.xml.txt", "s0516a.att.xml.txt", "s0517a.att.xml.txt", "s0519a.att.xml.txt"]
sutta_khuddaka2_ṭīkā = ["s0519t.tik.xml.txt", "s0501t.nrf.xml.txt"]

master_dict["sutta_khuddaka2_mūla"] = sutta_khuddaka2_mūla
master_dict["sutta_khuddaka2_aṭṭhakathā"] = sutta_khuddaka2_aṭṭhakathā
master_dict["sutta_khuddaka2_ṭīkā"] = sutta_khuddaka2_ṭīkā

# abhidhamma

abhidhamma_dhammasaṅgaṇī_mūla = ["abh01m.mul.xml.txt"]
abhidhamma_dhammasaṅgaṇī_aṭṭhakathā = ["abh01a.att.xml.txt"]
abhidhamma_dhammasaṅgaṇī_ṭīkā = ["abh01t.tik.xml.txt", "abh04t.nrf.xml.txt"]

master_dict["abhidhamma_dhammasaṅgaṇī_mūla"] = abhidhamma_dhammasaṅgaṇī_mūla
master_dict["abhidhamma_dhammasaṅgaṇī_aṭṭhakathā"] = abhidhamma_dhammasaṅgaṇī_aṭṭhakathā
master_dict["abhidhamma_dhammasaṅgaṇī_ṭīkā"] = abhidhamma_dhammasaṅgaṇī_ṭīkā

abhidhamma_vibhāṅga_mūla = ["abh02m.mul.xml.txt"]
abhidhamma_vibhāṅga_aṭṭhakathā = ["abh02a.att.xml.txt"]
abhidhamma_vibhāṅga_ṭīkā = ["abh02t.tik.xml.txt"]

master_dict["abhidhamma_vibhāṅga_mūla"] = abhidhamma_vibhāṅga_mūla
master_dict["abhidhamma_vibhāṅga_aṭṭhakathā"] = abhidhamma_vibhāṅga_aṭṭhakathā
master_dict["abhidhamma_vibhāṅga_ṭīkā"] = abhidhamma_vibhāṅga_ṭīkā

abhidhamma_dhātukathā_mūla = ["abh03m1.mul.xml.txt"]
abhidhamma_dhātukathā_aṭṭhakathā = ["abh03a.att.xml.txt"]
abhidhamma_dhātukathā_ṭīkā = ["abh03t.tik.xml.txt", "abh05t.nrf.xml.txt"]

master_dict["abhidhamma_dhātukathā_mūla"] = abhidhamma_dhātukathā_mūla
master_dict["abhidhamma_dhātukathā_aṭṭhakathā"] = abhidhamma_dhātukathā_aṭṭhakathā
master_dict["abhidhamma_dhātukathā_ṭīkā"] = abhidhamma_dhātukathā_ṭīkā

abhidhamma_puggalapaññatti_mūla = ["abh03m2.mul.xml.txt"]

master_dict["abhidhamma_puggalapaññatti_mūla"] = abhidhamma_puggalapaññatti_mūla

abhidhamma_kathāvatthu_mūla = ["abh03m3.mul.xml.txt"]

master_dict["abhidhamma_kathāvatthu_mūla"] = abhidhamma_kathāvatthu_mūla

abhidhamma_yamaka_mūla = ["abh03m4.mul.xml.txt", "abh03m5.mul.xml.txt", "abh03m6.mul.xml.txt"]

master_dict["abhidhamma_yamaka_mūla"] = abhidhamma_yamaka_mūla

abhidhamma_paṭṭhāna_mūla = ["abh03m7.mul.xml.txt", "abh03m8.mul.xml.txt", "abh03m9.mul.xml.txt", "abh03m10.mul.xml.txt", "abh03m11.mul.xml.txt"]

master_dict["abhidhamma_paṭṭhāna_mūla"] = abhidhamma_paṭṭhāna_mūla

abhidhamma_aññā_ṭīkā = ["abh06t.nrf.xml.txt", "abh07t.nrf.xml.txt", "abh08t.nrf.xml.txt", "abh09t.nrf.xml.txt"]

master_dict["abhidhamma_aññā_ṭīkā"] = abhidhamma_aññā_ṭīkā

# aññā

# aññā

aññā_visuddhimagga = ["e0101n.mul.xml.txt", "e0102n.mul.xml.txt"]
aññā_visuddhimagga_ṭīkā = ["e0103n.att.xml.txt", "e0104n.att.xml.txt", "e0105n.nrf.xml.txt"]
aññā_leḍī = ["e0201n.nrf.xml.txt", "e0301n.nrf.xml.txt", "e0401n.nrf.xml.txt", "e0501n.nrf.xml.txt"]
aññā_buddha_vandanā = ["e0601n.nrf.xml.txt", "e0602n.nrf.xml.txt", "e0603n.nrf.xml.txt", "e0604n.nrf.xml.txt", "e0605n.nrf.xml.txt", "e0606n.nrf.xml.txt", "e0607n.nrf.xml.txt", "e0608n.nrf.xml.txt"]
aññā_vaṃsa = ["e0701n.nrf.xml.txt", "e0702n.nrf.xml.txt", "e0703n.nrf.xml.txt"]
aññā_byākaraṇa = ["e0801n.nrf.xml.txt", "e0802n.nrf.xml.txt", "e0803n.nrf.xml.txt", "e0804n.nrf.xml.txt", "e0805n.nrf.xml.txt", "e0806n.nrf.xml.txt", "e0807n.nrf.xml.txt", "e0808n.nrf.xml.txt", "e0809n.nrf.xml.txt", "e0810n.nrf.xml.txt", "e0811n.nrf.xml.txt", "e0812n.nrf.xml.txt", "e0813n.nrf.xml.txt", "e1211n.nrf.xml.txt", "e1212n.nrf.xml.txt", "e1213n.nrf.xml.txt", "e1214n.nrf.xml.txt"]
aññā_pucchavisajjana = ["e0901n.nrf.xml.txt", "e0902n.nrf.xml.txt", "e0903n.nrf.xml.txt", "e0904n.nrf.xml.txt", "e0905n.nrf.xml.txt", "e0906n.nrf.xml.txt", "e0907n.nrf.xml.txt"]
aññā_nīti = ["e1001n.nrf.xml.txt", "e1002n.nrf.xml.txt", "e1003n.nrf.xml.txt", "e1004n.nrf.xml.txt", "e1005n.nrf.xml.txt", "e1006n.nrf.xml.txt", "e1007n.nrf.xml.txt", "e1008n.nrf.xml.txt", "e1009n.nrf.xml.txt", "e1010n.nrf.xml.txt"]
aññā_pakiṇṇaka = ["e1101n.nrf.xml.txt", "e1102n.nrf.xml.txt", "e1103n.nrf.xml.txt"]
aññā_sihaḷa = ["e1201n.nrf.xml.txt", "e1202n.nrf.xml.txt", "e1203n.nrf.xml.txt", "e1204n.nrf.xml.txt", "e1205n.nrf.xml.txt", "e1206n.nrf.xml.txt", "e1207n.nrf.xml.txt", "e1208n.nrf.xml.txt", "e1209n.nrf.xml.txt", "e1210n.nrf.xml.txt", "e1215n.nrf.xml.txt"]

master_dict["aññā_visuddhimagga"] = aññā_visuddhimagga
master_dict["aññā_visuddhimagga_ṭīkā"] = aññā_visuddhimagga_ṭīkā
master_dict["aññā_leḍī"] = aññā_leḍī
master_dict["aññā_buddha_vandanā"] = aññā_buddha_vandanā
master_dict["aññā_vaṃsa"] = aññā_vaṃsa
master_dict["aññā_byākaraṇa"] = aññā_byākaraṇa
master_dict["aññā_pucchavisajjana"] = aññā_pucchavisajjana
master_dict["aññā_nīti"] = aññā_nīti
master_dict["aññā_pakiṇṇaka"] = aññā_pakiṇṇaka
master_dict["aññā_sihaḷa"] = aññā_sihaḷa

# master list of sections

list_of_sections = [
	vinaya_pārājika_mūla,
	vinaya_pārājika_aṭṭhakathā,
	vinaya_pārājika_ṭīkā,
	vinaya_pācittiya_mūla,
	vinaya_pācittiya_aṭṭhakathā,
	vinaya_pācittiya_ṭīkā,
	vinaya_mahāvagga_mūla,
	vinaya_mahāvagga_aṭṭhakathā,
	vinaya_cūḷavagga_mūla,
	vinaya_cūḷavagga_aṭṭhakathā,
	vinaya_parivāra_mūla,
	vinaya_parivāra_aṭṭhakathā,
	vinaya_aññā_ṭīkā, 
	sutta_dīgha_mūla,
	sutta_dīgha_aṭṭhakathā,
	sutta_dīgha_ṭīkā,
	sutta_majjhima_mūla,
	sutta_majjhima_aṭṭhakathā,
	sutta_majjhima_ṭīkā,
	sutta_saṃyutta_mūla,
	sutta_saṃyutta_aṭṭhakathā,
	sutta_saṃyutta_ṭīkā,
	sutta_aṅguttara_mūla,
	sutta_aṅguttara_aṭṭhakathā,
	sutta_aṅguttara_ṭīkā,
	sutta_khuddaka1_mūla,
	sutta_khuddaka1_aṭṭhakathā,
	sutta_khuddaka2_mūla,
	sutta_khuddaka2_aṭṭhakathā,
	sutta_khuddaka2_ṭīkā,
	abhidhamma_dhammasaṅgaṇī_mūla,
	abhidhamma_dhammasaṅgaṇī_aṭṭhakathā,
	abhidhamma_dhammasaṅgaṇī_ṭīkā,
	abhidhamma_vibhāṅga_mūla,
	abhidhamma_vibhāṅga_aṭṭhakathā,
	abhidhamma_vibhāṅga_ṭīkā,
	abhidhamma_dhātukathā_mūla,
	abhidhamma_dhātukathā_aṭṭhakathā,
	abhidhamma_dhātukathā_ṭīkā,
	abhidhamma_puggalapaññatti_mūla,
	abhidhamma_kathāvatthu_mūla,
	abhidhamma_yamaka_mūla,
	abhidhamma_paṭṭhāna_mūla,
	abhidhamma_aññā_ṭīkā,
	aññā_visuddhimagga,
	aññā_visuddhimagga_ṭīkā,
	aññā_leḍī,
	aññā_buddha_vandanā,
	aññā_vaṃsa,
	aññā_byākaraṇa,
	aññā_pucchavisajjana,
	aññā_nīti,
	aññā_pakiṇṇaka,
	aññā_sihaḷa
]

all_files = ["abh01a.att.xml.txt", "abh01m.mul.xml.txt", "abh01t.tik.xml.txt", "abh02a.att.xml.txt", "abh02m.mul.xml.txt", "abh02t.tik.xml.txt", "abh03a.att.xml.txt", "abh03m1.mul.xml.txt", "abh03m10.mul.xml.txt", "abh03m11.mul.xml.txt", "abh03m2.mul.xml.txt", "abh03m3.mul.xml.txt", "abh03m4.mul.xml.txt", "abh03m5.mul.xml.txt", "abh03m6.mul.xml.txt", "abh03m7.mul.xml.txt", "abh03m8.mul.xml.txt", "abh03m9.mul.xml.txt", "abh03t.tik.xml.txt", "abh04t.nrf.xml.txt", "abh05t.nrf.xml.txt", "abh06t.nrf.xml.txt", "abh07t.nrf.xml.txt", "abh08t.nrf.xml.txt", "abh09t.nrf.xml.txt", "e0101n.mul.xml.txt", "e0102n.mul.xml.txt", "e0103n.att.xml.txt", "e0104n.att.xml.txt", "e0105n.nrf.xml.txt", "e0201n.nrf.xml.txt", "e0301n.nrf.xml.txt", "e0401n.nrf.xml.txt", "e0501n.nrf.xml.txt", "e0601n.nrf.xml.txt", "e0602n.nrf.xml.txt", "e0603n.nrf.xml.txt", "e0604n.nrf.xml.txt", "e0605n.nrf.xml.txt", "e0606n.nrf.xml.txt", "e0607n.nrf.xml.txt", "e0608n.nrf.xml.txt", "e0701n.nrf.xml.txt", "e0702n.nrf.xml.txt", "e0703n.nrf.xml.txt", "e0801n.nrf.xml.txt", "e0802n.nrf.xml.txt", "e0803n.nrf.xml.txt", "e0804n.nrf.xml.txt", "e0805n.nrf.xml.txt", "e0806n.nrf.xml.txt", "e0807n.nrf.xml.txt", "e0808n.nrf.xml.txt", "e0809n.nrf.xml.txt", "e0810n.nrf.xml.txt", "e0811n.nrf.xml.txt", "e0812n.nrf.xml.txt", "e0813n.nrf.xml.txt", "e0901n.nrf.xml.txt", "e0902n.nrf.xml.txt", "e0903n.nrf.xml.txt", "e0904n.nrf.xml.txt", "e0905n.nrf.xml.txt", "e0906n.nrf.xml.txt", "e0907n.nrf.xml.txt", "e1001n.nrf.xml.txt", "e1002n.nrf.xml.txt", "e1003n.nrf.xml.txt", "e1004n.nrf.xml.txt", "e1005n.nrf.xml.txt", "e1006n.nrf.xml.txt", "e1007n.nrf.xml.txt", "e1008n.nrf.xml.txt", "e1009n.nrf.xml.txt", "e1010n.nrf.xml.txt", "e1101n.nrf.xml.txt", "e1102n.nrf.xml.txt", "e1103n.nrf.xml.txt", "e1201n.nrf.xml.txt", "e1202n.nrf.xml.txt", "e1203n.nrf.xml.txt", "e1204n.nrf.xml.txt", "e1205n.nrf.xml.txt", "e1206n.nrf.xml.txt", "e1207n.nrf.xml.txt", "e1208n.nrf.xml.txt", "e1209n.nrf.xml.txt", "e1210n.nrf.xml.txt", "e1211n.nrf.xml.txt", "e1212n.nrf.xml.txt", "e1213n.nrf.xml.txt", "e1214n.nrf.xml.txt", "e1215n.nrf.xml.txt", "s0101a.att.xml.txt", "s0101m.mul.xml.txt", "s0101t.tik.xml.txt", "s0102a.att.xml.txt", "s0102m.mul.xml.txt", "s0102t.tik.xml.txt", "s0103a.att.xml.txt", "s0103m.mul.xml.txt", "s0103t.tik.xml.txt", "s0104t.nrf.xml.txt", "s0105t.nrf.xml.txt", "s0201a.att.xml.txt", "s0201m.mul.xml.txt", "s0201t.tik.xml.txt", "s0202a.att.xml.txt", "s0202m.mul.xml.txt", "s0202t.tik.xml.txt", "s0203a.att.xml.txt", "s0203m.mul.xml.txt", "s0203t.tik.xml.txt", "s0301a.att.xml.txt", "s0301m.mul.xml.txt", "s0301t.tik.xml.txt", "s0302a.att.xml.txt", "s0302m.mul.xml.txt", "s0302t.tik.xml.txt", "s0303a.att.xml.txt", "s0303m.mul.xml.txt", "s0303t.tik.xml.txt", "s0304a.att.xml.txt", "s0304m.mul.xml.txt", "s0304t.tik.xml.txt", "s0305a.att.xml.txt", "s0305m.mul.xml.txt", "s0305t.tik.xml.txt", "s0401a.att.xml.txt", "s0401m.mul.xml.txt", "s0401t.tik.xml.txt", "s0402a.att.xml.txt", "s0402m1.mul.xml.txt", "s0402m2.mul.xml.txt", "s0402m3.mul.xml.txt", "s0402t.tik.xml.txt", "s0403a.att.xml.txt", "s0403m1.mul.xml.txt", "s0403m2.mul.xml.txt", "s0403m3.mul.xml.txt", "s0403t.tik.xml.txt", "s0404a.att.xml.txt", "s0404m1.mul.xml.txt", "s0404m2.mul.xml.txt", "s0404m3.mul.xml.txt", "s0404m4.mul.xml.txt", "s0404t.tik.xml.txt", "s0501a.att.xml.txt", "s0501m.mul.xml.txt", "s0501t.nrf.xml.txt", "s0502a.att.xml.txt", "s0502m.mul.xml.txt", "s0503a.att.xml.txt", "s0503m.mul.xml.txt", "s0504a.att.xml.txt", "s0504m.mul.xml.txt", "s0505a.att.xml.txt", "s0505m.mul.xml.txt", "s0506a.att.xml.txt", "s0506m.mul.xml.txt", "s0507a.att.xml.txt", "s0507m.mul.xml.txt", "s0508a1.att.xml.txt", "s0508a2.att.xml.txt", "s0508m.mul.xml.txt", "s0509a.att.xml.txt", "s0509m.mul.xml.txt", "s0510a.att.xml.txt", "s0510m1.mul.xml.txt", "s0510m2.mul.xml.txt", "s0511a.att.xml.txt", "s0511m.mul.xml.txt", "s0512a.att.xml.txt", "s0512m.mul.xml.txt", "s0513a1.att.xml.txt", "s0513a2.att.xml.txt", "s0513a3.att.xml.txt", "s0513a4.att.xml.txt", "s0513m.mul.xml.txt", "s0514a1.att.xml.txt", "s0514a2.att.xml.txt", "s0514a3.att.xml.txt", "s0514m.mul.xml.txt", "s0515a.att.xml.txt", "s0515m.mul.xml.txt", "s0516a.att.xml.txt", "s0516m.mul.xml.txt", "s0517a.att.xml.txt", "s0517m.mul.xml.txt", "s0518m.nrf.xml.txt", "s0519a.att.xml.txt", "s0519m.mul.xml.txt", "s0519t.tik.xml.txt", "s0520m.nrf.xml.txt", "vin01a.att.xml.txt", "vin01m.mul.xml.txt", "vin01t1.tik.xml.txt", "vin01t2.tik.xml.txt", "vin02a1.att.xml.txt", "vin02a2.att.xml.txt", "vin02a3.att.xml.txt", "vin02a4.att.xml.txt", "vin02m1.mul.xml.txt", "vin02m2.mul.xml.txt", "vin02m3.mul.xml.txt", "vin02m4.mul.xml.txt", "vin02t.tik.xml.txt", "vin04t.nrf.xml.txt", "vin05t.nrf.xml.txt", "vin06t.nrf.xml.txt", "vin07t.nrf.xml.txt", "vin08t.nrf.xml.txt", "vin09t.nrf.xml.txt", "vin10t.nrf.xml.txt", "vin11t.nrf.xml.txt", "vin12t.nrf.xml.txt", "vin13t.nrf.xml.txt"]

#sanity test

print(f"{timeis()} {green}sanity tests")
print(f"{timeis()} master_dict {len(master_dict)}")
print(f"{timeis()} list_of_sections {len(list_of_sections)}")


print(f"{timeis()} all files {len(all_files)}")

all_files_in_sections = []
for section in list_of_sections:
	for filez in section:
		all_files_in_sections.append(filez)

print(f"{timeis()} all files in sections {len(all_files_in_sections)}")

all_files_in_master_dict = []
for values in master_dict.values():
	for value in values:
		all_files_in_master_dict.append(value)
print(f"{timeis()} all files in master_dict {len(all_files_in_master_dict)}")


difference1 = set(all_files) ^ set(all_files_in_sections)
difference2 = set(all_files_in_sections) ^ set(all_files_in_master_dict)

print(f"{timeis()} {red}difference1: {len(difference1)}")
print(f"{timeis()} {red}{difference1}")
print(f"{timeis()} {red}difference2: {len(difference2)}")
print(f"{timeis()} {red}{difference2}")

# makes csv of word counts

print(f"{timeis()} {green}making csvs of word counts")


count = 0
full_text = ""
for key, values in master_dict.items():
	print(f"{timeis()} {key}")
	text = ""
	for file in values:
		f = open(f"{rootdir}/{file}")
		fr = f.read()
		text += fr
		text += "\n\n"
	
	text = text.lower()
	text = re.sub("\d", "", text)
	text = re.sub("\.", " ", text)
	text = re.sub(",", " ", text)
	text = re.sub("‘", "", text)
	text = re.sub("'", "", text)
	text = re.sub("`", "", text)
	text = re.sub(";", " ", text)
	text = re.sub("’", "", text)
	text = re.sub("!", " ", text)
	text = re.sub("\?", " ", text)
	text = re.sub("\+", " ", text)
	text = re.sub("=", " ", text)
	text = re.sub("\\=", " ", text)
	text = re.sub("-", " ", text)
	text = re.sub("–", "", text)
	text = re.sub("…", " ", text)
	text = re.sub("॰", " ", text)
	text = re.sub("\^", " ", text)

	text = re.sub("^", " ", text)
	text = re.sub("§", " ", text)
	
	text = re.sub("﻿", "", text)
	text = re.sub("⟪", "", text)
	text = re.sub("⟫", "", text)
	text = re.sub("\(", "", text)
	text = re.sub("\)", "", text)
	text = re.sub("\[", " ", text)
	text = re.sub("\]", " ", text)
	text = re.sub("\t", " ", text)
	text = re.sub("\n", " \n ", text)

	text = re.sub("ऐ", "a", text)
	text = re.sub("ऋ", "", text)
	text = re.sub("औ", "ā", text)

	text = re.sub("ः", "", text)
	text = re.sub("āः", "ā", text)
	text = re.sub("oः", "o", text)
	text = re.sub("eः", "e", text)
	text = re.sub("ṃः", "ṃ", text)

	text = re.sub("kै", "ka", text)
	text = re.sub("cै", "ca", text)
	text = re.sub("pै", "pa", text)
	text = re.sub("vै", "ve", text)

	text = re.sub("ṭौ", "ṭa", text)
	text = re.sub("mौ", "ma", text)
	text = re.sub("yौ", "ya", text)
	text = re.sub("hौ", "ha", text)
	text = re.sub("lौ", "la", text)

	text = re.sub("ï", "i", text)
	text = re.sub("ḥ", "", text)
	text = re.sub("", "u", text)

	# [^a-zāīūñṅṇṃṭḍḷ]

	with open(f"output/rawtext/{key}.txt", "w") as rawtext:
		rawtext.write(text)
	
	full_text += text

	words = nltk.word_tokenize(text)
	freq = nltk.FreqDist(words).most_common()
	section_text_df = pd.DataFrame(freq)
	section_text_df.to_csv(f"output/word count csvs/{key}.csv", sep="\t", index=None, header=None)

# saving tipitaka.csv 

print(f"{timeis()} {green}making csv of tipiṭaka word counts")

with open(f"output/rawtext/tipiṭaka.txt", "w") as rawtext:
		rawtext.write(full_text)

words = nltk.word_tokenize(full_text)
freq = nltk.FreqDist(words).most_common()
full_text_df = pd.DataFrame(freq)
full_text_df.to_csv(f"output/word count csvs/tipiṭaka.csv", sep="\t", index=None, header=None)

print(f"{timeis()} {green}fin")
print(f"{timeis()} ----------------------------------------")

