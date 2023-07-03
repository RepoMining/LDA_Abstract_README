# Github README Spider

This script contains a program for crawling GitHub README files of specified repositories and clean the text data.


## Features

* Crawls the README file content of a given GitHub repository link.
* Clean data and save them in file.


## Usage

1. Install the required dependencies:

   ```python
   pip install BeautifulSoup
   pip install requests
   pip install nltk
   ```
2. Run the program:

   ```python
   save_readmes(urls, save_file_path)
   ```
3. Enter the GitHub repository links list you want to crawl.
4. The program will crawl the README files of the specified repository and save the content in 'save_file_path'.
5. Every five pieces of data will be saved once.

## Notes

* Make sure to provide a valid GitHub repository link with a publicly accessible README file.
* The program depends on the requests library, so ensure that it is installed.
