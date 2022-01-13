import pandas as pd

# Bokeh libraries
from bokeh.plotting import figure, show, curdoc
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource, HoverTool, Div
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import column
from bokeh.models import NumeralTickFormatter

df = pd.read_csv('data/covid_19_indonesia_time_series_all.csv')

df = df[['Date', 'Location', 'Island', 'New Cases',
           'New Recovered', 'New Deaths',
           'Total Cases', 'Total Recovered',
           'Total Deaths']]

df['Date'] = pd.to_datetime(df['Date'])
df = df.rename(columns={"New Cases": "NewCases",
                          "New Recovered": "NewRecovered",
                          "NewDeaths": "NewDeaths",
                          "Total Cases": "TotalCases",
                          "Total Recovered": "TotalRecovered",
                          "Total Deaths": "TotalDeaths"})

# Output to file
output_notebook()
output_file('Covid-Indonesia.html',
            title='Covid Indonesia')


######################################################################
########### Plotting for covid 19 in Indonesia Starts Here ###########
######################################################################


###### CDS Seluruh Indonesia #######
indonesia = df[df['Location'] == 'Indonesia']
indonesia['Island'] = 'Indonesia'
indonesia_cds = ColumnDataSource(indonesia)


# # Create and configure the figure for covid case in Indonesia
tot_case_ind = figure(x_axis_type='datetime',
                      plot_height=500, plot_width=800,
                      title='Total Kasus Covid',
                      x_axis_label='Tanggal', y_axis_label='Total Kasus')

new_case_ind = figure(x_axis_type='datetime',
                      plot_height=500, plot_width=800,
                      title='Kasus Baru',
                      x_axis_label='Tanggal', y_axis_label='Kasus Baru')

# # Format the y-axis
tot_case_ind.yaxis.formatter = NumeralTickFormatter(format="00")
new_case_ind.yaxis.formatter = NumeralTickFormatter(format="00")

# # Render the case as lines
tot_case_ind.line('Date', 'TotalCases',
                  color='#CE1141', legend_label='Total Kasus di Seluruh Indonesia',
                  source=indonesia_cds)

new_case_ind.line('Date', 'NewCases',
                  color='#CE1141', legend_label='Kasus Baru di Seluruh Indonesia',
                  source=indonesia_cds)

# # Move the legend to the upper left corner
tot_case_ind.legend.location = 'top_left'
new_case_ind.legend.location = 'top_left'

# Format the tooltip
tooltips1 = [
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@TotalCases'),
]

tooltips2 = [
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@NewCases'),
]

# Configure a renderer to be used upon hover
hover_glyph = tot_case_ind.circle(x='Date', y='TotalCases', source=indonesia_cds,
                                  size=5, alpha=0,
                                  hover_fill_color='black', hover_alpha=0.5)
hover_glyph2 = new_case_ind.circle(x='Date', y='NewCases', source=indonesia_cds,
                                   size=5, alpha=0,
                                   hover_fill_color='black', hover_alpha=0.5)

# Add the HoverTool to the figure
tot_case_ind.add_tools(HoverTool(tooltips=tooltips1, formatters={
                       '@Date': 'datetime'}, renderers=[hover_glyph, hover_glyph2]))
new_case_ind.add_tools(HoverTool(tooltips=tooltips2, formatters={
                       '@Date': 'datetime'}, renderers=[hover_glyph, hover_glyph2]))

# Increase the plot widths
tot_case_ind.plot_width = new_case_ind.plot_width = 1000

# Create two panels, one for each conference
tot_case_ind_panel = Panel(child=tot_case_ind, title='Total Kasus')
new_case_ind_panel = Panel(child=new_case_ind, title='Kasus Baru')

# Assign the panels to Tabs
tabs = Tabs(tabs=[tot_case_ind_panel, new_case_ind_panel])





###### CDS Pulau Jawa dan Nusa Tenggara #######
jawa = df[df['Island'] == 'Jawa']
jawa = jawa.groupby(['Date']).sum().reset_index()
jawa['Island'] = 'Jawa'
jawa_cds = ColumnDataSource(jawa)

nusa = df[df['Island'] == 'Nusa Tenggara']
nusa = nusa.groupby(['Date']).sum().reset_index()
nusa['Island'] = 'Nusa Tenggara'
nusa_cds = ColumnDataSource(nusa)

###### CDS Sumatera #######
sumatera = df[df['Island'] == 'Sumatera']
sumatera = sumatera.groupby(['Date']).sum().reset_index()
sumatera['Island'] = 'Sumatera'
sumatera_cds = ColumnDataSource(sumatera)

###### CDS Kalimantan #######
Kalimantan = df[df['Island'] == 'Kalimantan']
Kalimantan = Kalimantan.groupby(['Date']).sum().reset_index()
Kalimantan['Island'] = 'Kalimantan'
kalimantan_cds = ColumnDataSource(Kalimantan)

