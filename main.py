import datetime
from typing import List
import csv
import time
import shlex
import argparse
from subprocess import Popen, PIPE

lc: int = 5000
hc: int = 5000
s_samples: int = 5
interval: int = 60

config: str = "kiwiplot-source.csv"
f: List[float] = []
server: List[str] = []
port: List[int] = []

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='username / callsign')
args = vars(parser.parse_args())

if args["user"]:
    username: str = args["user"]
else:
    username: str = "kiwiplot"

m: int = 0

with open(config) as configfile:
    csvfile = csv.reader(configfile, delimiter=',')
    for row in csvfile:
        if float(row[0]) > 0:
            #print(row)
            f.append(float(row[0]))
            server.append(str(row[1]))
            port.append(int(row[2]))
            m += 1

while 1:
    for loop in range(m):
        command = shlex.split("python3 kiwirecorder.py -k 5 -s " + server[loop] + " -p " + str(port[loop]) + " -f " + str(f[loop]) + " -m am -L -" + str(lc) + " -H " + str(hc) +" --s-meter=" + str(s_samples) + " --user=" + username)
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        pwr = stdout.decode('UTF-8')[6:]
        fdate = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        if len(pwr):
            out = str(f[loop])
            out = out.replace(".", "_")+".csv"
            with open(out, 'a') as fd:
                fd.write(fdate+","+str(pwr))
                print(f'{server[loop]:20s}-> f:{f[loop]:7} p:{pwr:6}', end='')

    time.sleep(interval)



