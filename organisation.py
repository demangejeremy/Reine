# 
# Algorithme Reine
# By @DemangeJeremy
# 

# Importations NLTK
import nltk
from nltk.corpus import stopwords

# Téléchargement des stop-words
# nltk.download('stopwords')

# Importation de Spacy
import spacy

# Importations SK Learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# Importation 
from iramuteq_to_list import transform

# Réglages
LEM = True
NB_ARBRES = 4
NB_MOTS = 10
NB_ITERATIONS = 100
NB_INIT = 1
DOCUMENT_LINK = "./test/test2.txt"

# Mise en place des documents
# documents = ["This little kitty came to play when I was eating at a restaurant.",
#              "Merley has the best squooshy kitten belly.",
#              "Google Translate app is incredible.",
#              "If you open 100 tab in google you get a smiley face.",
#              "Best cat photo I've ever taken.",
#              "Climbing ninja cat.",
#              "Impressed with google map feedback.",
#              "Key promoter extension for Google Chrome."]

# documents = ["Pour apprendre le langage Python, il ne faut pas utiliser qu'une seule façon d'apprendre, mais pleins !",
#              "J'ai appris Python en autodidacte, seul.",
#              "Je préfère travailler et coder de nuit, je suis davantage productif !",
#              "Il y a de multiples façons pour apprendre la programmation, le tout, c'est de savoir bien chercher et d'être curieux !"]

# Document
documents = transform(DOCUMENT_LINK)

# Lire chaque texte
newDoc = []
if LEM:
  # Charger le français dans spacy
  nlp = spacy.load('fr_core_news_md')
  for d in documents:
    myText = ""
    tok = nlp(d)
    for t in tok:
      if t.is_alpha:
        myText += t.lemma_
        myText += " "
    newDoc.append(myText)
else:
  newDoc = documents


# Suppression des stops words
final_stopwords_list = stopwords.words('english') + stopwords.words('french')

# Vectorisation
vectorizer = TfidfVectorizer(stop_words=final_stopwords_list)
X = vectorizer.fit_transform(newDoc)

# Création des models
model = KMeans(n_clusters=NB_ARBRES, init='k-means++', max_iter=NB_ITERATIONS, n_init=NB_INIT)
model.fit(X)

# Affichage des résultats
print("Termes par arbres :")
print("")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(NB_ARBRES):
    print(f"Arbre {str(i+1)}:"),
    for ind in order_centroids[i, :NB_MOTS]:
        print('- %s' % terms[ind]),
    print("")
