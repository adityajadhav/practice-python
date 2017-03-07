import subprocess

subprocess.call(["echo", "Hello World!"], shell=True)

subprocess.check_call(["echo", "Hello World!"], shell=True)

subprocess.check_call("dir", shell=True)
