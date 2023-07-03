# Dataset: Abstract and README files

This dataset contains abstract and README files for various projects. The dataset is designed to provide researchers and developers with a collection of textual data that can be used for various natural language processing (NLP) tasks, such as text classification, summarization, and language modeling.


## Dataset Description

* Encoding: UTF-8
* Abstract dataset based from abstract_repos.json. [https://github.com/paperswithcode/paperswithcode-data](https://github.com/paperswithcode/paperswithcode-data)

## File Format

* abstract_corpus.json: Each row is a sample.
* abstract_doc_classes.json: Each sample is a key value pair with abstract as the key and task list as the value.
* github_urls.txt: a list of URLs for README files.
* readme_corpusa.json: Each row is a sample.

## Data Files

abstract_corpus.json: Preprocessed abstract text data.

readme_corpusa.json: Preprocessed README text data.


## Scripts

extract_data.ipynb: Extract urls from abstract_repos.json and save them.

abstract_corpus.ipynb: Preprocess the abstract data and save them as "abstract_corpus.json".
