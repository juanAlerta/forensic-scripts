import hashlib
import os
import requests
import sys
import json

api_key = "63df35d4d960b46bfccc0a9ff630bde361edf5a5075ee46474e7bee603077cf6"

if len(sys.argv) > 1:
	current_dir = sys.argv[1]
else:
	current_dir = os.getcwd()

def calculate_file_hashes(directory):
	hashes = {}

	for file in os.listdir(current_dir):
		if os.path.isfile(file):
			with open(file, 'rb') as f:
				sha1 = hashlib.sha1()
				sha1.update(f.read())
				hashes[f.name] = sha1.hexdigest()

	return hashes

def vt_diagnosis(hashes):

	for h in hashes.values():
		url = "https://www.virustotal.com/api/v3/files/" + h + "/votes"
		headers = {
			"accept": "application/json",
		    "x-apikey": api_key
		}
		response = requests.get(url, headers=headers)
		print(response.text)
	# return

# parsear veredicto a partir del json devuelto
def parser(response):
	f = open(response, "r")
	vote = json.load(f)
	
	print(vote["verdict"].text)

file_hashes = calculate_file_hashes(current_dir)
for key in file_hashes.keys():
    print(key, ":", file_hashes[key])

vt_diagnosis(file_hashes)






# TO-DO 
# -----------------------------------------------------------
# Solicitar ruta cuando se ejecuta el script ❓
# Replicar script en Python ✅
# Incorporar API VT ✅
# Automatizar búsqueda en VT ✅
# Sacar API key del código
# Parsear respuesta de la petición
# -----------------------------------------------------------

