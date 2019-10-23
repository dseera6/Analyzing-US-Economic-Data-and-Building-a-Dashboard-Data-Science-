import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

#The function will produce a dashboard as well as an html file.
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
 
#The dictionary links contain the CSV files with all the data. The value for the key GDP is the file that contains the GDP data. The value for the key unemployment contains the unemployment data.
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

#Creating a dataframe that contains the GDP data and display the first five rows of the dataframe.
x = pd.read_csv(links["GDP"])
df = pd.DataFrame(x)
dff = x.head()
print(dff)

#Creating a dataframe that contains the unemployment data. Display the first five rows of the dataframe. 
dfg = pd.read_csv(links["unemployment"])
y = pd.DataFrame(dfg)
print(y.head())

#to Display a dataframe where unemployment was greater than 8.5%.
yy = y[y['unemployment'] > 8.5]
print(yy)

#Use the function make_dashboard to make a dashboard
dfd = pd.DataFrame(x['date'])
print(date)

#Create a new dataframe with the column 'change-current'  called gdp_change from the dataframe that contains the GDP data.
gdp_change = pd.DataFrame(x['change-current'])
print(gdp_change)

#Create a new dataframe with the column 'unemployment'  called unemployment.  from the dataframe that contains the  unemployment data.
unemployment = pd.DataFrame(y['unemployment'])
print(unemployment)

title = 'Dashboard'
file_name = "index.html"

#Calling the function make_dashboard , to produce a dashboard.
# Fill up the parameters in the following function:
# make_dashboard(x=, gdp_change=, nemployment=, title=, file_name=)
make_dashboard(dfd, gdp_change, unemployment, title, file_name)
