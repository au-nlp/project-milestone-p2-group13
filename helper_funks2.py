import pandas as pd
import altair as alt
import numpy as np

def show_me(source, my_title): # simple box plot
    return alt.Chart(source, title=my_title).mark_boxplot().encode(
        x='column',
        y='value',
        color='column'
        
    ).properties(width=800)
    
