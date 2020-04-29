# 
# Algorithme Reine
# By @DemangeJeremy
# 

# Fonction transformation du texte iramuteq
def transform(lien_fichier):
    with open(lien_fichier, "r") as fh:
        get_text = fh.read()
        decoupage = get_text.split("****")
        newDecoupage = []
        for i in decoupage:
            # Remove si ce n'est pas un symbole ci-dessous.
            # "^a-zA-Z0-9àÀâÂäÄáÁåÅãéÉèÈêÊëËìÌîÎïÏíÍóÓòÒôÔöÖõÕøØùÙûÛüÜúÚçÇßœŒ’ñÑ.:,;!?'_-"
            newDecoupage.append(" ".join(filter(lambda x:x[0]!='*', i.split())))
        return newDecoupage
    return []