import pandas as pd
import numpy as np
import matplotlib.pyplot as plp
import  scipy.stats as stats
import plotly.express as px
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
#  data cleaning  and preprocessing
df = pd.read_csv('/home/maren/Downloads/Python-project/food_prices_ind.csv')
df.drop(index = 0,inplace = True)
df['latitude'] = df['latitude'].replace(np.nan,20.953)
df['longitude'] = df['longitude'].replace(np.nan,80.952)
df[['admin1','admin2']] = df[['admin1','admin2']].replace(np.nan,'India')
# df['date'] = pd.to_timedelta(df['date'])
df[['latitude','longitude','price','usdprice']] = df[['latitude','longitude','price', 'usdprice']].astype(float)


for place in df.admin1.unique():
    df_place = df.groupby('admin1').get_group(place).sort_values(by='usdprice',ascending=True)
    df_place = df_place[['date','market','category','price','usdprice']]
    # For a particular city different category price
    for category in df_place.category.unique():
        # df_place_category = df_place.groupby('category').get_group('category').sort_values(['date','usdprice'], ascending=False)
        df_place_category = df_place[df_place['category'] == category].sort_values(['date','usdprice'],ascending = False)
        df_place_category = df_place_category[['date','market','category','price','usdprice']]
        df_place_category.drop_duplicates(subset = 'date',inplace = True)
        fig = px.scatter_3d(df_place_category,x= "date",y="usdprice",title=f'{place}  {category} prices')
        fig.show()
