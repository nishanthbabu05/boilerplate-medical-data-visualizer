import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight']= df['weight']/((df['height']/100)**2)
df.loc[df['overweight']<=25,'overweight']=df.loc[df['overweight']<=25,'overweight']*0 
df.loc[df['overweight']>25,'overweight']=(df.loc[df['overweight']>25,'overweight']*0)+1
df['overweight']=df['overweight'].astype(int)
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df=df.replace({
    'cholesterol': {
        1: 0
        
    },
    'gluc': {
        1: 0
    }
})
df.loc[df['cholesterol']>0,'cholesterol']=(df.loc[df['cholesterol']>0,'cholesterol']*0)+1
df.loc[df['gluc']>0,'gluc']=(df.loc[df['gluc']>0,'gluc']*0)+1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat=pd.melt(df, id_vars =['cardio'],value_vars =['active','alco','cholesterol','gluc','overweight','smoke'])
    
    


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
   #

    # Draw the catplot with 'sns.catplot()'
    g=sns.catplot(x='variable',hue="value",col="cardio",kind="count",data=df_cat)
    g.set_axis_labels("variable", "total")
    fig = g.fig
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[(df['ap_lo'] <= df['ap_hi'])&(df['height'] >=df['height'].quantile(0.025))&(df['height'] <= df['height'].quantile(0.975))&(df['weight'] >= df['weight'].quantile(0.025))&(df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 10))
    

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, linewidths=.5, vmin = -.16, vmax = .32, fmt=".1f", center=0)



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
