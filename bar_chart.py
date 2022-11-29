import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.options.global_options import ThemeType

df = pd.read_csv("AgeDataset-V1.csv")
df.dropna()
america = df[df['Country']=='United States of America']
cause = america['Manner of death'].unique()
occupation = america['Occupation'].unique()

print(occupation)

death_sum = {}
for i in cause:
    count = len(america[america["Manner of death"] == i])
    death_sum[i] = count
order = sorted(death_sum.items(),key = lambda item:item[1], reverse = True)

top10_cause=[i[0] for i in order[1:11]]
top10_deathnumber = [ i[1] for i in order[1:11]]

occ_sum={}
for i in top10_cause:
    count = len(america[america["Manner of death"] == i])
    death_sum[i] = count
order = sorted(death_sum.items(),key = lambda item:item[1], reverse = True)

occupation= america['Occupation'].unique()
occ_sum = {}
for i in occupation:
    count = len(america[america["Occupation"] == i])
    occ_sum[i] = count
occ_order = sorted(occ_sum.items(),key = lambda item:item[1], reverse = True)


color_series = ['#B33000','#FF4500','#9932CC','#6DBC49','#CD853F','#14ADCF','#FFA500']
top10_occ=[i[0] for i in occ_order[0:10]]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
l10=[]
for i in range(7):
    part = america[america["Manner of death"] == top10_cause[i]]
    l1.append(len(part[part["Occupation"] == top10_occ[0]]))
    l2.append(len(part[part["Occupation"] == top10_occ[1]]))
    l3.append(len(part[part["Occupation"] == top10_occ[2]]))
    l4.append(len(part[part["Occupation"] == top10_occ[3]]))
    l5.append(len(part[part["Occupation"] == top10_occ[4]]))
    l6.append(len(part[part["Occupation"] == top10_occ[5]]))
    l7.append(len(part[part["Occupation"] == top10_occ[6]]))
    l8.append(len(part[part["Occupation"] == top10_occ[7]]))
    l9.append(len(part[part["Occupation"] == top10_occ[8]]))
    l10.append(len(part[part["Occupation"] == top10_occ[9]]))

bar = (
    Bar(init_opts=opts.InitOpts(bg_color='rgba(176,224,230,0.7)'))
    .add_xaxis(top10_cause[:6])
    .add_yaxis(top10_occ[0], l1,color=color_series[0])
    .add_yaxis(top10_occ[1], l2,color=color_series[1])
    .add_yaxis(top10_occ[2], l3,color=color_series[2])
    .add_yaxis(top10_occ[3], l4,color=color_series[3])
    .add_yaxis(top10_occ[4], l5,color=color_series[4])
    .add_yaxis(top10_occ[5], l6,color=color_series[5])
    .add_yaxis(top10_occ[6], l7,color=color_series[6])
    .set_global_opts(title_opts=opts.TitleOpts(title="Occupation in top death cause", subtitle="bar chart"),xaxis_opts=opts.AxisOpts(name_rotate=0,name="death cause",axislabel_opts={"rotate":10}),yaxis_opts=opts.AxisOpts(name= "Occupation")
                    ,legend_opts=opts.LegendOpts(is_show=True,pos_left='50%'))
)
bar.render(path='bar.html')


