import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go

import argparse

sweepmode: bool = False


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='csv datafile')
parser.add_argument('-s', '--sweep', action='store_true', help='file was recorded in sweep mode')
args = vars(parser.parse_args())

if args['sweep']:
    sweepmode = True

if args['input']:
    csvfile: str = args["input"]
else:
    print("please specify input file name with -i")
    exit(1)

df = pd.read_csv(csvfile+"_1.csv")
df1 = pd.read_csv(csvfile+"_2.csv")

if sweepmode:
    df.columns = ["time", "freq", "power", "pass"]
    df1.columns = ["time", "freq", "power", "pass"]

    trace1 = go.Scatter(x=df['freq'], y=df['power'], mode='lines', name='Line 1')
    trace2 = go.Scatter(x=df1['freq'], y=df1['power'], mode='lines', name='Line 2')

    #fig = make_subplots(rows=1, cols=2)
    #fig = add_trace(go.scatter(df, x = 'freq', y = 'power', title='dbm @ freq'))
    #
    #fig2 = add_trace(go.scatter(df, x = 'freq', y = 'power', title='dbm @ freq pass 2'))
    fig = go.Figure(data=[trace1, trace2])
else:
    df.columns = ["time", "power"]
    fig = go.scatter(df, x = 'time', y = 'power', title='dbm over time')
fig.show()
