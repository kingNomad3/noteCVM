#!/bin/bash



# -e fichier exist?
# -f c'est un fichier?
# -d c'est un dossier?


if [[ -e $1 ]]
then
    echo "le fichier existe"

else
    echo "Le fichier n'existe pas"
fi

if [[ -f $1 ]]
then
    echo "il existe c'est un fichier"
elif [[ -d $1 ]]
 then
    echo "il exist c'est un dossier"
fi