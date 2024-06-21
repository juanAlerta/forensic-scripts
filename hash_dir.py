# hash_dir.py -----------------------------------------------------------
# -----------------------------------------------------------------------
# This script prints the hashes of the files in the current directory
# and execute a request to VirusTotal to 
# obtain a diagnosis of the suspicious file
# 
# author: github.com/juanAlerta
# -----------------------------------------------------------------------

import hashlib
import os
import requests
import sys

api_key = "your_api_key" # https://www.virustotal.com/gui/user/USER_NAME/apikey

if len(sys.argv) > 1:
	current_dir = sys.argv[1]
else:
	current_dir = os.getcwd()

def value_from_key(dicc, value):
	for key, actual_value in dicc.items():
		if actual_value == value:
			return key
	return None

def calculate_file_hashes():
	hashes = {}

	for file in os.listdir(current_dir):
		if os.path.isfile(file):
			with open(file, 'rb') as f:
				sha1 = hashlib.sha1()
				sha1.update(f.read())
				hashes[f.name] = sha1.hexdigest()

	return hashes

def vt_diagnosis(hashes):

	headers = {
			"accept": "application/json",
		    "x-apikey": api_key
		}

	for h in hashes.values():
		url = "https://www.virustotal.com/api/v3/files/" + h + "/votes"
		response = requests.get(url, headers=headers)	

		key = value_from_key(hashes, h)

		if response.status_code == 200:
			parser(response.text, key, h)

		else: print(str(h) + "  " + str(key) + " is an unknown file 🟠")

# parsear veredicto a partir del json devuelto
def parser(response, key, value):

	if "malicious" in response:
		print(str(value) + "  " + str(key) + " is malicius 🔴")
	else: print(str(value) + "  " + str(key) + " is harmless 🟢")	

file_hashes = calculate_file_hashes()
vt_diagnosis(file_hashes)
