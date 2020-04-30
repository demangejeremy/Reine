# 
# Algorithme Reine
# By @DemangeJeremy
# 

# Importation des process
import subprocess
import sys

# Importations SK Learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# Importation librairie locale
from iramuteq_to_list import transform


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

  # Info 
  i = 1

  # Si lematise
  if LEM:
    # Charger spacy
    import spacy
    # Charger le français dans spacy
    print("Chargement du dictionnaire...")
    nlp = spacy.load('fr_core_news_md')
    for d in documents:
      print(f"Lecture du corpus {str(i)} / {str(len(documents))}")
      i += 1
      myText = ""
      tok = nlp(d)
      for t in tok:
        if t.is_alpha:
          myText += t.lemma_
          myText += " "
      newDoc.append(myText)
  else:
    # Charger spacy
    import spacy
    # Charger le français dans spacy
    print("Chargement du dictionnaire...")
    nlp = spacy.load('fr_core_news_md')
    for d in documents:
      print(f"Lecture du corpus {str(i)} / {str(len(documents))}")
      i += 1
      myText = ""
      tok = nlp(d)
      for t in tok:
        if t.is_alpha:
          myText += t.text
          myText += " "
      newDoc.append(myText)
    newDoc = documents


  # Suppression des stops words
  final_stopwords_list = ["a","à","â","abord","afin","ah","ai","aie","ainsi","allaient","allo","allô","allons","après","assez","attendu","au","aucun","aucune","aujourd","aujourd\u0027hui","auquel","aura","auront","aussi","autre","autres","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","ayant","b","bah","beaucoup","bien","bigre","boum","bravo","brrr","c","ça","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chaque","cher","chère","chères","chers","chez","chiche","chut","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","delà","depuis","derrière","des","dès","désormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","différent","différente","différentes","différents","dire","divers","diverse","diverses","dix","dix-huit","dixième","dix-neuf","dix-sept","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","e","effet","eh","elle","elle-même","elles","elles-mêmes","en","encore","entre","envers","environ","es","ès","est","et","etant","étaient","étais","était","étant","etc","été","etre","être","eu","euh","eux","eux-mêmes","excepté","f","façon","fais","faisaient","faisant","fait","feront","fi","flac","floc","font","g","gens","h","ha","hé","hein","hélas","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","i","il","ils","importe","j","je","jusqu","jusque","k","l","la","là","laquelle","las","le","lequel","les","lès","lesquelles","lesquels","leur","leurs","longtemps","lorsque","lui","lui-même","m","ma","maint","mais","malgré","me","même","mêmes","merci","mes","mien","mienne","miennes","miens","mille","mince","moi","moi-même","moins","mon","moyennant","n","na","ne","néanmoins","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notre","nôtre","nôtres","nous","nous-mêmes","nul","o","o|","ô","oh","ohé","olé","ollé","on","ont","onze","onzième","ore","ou","où","ouf","ouias","oust","ouste","outre","p","paf","pan","par","parmi","partant","particulier","particulière","particulièrement","pas","passé","pendant","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","plein","plouf","plus","plusieurs","plutôt","pouah","pour","pourquoi","premier","première","premièrement","près","proche","psitt","puisque","q","qu","quand","quant","quanta","quant-à-soi","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","revoici","revoilà","rien","s","sa","sacrebleu","sans","sapristi","sauf","se","seize","selon","sept","septième","sera","seront","ses","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","stop","suis","suivant","sur","surtout","t","ta","tac","tant","te","té","tel","telle","tellement","telles","tels","tenant","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutes","treize","trente","très","trois","troisième","troisièmement","trop","tsoin","tsouin","tu","u","un","une","unes","uns","v","va","vais","vas","vé","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vôtre","vôtres","vous","vous-mêmes","vu","w","x","y","z","zut","alors","aucuns","bon","devrait","dos","droite","début","essai","faites","fois","force","haut","ici","juste","maintenant","mine","mot","nommés","nouveaux","parce","parole","personnes","pièce","plupart","seulement","soyez","sujet","tandis","valeur","voie","voient","état","étions"]

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
  myTerms = []

  # Générer le cluster
  order_centroids = model.cluster_centers_.argsort()[:, ::-1]
  terms = vectorizer.get_feature_names()

  # Réalisation de la loop
  for i in range(NB_ARBRES):
    print(f"Arbre {str(i+1)}:")
    for ind in order_centroids[i, :NB_MOTS]:
      print('- %s' % terms[ind])
      myTerms.append(terms[ind])
    saveTerms.append(myTerms)
    myTerms = []
    print("")

  # Générer le HTML
  generate_html(saveTerms, DOCUMENT_LINK)


# Appel de la fonction
call_reine(DOCUMENT_LINK = "/Users/jeremydemange/Documents/GitHub/Reine/test/output_1.txt", LEM = True, NB_ARBRES = 6, NB_MOTS = 10, NB_ITERATIONS = 100, NB_INIT = 1)