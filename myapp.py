import pandas as pd

# Library-library yang digunakan
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

# Proses output file data covid_19_indonesia_time_series_all.csv
output_notebook()
output_file('Covid-Indonesia.html',
            title='Covid Indonesia')





# Kasus untuk seluruh Indonesia
indonesia = df[df['Location'] == 'Indonesia']
indonesia['Island'] = 'Indonesia'
indonesia_case = ColumnDataSource(indonesia)


# Definisikan figure untuk dijadikan sebagai plot diagram
total_case_ind = figure(x_axis_type='datetime',
                      plot_height=500, plot_width=800,
                      title='Total Kasus Covid',
                      x_axis_label='Per Tanggal', y_axis_label='Jumlah Kejadian')

new_case_ind = figure(x_axis_type='datetime',
                      plot_height=500, plot_width=800,
                      title='Kasus Terkini',
                      x_axis_label='PerTanggal', y_axis_label='Jumlah Kejadian')

# Definisikan y-axis
total_case_ind.yaxis.formatter = NumeralTickFormatter(format="00")
new_case_ind.yaxis.formatter = NumeralTickFormatter(format="00")

# Definisikan line / proses render line
total_case_ind.line('Date', 'TotalCases',
                  color='#CE1141', legend_label='Total Kasus di Seluruh Indonesia',
                  source=indonesia_case,line_width=3)

new_case_ind.line('Date', 'NewCases',
                  color='#CE1141', legend_label='Kasus Terkini di Seluruh Indonesia',
                  source=indonesia_case,line_width=3)

# Definisikan legend dengan lokasi atas kiri
total_case_ind.legend.location = 'top_left'
new_case_ind.legend.location = 'top_left'

# Definisikan tooltips
tooltips1 = [
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@TotalCases'),
]

tooltips2 = [
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@NewCases'),
]

# Defnisikan renderer sebagai hover
hover = total_case_ind.circle(x='Date', y='TotalCases', source=indonesia_case,
                                  size=5, alpha=0,
                                  hover_fill_color='black', hover_alpha=0.5)
hover2 = new_case_ind.circle(x='Date', y='NewCases', source=indonesia_case,
                                   size=5, alpha=0,
                                   hover_fill_color='black', hover_alpha=0.5)

# Masukkan hover ke diagram / figure
total_case_ind.add_tools(HoverTool(tooltips=tooltips1, formatters={
                       '@Date': 'datetime'}, renderers=[hover, hover2]))
new_case_ind.add_tools(HoverTool(tooltips=tooltips2, formatters={
                       '@Date': 'datetime'}, renderers=[hover, hover2]))

# Konfigurasi ukuran plot / diagram
total_case_ind.plot_width = new_case_ind.plot_width = 1270

# Definisikan dua panel berisi total kasus dan Kasus Terkini
total_case_ind_panel = Panel(child=total_case_ind, title='Total Kasus')
new_case_ind_panel = Panel(child=new_case_ind, title='Kasus Terkini')

# Masukkan panel pada tabs button
tabs = Tabs(tabs=[total_case_ind_panel, new_case_ind_panel])


# Kasus untuk Pulau Jawa 
jawa = df[df['Island'] == 'Jawa']
jawa = jawa.groupby(['Date']).sum().reset_index()
jawa['Island'] = 'Jawa'
jawa_cds = ColumnDataSource(jawa)

# Kasus untuk Pulau Nusa Tenggara 
nusa = df[df['Island'] == 'Nusa Tenggara']
nusa = nusa.groupby(['Date']).sum().reset_index()
nusa['Island'] = 'Nusa Tenggara'
nusa_cds = ColumnDataSource(nusa)

# Kasus untuk Pulau Sumatera
sumatera = df[df['Island'] == 'Sumatera']
sumatera = sumatera.groupby(['Date']).sum().reset_index()
sumatera['Island'] = 'Sumatera'
sumatera_cds = ColumnDataSource(sumatera)

# Kasus untuk Pulau Kalimantan
Kalimantan = df[df['Island'] == 'Kalimantan']
Kalimantan = Kalimantan.groupby(['Date']).sum().reset_index()
Kalimantan['Island'] = 'Kalimantan'
kalimantan_cds = ColumnDataSource(Kalimantan)

# Kasus untuk Pulau Sulawesi
sulawesi = df[df['Island'] == 'Sulawesi']
sulawesi = sulawesi.groupby(['Date']).sum().reset_index()
sulawesi['Island'] = 'Sulawesi'
sulawesi_cds = ColumnDataSource(sulawesi)

# Kasus untuk Pulau Papua
papua = df[df['Island'] == 'Papua' ]
papua = papua.groupby(['Date']).sum().reset_index()
papua['Island'] = 'Papua'
papua_cds = ColumnDataSource(papua)

