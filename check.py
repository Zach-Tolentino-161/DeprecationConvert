# os.system has been deprecated. So this python file will change it to subprocess.run
file = input("Please enter the file that you want to replace os.system.\n")
with open(file, "r") as main:
      filedataread = main.read()
      if("os.system" in filedataread):
        filedata1 = filedataread.replace('os.system', 'subprocess.run')
        with open(file, 'w') as main:
          main.write(filedata1)
          print("Please import subprocess for subprocess.run to work if subprocess isn't imported already.")
          print("Replaced all OS.system with subprocess.run")
      else:
        print("There is no OS.system to replace.")
