[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hgNAtOO3)

# Experimental Analysis of Biases in Large Language Models and Metrics

## Abstract

This paper examines the existence of biases in popular large language models as well as biases in popular evaluation metrics. It will specifically examine models and metrics created with the purpose of generating and evaluating summaries. The evaluations are done on the TL;DR dataset as it provides a large amount of text and summaries divided into 29 different categories. Comparisons were done on summaries from 5 different models which were evaluated using 5 different metrics. The results where compared across all different categories, and the summaries from categories that deviated from most from the mean were subjected to human evaluations and a case study. The study found several different biases including an omission bias towards texts where important aspects of the story only account for very small parts of the text. Additionally, an evaluation bias was found in the NOIR metric, as its focus on capturing semantic meaning of the original post, does not allow it to detect important missing details. Furthermore, a bias was found towards the topics of "BreakUps" and "offmychest", and a hallucination bias was found in the category of "tifu". In conclusion, the study uncovered several pitfalls that you must be aware of when choosing which methods to evaluate your summarization models as well as when choosing what summarization models to use.

## Contributions

The contribution of this paper is to provide crucial insights into the biases of commonly used LLMs. This knowledge will improve the use of these models by providing information on short comings of the different models. Additionally, it could help improving the models performance in general by showing the weaknesses of the models, and thereby providing a starting point for further training of the models. Furthermore, this paper contributes with information on biases in metrics which help researchers by choosing metrics that best fit their data type.

## Methods

The project will be evaluating 5 different models, which all have in common that they have a very high download rate on huggingface.co[2]. The 5 models are T5 small [4], Bart base [5], Pegasus [6], bart-large [3], and T5 Large [7]. The models will be evaluated on the following metrics: Rogue[8], BLEURT[9], NOIR[10], BERT-Score[11], BLEU[12]. The models will be evaluated on the TL;DR [1] dataset. This dataset consists of entries with a prompt and then a completion. The prompt is a text that must be summarized, and this prompt and it summarization have the same semantic information. Not all topics are represented equally in the dataset and to ensure equal representation of topics we will use 114 prompts from each topic, as this is the amount of topics in the least represented topic. We will be using the training part of the dataset in order to maximize the amount of data to evaluate the models on. Using the training part of the dataset is not causing problems as none of the models are trained on this dataset.
The dataset needs minimal preprocessing and the only real preprocessing needed is to devide the dataset into their respective subreddits. The information of which subreddit a post belongs to is provided as the first information in the prompt. Therefore, the dataset is divided by this provided label. All preprocessing needed for the individual model is handeled by the pipeline functionality of huggingface[1].
Additionally, the study will include a case study and a human evaluations of different examples for each of the models to provide an explanation of why the models/metrics have the biases that was found in the study.
In this study the type of biases that will be examined described by Z. Asimiyu [13], V. Reddy [14], and J. Steen and K. Markert [15]. They introduce multiple types of biases, one of which is omission bias which is where a model systematically exclude key facts or perspectives. Furthermore, hallucination bias where models starts creating summaries that are not supported by the input. In addition, biases such as metric blindness is introduced where metrics does not catch errors in certain subgroups of the data. A more comprehensive explanation of the term "bias" as it is used in this study can be found in the attached report.

## Timeline

For project milestone 2, we have started with evaluating the first 3 models listed above with the 3 first metrics listed there too. The goal is to prove that we can handle the amount of data, that we can display usable results, and that there exists biases in LLMs.

For project milestone 3, we will consider the rest of the models and the metrics. The goal is to make a complete analysis of biases in the models and the metrics. In case that the project has additional time available, we will extend the experiment with additional models and metrics. Additionally, in case of additional time we would like to extend the research by finetuning the models on the TL;DR dataset, and then evaluate the models again. The goal of this is to test the models for fundamental biases in the architecture of the models. The hope is that the architecture of some of the models as better suited for certain topics, and that we can unveil these biases by first finetuning the models to the data, and then seeing which biases remain.

We considered extending with different datasets to increase the amount of topics in the data, however, we have chosen to extend the experiments with more models and metrics in order to find biases in as many models and metrics as possible. However, if the project has a considerable amount of additional time, we will include different datasets in order to test the models for an extended amount of biases.

## Milestones

The miles stones of the project are:

- Run the analysis on the first 3 models.
- Evaluate the models on the first 3 metrics.
- Run the analysis on the rest of models and evaluate with the rest of the metrics.
- (If time permits) Extend the analysis with extra models and metrics.
- (If time permits) Fine tune models to test for more fundamental biases.
- (If time permits) Extend data with new datasets.
- Analyse results and do both the quantitative and case study analysis.

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

# Appendix

## Repository Organisation

main.ipynb ... most important model evaluations as well as the most important data analysis and case studies.
evals ... folder with results of preliminary evaluation run on 114 examples from each subreddit.
evaluations ... folder containing the final evaluations of all 114 examples from each subreddit.
case_studies ... folder containing the case studies which are the randomly chosen posts and their humanly annotated scores.
initial_statistics.ipynb ... the majority of the data analysis and the case study evaluations. Includes a large part of the content of main.ipynb, but includes extra information.
test_data, train_data, validation_data ... folders with subsets of our data
helper_funks.py ... helper functions needed for evaluation of the models, however, not a central part of the main logic.
The remaining files are mainly used for internal use and testing in the group.
summaries.csv ... posts, summaries and labels for all evaluated data points.