# Kasus untuk Pulau Maluku
maluku = df[df['Island'] == 'Maluku']
maluku = maluku.groupby(['Date']).sum().reset_index()
maluku['Island'] = 'Maluku'
maluku_cds = ColumnDataSource(maluku)

# Definisikan figure untuk dijadikan sebagai diagram 
total_case = figure(x_axis_type='datetime',
                  plot_height=500, plot_width=800,
                  title='Total Kasus Covid',
                  x_axis_label='Per Tanggal', y_axis_label='Jumlah Kejadian')

new_case = figure(x_axis_type='datetime',
                  plot_height=500, plot_width=800,
                  title='Kasus Terkini',
                  x_axis_label='Per Tanggal', y_axis_label='Jumlah Kejadian')

# Definisikan y-axis
total_case.yaxis.formatter = NumeralTickFormatter(format="00")
new_case.yaxis.formatter = NumeralTickFormatter(format="00")

# Definisikan line / proses render line
total_case.line('Date', 'TotalCases',
              color='green', legend_label='Total Kasus Pulau Sumatera',
              source=sumatera_cds,line_width=3)
total_case.line('Date', 'TotalCases',
              color='blue', legend_label='Total Kasus Pulau Jawa',
              source=jawa_cds,line_width=3)
total_case.line('Date', 'TotalCases',
              color='pink', legend_label='Total Kasus Pulau Nusa',
              source=nusa_cds,line_width=3)
total_case.line('Date', 'TotalCases',
              color='black', legend_label='Total Kasus Pulau Kalimantan',
              source=kalimantan_cds,line_width=3)
total_case.line('Date', 'TotalCases',
              color='yellow', legend_label='Total Kasus Pulau Sulawesi',
              source=sulawesi_cds,line_width=3)
total_case.line('Date', 'TotalCases',
              color='purple', legend_label='Total Kasus Pulau Papua',
              source=papua_cds,line_width=3)
total_case.line('Date', 'TotalCases',
              color='gray', legend_label='Total Kasus Pulau Maluku',
              source=maluku_cds,line_width=3)

new_case.line('Date', 'NewCases',
              color='green', legend_label='Kasus Terkini Pulau Sumatera',
              source=sumatera_cds,line_width=3)
new_case.line('Date', 'NewCases',
              color='blue', legend_label='Kasus Terkini Pulau Jawa',
              source=jawa_cds,line_width=3)
new_case.line('Date', 'NewCases',
              color='pink', legend_label='Kasus Terkini Pulau Nusa',
              source=nusa_cds,line_width=3)
new_case.line('Date', 'NewCases',
              color='black', legend_label='Kasus Terkini Pulau Kalimantan',
              source=kalimantan_cds,line_width=3)
new_case.line('Date', 'NewCases',
              color='yellow', legend_label='Kasus Terkini Pulau Sulawesi',
              source=sulawesi_cds,line_width=3)
new_case.line('Date', 'NewCases',
              color='purple', legend_label='Kasus Terkini Pulau Papua',
              source=papua_cds,line_width=3)
new_case.line('Date', 'NewCases',
              color='gray', legend_label='Kasus Terkini Pulau Maluku',
              source=maluku_cds,line_width=3)

# Definisikan legend dengan lokasi atas kiri
total_case.legend.location = 'top_left'
new_case.legend.location = 'top_left'

# Definisikan tooltips
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

# Masukkan hover ke diagram / figure
total_case.add_tools(HoverTool(tooltips=tooltips3,
                             formatters={'@Date': 'datetime'}))
new_case.add_tools(HoverTool(tooltips=tooltips4,
                             formatters={'@Date': 'datetime'}))

# Konfigurasi ukuran plot / diagram
total_case.plot_width = new_case.plot_width = 1270

# Definisikan dua panel berisi total kasus dan Kasus Terkini
total_case_panel = Panel(child=total_case, title='Total Kasus')
new_case_panel = Panel(child=new_case, title='Kasus Terkini')

# Masukkan panel pada tabs button
tabs2 = Tabs(tabs=[total_case_panel, new_case_panel])

# Tambahkan judul untuk Figure 1 yaitu Jumlah Kasus Covid-19 di Seluruh Indonesia
html = """<h3>Persebaran Covid-19 Di Indonesia</h3>
<b><i>2020-2021</i>
<br>
"""

# Tambahkan judul untuk Figure 2 yaitu Jumlah Kasus Covid-19 untuk setiap Pulau di Indonesia
html2 = """<h3>Perbandingan Persebaran Covid-19 Di Pulau-Pulau Indonesia</h3>
<b><i>2020-2021</i>
<br>
"""

# Tambahkan spasi satu line
space = "<br>"

sup_title1 = Div(text=html)
sup_title2 = Div(text=html2)
spacing = Div(text=space)

# Lakukan running untuk hasil akhir
curdoc().add_root(column(sup_title1, tabs, spacing, sup_title2, tabs2))
