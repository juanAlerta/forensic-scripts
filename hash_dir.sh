<<<<<<< HEAD
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
=======
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
>>>>>>> d21020ed9209d0e1f3230023431d6974b75cd7d5
