import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as math
import seaborn as sns

#I can't find a csv with the information I'm looking for so instead I'll create the df from scratch. Hawaii became a state in 1959 and conducted elections for Senate that year.
#Then there was an election every two years in line with the federal schedule beginning in 1960. Rather than type every year, we'll generate a list using a for loop.

#initialize an empty list for election years
year = []

 #initialize a loop incrementing year by 2 between 1960 and 2022. Convert the result of each interation to a string and append it to the empty list 'year'
for i in range(1960,2024, 2):

    year.append(str(i))

#insert the 1959 election at index zero
year.insert(0,'1959')

#print the list to ensure we've done it correctly
print(year)

election_summary_data = {
    'Year' : year,
    'Registered_voters': [123298,137619,157022,170857,187485,204679,219379,253752,256097,268110,295581,284013,284253,292201,292653,308140,314832,304539,335173,377287,411071,439934,464673,430285,447727,450522,460244,461896,466553,483076,490408,525153,562630],
    'Voter_Turnout_Primary': [102274,94149,123321,111946,129677,124694,152557,151735,178729,189267,219379,196283,197904,153275,208640,201358,188640,172039,225406,199201,201583,189432,192146,184860,192322,167047,207461,206105,202728,169531,189421,275744,228522],
    'Voter_Turnout_General': [121999,136812,147728,161913,166187,183166,189812,220594,205903,234152,219584,234469,239970,258811,253470,270223,252621,272081,269121,261781,291114,257840,270071,300265,239753,308443,266266,298815,249436,291446,262700,385442,277194]

}

df = pd.DataFrame.from_dict(election_summary_data)
print(df)

 

plt.plot('Year','Voter_Turnout_Primary', data= df, label = 'Primary Elections')
plt.plot('Year','Voter_Turnout_General', data= df, label = 'General Elections')
plt.xticks(rotation = 90)
plt.legend()
plt.show()

 

#let's separate presidential and midterm elections by subsetting the df for every nth row and omitting the 1959 congressional election due to it's special circumstances. n = 2

presidential_elections = df.iloc[1::2]
midterm_elections = df.iloc[2::2]
print(presidential_elections)
print(midterm_elections)
plt.scatter(data = presidential_elections, x='Year', y='Voter_Turnout_General')
plt.show()


