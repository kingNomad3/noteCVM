# Android Studio : Notes sur le Stockage Interne

## Introduction

Dans Android, lorsqu'il s'agit de sauvegarder des données de manière persistante entre les sessions utilisateur sans utiliser une base de données complète, le stockage interne (notamment les fichiers) est une option efficace. Ces notes expliqueront comment gérer les données via les mécanismes de stockage interne d'Android.

## Stockage interne vs Stockage externe

- **Stockage interne:**
  - **Format:** 
    - `.xml` (SharedPreferences)
    - `.txt` (fichier texte)
  - **Accessibilité:** Seule l'application qui a créé le fichier y a accès.
  
- **Stockage externe:** 
  - **Avant SDK 29 / API 10:** Stockage sur stockage externe primaire ou secondaire (comme une carte SD). Nécessite des permissions dans `AndroidManifest.xml`.
  - **À partir de SDK 29 / API 10:** Introduit le "Scoped Storage", limitant la création de fichiers mais réduisant les permissions nécessaires.

## Les Flots de Données (Streams)

Un flot de données est une suite ordonnée d'infos provenant d'une source (`input stream`) ou allant vers une destination (`output stream`). Il y a deux catégories majeures :

- **Flots d'octets / binaires:** Pour les images, sons, ou sérialisation d'objets. 
  - Exemples: `FileInputStream`, `FileOutputStream`.
- **Flots de caractères:** Pour traiter des caractères. 
  - Exemples: `FileReader`, `FileWriter`.

## Importance des Buffers

Les buffers (tampons) régularisent l'accès aux données. L'usage d'un buffer empêche que chaque lecture ou écriture nécessite un accès direct au fichier.

**Points Clés :**
- **Flush:** Vide le buffer dans le fichier texte de destination.
- **Append:** Paramètre pour la méthode `openFileOutput`.

## Méthodes pour le stockage

### Android:

| En écriture                 | En lecture                       |
|-----------------------------|----------------------------------|
| `openFileOutput`            | `openFileInput`                  |
| `OutputStreamWriter`        | `InputStreamReader`              |
| `BufferedWriter`            | `BufferedReader`                 |

### Java Pur:

| En écriture                     | En lecture                           |
|---------------------------------|--------------------------------------|
| `new FileWriter` ou `new FileOutputStream` | `new FileReader` ou `new FileInputStream` |
| `BufferedWriter` ou `BufferedOutputStream`  | `BufferedReader` ou `BufferedInputStream` |

# Exemple
# Sauvegarde et Lecture d'un Mémo avec Android Studio

## Sauvegarde d'un mémo dans le stockage interne

