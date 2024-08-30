def stdin_to_freq(in_file):
  import pandas as pd
  df = pd.DataFrame(in_file, columns=['items'])
  count = df['items'].value_counts()
  count.columns = ['items','count']
  total=count['count'].sum()
  count['n_count']=count['count']/total
  freq=count['count','n_count','items']
  return freq.to_csv(sep='\t')
