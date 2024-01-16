#!/bin/bash

# La ligne suivante permet de v�rifier si un mot existe dans le dictionnaire
# Il faut suffixer cet URL avec le mot entr� par l'uasger (ex: word=chat)
#wget -qO - http://dictionary.objectif8.com/exists.php?word=

# demande a l<usager un mot 
# echo -n "entrez un mot"
# read mot

# verifier si le mot existe en utilisant lurl
# affichier a l ecran si le mot exite ou pas

read -p "Entrez un mot: " mot
resultat=`wget -qO - http://dictionary.objectif8.com/exists.php?word=$mot`


if [[ $resultat = 1 ]]
then 
    echo "le mot exist"

else
    echo "le mot exite pas"
fi