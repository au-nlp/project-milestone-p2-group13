[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hgNAtOO3)

# Experimental Analysis of Biases in Large Language Models and Metrics

## Abstract

This paper examines the possible existence of biases in commonly used LLMs and evaluation metrics for summarization. The goal of this paper is to broaden the understanding of commonly used LLMs by providing information on which topics the LLMs have an advantage or disadvantage when creating summarizations. This will help applications choose the best model for their type of data, as well as providing insights into what data the different models needs to be fine tuned with in order to have more well rounded LLMs. The models will be evaluated using different metrics in order to check for different types of biases the models have on the different topics. In addition, the study will examine the metrics for biases, in order to evaluate if the metrics have biases on any of the topics. This evaluation of the metrics will allow developers to avoid metrics that perform too poorly or too well on a specific type of data, and thereby getting a more accurate evaluation of the LLMs.

## Contributions

The contribution of this paper is to provide crucial insights into the biases of commonly used LLMs. This knowledge will improve the use of these models by providing information on short comings of the different models. Additionally, it could help improving the models performance in general by showing the weaknesses of the models, and thereby providing a starting point for further training of the models. Furthermore, this paper contributes with information on biases in metrics which help researchers by choosing metrics that best fit their data type.

## Methods

The project will be evaluating 5 different models, which all have in common that they have a very high download rate on huggingface.co[2]. The 5 models are T5 small [4], Bart base [5], Pegasus [6], bart-large [3], and T5 Large [7]. The models will be evaluated on the following metrics: Rogue[8], BLEURT[9], NOIR[11], GLUE[10], BERT-Score[12], BLEU[13]. The models will be evaluated on the TL;DR [1] dataset. This dataset consists of entries with a prompt and then a completion. The prompt is a text that must be summarized, and this prompt and it summarization have the same semantic information. Not all topics are represented equally in the dataset and to ensure equal representation of topics we will use 114 prompts from each topic, as this is the amount of topics in the least represented topic. We will be using the training part of the dataset in order to maximize the amount of data to evaluate the models on. Using the training part of the dataset is not causing problems as none of the models are trained on this dataset.
The dataset needs minimal preprocessing and the only real preprocessing needed is to devide the dataset into their respective subreddits. The information of which subreddit a post belongs to is provided as the first information in the prompt. Therefore, the dataset is divided by this provided label. All preprocessing needed for the individual model is handeled by the pipeline functionality of huggingface[1].
Additionally, the study will include a case study of different examples for each of the models to provide an explanation of why the models/metrics have the biases that was found in the study.

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
[10] GLUE - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/glue. Seen oct 2025.
[11] Foland, Andrew D. “An Automated Length-Aware Quality Metric for Summarization”. arXiv:2507.07653, arXiv, 10. juli 2025. arXiv.org, https://doi.org/10.48550/arXiv.2507.07653.
[12] BERT Score - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/bertscore. Seen oct 2025.
[13] BLEU - a Hugging Face Space by evaluate-metric. https://huggingface.co/spaces/evaluate-metric/bleu. Seen oct 2025.

# Appendix

## Repository Organisation

main.ipynb ... our data analysis and preliminary model evaluation and metric analysis
evals ...folder with results of preliminary evaluation run on 114 examples from each subreddit
test_data, train_data, validation_data ... folders with subsets of our data
helper_funks.py ... helper functions needed for evaluation of the models, however, not a central part of the main logic.
The remaining files are mainly used for internal use and testing in the group.

## Questions for TAs

Under our Milestones, we have listed 3 items marked (if time permits). We would like to ask for advise about which of them should we focus on most, i.e. which one should we prioritize.

Note for TA: The visualizations are not rendered in github, but if you clone the repository and open them in Visual Studio Code the visuallizations are rendered without having to run the code. An extention to handle notebooks might be needed.

