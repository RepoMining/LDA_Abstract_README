from bs4 import BeautifulSoup
from nltk import PorterStemmer
from nltk.corpus import stopwords
import nltk
import string
import re
import requests


def readFile(path):
    with open(path) as f:
        lines = f.read()
    return lines


def get_readme_content(repo_url):
    # get the username and repo name in the url
    parts = repo_url.strip().split('/')
    username = parts[-2]
    repo_name = parts[-1]

    # build the url of README file
    readme_url = f"https://raw.githubusercontent.com/{username}/{repo_name}/master/README.md"
    try:
        # GET the README file
        response = requests.get(readme_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve README (status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None


def extract_text_from_readme(content):
    # only focuse on text
    text = re.sub(r'<.*?>', ' ', content)  # remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # remove non English char
    return text


def collapse_spaces(text):
    # remove multiply spaces
    collapsed_text = re.sub(r'\s+', ' ', text)
    return collapsed_text


def textPrecessing(text):
    # lower
    text = text.lower()
    # remove punctuation
    for c in string.punctuation:
        text = text.replace(c, ' ')
    # split words
    wordLst = nltk.word_tokenize(text)
    # remove stop words
    filtered = [w for w in wordLst if w not in stopwords.words('english')]
    # only keep noun
    refiltered = nltk.pos_tag(filtered)
    filtered = [w for w, pos in refiltered if pos.startswith('NN')]
    # stemmer
    ps = PorterStemmer()
    filtered = [ps.stem(w) for w in filtered]

    return " ".join(filtered)


def gen_data(content):
    docLst = []
    for desc in content:
        docLst.append(textPrecessing(desc).encode("utf-8"))
    return docLst


def save_data(docLst, path, mode="w"):
    with open(path, mode) as f:
        for line in docLst:
            f.write(line.decode("utf-8") + '\n')


def load_data(path):
    docLst = []
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            docLst.append(line)
    return docLst


def save_readmes(urls, path):
    readme_contents = []
    max_doc = 5
    doc = 0
    count = 1
    total = len(urls)
    error_urls = []
    docLst = []
    for url in urls:
        readme_content = get_readme_content(url)
        if not readme_content:
            error_urls.append(url)
            continue
        soup = BeautifulSoup(readme_content, 'html.parser')
        text = extract_text_from_readme(soup.get_text()).strip()
        text = collapse_spaces(text)
        readme_contents.append(text)
        docLst = gen_data(readme_contents)
        doc += 1
        if doc == max_doc:
            print("Saving", doc * count, "/", total, "README")
            count += 1
            save_data(docLst, path, "a")
            readme_contents = []
            docLst = []
            doc = 0
    if len(docLst) != 0:
        save_data(docLst, path, "a")
    return error_urls


def print_top_words(model, feature_names, n_top_words):
    """
    Print the top n most relevant words for each topic
    """
    tword = []
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        topic_w = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        tword.append(topic_w)
        print(topic_w)
    return tword