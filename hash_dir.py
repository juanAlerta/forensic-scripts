import hashlib
import os

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

# TO-DO 
# -----------------------------------------------------------
# Solicitar ruta cuando se ejecuta el script
# Replicar script en Python ✅
# Incorporar API VT
# Automatizar búsqueda en VT
# -----------------------------------------------------------

