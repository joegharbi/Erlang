import os
import subprocess
import time

# Run the first script and wait for it to finish
# print("---- Starting 1st measurement ----")

# c_server_command = "c_server_win.exe"
# c_proc = subprocess.Popen(c_server_command, shell= True)
# time.sleep(5)

# subprocess.call(['python', 'client_c.py'])
# print("---- Finished 1st measurement ----")
# time.sleep(5)

# # Then kill the process
# subprocess.run(f'taskkill /F /IM c_server_win.exe', shell=True)


# Run the second script and wait for it to finish
print("---- Starting 2nd measurement ----")

erl_server_command =  "erl -noshell -eval 'echo_server_prod:start().'"
erl_proc = subprocess.Popen(erl_server_command)
time.sleep(5)

erl_command = "python client_erlang.py"
# subprocess.call(['python', 'client_erlang.py'])
subprocess.Popen(erl_command, shell=True)
print("---- Finished 2nd measurement ----")
time.sleep(5)

# Then kill the process
subprocess.run(f'taskkill /F /IM erl.exe', shell=True)

# Shut down the computer (works on Windows)
# os.system('shutdown /s /t 1')
