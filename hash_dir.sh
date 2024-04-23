#!/bin/bash

declare -a hashes

for file in * 
do 
	if [ -f "$file" ]; then
		hash=$(sha1sum "$file")
		hashes+=("$hash")
	fi
done

for i in "${hashes[@]}"; do
	echo "$i"
done

# TO-DO 
# -----------------------------------------------------------
# Solicitar ruta cuando se ejecuta el script
# Replicar script en Python ✅

# -----------------------------------------------------------
