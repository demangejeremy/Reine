<div align="center"><h1>Reine<br>👸</h1><br>Classification automatisée et organisation interne du discours.</div>
<br>

## Installation

Sur votre machine, installez au préalable une version supérieure ou égale à 3.6 de Python. Ensuite, lancez la commande suivante sur votre machine :

```
pip install reine
```

## Mise à jour

Veillez à mettre à jour régulièrement la librairie en lançant la commande suivante :

```
pip install --upgrade reine
```

## Utilisation

En ligne de commande avec la commande **reine**. 
```
$ reine 
Usage: reine [OPTIONS] COMMAND [ARGS]...

  Reine. Classification automatisée et organisation interne du discours.

Options:
  --help  Show this message and exit.

Commands:
  classes  Générer les différentes classes du corpus.
```
Seule la commande `classes` a été implémenté.
```
$ reine classes --help
Usage: reine classes [OPTIONS] CHEMIN_COMPLET_DU_FICHIER

  Générer les différentes classes du corpus.

Options:
  -lem, --lemmatisation  Écrire ce paramètre s'il faut lemmatiser votre texte
                         (prendra plus de temps en analyse).

  --arbres INTEGER       Nombre d'arbres à générer.
  --mots INTEGER         Mots à afficher par arbres.
  --iterations INTEGER   Nombre d'itérations de l'algorithme.
  --init INTEGER         Nombre initialisateur.
  --help                 Show this message and exit.
```

```
$ reine classes ./moncorpus.txt
```
cette commande génére en sortie l'affichages des classes de l'arbre dans le terminal et un fichier html représentant l'arbre `./moncorpus_classes.html`
## Crédits 

Développé par Jérémy DEMANGE et inspiré par le logiciel Alceste et par la méthode Reinert inclus par Pierre Ratinaud dans Iramuteq, cette librairie se veut entièrement portée sur Python pour une utilisation plus simple et plus performante.
