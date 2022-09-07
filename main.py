import subprocess
from playsound import playsound

command = 'python Hello.py' # file

ret = subprocess.run(command, capture_output=True, shell=True)
print(ret.returncode)
if ret.returncode == 0:
    print("Success")
    playsound('BreakingDown.mp3')

else:
    print("Failed")
    playsound('Dark side.mp3')
