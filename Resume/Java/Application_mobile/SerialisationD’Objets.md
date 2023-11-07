# Sérialisation d’objets
Nous avons vu à l’annexe 1 une façon de conserver des données au-delà de la fermeture de l’app, en utilisant des fichiers texte en mémoire interne
Certains problèmes existent avec cette façon :

•	Il n’y avait aucun modèle de donner dans notre application 

•	On ne pouvait que sauvegarder un mémo à la fois et on devait recréer les flux de données a chaque ajouts 

Pour résoudre le premier défi, on peut avoir recours à un Singleton de même qu’aux méthodes préétablies du cycle de vie d’une app Android 

![Resume\Java\Application_mobile\Stockage.m\cycleDeVie.png](cycleDeVie.png)

```java

