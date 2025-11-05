import pandas as pd
import altair as alt
import numpy as np

def show_me(source, my_title):
    return alt.Chart(source, title=my_title).mark_boxplot().encode(
        x='column',
        y='value',
        color='column'
        
    ).properties(width=800).interactive()
    
    
def show_me_more(source, my_title):
    bar = alt.Chart(source, title=my_title).mark_bar().encode(
    x=alt.X('Topics:N').sort(),
    y='amount:Q',
    tooltip='amount',
    color='amount'

    ).interactive()

    rule = alt.Chart(source).mark_rule(color='magenta').encode(
    y='mean(amount):Q'
    )
    return (bar + rule).properties(width=600)