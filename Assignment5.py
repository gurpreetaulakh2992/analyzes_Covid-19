# import API's
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import seaborn as sns

# read CSV file using panda API
data = pd.read_csv('conposcovidloc.csv')
# fecthing columns from csv file
data.columns = ['row_id','accurate_episode_date','case_reported_date','test_reported_date','specimen_date','age_group','client_gender','case_acquisitioninfo','outcome','outbreak_related','reporting_phu_id','reporting_phu','reporting_phu_address','reporting_phu_city','reporting_phu_postal_code','reporting_phu_website','reporting_phu_latitude','reporting_phu_longitude']
# removing extra spaces from columns
data.columns = data.columns.str.strip()


phu_name=sorted(list(dict.fromkeys(data.reporting_phu_city)))
date=sorted(list(dict.fromkeys(data.case_reported_date)))

# mapping using aggregation and group by
outcome=data.groupby(['outcome']).agg({'row_id':'count'}).reset_index()
outcome=outcome.set_index('outcome')

data=data.groupby(['reporting_phu_city','case_reported_date']).agg({'row_id':'count'}).reset_index()


for date1 in date:
    for city in phu_name:
        row=data.loc[(data["case_reported_date"] == date1) & (data["reporting_phu_city"] == city)]
        if row.empty:
            new_row = {"case_reported_date": date1, "reporting_phu_city": city, "row_id":0}
            data = data.append(new_row, ignore_index=True, verify_integrity=False, sort=None)

# Line graph generation
fig, ax = plt.subplots(figsize=(18,12))

for city in phu_name:
    phu_cases = data.loc[(data['reporting_phu_city'] == city)]
    x = sorted(phu_cases['case_reported_date'].tolist())
    y = phu_cases['row_id'].tolist()
    plt.plot(x, y, label = city)

# set label for x and y axis and title of the line graph
ax.set(xlabel="Date", ylabel="Active Cases", title="Active cases by PHU")
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval = 3))
plt.legend(loc='best')
plt.grid(True)
plt.show()


# heatmap using seaborn
heatcovid=data.pivot("reporting_phu_city","case_reported_date","row_id")
ax=sns.heatmap(heatcovid,cmap="turbo",xticklabels=15,yticklabels=1)

figure=ax.get_figure()


deaths=[value.row_id for index,value in outcome.T.iteritems() if index =="Fatal"]
resolved=[value.row_id for index,value in outcome.T.iteritems() if index =="Resolved"]
active=[value.row_id for index,value in outcome.T.iteritems() if index =="Not Resolved"]
ax.set(title="Covid 19 HeatMap",xlabel="Dates",ylabel="PHU")
date_form1 = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form1)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval = 5))
plt.grid(True)
plt.show()