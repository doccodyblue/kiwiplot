(This is not a finished software. It was used to monitor noise levels on specific frequencies)

2 simple components to:

1. **record.py** receive power level from one or more Kiwis to multiple .csv files
2. **plotcsv.py** plot a simple graph from the recorded .csv to show received power vs time

**Usage**  
Requirements:  
pip3 install pandas plotly
...maybe some more

You need to have kiwirecorder.py in the same directory (a symbolic link works fine!)

Adapt a kiwiplot-source.csv from the example file.  
Example:  
9000,dg7lan.kiwi.com,8073  
147.3,dg7lan.kiwi.com,8073  

Frequency (Hz), Kiwi URL, Kiwi port

Start record.py (record.py [-u username])

When finished, start plotcsv.py -i filename.csv

<img width="935" alt="image" src="https://user-images.githubusercontent.com/20392230/210586769-3ecf6de4-95b7-42f3-8327-88d8e7eb2864.png">



