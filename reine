# Importations
import click
import requests
import subprocess
import os
import ssl

# Import principale
from src.organisation import call_reine

# Application principale
@click.group()
def main():
    """
    Reine. Classification automatisée et organisation interne du discours.
    """
    pass

# Script principale
@main.command()
@click.argument('chemin_complet_du_fichier')
@click.option('--lemmatisation', '-lem', is_flag=True, help="Écrire ce paramètre s'il faut lemmatiser votre texte (prendra plus de temps en analyse).")
@click.option('--arbres', default=3, help='Nombre d\'arbres à générer.')
@click.option('--mots', default=8, help='Mots à afficher par arbres.')
@click.option('--iterations', default=100, help='Nombre d\'itérations de l\'algorithme.')
@click.option('--init', default=1, help='Nombre initialisateur.')
def classes(chemin_complet_du_fichier, lemmatisation, arbres, mots, iterations, init):
    """Générer les différentes classes du corpus."""
    if lemmatisation:
        call_reine(DOCUMENT_LINK = chemin_complet_du_fichier, LEM = True, NB_ARBRES = arbres, NB_MOTS = mots, NB_ITERATIONS = iterations, NB_INIT = init)
    else:
        call_reine(DOCUMENT_LINK = chemin_complet_du_fichier, LEM = False, NB_ARBRES = arbres, NB_MOTS = mots, NB_ITERATIONS = iterations, NB_INIT = init)


# Lancement de l'application
if __name__ == "__main__":
    main()