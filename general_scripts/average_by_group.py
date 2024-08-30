def average_by_group(in_file):
  import pandas as pd
  df = pd.read_csv(in_file, sep='\t', header = none, names=['value','category'])
  avg_by_group = df.groupby('category').mean()
  return avg_by_group.to_csv(sep='\t')
