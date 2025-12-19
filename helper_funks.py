import pandas as pd
import altair as alt
import numpy as np

def show_me(source, my_title): # simple box plot
    return alt.Chart(source, title=my_title).mark_boxplot().encode(
        x='column',
        y='value',
        color='column'
        
    ).properties(width=800).interactive()
    
    
def show_me_more(source, my_title, my_color, reverse_color=True): # bar chart with line showing average
    bar = alt.Chart(source, title=my_title).mark_bar().encode(
    x=alt.X('Topics:N').sort(),
    y='amount:Q',
    tooltip='amount',
    color=alt.Color('amount').scale(scheme=my_color, reverse=reverse_color)
    ).interactive()

    rule = alt.Chart(source).mark_rule(color='magenta').encode(
    y='mean(amount):Q'
    )
    return (bar + rule).properties(width=600)


# This is the NOIR metric which has been retreived from the repository https://github.com/afoland/NOIR
# (C) Andrew Foland, Sonnetiq, 2024; license granted under Apache 2.0
import torch
from transformers import AutoModel, AutoTokenizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(vector1, vector2):
    # Calculate cosine similarity between two vectors
    return cosine_similarity([vector1], [vector2])[0][0]

def embed_string(text, model, tokenizer):
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)
    with torch.no_grad():
        embedding = model(input_ids).last_hidden_state.mean(dim=1).squeeze().tolist()
    return embedding

noir_model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
noir_tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
def NOIR(text, summary):
    text_embedding = embed_string(text, noir_model, noir_tokenizer)
    summary_embedding = embed_string(summary, noir_model, noir_tokenizer)
    D = calculate_cosine_similarity(text_embedding, summary_embedding)

    text_length = len(noir_tokenizer.encode(text))
    summary_length = len(noir_tokenizer.encode(summary))
    k = summary_length / text_length

    sque_metric = np.log(k) / np.log(D)
    return sque_metric


import time
import evaluate

#Load the rouge and bleurt metric for evaluation.
rouge = evaluate.load("rouge")
bleurt = evaluate.load("bleurt", module_type="metric")
bertscore = evaluate.load("bertscore")
bleu = evaluate.load("bleu")

#Compute the NOIR, bleurt and rouge scores for the given pipeline.
def compute_evaluation_scores(df):
  noirScores = []
  
  #Get the prompts and the labels of the given subreddit.
  prompts = df['prompt']
  labels = df['label']
  generatedTexts = df['summary']

  #Compute the NOIR score for each summary
  for prompt, generatedText in zip(prompts, generatedTexts):    
    noirScore = NOIR(prompt, generatedText)
    noirScores.append(noirScore)
  
  #Compute the BLEURT score for each summary
  bleurtScore = bleurt.compute(predictions=generatedTexts, references=labels)['scores']

  #Compute the average ROUGE-1, ROUGE-2, ROUGE-L and ROUGE-Lsum for the generated summaries.
  rougeScore = rouge.compute(predictions=generatedTexts, references=labels, use_aggregator=False)['rouge1']
  
  #Compute the BERT Score for each summary
  bertScore = bertscore.compute(predictions=generatedTexts, references=labels, lang='en')['precision']
  
  #Compute the BLEU Score for each summary
  bleuScores = []
  for generatedText, label in zip(generatedTexts, labels):
    bleuScore = bleu.compute(predictions=[generatedText], references=[label])['bleu']
    bleuScores.append(bleuScore)

  return noirScores, bleurtScore, rougeScore, bertScore, bleuScores