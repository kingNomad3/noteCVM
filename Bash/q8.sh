#!/bin/bash


read -p "Entrez un chiffre: " chiffre1
read -p "Entrez un chiffre: " chiffre2

let resultat=$chiffre1+$chiffre2
echo $resultat