import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def distribution():
    ##testing_results = pd.read_csv('https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_timeline_testing.csv')
    confirmed_results = pd.read_csv('https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_timeline_confirmed.csv')
    
    trial = pd.notnull(confirmed_results["age"])

    ##attempt = pd.isnull(confirmed_results["age"])
    
    return(confirmed_results[trial].drop(columns=['case_id', 'YYYYMMDD','geo_subdivision']))

def  distribution_plot():
    confirmed_results = pd.read_csv('https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_timeline_confirmed.csv')
    trial = pd.notnull(confirmed_results["age"])
    ##attempt = pd.isnull(confirmed_results["age"])
    print('Enter the number of bins between 0 and 100')
    n_of_bins = input(str())
    print('Enter the number of xticks between 0 and 4')
    xticks =  input(str())
    plt.figure(figsize=(15,8)) #Set figure size
    plt.title('Distribution of Age of the COVID-19 Positive Cases in South Africa') #Set axis title
    plt.xticks(np.arange(confirmed_results[trial]['age'].min(), confirmed_results[trial]['age'].max(), step=4))  # Set label locations.

    plots = sns.distplot(confirmed_results[trial]['age'],
                 bins=int(n_of_bins),
                 kde=True,
                 rug=True) #"rug" will give the ticks on the x-axis
    print('The highest age of all COVID-19 patients is: ' + str(confirmed_results[trial]['age'].max()))
    
    return(plots)
    
def other_distributions():
    confirmed_results = pd.read_csv('https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_timeline_confirmed.csv')
    trial = pd.notnull(confirmed_results["age"])
    ##attempt = pd.isnull(confirmed_results["age"])
    plt.figure(figsize=(15,8)) #Set figure size
    plt.title('Countplot of the COVID-19 Positive Cases in each South African Province')

    sns.countplot(confirmed_results[trial]['province'],
                  order = confirmed_results[trial]['province'].value_counts().index,
                  palette='RdBu')
    plt.figure(figsize=(15,8)) #Set figure size
    plt.title('Gender difference of the COVID-19 in South Africa')

    sns.countplot(confirmed_results[trial]['gender'])
    print('Number of rows and columns in the dataframe: ' + str(confirmed_results[trial].shape)) #"shape" will give this tupple of rows and columns
    print('Number of rows: ' + str(confirmed_results[trial].shape[0])) #you can index a tuple like a list!
    confirmed_results[trial][['date', 'country']].groupby('date').count()
    confirmed_results[trial][['date', 'country']].groupby('date').count().cumsum().reset_index().rename(columns={'country':'cumulative sum'}) # "cumsum()" will give the cumulative sum
    plt.figure(figsize=(25,8)) #Set figure size
    plt.title('The Number of patients infected with the COVID-19 in South Africa')
    cumulative_cases = confirmed_results[trial][['date', 'country']].groupby('date').count().cumsum().reset_index().rename(columns={'country':'cumulative sum'}) #create cumulative dataframe

    ax = sns.lineplot(data=cumulative_cases, x='date', y='cumulative sum', 
                      marker='o', 
                      dashes=False)

    for i in cumulative_cases.groupby('date'):
        #i[1] is a grouped data frame; looping through each data row in the cumulative dataframe
        for x,y,m in i[1][['date','cumulative sum','cumulative sum']].values:  # x = x value; y = y_value ; m = marker value
            ax.text(x,y,f'{m:.0f}') #ax.text will 

    return(plt.show())

def overall_data():
    confirmed_results = pd.read_csv('https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_timeline_confirmed.csv')
    trial = pd.notnull(confirmed_results["age"])
    attempt = pd.isnull(confirmed_results["age"])
    cumulative_cases = confirmed_results[trial][['date', 'country']].groupby('date').count().cumsum().reset_index().rename(columns={'country':'cumulative sum'}) #create cumulative dataframe
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(35,10))

    graph1 = sns.distplot(confirmed_results[trial]['age'],
                 bins=20,
                 kde=True,
                 rug=True,
                 ax=ax[0,0])
    ax[0,0].title.set_text('Distribution of Age of the COVID-19 Positive Cases in South Africa')

    graph2 = sns.countplot(confirmed_results[trial]['province'],
                  order = confirmed_results[trial]['province'].value_counts().index,
                  palette='RdBu',
                  ax=ax[0,1])

    ax[0,1].title.set_text('Countplot of the COVID-19 Positive Cases in each South African Province')

    graph3 = sns.countplot(confirmed_results[trial]['gender'], ax=ax[1,0])

    ax[1,0].title.set_text('Gender difference of the patients infected with COVID-19 in South Africa')

    graph4 = sns.lineplot(data=cumulative_cases, x='date', y='cumulative sum', 
                      marker='o', 
                      dashes=False,
                      ax=ax[1,1])


    for i in cumulative_cases.groupby('date'):
        #i[1] is a grouped data frame; looping through each data row in the cumulative dataframe
        for x,y,m in i[1][['date','cumulative sum','cumulative sum']].values:  # x = x value; y = y_value ; m = marker value
            ax[1,1].text(x,y,f'{m:.0f}') #ax.text will 

    ax[1,1].title.set_text('The Number of patients infected with the COVID-19 in South Africa')
    ax[1,1].tick_params(labelrotation=45)

    print('Total Number of Cases without Null Values: ' + str(confirmed_results[trial].shape[0]))
    print('Total Number of Cases with Null Values: ' + str(confirmed_results[attempt].shape[0]))
    print('Total Number of Cases: ' + str(confirmed_results.shape[0]))
    
    return(graph1,graph2,graph3,graph4)