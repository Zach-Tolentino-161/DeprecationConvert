file = input("Please enter the file that you want to replace os.system.\n")
with open(file, "r") as main:
    filedataread = main.read()
    if("os.system" in filedataread):
        filedata1 = filedataread.replace('os.system', 'subprocess.run')
        with open(file, "w") as main:
            main.write(filedata1)
            print("Please import subprocess for subprocess.run to work if subprocess isn't already imported.")
            print("Replaced all os.system with subprocess.run")
    else:
        print('Could not find os.system')
