import pandas as pd
from sys import argv


df = pd.read_excel(argv[1])
df.to_csv(argv[2], index=False)
