# 
# Setup Reine
# By @DemangeJeremy
# 

# Importations
import setuptools

# Lire le README
with open("README.md", "r") as fh:
    long_description = fh.read()

# Mise en place du setup
setuptools.setup(
     name='reine',  
     version='0.5',
     scripts=['reine'] ,
     author="Jérémy DEMANGE",
     author_email="jeremy@fakir.io",
     description="Classification automatisée et organisation interne du discours.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/demangejeremy/reine",
     install_requires=[
        'spacy', 'nltk', 'numpy', 'requests', 'click'
     ],
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)