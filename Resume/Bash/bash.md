# Script Bash .sh


## shebang
- indique que le script doit être interprété et exécuté en utilisant le shell Bash.

```bash
#!/bin/bash
```
## commentaire
- Les commentaires en Bash commencent par le symbole # et sont ignorés par l'interpréteur. Dans ce cas, cela semble être un espace réservé ou peut-être une faute de frappe.
# wasfasdf

## Echo
- Cette ligne utilise la commande echo pour afficher "Hello World" suivi de la valeur de la variable $USER (qui représente l'utilisateur actuel).
```bash
echo "Hello World" $USER
```
## Exit
- La commande exit est généralement utilisée pour quitter le script.
```bash
# exit
```

## -n pas de retour à la ligne
- L'option -n pour echo supprime le saut de ligne final, donc "Vive " et "Linux" seront imprimés sur la même ligne.
```bash
echo -n "Vive "
echo "Linux"
```

## -e
- -e permet d'interpréter les retours de ligne, etc. (\n \t)
```bash
echo -e "1\n2\n3"
```
L'option -e active l'interprétation des échappements avec un antislash, permettant l'utilisation de caractères spéciaux tels que \n pour un saut de ligne et \t pour une tabulation. Donc, cela imprime :
1
2
3

## Input
- poser une question à un utilisateur. Cette ligne utilise la commande read pour demander à l'utilisateur avec le message "Quel âge avez-vous ?" et stocke leur réponse.

```bash
read -p "Quel âge avez-vous? " age
```

## Variable
- Cette ligne affiche la valeur de $age suivie de la chaîne "vous êtes jeunes". 
```bash
echo $age "!vous etes jeunes"
```

# Variables en Bash

## Pour affecter une variable, il ne faut pas mettre d'espace

```bash
prenom=Benjamin
echo $prenom
```

## Declaration
- Pour affecter une variable, vous n'avez pas besoin de mettre d'espace autour du signe égal.
```bash
declare -i age=33
```

## declare
 est utilisée pour déclarer une variable entière age avec une valeur de 33. L'option -r avec declare crée une variable en lecture seule (constante) appelée CHEMIN avec la valeur "/bin".
```bash
# -r donne une constante
declare -r CHEMIN=/bin
```
## #0 
- La variable spéciale $0 donne le nom du premier script, c'est-à-dire le nom du script actuellement en cours d'exécution.
```bash
# $0 donne le premier script
echo "Nom script" $0
```
 # $#
- La variable spéciale $# donne le nombre de paramètres passés au script. Dans cet exemple, elle affiche le nombre de paramètres passés.
```bash
# $# veut dire combien on passe de paramètres
echo "Nombre params" $#
```

# calcules

- Une variable valeur est déclarée, et elle est initialisée avec le résultat de l'opération 10 + 10. Ensuite, la valeur de la variable est affichée avec echo.
```bash
valeur=$((10+10))
echo $valeur
```
## Input
- Les commandes read sont utilisées pour demander à l'utilisateur de saisir deux nombres (nb1 et nb2).
- L'option -p dans la commande read est utilisée pour spécifier un message d'invite (prompt) à afficher à l'utilisateur. Dans cet exemple, il sert à demander à l'utilisateur de saisir les nombres.
```bash
read -p "nb 1:" nb1
read -p "nb 2:" nb2
```
## Let
- La commande let est utilisée pour effectuer des calculs arithmétiques. Ici, le produit de nb1 et nb2 est stocké dans la variable resultat, puis affiché avec echo.
```bash
let resultat=$nb1*$nb2
echo $resultat
```
# Conditions

## pas d'espace dans les affectations
- Lors des affectations de variables, il ne faut pas mettre d'espace autour du signe égal.
```bash
note=75
```
## if
- Utilisation de la structure if pour évaluer des conditions.
```bash
if [[ note -lt 60 ]]
then 
    echo "Désolé... vous échouez"
elif test $note -eq 60
then
    echo "Ouf"
else
    echo "Beau travail!"
fi
```

## Input et Case
- La commande read est utilisée pour demander à l'utilisateur de saisir une lettre.
- Utilisation de la structure case pour évaluer différentes conditions basées sur la valeur de la lettre.
```bash
read -p "Entrez une lettre" lettre

case $lettre in 
    [[:lower:]])
    echo "La lettre est minuscule"
    ;;
    *)
    echo "Autre"
    ;;
esac
```
## Chaînes de caractères
- Lorsqu'on utilise des chaînes de caractères, on utilise la nomenclature de C++.
```bash
if [[ $lettre != "a" ]]
then
    echo "Différent de 'a'"
fi
```
# Boucles

## Boucle for
- Pas besoin du signe de dollar lors de l'utilisation de la variable `i`.
```bash
for((i=0;i<5;i++))
do 
    echo $i 
done 
```
## Backticks (``)
- Les backticks (``) permettent l'exécution d'une commande et de mettre le résultat dans une variable.
``` bash
liste=`ls`

for fichier in $liste
do
    echo $fichier
done
```

## Boucle while
- Les espaces sont importants dans la condition while.
```bash
resultat=o
while [[ $resultat = o ]]
do 
    read -p "choix : " resultat
done
```

## Déclaration d'un tableau
- L'option `-a` permet de déclarer un tableau. À l'indice 0, on a "The", et à l'indice 1, on a "Matrix".
```bash
declare -a film=("The" "Matrix")
echo ${film[0]}
echo ${film[1]}
echo "Nombre d'éléments:" ${#film[@]}
```
## Définition d'une fonction
```bash
maFonction(){

    echo "param: " $1
}
```
- La fonction maFonction est définie pour afficher le premier paramètre passé.

## Appels de fonction
```bash
maFonction "salut"
maFonction "toi"
```
- La fonction maFonction est appelée deux fois avec des paramètres différents ("salut" et "toi").


## Input avec `read`
```bash
read -p "Texte : " txt
```
- La commande read est utilisée pour demander à l'utilisateur de saisir du texte et le stocker dans la variable txt.
## Condition avec regex
```bash
if [[ $txt =~ ^[0-9]+$ ]]
then
    echo "Numérique"
fi
```
- Une condition est utilisée pour vérifier si le contenu de la variable txt correspond à un motif numérique. La regex ^[0-9]+$ vérifie si la chaîne est composée uniquement de chiffres.

## Vérification de l'existence d'un fichier

```bash
# -e fichier existe?
# -f c'est un fichier?
# -d c'est un dossier?
if [[ -e $1 ]]
then
    echo "Le fichier existe"
fi
```
- La condition utilise les options -e, -f, et -d pour vérifier différentes propriétés du fichier spécifié en tant que premier argument.