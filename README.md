(This is not a finished software. It was used to monitor noise levels on specific frequencies)

2 simple components to:

1. **record.py** receive power level from one or more Kiwis to multiple .csv files
2. **plotcsv.py** plot a simple graph from the recorded .csv to show received power vs time

**Usage**

Adapt a kiwiplot-source.csv from the example file.  
Example:  
9000,dg7lan.kiwi.com,8073  
147.3,dg7lan.kiwi.com,8073  

Frequency (Hz), Kiwi URL, Kiwi port

Start record.py (record.py [-u username])

When finished, start plotcsv.py -i filename.csv