### Étape 1: Demande de permissions
Assurez-vous d'avoir les permissions nécessaires dans votre fichier `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.WRITE_INTERNAL_STORAGE"/>
```
### Étape 2: Écrire dans un fichier
- Utilisez les méthodes fournies par Android pour écrire dans le stockage interne:
```java
String fileName = "memo.txt";
String content = "Ceci est un exemple de mémo.";
try {
    FileOutputStream fos = openFileOutput(fileName, Context.MODE_PRIVATE);
    OutputStreamWriter osw = new OutputStreamWriter(fos);
    BufferedWriter bw = new BufferedWriter(osw);
    bw.write(content);
    bw.close();
} catch (IOException e) {
    e.printStackTrace();
}
```
## Lecture d'un mémo du stockage interne
### Étape 1: Lire depuis un fichier
```java
String fileName = "memo.txt";
String content = "Ceci est un exemple de mémo.";
try {
    FileInputStream fis = openFileInput(fileName);
    InputStreamReader isr = new InputStreamReader(fis);
    BufferedReader br = new BufferedReader(isr);
    StringBuilder sb = new StringBuilder();
    String line;

    while ((line = br.readLine()) != null) {
        sb.append(line).append("\n");
    }

    String contentRead = sb.toString();
    // Utilisez contentRead comme vous le souhaitez
    br.close();

} catch (IOException e) {
    e.printStackTrace();
}
```

# Lecture et écriture de fichiers en Java

## Concepts Clés:

1. **Flux de Fichiers**: Java utilise `FileInputStream` et `FileOutputStream` pour lire et écrire des fichiers octet par octet.

2. **Lecteurs et Écrivains**: Pour lire et écrire des caractères, Java utilise `InputStreamReader` et `OutputStreamWriter` qui convertissent les octets en caractères et vice versa.

3. **Mise en mémoire tampon**: `BufferedReader` et `BufferedWriter` enveloppent les lecteurs et écrivains pour mettre en mémoire tampon l'entrée et la sortie, rendant l'opération plus efficace.

4. **Opérations sur les fichiers** :
   - **Lire des lignes**: Utilisation de `BufferedReader.readLine()` pour lire des lignes de texte d'un fichier.
   - **Écrire des lignes**: Utilisation de `BufferedWriter.write()` pour écrire des lignes de texte dans un fichier.
   - **Fermeture de flux**: Toujours fermer les flux avec `close()` pour libérer les ressources.

## flush

- Lorsque nous allons fermer la connection,".close " tout l'information qui sera stocker dans le buffer sera flusher dans le fichier txt. On peut appeler flush ".flush" tout seul si nous voulons pas fermer la conection 

![](Stockage.m\d1b4d588-92fb-5b2e-8a70-7b3121e3e9ce.svg)## Exemples de Code:


### Question A - Compter les lignes:
```java
   public long questionA(){
        String fileName = "file.txt";
        long nbligne =0;
        try {
            FileInputStream fis = openFileInput(fileName);
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            String line = br.readLine();
            while (line != null){
                nbligne++;
                line = br.readLine();
            }
            qa.setText(String.valueOf(nbligne));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return nbligne;
    }

```
###  Question B - Compter les caractères:
```java
 public long questionB(){
        String fileName = "file.txt";
        long caractere =0;
        try {
            FileInputStream fis = openFileInput(fileName);
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            String line;
            while ((line = br.readLine()) != null){
                caractere += line.length();
            }
            qb.setText(String.valueOf(caractere));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return caractere;
    }
```
### Question C - Compter les occurrences de 'c':
```java
public long questionC(){
        String fileName = "file.txt";
        long caractere =0;
        int c; // retourne est le caractere unicode du caractere lu
        try {
            FileInputStream fis = openFileInput(fileName);
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            while ((c = br.read()) != -1) { // Lire les caractères jusqu'à la fin du fichier (EOF)
                if ((char) c == 'c') { // Vérifier si le caractère est 'c'
                    caractere++; // Incrémenter le compteur si c'est 'c'
                }
            }
            // Supposons que qd est un composant d'interface utilisateur (TextView) qui doit être mis à jour dans le thread UI.
            qc.setText(String.valueOf(caractere));
        } catch (IOException e) {
            e.printStackTrace();
            // Gérer l'exception, éventuellement informer l'utilisateur
        }
        return caractere; // Retourner le compte de 'c'
    }
```
### Question D - Écrire dans un fichier:
```java
 public void questionD(){
        String nom = "Benjamin Joinvil";
        try {
            FileOutputStream fos = openFileOutput("file.txt", Context.MODE_APPEND); //append ecrit a la fin
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            BufferedWriter bw = new BufferedWriter(osw); // Toujours utiliser car plus efficace
            bw.newLine(); // Écrire une nouvelle ligne
            bw.write(nom); // Écrire le nom
            bw.flush(); // Assurez-vous que tout est écrit dans le fichier avant de fermer quand metter flush
        } catch (IOException fnfe) {
            fnfe.printStackTrace();
        }
    }
```
### Question E - Compter les mots avec Scanner:
```java
public int nbMotScanner(){
        String fileName = "file.txt";
        Scanner sc = null;
        int compteur = 0;

        try {
            FileInputStream fis = openFileInput(fileName);
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            String ligne = br.readLine();;
            while (ligne  != null) {
                sc = new Scanner(ligne);
                //Le delimiteur par defaut est un caractere blanc ( espace,\r ,\n etc)
                sc.useDelimiter("\\d"); // changer le delimiteur
                while (sc.hasNext()) {
                    sc.next();
                    compteur++;
                }
              ligne = br.readLine();
            }
            qd.setText(String.valueOf(compteur));
        }catch (IOException e){
            e.printStackTrace();
        }
            return compteur;
    }
```

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Vector<String> lines = new Vector<>();
        try {
            lines = readLines();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Vector<String> readLines() throws Exception {
        Vector<String> lines = new Vector<>();
        String line;
        FileInputStream fis = null;

        fis = openFileInput("coordonees.txt");
        InputStreamReader isr = new InputStreamReader(fis);
        BufferedReader br = new BufferedReader(isr);

        line = br.readLine();
        while(line != null) {
            lines.add(line);
            line = br.readLine();
        }

        fermerFlux(br);
        return lines;
    }

    public void fermerFlux (BufferedReader br){
        try {
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```java
 private class Ecouteur implements AdapterView.OnItemSelectedListener
    {

        @Override
        public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
            ObjectOutputStream oos;
            index = position;
            if (firstEntry == false){
                try{
                    groupeSelect = liste[position];
                    FileOutputStream fos = openFileOutput("fichier.ser", Context.MODE_PRIVATE);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(groupeSelect);
                    oos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            setImage();
            firstEntry = false;
        }

        @Override
        public void onNothingSelected(AdapterView<?> parent) {

        }
    }
```
