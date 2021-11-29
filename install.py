import shutil
import subprocess
import sys

print("Checking for JsonCrypt upgrades")
subprocess.check_call([sys.executable, "-m", "pip", "install", "jsoncrypt", "--upgrade"])
reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
installed_packages = [r.decode().split("==")[0] for r in reqs.split()]
print(installed_packages)

print("In order to use the commands 'json-encrypt' and 'json-decrypt'")
print("is necessary to copy the files to your /local/bin folder")
print("Copying ./json-encrypt to /usr/local/bin/json-encrypt")
print("Copying ./json-decrypt to /usr/local/bin/json-deecrypt")

subprocess.call(["chmod", "+x", "./json-encrypt"])
subprocess.call(["chmod", "+x", "./json-decrypt"])

file1 = r"./json-encrypt"
file2 = r"./json-decrypt"

target1 = r"/usr/local/bin/json-encrypt"
target2 = r"/usr/local/bin/json-decrypt"

shutil.copyfile(file1, target1)
shutil.copyfile(file2, target2)

