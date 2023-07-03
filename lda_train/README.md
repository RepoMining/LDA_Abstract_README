# LDA Training Scripts for Abstract and README

There are two scripts for training Latent Dirichlet Allocation (LDA) models on abstract and README data. These scripts are designed to facilitate topic modeling and analysis of textual data.

## Abstract LDA Training

The `abstract_LDA.ipynb` script is specifically designed to train an LDA model on abstract data. It takes as input a corpus of abstract documents and generates a topic model that can uncover underlying themes in the abstracts. The trained LDA model can be used for various tasks, such as topic visualization, document clustering, and topic inference.

To train an LDA model on abstract data, follow these steps:

1. Prepare the abstract data: The data from `../data/abstract_corpus.txt`.
2. Install the necessary Python libraries installed, such as `sklearn` and `joblib`.
3. Run the `abstract_LDA.py` script. Extracted 100 keywords for training. The parameters are:

   ```
   max_iter=100000, learning_method="batch", learning_offset=50, n_jobs=-1, doc_topic_prior=0.04163183877389392,
                                           n_components=n_t, topic_word_prior=0.04911253614440047
   ```
4. A total of 4 models were trained and saved in  `../abstract_model`.

## README files LDA Training

The `readme_LDA.ipynb` script is specifically designed to train an LDA model on README data. It takes as input a corpus of README documents and generates a topic model that can uncover underlying themes in the github repository.

To train an LDA model on README data, follow these steps:

1. Prepare the abstract data: The data from `../data/readme_corpus.txt`.
2. Install the necessary Python libraries installed, such as `sklearn` and `joblib`.
3. Run the `readme_LDA.py` script. Extracted 150 keywords for training. The parameters are:

   ```
   max_iter=100000, learning_method="batch", learning_offset=50, n_jobs=-1, doc_topic_prior=0.04163183877389392,
                                           n_components=n_t, topic_word_prior=0.04911253614440047
   ```
4. A total of 7 models were trained and saved in  `../readme_model`.

## Dependencies

Both scripts require the following dependencies:

* Python 3.x
* `sklearn` library for LDA model training
* `nltk` library for text preprocessing and tokenization
