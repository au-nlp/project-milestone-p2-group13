import pandas as pd
import altair as alt
import numpy as np

def show_me(source):
    return alt.Chart(source, title="ainize_bleurtScores.csv").mark_boxplot().encode(
        x='column',
        y='value',
        color='column'
        
    ).properties(width=800).interactive()