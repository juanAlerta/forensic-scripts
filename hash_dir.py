import hashlib
import os
import requests

def calculate_file_hashes(directory):
	hashes = {}

	for file in os.listdir(current_dir):
		# filepath = os.path.join(directory, filename)
		if os.path.isfile(file):
			with open(file, 'rb') as f:
				sha1 = hashlib.sha1()
				sha1.update(f.read())
				hashes[f] = sha1.hexdigest()

	return hashes

current_dir = os.getcwd()
file_hashes = calculate_file_hashes(current_dir)
print(file_hashes)


# 🌐VirusTotal diagnosis
api_key = 63df35d4d960b46bfccc0a9ff630bde361edf5a5075ee46474e7bee603077cf6

# definir hash_id
url = "https://www.virustotal.com/api/v3/files/id" + hash_id




# TO-DO 
# -----------------------------------------------------------
# Solicitar ruta cuando se ejecuta el script
# Replicar script en Python ✅
# Incorporar API VT
# Automatizar búsqueda en VT
# -----------------------------------------------------------

