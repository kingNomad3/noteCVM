# Sérialisation d’objets
Nous avons vu à l’annexe 1 une façon de conserver des données au-delà de la fermeture de l’app, en utilisant des fichiers texte en mémoire interne
Certains problèmes existent avec cette façon :

•	Il n’y avait aucun modèle de donner dans notre application 

•	On ne pouvait que sauvegarder un mémo à la fois et on devait recréer les flux de données a chaque ajouts 

Pour résoudre le premier défi, on peut avoir recours à un Singleton de même qu’aux méthodes préétablies du cycle de vie d’une app Android 

![Resume\Java\Application_mobile\Stockage.m\cycleDeVie.png](cycleDeVie.png)

## 1. Introduction :
   - La sérialisation est le processus de conversion de l'état d'un objet en un flux d'octets.
   - En Java, elle permet de sauvegarder des objets et de les reconstruire ultérieurement.

## 2. Problèmes liés au stockage dans des fichiers texte :
   - Problèmes :
     - Absence d'un modèle de données dans l'application.
     - Limitation à la sauvegarde d'un seul mémo à la fois, avec la nécessité de recréer les flux de données pour chaque ajout.

## 3. Implémentation du Singleton :
   - Utiliser un modèle Singleton pour une instance partagée.
   - Variable d'instance : `ArrayList<String>` pour stocker les mémos.
   - Utiliser les méthodes du cycle de vie de l'activité Android pour une gestion appropriée.
     - Référence : [Cycle de vie des activités Android](https://developer.android.com/guide/components/activities/activity-lifecycle), [Article Medium](https://medium.com/@theabhishekavi/android-activity-lifecycle-9bc7de812dff)

## 4. Opérations locales sur l'ArrayList :
   - Implémenter des opérations pour ajouter et afficher des mémos localement (sans persistance).
   - Travailler avec l'ArrayList pour gérer les données en mémoire.

## 5. Sérialisation des objets :
   - Objectif : Conserver l'état de l'objet dans un fichier de sérialisation binaire (`.ser`) pour une conservation à long terme.
   - Ce qui peut être sérialisé :
     - Objets des bibliothèques standard : S'assurer que la classe implémente l'interface `Serializable`.
     - Objets de classes personnalisées : Implémenter `Serializable` et s'assurer que toutes les variables sont sérialisables.
       - Exemple : `public class Maison implements Serializable`

## 6. Sauvegarde de l'état dans un fichier de sérialisation :
   - Dans le Singleton :
     - Implémenter une méthode pour sauvegarder l'état de l'ArrayList dans un fichier de sérialisation binaire (`.ser`).

## Exemple de singleton
```java
//pas besoin de extends seriazable dans la classe car le array liste est deja seriazable
    public void seriazableListe(){ // throws Exception
        //On n;a pas acces a open file output car nous sommes dans une classe normal et non une activite alors on utilise le context
        //ici on va utiliser mode private car mode append va garder l'ancienne liste ici on veut ecraser la vielle et mettre la nouvelle (avec les anciens memo)
        try (
            FileOutputStream fos = context.openFileOutput("fichier.ser", Context.MODE_PRIVATE);
            //buffer special pour les objets
            ObjectOutputStream oos = new ObjectOutputStream(fos)
            )
        {
            oos.writeObject(liste);

        }catch (Exception o){
            o.printStackTrace();
        }
    }
public ArrayList<String> deSeriazableListe() {
        try (
            FileInputStream fis = context.openFileInput("fichier.ser");
            //buffer special pour les objets
            ObjectInputStream ois = new ObjectInputStream(fis))
        {
            liste = (ArrayList<String>) ois.readObject();

        }catch (Exception o){
            o.printStackTrace();
        }
        return liste;
    }
```

## Est-ce qu'un SeekBar est sérialisable ? non

À l'aide du processus de sérialisation, faites en sorte qu'on puisse retrouver les mêmes valeurs pour les SeekBars quand on redémarre l'app suite à une fermeture par le bouton back ou autre..

```java
   protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        seekbarSonnerie = findViewById(R.id.seekBarSonnerie);
        seekBarMedia = findViewById(R.id.seekBarMedia);
        seekBarNotif = findViewById(R.id.seekBarNotif);



        //deserialisation
        try{
            ObjectInputStream ios= null;
            FileInputStream fos = openFileInput("fichier.ser");

            ios = new ObjectInputStream(fos);

            seekBarMedia.setProgress((int)ios.readObject());
            seekBarNotif.setProgress((int)ios.readObject());
            seekbarSonnerie.setProgress((int)ios.readObject());


        }catch (ClassNotFoundException | IOException fnfe){
            fnfe.printStackTrace();
        }

    }

  protected void onStop() {
        super.onStop();

        //serialisation
        try(
            FileOutputStream fos = openFileOutput("fichier.ser",Context.MODE_PRIVATE);
            ObjectOutputStream oos = new ObjectOutputStream(fos)){

            oos.writeObject(seekBarMedia.getProgress());
            oos.writeObject(seekBarNotif.getProgress());
            oos.writeObject(seekbarSonnerie.getProgress());

        }catch (Exception e){
            e.printStackTrace();
        }
```
