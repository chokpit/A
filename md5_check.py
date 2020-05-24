# md5_check.py
# Exports md5 checksum for the local file

import hashlib
import sys
file_name = sys.argv[1]
md5_hash = hashlib.md5()

a_file = open(file_name, "rb")
content = a_file.read()
md5_hash.update(content)

digest = md5_hash.hexdigest() # Returns the md5 checksum in hexadecimal value
print(digest)

with open('md5_source.txt', 'w') as file:
   file.write(digest)
