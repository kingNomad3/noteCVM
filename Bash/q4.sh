#!/bin/bash

liste=`ls`
for fichier in $liste
do
    echo "le répertoire $0 contient le fichier $fichier"
done
