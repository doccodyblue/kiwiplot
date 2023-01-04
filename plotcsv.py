import pandas as pd
import plotly.express as px
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='csv datafile')

args = vars(parser.parse_args())

if args['input']:
    csvfile: str = args["input"]
else:
    print("please specify input file name with -i")
    exit(1)

df = pd.read_csv(csvfile)
df.columns = ["time", "power"]
fig = px.line(df, x = 'time', y = 'power', title='dbm over time')
fig.show()
