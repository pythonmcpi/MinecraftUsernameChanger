import sys
import time
import json

filepath = "launcher_profiles.json"
usernames = ["Steve","MK_Python","RK_Python","Cat_Pillar"]
jsonKey = "DisplayName"

# Get original JSON data
file = open(filepath,'r')
rawJson = file.read()
file.close()

# Open file to overwrite
file = open(filepath,'w')

# Load JSON Data
jsonDict = json.loads(rawJson)

# UI
print ("Welcome to the Minecraft username modifier!")
print ("Choose a number, or press Ctrl+C to specify your own username.")
print ("Current username is:",jsonDict[jsonKey])
for Id in range(len(usernames)):
    print (str(Id)+") "+usernames[Id])

try:
    selectedId = int(input("Enter your selection: "))
    try:
        selectedName = usernames[selectedId]
    except ValueError:
        print ("Invalid Number. Restart this script and choose a valid selection.",file=sys.stderror)
        time.sleep(10)
        file.write(rawJson) # Restore the file contents
        file.close()
        sys.exit()
except KeyboardInterrupt:
    selectedName = input("Enter a valid username: ")
    if not (3 < len(selectedName) < 16):
        print ("Username is too short or too long. Username must be between 3-16. Restart this script and choose a valid username.",file=sys.stderror)
        time.sleep(10)
        file.write(rawJson) # Restore the file contents
        file.close()
        sys.exit()
# Check for valid characters 'abcdefghijklmnopqrstuvwxyz_1234567890'
if '#' in selectedName: # '#' will be placeholder char
    print ("Username cannot contain special characters. Please use only 'abcdefghijklmnopqrstuvwxyz_1234567890'. Restart this script and choose a valid username.",file=sys.stderror)
    time.sleep(10)
    file.write(rawJson) # Restore the file contents
    file.close()
    sys.exit()

nameClone = selectedName.lower()
for char in 'abcdefghijklmnopqrstuvwxyz_1234567890':
    nameClone = nameClone.replace(char,'#')
for charId in range(len(nameClone)):
    if nameClone[charId-1] != '#':
        print ("Username cannot contain special characters. Please use only 'abcdefghijklmnopqrstuvwxyz_1234567890'. Restart this script and choose a valid username.",file=sys.stderror)
        time.sleep(10)
        file.write(rawJson) # Restore the file contents
        file.close()
        sys.exit()
# Username is probably valid, save it
jsonDict[jsonKey] = selectedName
newJson = json.dumps(jsonDict, indent=4, sort_keys=True)
file.write(newJson)
file.close()
print ("Username updated to",selectedName,"successfully! Start the Minecraft launcher and look in the bottom right corner to check!")
