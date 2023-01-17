import datetime
from typing import List
import csv
import time
import shlex
import argparse
from subprocess import Popen, PIPE

bw: float = 10000
lc: float = 5000
hc: float = 5000
s_samples: int = 5
interval: int = 60
increment: int = 0
username: str = "kiwiplot"
measurementname: str = "undefined"

config: str = "kiwiplot-source.csv"
f: List[float] = []
server: List[str] = []
port: List[int] = []
ftop: float = 10
fbottom: float = 30000
fcurrent: float= 0
m: int = 0

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='username / callsign')
parser.add_argument('-w', '--bw', help='bw in Hz')
parser.add_argument('-i', '--increment', help='if set, will go through a range in [increment] steps (Hz), ignoring the frequency set in the config file')
parser.add_argument('-b', '--bottom', help='if -i is set this will be the first frequency (kHz) to measure')
parser.add_argument('-t', '--top', help='if -i is set this will be the last frequency (kHz) to measure')
parser.add_argument('-s', '--ssamples', help='smeter samples')
parser.add_argument('-n', '--name', help='name of measurement (identifier)')
parser.add_argument('-d', '--delay', help='wait n seconds between measurements')

args = vars(parser.parse_args())

if args["user"]:
    username = args["user"]

if args["bw"]:
    bw = int(args["bw"])
    if bw in range(1000,50000):
        lc = bw / 2
        hc = bw / 2

if args["ssamples"]:
    s_samples = int(args["ssamples"])


if args["increment"]:
    increment = int(args["increment"])
    interval = 0  # default delay for sweep should be 0
    if args["bottom"]:
        fbottom = float(args["bottom"])
        fcurrent = fbottom
    if args["top"]:
        ftop = float(args["top"])

if args["delay"]:
    interval = int(args["delay"])

if args["name"]:
    measurementname = args["name"]

with open(config) as configfile:
    csvfile = csv.reader(configfile, delimiter=',')
    for row in csvfile:
        if len(row)>0:
            f.append(float(row[0]))
            server.append(str(row[1]))
            port.append(int(row[2]))
            m += 1

if increment == 0:
    # measure a single frequency like defined in kiwiplot-source.csv
    print("starting single frequency measurement loop")
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
                    print(f'{server[loop]:20s}-> f:{f[loop]:<7}  bw: {bw:<6}  p:{pwr:<6}', end='')

        time.sleep(interval)

else:
    # measure a full spectrum
    print("starting sweep mode..")
    # start date
    while fcurrent < ftop:
        command = shlex.split("python3 kiwirecorder.py -k 5 -s " + server[0] + " -p " + str(port[0]) + " -f " + str(
                fcurrent) + " -m am -L -" + str(lc) + " -H " + str(hc) + " --s-meter=" + str(
                s_samples) + " --user=" + username)
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        pwr = stdout.decode('UTF-8')[6:].replace("\n", "")
        fdate = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

        if len(pwr):
            out = "sweep_" + server[0] + ".csv"
            with open(out, 'a') as fd:
                fd.write(fdate + "," + str(fcurrent) + "," + str(pwr) + "," + measurementname + "\n")
                print(f'{server[0]:20s}-> f:{fcurrent:<7}  bw: {bw:<6}  p:{pwr:<6}')

        fcurrent += increment

    print(f'Finished! Now run plotcsv.py -s -i {out} to visualize your data')





