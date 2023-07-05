# LDA_Abstract_README

This repository contains a collection of scripts, dataset and tools for LDA model for Abstract topics and README topics.

## Requirements

```
nltk~=3.7
requests~=2.31.0
bs4~=0.0.1
beautifulsoup4~=4.10.0
```

## Features

* **LDA Training and Prediction** : Train and predict topics using Latent Dirichlet Allocation (LDA) models.Two scripts are available: `abstract_LDA.py` for training LDA on abstract data and `readme_lda.LDApy` for training LDA on README data. Two scripts are available: `abstract_predict.py` for predict distributions and topics of abstract data and `readme_predict.LDApy` for predict distributions and topics of README data.
* **LDA Visualization** : Visualize LDA topics and their associated keywords using interactive visualizations with the help of the `pyLDAvis` library.
* **Text Preprocessing** : Perform text preprocessing tasks such as tokenization, stop word removal, stemming, and more using the `nltk` library.
* **Data Extraction** : Extract text data from github README files.

## Getting Started

To get started with the Textual Analysis Toolbox, follow these steps:

1. **Clone the Repository** : Clone this repository to your local machine using the following command:

```
git clone https://github.com/PythonSimilarity/LDA_Abstract_README.git
```

2. **Install Dependencies** : Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## directory

`./abstract_model` and `./readme_model`: These two directories store the trained LDA models.

`./utils`: This directory contains preprocessing methods and web scraping scripts.

`./crawler`: Start the crawler to crawl the README files in Github.

`./lda_predict`: Prediction and visualization of two LDA models.

`./lda_train`: Train two LDA models.

`data`: All data to train LDA models.

## Examples and Documentation

The repository includes examples and documentation for each script and tool. Please refer to the individual script files and the accompanying documentation for detailed instructions on usage, customization, and examples.
