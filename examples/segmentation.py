import pandas as pd
from smart_tools.sklearn import segmentation

df=pd.read_csv(r'..\cs_predicted_data.csv')
features = ['Transaction_amount', 'Number_of_transactions']
m,s = segmentation.segment(df=df, features= features, n_clusters=15)

df['segment'] = s
print(f"Cluster center: \n {m.cluster_centers_}")
print(f"Segments: {df['segment'].sort_values().unique()}")

segmentation.plot(df, segmented_by=features)
