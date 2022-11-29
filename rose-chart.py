import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

df = pd.read_csv("AgeDataset-V1.csv")
df.dropna()
#america = df[df['Country']=='United States of America']
america = pd.read_csv("res.csv")
cause = america['Manner of death'].unique()

death_sum = {}
for i in cause:
    count = len(america[america["Manner of death"] == i])
    death_sum[i] = count
order = sorted(death_sum.items(),key = lambda item:item[1], reverse = True)

top10_cause=[i[0] for i in order[1:11]]
top10_deathnumber = [ i[1] for i in order[1:11]]

print(top10_cause,top10_deathnumber)

# life_sum={}
# for i in top10_cause:
#     if len(america[america["Manner of death"] == i]) !=0:
#         average = america[america['Manner of death'] == i]['Age of death'].sum()/len(america[america["Manner of death"] == i])
#         life_sum[i] = round(average,2)

#average_sort = sorted(life_sum.items(),key = lambda item:item[1], reverse = True)

# average_cause=[]
# for item in average_sort[:10]:
#     x = item[0].replace('suicide; ','')
#     x = x.replace('; natural cause', '')
#     average_cause.append(x)

# correct_average=[]
# for i in top10_cause:
#     correct_average.append(life_sum[i])
#print(correct_average)

life_sum=[]
for i in top10_cause:
    if len(america[america["Manner of death"] == i]) !=0:
        average = america[america['Manner of death'] == i]['Age of death'].sum()/len(america[america["Manner of death"] == i])
        life_sum.append(round(average,2))


#create the color_series for the rosechart

color_series = ['#802200','#B33000','#FF4500','#FAA327','#9ECB3C','#6DBC49','#37B44E','#14ADCF','#209AC9','#1E91CA','#2C6BA0','#2B55A1','#2D3D8E','#44388E','#6A368B','#D02C2A','#D44C2D','#F57A34','#FA8F2F','#D99D21']
color_2=['#2C6BA0','#2B55A1','#2D3D8E','#44388E','#6A368B','#D02C2A','#D44C2D','#F57A34','#FA8F2F','#D99D21']
rosechart = Pie(init_opts=opts.InitOpts(width='1650px', height='950px'))
# set the color
rosechart.set_colors(color_series)

# add the data to the rosechart
rosechart.add("", [list(z) for z in zip(top10_cause, life_sum)],
        radius=["15%", "60%"],
        center=["30%", "60%"],   # center of the chart
        rosetype="area")

# set the global options for the chart
rosechart.set_global_opts(title_opts=opts.TitleOpts(title='Life expectancy in the United States with top10 cause of death',subtitle="Nightingle Rose Chart"),
                     legend_opts=opts.LegendOpts(is_show=True,pos_left='50%',orient="vertical")
                     )
# set the series options
rosechart.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="outside", font_size=10,formatter="{b}:{c}", font_style="italic",font_weight="bold", font_family="Century"))
rosechart.render(path = 'rose.html')