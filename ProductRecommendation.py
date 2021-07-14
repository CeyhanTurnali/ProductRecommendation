import pandas as pd
meta=pd.read_csv('meta.csv')
events=pd.read_csv('events.csv')
merged_data=meta.merge(events,on="productid")
merged_data.to_csv("merged_data.csv")
data=pd.read_csv('merged_data.csv')
data=data.drop(['Unnamed: 0'], axis=1)
data['sessionid'].isna().sum()
data = data.dropna(subset=['sessionid'])
data['event'] = data['event'].replace(['cart'],'1')
data['event'] = data['event'].astype(float)
customer_item_matrix = data.pivot_table(
    index='sessionid',
    columns='productid',
    values='event',
    aggfunc='sum'
)
customer_item_matrix = customer_item_matrix.applymap(lambda x: 1 if x > 0 else 0)
from sklearn.metrics.pairwise import cosine_similarity
item_item_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix.T))
item_item_sim_matrix.columns = customer_item_matrix.T.index

item_item_sim_matrix['productid'] = customer_item_matrix.T.index
item_item_sim_matrix = item_item_sim_matrix.set_index('productid')

def recom(product):
    top_10_similar_items = list(
        item_item_sim_matrix.loc[product].sort_values(ascending=False).iloc[1:11].index)
    print(top_10_similar_items)
    print()
    print("Similar items to product: ")
    return(data.loc[
              data['productid'].isin(top_10_similar_items),
              ['productid', 'name']
          ].drop_duplicates().set_index('productid').loc[top_10_similar_items])

