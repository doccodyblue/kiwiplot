import pandas as pd
import plotly.express as px
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

df = pd.read_csv(csvfile)
if sweepmode:
    df.columns = ["time", "freq", "power"]
    fig = px.line(df, x = 'freq', y = 'power', title='dbm @ freq')
else:
    df.columns = ["time", "power"]
    fig = px.line(df, x = 'time', y = 'power', title='dbm over time')
fig.show()
