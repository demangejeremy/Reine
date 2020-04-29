# 
# Algorithme Reine
# By @DemangeJeremy
# 

# Importation des process
import subprocess
import sys

# Définition pour installation de package non installés
def install(package, arg = "-m"):
  subprocess.check_call([sys.executable, arg, "pip", "install", package])

# Importations NLTK
try:
  import nltk
except:
  try:
    install("nltk")
    import nltk
  except:
    print("Problème lors de l'installation de NLTK")
    print("Essayez de l'installer manuellement avec la commande suivante :")
    print("pip install nltk")
    raise
  pass

# Importation des stop-words
try:
  from nltk.corpus import stopwords
except:
  try:
    nltk.download('stopwords')
    from nltk.corpus import stopwords
  except:
    print("Problème lors de l'installation des stops-words")
    print("Essayez de l'installer manuellement avec la commande suivante :")
    print("nltk.download('stopwords')")
    raise
  pass

# Importations SK Learn
try:
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.cluster import KMeans
  from sklearn.metrics import adjusted_rand_score
except:
  try:
    install("scikit-learn")
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    from sklearn.metrics import adjusted_rand_score
  except:
    print("Problème lors de l'installation de la librairie sklearn")
    print("Essayez de l'installer manuellement avec la commande suivante :")
    print("pip install -U scikit-learn")
    raise
  pass

# Importation librairie locale
from src.iramuteq_to_list import transform

# Appel de la fonction principale
def call_reine(DOCUMENT_LINK = "./test/test2.txt", LEM = True, NB_ARBRES = 4, NB_MOTS = 10, NB_ITERATIONS = 100, NB_INIT = 1):
  # Exemple de mise en forme de document
  # 
  # documents = ["Ceci est un premier texte de corpus.",
  #              "Ici un deuxième texte de corpus",
  #              "Taille de la liste sans limite"]

  # Document mis en forme
  documents = transform(DOCUMENT_LINK)

  # Lire chaque texte
  newDoc = []
  # Si lematise
  if LEM:
    print("La programme est en cours d'exécution.")
    print("Cela peut prendre plusieurs minutes...")
    print("")
    # Importation de Spacy
    try:
      import spacy
    except:
      try:
        install("spaCy", "-U")
        import spacy
      except:
        print("Problème lors de l'installation de la librairie spacy")
        print("Essayez de l'installer manuellement avec la commande suivante :")
        print("pip install -U spaCy")
        raise
      pass
    # Charger le français dans spacy
    try:
      nlp = spacy.load('fr_core_news_md')
    except:
      try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "fr"])
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "fr_core_news_md"])
        nlp = spacy.load('fr_core_news_md')
      except:
        print("Problème lors de l'installation de la librairie spacy")
        print("Essayez de l'installer manuellement avec les commandes suivantes :")
        print("python -m spacy download fr")
        print("python -m spacy download fr_core_news_md")
        raise
      pass
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
  print("Termes par arbre :")
  print("")
  order_centroids = model.cluster_centers_.argsort()[:, ::-1]
  terms = vectorizer.get_feature_names()
  for i in range(NB_ARBRES):
      print(f"Arbre {str(i+1)}:"),
      for ind in order_centroids[i, :NB_MOTS]:
          print('- %s' % terms[ind]),
      print("")