###### CDS Sulawesi ########
sulawesi = df[df['Island'] == 'Sulawesi']
sulawesi = sulawesi.groupby(['Date']).sum().reset_index()
sulawesi['Island'] = 'Sulawesi'
sulawesi_cds = ColumnDataSource(sulawesi)

###### CDS Papua dan Maluku #####
papua = df[df['Island'] == 'Papua' ]
papua = papua.groupby(['Date']).sum().reset_index()
papua['Island'] = 'Papua'
papua_cds = ColumnDataSource(papua)

maluku = df[df['Island'] == 'Nusa Tenggara']
maluku = maluku.groupby(['Date']).sum().reset_index()
maluku['Island'] = 'Maluku'
maluku_cds = ColumnDataSource(maluku)

# # Create and configure the figure
tot_case = figure(x_axis_type='datetime',
                  plot_height=500, plot_width=800,
                  title='Total Kasus Covid',
                  x_axis_label='Tanggal', y_axis_label='Total Kasus')

new_case = figure(x_axis_type='datetime',
                  plot_height=500, plot_width=800,
                  title='Kasus Baru',
                  x_axis_label='Tanggal', y_axis_label='Kasus Baru')

# # Format the y-axis
tot_case.yaxis.formatter = NumeralTickFormatter(format="00")
new_case.yaxis.formatter = NumeralTickFormatter(format="00")

# # Render the case as lines
tot_case.line('Date', 'TotalCases',
              color='green', legend_label='Total Kasus Pulau Sumatera',
              source=sumatera_cds)
tot_case.line('Date', 'TotalCases',
              color='blue', legend_label='Total Kasus Pulau Jawa',
              source=jawa_cds)
tot_case.line('Date', 'TotalCases',
              color='pink', legend_label='Total Kasus Pulau Nusa',
              source=nusa_cds)
tot_case.line('Date', 'TotalCases',
              color='black', legend_label='Total Kasus Pulau Kalimantan',
              source=kalimantan_cds)
tot_case.line('Date', 'TotalCases',
              color='yellow', legend_label='Total Kasus Pulau Sulawesi',
              source=sulawesi_cds)
tot_case.line('Date', 'TotalCases',
              color='purple', legend_label='Total Kasus Pulau Papua',
              source=papua_cds)
tot_case.line('Date', 'TotalCases',
              color='gray', legend_label='Total Kasus Pulau Maluku',
              source=maluku_cds)

new_case.line('Date', 'NewCases',
              color='green', legend_label='Kasus Baru Pulau Sumatera',
              source=sumatera_cds)
new_case.line('Date', 'NewCases',
              color='blue', legend_label='Kasus Baru Pulau Jawa',
              source=jawa_cds)
new_case.line('Date', 'NewCases',
              color='pink', legend_label='Kasus Baru Pulau Nusa',
              source=nusa_cds)
new_case.line('Date', 'NewCases',
              color='black', legend_label='Kasus Baru Pulau Kalimantan',
              source=kalimantan_cds)
new_case.line('Date', 'NewCases',
              color='yellow', legend_label='Kasus Baru Pulau Sulawesi',
              source=sulawesi_cds)
new_case.line('Date', 'NewCases',
              color='purple', legend_label='Kasus Baru Pulau Papua',
              source=papua_cds)
new_case.line('Date', 'NewCases',
              color='gray', legend_label='Kasus Baru Pulau Maluku',
              source=maluku_cds)

# # Move the legend to the upper left corner
tot_case.legend.location = 'top_left'
new_case.legend.location = 'top_left'

# Format the tooltip
tooltips3 = [
    ('Pulau', '@Island'),
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@TotalCases'),
]

tooltips4 = [
    ('Pulau', '@Island'),
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@NewCases'),
]

# Add the HoverTool to the figure
tot_case.add_tools(HoverTool(tooltips=tooltips3,
                             formatters={'@Date': 'datetime'}))
new_case.add_tools(HoverTool(tooltips=tooltips4,
                             formatters={'@Date': 'datetime'}))

# Increase the plot widths
tot_case.plot_width = new_case.plot_width = 1000

# Create two panels, one for each conference
tot_case_panel = Panel(child=tot_case, title='Total Kasus')
new_case_panel = Panel(child=new_case, title='Kasus Baru')

# Assign the panels to Tabs
tabs2 = Tabs(tabs=[tot_case_panel, new_case_panel])

# Add a title for the covid-19 in Indonesia visualization using Div
html = """<h3>Persebaran Covid-19 Di Indonesia</h3>
<b><i>2020-2021</i>
<br>
"""

# Add a title for the covid-19 in Indonesian Island visualization using Div
html2 = """<h3>Perbandingan Persebaran Covid-19 Di Pulau-Pulau Indonesia</h3>
<b><i>2020-2021</i>
<br>
"""

# creating vertical space
space = "<br>"

sup_title1 = Div(text=html)
sup_title2 = Div(text=html2)
spacing = Div(text=space)

# This final command is required to launch the plot in the browser
curdoc().add_root(column(sup_title1, tabs, spacing, sup_title2, tabs2))
