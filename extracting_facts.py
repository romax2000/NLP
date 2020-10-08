import spacy
import neuralcoref
import textacy.extract


# Загрузка английской NLP-модели
nlp = spacy.load('en')

neuralcoref.add_to_pipe(nlp)

# Текст для анализа
f = open('text.txt', 'r')
text = f.read()

# Анализ
doc = nlp(text)
print(doc._.coref_clusters[0])
print()

statements = []

# Извлечение полуструктурированных выражений с ключевыми словами
for cluster in set(doc._.coref_clusters[0]):
    statements += textacy.extract.semistructured_statements(doc, str(cluster))

print("Ford facts:")

for statement in set(statements):
    subject, verb, fact = statement
    print(f" - {fact}")
