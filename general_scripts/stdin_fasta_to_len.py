def stdin_fasta_to_len(data):
  import pandas as pd
  df = pd.read_csv(data, sep='\n', header=None, names=['data'])
  df['id'] = df['data'].str.contains('>')
  df['id'] = df['id'].cumsum()
  length = df[`df['data'].str.contains('>')].groupby('id')['data'].apply(lambda x: x.str.len().sum())
  return length.to_csv(sep='\t')
