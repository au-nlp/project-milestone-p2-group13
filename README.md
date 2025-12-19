[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hgNAtOO3)

# Experimental Analysis of Biases in Large Language Models and Metrics

## Abstract

This paper examines the existence of biases in popular large language models as well as biases in popular evaluation metrics. It will specifically examine models and metrics created with the purpose of generating and evaluating summaries. The evaluations are done on the Reddit TL;DR dataset as it provides a large amount of text and summaries divided into 29 different categories. Comparisons were done on summaries from 5 different models which were evaluated using 5 different metrics. The results where compared across all different categories, and the summaries from categories that deviated from most from the mean were subjected to human evaluations and a case study. The study found several different biases including an omission bias towards texts where important aspects of the story only account for very small parts of the text. Additionally, an evaluation bias was found in the NOIR metric, as its focus on capturing semantic meaning of the original post, does not allow it to detect important missing details. Furthermore, a bias was found towards the topics of "BreakUps" and "offmychest", and a hallucination bias was found in the category of "tifu". In conclusion, the study uncovered several pitfalls that you must be aware of when choosing which methods to evaluate your summarization models as well as when choosing what summarization models to use.

## Contributions

The contribution of this paper is to provide crucial insights into the biases of commonly used LLMs. This knowledge will improve the use of these models by providing information on short comings of the different models. Additionally, it could help improving the models performance in general by showing the weaknesses of the models, and thereby providing a starting point for further training of the models. Furthermore, this paper contributes with information on biases in metrics which help researchers by choosing metrics that best fit their data type.

## Methods

The project was evaluating 5 different models, which all have in common that they have a very high download rate on huggingface.co[2]. The 5 models are T5 small [4], Bart base [5], Pegasus [6], bart-large [3], and T5 Large [7]. The models weree evaluated on the following metrics: Rogue[8], BLEURT[9], NOIR[10], BERT-Score[11], BLEU[12]. The models will be evaluated on the TL;DR [1] dataset. This dataset consists of entries with a prompt and then a completion. The prompt is a text that must be summarized, and this prompt and it summarization have the same semantic information. Not all topics are represented equally in the dataset and to ensure equal representation of topics we used 114 prompts from each topic, as this is the amount of topics in the least represented topic. We were using the training part of the dataset in order to maximize the amount of data to evaluate the models on. Using the training part of the dataset did not cause problems as none of the models are trained on this dataset.
The dataset needed minimal preprocessing and the only real preprocessing needed was to devide the dataset into their respective subreddits. The information of which subreddit a post belongs to is provided as the first information in the prompt. Therefore, the dataset is divided by this provided label. All preprocessing needed for the individual model is handeled by the pipeline functionality of huggingface[1].
Additionally, the study included case studies with human evaluations of different examples for some of the models to provide an explanation of why the models/metrics have the biases that were found in the study.
In this study the type of biases that were examined described by Z. Asimiyu [13], V. Reddy [14], and J. Steen and K. Markert [15]. They introduce multiple types of biases, one of which is omission bias which is where a model systematically exclude key facts or perspectives. Furthermore, hallucination bias where models starts creating summaries that are not supported by the input. In addition, biases such as metric blindness is introduced where metrics does not catch errors in certain subgroups of the data. A more comprehensive explanation of the term "bias" as it is used in this study can be found in the attached report.

## Timeline

For project milestone 2, we started with evaluating the first 3 models listed above with the 3 first metrics listed there too. The goal was to prove that we can handle the amount of data, that we can display usable results, and that there exist biases in LLMs.

For project milestone 3, we have considered the rest of the models and the metrics. The goal was to make a complete analysis of biases in the models and the metrics. The goal of this was also to test the models for fundamental biases in the architecture of the models. The hope was that the architecture of some of the models as better suited for certain topics, and that we could unveil these biases by first finetuning the models to the data, and then seeing which biases remain.
However, we did not have time to look at the architecture level. Instead, we focused solely on analysing biases in the model-outputs and metrics.

## References

[1] trl-lib/tldr · Datasets at Hugging Face. 6. november 2025, https://huggingface.co/datasets/trl-lib/tldr.
[2] Hugging Face – The AI community building the future. https://huggingface.co/.
[3] facebook/bart-large-cnn · Hugging Face. 18. januar 2024, https://huggingface.co/facebook/bart-large-cnn.
[4] Falconsai/text_summarization · Hugging Face. https://huggingface.co/Falconsai/text_summarization. Seen oct 2025.
[5] ainize/bart-base-cnn · Hugging Face. 18. januar 2024, https://huggingface.co/ainize/bart-base-cnn.
[6] google/pegasus-large · Hugging Face. https://huggingface.co/google/pegasus-large. Seen oct 2025.
[7] google-t5/t5-large · Hugging Face. 5. marts 2024, https://huggingface.co/google-t5/t5-large.
[8] ROUGE - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/rouge. Seen oct 2025.
[9] BLEURT - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/bleurt. Seen oct 2025.
[10] Foland, Andrew D. “An Automated Length-Aware Quality Metric for Summarization”. arXiv:2507.07653, arXiv, 10. juli 2025. arXiv.org, https://doi.org/10.48550/arXiv.2507.07653.
[11] BERT Score - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/bertscore. Seen oct 2025.
[12] BLEU - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/bleu. Seen oct 2025.
[13] Zainab Asimiyu. Bias in personalized summarization: Risk, detection, and mitigation techniques, 06 2025. urlhttps://www.researchgate.net/publication/393357460 [Accessed: 09/12/2025].
[14] Vineeth Reddy. Bias taxonomy: A field guide to the hidden biases in ai systems every developer should know. https://huggingface.co/blog/Iceman20/bias-taxonomy [Accessed: 09/12/2025].
[15] Julius Steen and Katja Markert. Bias in news summarization: Measures, pitfalls and corpora, 2024.

# Contributions of team members

There has been no real distribution of the work. The team members have worked together, then divided some work, then worked together, then made a different division of some work, etc. such that all team members had a part in all aspects of the report.

# Repository Organisation

main.ipynb ... most important model evaluations as well as the most important data analysis and case studies.

main_copy_with_interactive_charts.ipynb ... our original main with our original interactive Altair charts - we had to save and show them them in a different way, because the interactive Altair charts cannot be rendered on GitHub directly.

evals_m2 ... folder with results of preliminary evaluation run on 114 examples from each subreddit used in Milestone 2.

evaluations ... folder containing the final evaluations of all 114 examples from each subreddit.

case_studies ... folder containing the case studies which are the randomly chosen posts and their humanly annotated scores.

diverse ... folder with files we have used during the process - mainly used for internal use and testing in the group.

plots ... folder used to safe images of plots so they can be displayed on GitHub.

test_data, train_data, validation_data ... folders with subsets of our data.

helper_funks.py ... helper functions needed for evaluation of the models, however, not a central part of the main logic.

summaries.csv ... posts, summaries and labels for all evaluated data points.
