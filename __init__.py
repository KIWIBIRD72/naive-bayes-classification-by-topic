from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from rich import inspect
import logging
from rich.logging import RichHandler
from rich.traceback import install
import click
from os.path import abspath
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import spacy

# Logging
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])]
)
log = logging.getLogger("rich")
install(show_locals=True)

# init model
model = MultinomialNB(fit_prior=False)
nlp = spacy.load("ru_core_news_sm")


def spacy_preprocessor(text):
    doc = nlp(text)
    return " ".join([
        token.lemma_              # use the lemmatized form
        for token in doc
        if not token.is_stop      # exclude stop words
        and not token.is_punct    # exclude punctuation
    ])


# import dataset. 10085 entries
dataset_path = abspath(
    'assets/topic modeling supervised/pravda_first_semester_2024.tsv')
df = pd.read_csv(dataset_path, sep="\t")

df['section'].value_counts()

# Labels
features = df['headline']

# vectorize
vectorizer = TfidfVectorizer(
    preprocessor=spacy_preprocessor)  # could be any vectorizer
dtm = vectorizer.fit_transform(features)

# prepare data for training model
X = dtm
y = df['section']
test_size = 0.3         # 30% of the data is reserved for testing purposes.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42)

# train model
model.fit(X_train, y_train)

# predictions
pred = model.predict(X)

# testing predictions
new_pred = model.predict(X_test)
inspect(new_pred)

# classification report
print(classification_report(y_test, new_pred, digits=4))

# confusion matrix
cm = confusion_matrix(y_test, new_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()
