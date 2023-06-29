import json
filename='data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)
# readable_file='data/readable_eq_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_data,f,indent=4)
    all_eq_dict=all_eq_data['features']
    mags,titles,lons,lats=[],[],[],[]
    for eq_dict in all_eq_dict:
        mag=eq_dict['properties']['mag']
        title=eq_dict['properties']['title']
        lon=eq_dict['geometry']['coordinates'][0]
        lat=eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        titles.append(title)
        lons.append(lon)
        lats.append(lat)
print(lons[:5])
import plotly.express as px
import pandas as pd
data=pd.DataFrame(data=list(zip(lons,lats,titles,mags)),columns=['经度','维度','位置','震级'])
fig=px.scatter(
    data,
    x='经度',y='维度',range_x=[-200,200],range_y=[-90,90],
    width=800,height=800,
    title='全球散点图',
    size='震级',#定制标记尺寸
    size_max=10,#定制标记颜色
    color='震级'
    )
fig.write_html('global_earthquake.html')
fig.show() 
