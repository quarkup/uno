import pandas as pd
import cufflinks as cf
from IPython.display import display, HTML

#cf.set_config_file(sharing='public', theme='white', offline=True)
cf.set_config_file(sharing='public', theme='white', offline=True)
#---------------------------------------------
cf.getThemes()

#---------------------------------------------
pd.set_option('display.max_rows', 5000)   #?????????????????????????????????????????????
pd.read_csv('population_total.csv')
#---------------------------------------------
df_population = pd.read_csv('population_total.csv')
df_population = df_population.dropna() # BORRAR VALORES NULOS -> "na"
#df_population
#---------------------------------------------------------
df_population =  df_population.pivot(index  ='year',
                                     columns='country',
                                     values ='population')
#---------------------------------------------------------
df_population=df_population[['United States','India', 'China','Indonesia','Brazil']]


# LINEPLOT
#---------------------------------------------------------
#df_population.iplot(kind='line')  #-----------------NO TRABAJA  'iplot'
df_population.plot(kind='line')
df_population