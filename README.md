# About
## Topic modeling using supervised learning
Text classification on topics:
- politics
- economics
- sport

### Naive bayes algorithm
https://www.geeksforgeeks.org/naive-bayes-classifiers/

Naive bayes algorithm - probabilistic model. Простыми словами считает кол-во слов в тексте и выдает частотность его встречаемости в тексте

| documents collection/terms | football | money | elections | label     |
|----------------------------|----------|-------|-----------|-----------|
| doc 1                      | 3        | 2     | 1         | sport     |
| doc 2                      | 0        | 1     | 0         | economics |
| doc 3                      | 1        | 0     | 3         | politics  |
| total count                | 4        | 3     | 4         |           |

P(sport) = (3|4)
P(economics) = (3|2)
P(politics) = (4|3)

Для supervised learning важно labeled data
Чтобы избежать underfloat number в вероятностях, берется log для вероятностей

input -> model

# 🚀 Getting started

1. **Установка зависимостей**
```
poetry install
```
2. **Запуск проекта**
```
poetry run python __init__.py
```

### Download spacy model
```shell
poetry add https://github.com/explosion/spacy-models/releases/download/ru_core_news_sm-3.5.0/ru_core_news_sm-3.5.0-py3-none-any.whl
```