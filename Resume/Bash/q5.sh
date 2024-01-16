#!/bin/bash

i=0

while [[ $i -le 5 ]]
do 
mkdir echo "Dossier $i"
echo "création du sous répertoire $i"
let i++
done