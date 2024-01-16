#!/bin/bash

afficherMenu(){
    
      clear

    echo "Menu"
    echo "Si on tape la lettre q ou Q, quitter le programme (en sortant de la boucle)"
    echo "Si on tape la lettre a  ou A, afficher le contenu du répertoire /root"
    echo "Si on tape la lettre b ou B, afficher le contenu du fichier /etc/passwd."
    
    
}

while [[ $choix != q ]]

do 
  afficherMenu
  
read -p "choix : " choix
if [[ $choix = q || $choix = Q ]]
then
  exit
elif [[ $choix = a || $choix = A ]]
then
 ls /root
elif [[ $choix = B || $choix = B ]]
then
ls /etc/passwd
fi
sleep 2
  

done