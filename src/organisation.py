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


# Générer un HTML
def generate_html(terms, doclink):

  # Lien sauvegarde
  doclink = doclink.replace(".txt", "_classes.html")

  # Code pour ajout
  codeAdd = """
      <li>
        <a href="#" class="bl">Résultats</a>
        <ul>
  """

  # Itération
  it = 1

  # Lire les termes
  for t in terms:

    # Ajout du titre
    codeAdd += f""" 
          <li>
            <a href="#">Classe {str(it)}</a>
            <ul>
              <li>
                <a href="#">
    """

    # Itérer le résultat
    it += 1

    # Ajouter les termes
    for x in t:
      codeAdd += f"- {x}<br><br>"

    # Ajout
    codeAdd += """
      </a>
              </li>
            </ul>
          </li>
    """


  # Code HTML
  html = """
  <!DOCTYPE html>
  <html lang="fr" >
  <head>
    <meta charset="UTF-8">
    <title>Résultat</title>
    <style>
    * {
      margin: 0; 
      padding: 0; 
      font-size: 35px;
    }

    .tree ul {
      padding-top: 20px; position: relative;
      
      transition: all 0.5s;
      -webkit-transition: all 0.5s;
      -moz-transition: all 0.5s;
    }

    .tree li {
      float: left; text-align: center;
      list-style-type: none;
      position: relative;
      padding: 20px 5px 0 5px;
      
      transition: all 0.5s;
      -webkit-transition: all 0.5s;
      -moz-transition: all 0.5s;
    }

    .tree li::before, .tree li::after{
      content: '';
      position: absolute; top: 0; right: 50%;
      border-top: 1px solid #ccc;
      width: 50%; height: 20px;
    }
    .tree li::after{
      right: auto; left: 50%;
      border-left: 1px solid #ccc;
    }

    .tree li:only-child::after, .tree li:only-child::before {
      display: none;
    }

    .tree li:only-child{ padding-top: 0;}

    .tree li:first-child::before, .tree li:last-child::after{
      border: 0 none;
    }

    .tree li:last-child::before{
      border-right: 1px solid #ccc;
      border-radius: 0 5px 0 0;
      -webkit-border-radius: 0 5px 0 0;
      -moz-border-radius: 0 5px 0 0;
    }
    .tree li:first-child::after{
      border-radius: 5px 0 0 0;
      -webkit-border-radius: 5px 0 0 0;
      -moz-border-radius: 5px 0 0 0;
    }

    .tree ul ul::before{
      content: '';
      position: absolute; top: 0; left: 50%;
      border-left: 1px solid #ccc;
      width: 0; height: 20px;
    }

    .tree li a{
      border: 1px solid #ccc;
      padding: 5px 10px;
      text-decoration: none;
      color: #666;
      font-family: arial, verdana, tahoma;
      font-size: 11px;
      display: inline-block;
      
      border-radius: 5px;
      -webkit-border-radius: 5px;
      -moz-border-radius: 5px;
      
      transition: all 0.5s;
      -webkit-transition: all 0.5s;
      -moz-transition: all 0.5s;
    }

    .tree li a:hover, .tree li a:hover+ul li a {
      background: #c8e4f8; color: #000; border: 1px solid #94a0b4;
    }

    .tree li a:hover+ul li::after, 
    .tree li a:hover+ul li::before, 
    .tree li a:hover+ul::before, 
    .tree li a:hover+ul ul::before{
      border-color:  #94a0b4;
    }

    .bl {
      background-color: black;
      color: white !important;
    }

    .bl:hover {
      background-color: black !important;
      color: white !important;	
    }

    </style>
  </head>
  <body>
  <div class="tree">
    <ul>""" + codeAdd + """


        </ul>
      </li>
    </ul>
  </div>  
  </body>
  </html>
  """

  # Sauvegarde 
  with open(doclink, 'w') as myFile:
    myFile.write(html)

  # Retourner la réponse
  return html


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
  print("DEBUG")
  print("Termes par arbre :")
  print("")

  # Variables de sauvegardes
  saveTerms = []
  terms = []

  # Générer le cluster
  order_centroids = model.cluster_centers_.argsort()[:, ::-1]
  terms = vectorizer.get_feature_names()

  # Réalisation de la loop
  for i in range(NB_ARBRES):
    print(f"Arbre {str(i+1)}:")
    for ind in order_centroids[i, :NB_MOTS]:
      print('- %s' % terms[ind])
      terms.append(terms[ind])
    saveTerms.append(terms)
    terms = []
    print("")

  # Générer le HTML
  generate_html(saveTerms, DOCUMENT_LINK)


# Appel de la fonction
#call_reine(DOCUMENT_LINK = "./test/test2.txt", LEM = True, NB_ARBRES = 4, NB_MOTS = 10, NB_ITERATIONS = 100, NB_INIT = 1)
