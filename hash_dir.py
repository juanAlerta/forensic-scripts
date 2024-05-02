import hashlib
import os
import requests
import sys

def calculate_file_hashes(directory):
	hashes = {}

	for file in os.listdir(current_dir):
		if os.path.isfile(file):
			with open(file, 'rb') as f:
				sha1 = hashlib.sha1()
				sha1.update(f.read())
				hashes[f.name] = sha1.hexdigest()

	return hashes
# path actual o path pasado como argumento
if len(sys.argv) > 1:
	current_dir = sys.argv[1]
else:
	current_dir = os.getcwd()

file_hashes = calculate_file_hashes(current_dir)
for key in file_hashes.keys():
    print(key, ":", file_hashes[key])


# -----🌐VirusTotal diagnosis -----------------------------------

def vt_diagnosis(hash):
	api_key = "63df35d4d960b46bfccc0a9ff630bde361edf5a5075ee46474e7bee603077cf6"

	url = "https://www.virustotal.com/api/v3/files/" + hashes()
	headers = {
		"accept": "application/json",
	    "x-apikey": api_key
	}
	response = requests.get(url, headers=headers)

	print(response.text)





# TO-DO 
# -----------------------------------------------------------
# Solicitar ruta cuando se ejecuta el script
# Replicar script en Python ✅
# Incorporar API VT
# Automatizar búsqueda en VT
# -----------------------------------------------------------

