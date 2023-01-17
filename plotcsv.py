import pandas as pd
import plotly.graph_objects as go
import argparse

sweepmode: bool = False
debug: bool = False
filename: str = ""

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='csv datafile (may contain multiple measurements)')
parser.add_argument('-s', '--sweep', action='store_true', help='file was recorded in sweep mode')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
args = vars(parser.parse_args())

if args['sweep']:
    sweepmode = True

if args['verbose']:
    debug = True

if args['input']:
    filename = args["input"]
else:
    print("please specify input file name with -i")
    exit(1)


fig = go.Figure()

# read csv into dataframe
df = pd.read_csv(filename)

if sweepmode:
    df.columns = ["time", "freq", "power", "pass"]

    # find unique measurement names in csv
    measurements = set(df['pass'])
    if debug: print(measurements)

    for i in measurements:
        df_result = df[df['pass'] == i]
        fig.add_trace(go.Scatter(x=df_result['freq'], y=df_result['power'], mode='lines', name=i))

else:
    # no sweepmode
    df.columns = ["time", "power"]
    fig.add_trace(go.Scatter(x = df['time'], y = df['power'], mode='lines', name='dbm over time'))

fig.show()
