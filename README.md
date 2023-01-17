***What it does***

2 simple components to:

1. **record.py** receive power level from one or more Kiwis to multiple .csv files **OR** sweep over a defined freq range
2. **plotcsv.py** plot a simple graph from the recorded .csv to show received power vs time / received power vs frequency

**Usage**  
Requirements:  
pip3 install pandas plotly
...maybe some more

You need to have kiwirecorder.py in the same directory (a symbolic link works fine!)

Adapt a kiwiplot-source.csv from the example file.  
Example to measure single frequencies over time:  
9000,dg7lan.kiwi.com,8073  
147.3,dg7lan.kiwi.com,8073  

Frequency (Hz), Kiwi URL, Kiwi port

Start record.py (record.py [-u username])

When finished, use plotcsv.py -i filename.csv

<img width="935" alt="image" src="https://user-images.githubusercontent.com/20392230/210586769-3ecf6de4-95b7-42f3-8327-88d8e7eb2864.png">


Example to sweep over a frequency range:  
record.py -u dg7lan_measure -w 5000 -i 20 -s 2 -b 2 -t 30000 -n no_filter_1000

usage: record.py [-h] [-u USER] [-w BW] [-i INCREMENT] [-b BOTTOM] [-t TOP] [-s SSAMPLES] [-n NAME]  
| Switch | Command | Description |
| -h | --help | show this help message and exit |  
| -u USER | --user USER | username / callsign |  
| -w BW | --bw BW | bw in Hz |
| -i INCREMENT | --increment INCREMENT | if set, will go through a range in [increment] steps (Hz), ignoring the frequency set in the config file |  
| -b BOTTOM | --bottom BOTTOM | if -i is set this will be the first frequency (kHz) to measure |
| -t TOP | --top TOP | if -i is set this will be the last frequency (kHz) to measure |  
| -s SSAMPLES | --ssamples SSAMPLES |smeter samples |
| -n NAME | --name NAME | name of measurement (identifier) |



