[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hgNAtOO3)


# Experimental Analysis of Biases in Large Language Models and Metrics

## Abstract
This paper examines the possible existence of biases in commonly used LLMs and evaluation metrics for summarization. The goal of this paper is to broaden the understanding of commonly used LLMs by providing information on which topics the LLMs have an advantage or disadvantage when creating summarizations. This will help applications choose the best model for their type of data, as well as providing insights into what data the different models needs to be fine tuned with in order to have more well rounded LLMs. The models will be evaluated using different metrics in order to check for different types of biases the models have on the different topics. In addition, the study will examine the metrics for biases, in order to evaluate if the metrics have biases on any of the topics. This evaluation of the metrics will allow developers to avoid metrics that perform too poorly or too well on a specific type of data, and thereby getting a more accurate evaluation of the LLMs.

## Contributions
The contributions of this paper is to provide crucial insights into the biases of commonly used LLMs. This knowledge will improve the use of these models by providing information on short comings of the different models. Additionally, it could help improving the models performance in general by showing the weaknesses of the models, and thereby providing a starting point for further training of the models. Furthermore, this paper contributes information on biases in metrics which help researchers by choosing metrics that best fit their data type.

## Datasets
Do we need this section or is solely for additional datasets? I guess we could describe the TL;DR dataset and how we are going to use it. 

## Methods
The project will be evaluating 5 different models, which all have in common that they are have a very high download rate on huggingface.co[2]. The 5 models are bart-large [3], T5 small [4], Bart base [5], Pegasus [6], and T5 Small [7]. The models will be evaluated on the following metrics: Rogue[8], Cross-Entropy[9], GLUE[10], NOIR[11], BERT-Score[12]. The models will be evaluated on the TL;DR [1] dataset. This dataset consists of entries with a prompt and then a completion. The prompt is a text that must be summarized, and this prompt contains information of the 

## Timeline

## Milestones

## References
[1] https://huggingface.co/datasets/trl-lib/tldr
[2] https://huggingface.co/
[3] https://huggingface.co/facebook/bart-large-cnn
[4] https://huggingface.co/Falconsai/text_summarization
[5] https://huggingface.co/ainize/bart-base-cnn
[6] https://huggingface.co/google/pegasus-xsum    
[7] https://huggingface.co/google-t5/t5-small
[8] TODO
[9] TODO
[10] TODO
[11] TODO
[12] TODO

# Appendix
## Repository Organisation
## Questions for TAs
Optional


# Own Notes
We have two t5 small models which is probably not a very good idea