# Sérialisation d’objets


- Il faut creer le fichier "fichier.ser" dans le file explorer data, data, nom du projet dans files creer un nouveau dossier 
## avec un singleton
```java
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
```

```java 
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
```java
public class Groupe implements Serializable {
    String nomCours;
    int adresseImage;

    public Groupe(String nomCours, int adresseImage) {
        this.nomCours = nomCours;
        this.adresseImage = adresseImage;
    }

    public String getNomCours() {
        return nomCours;
    }

    public int getAdresseImage() {
        return adresseImage;
    }
```