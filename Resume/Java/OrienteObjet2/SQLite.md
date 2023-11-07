# Introduction à SQLite:
- SQLite est une bibliothèque intégrée à Android permettant la création et la gestion de bases de données locales. Elle est particulièrement appréciée pour son interface SQL tout en nécessitant peu de ressources et en offrant une rapidité satisfaisante.

Comparaison SQLite vs Oracle:
Similitudes :
Commandes courantes : INSERT, CREATE TABLE, SELECT
Différences :
Typage des données : Dans SQLite, on peut stocker une valeur de n'importe quel type dans n'importe quelle colonne, indépendamment de son type déclaré.
Absence de certaines fonctionnalités avancées dans SQLite : par exemple, les contraintes de clé étrangères et les jointures externes.
Remarque: Android ne fournit aucune base de données par défaut. Il est donc nécessaire de créer la base de données et ses tables.

## Types de données dans SQLite:
1. INTEGER:
C'est un type de données utilisé pour stocker une valeur numérique entière. En fonction de la valeur, la taille du stockage peut varier de 1 à 8 octets.

- Booléens:
 SQLite n'a pas de type de données BOOLEAN distinct.
Au lieu de cela, les valeurs booléennes sont généralement stockées comme des entiers.
La valeur 0 est généralement utilisée pour représenter false, et 1 pour représenter true.

2. REAL:
Représente un nombre à virgule flottante, stocké sur 8 octets (équivalent à un double en Java ou en C++). C'est utile pour stocker des valeurs décimales comme 3.14, 0.001, etc.

3. TEXT:
Utilisé pour stocker du texte. En SQLite, les valeurs TEXT sont stockées en utilisant l'encodage UTF-8, UTF-16BE ou UTF-16LE, selon la manière dont la base de données est configurée.

4. NULL:
Une valeur spéciale qui représente une "absence de données". Elle est utile pour indiquer qu'une valeur particulière est inconnue ou non applicable.

### Index et clé primaire:
Dans SQLite, lorsqu'on déclare une colonne avec le type INTEGER PRIMARY KEY, elle est traitée comme une clé primaire auto-incrémentée, c'est-à-dire que chaque nouvelle entrée dans cette colonne reçoit une valeur qui est le maximum actuel + 1.

- AUTOINCREMENT : Si vous voulez garantir que SQLite n'utilise jamais des clés précédemment supprimées, ajoutez la clause AUTOINCREMENT. Cela rend l'insertion légèrement plus lente et plus grande car SQLite doit suivre les clés utilisées.

_id : De nombreuses bibliothèques et utilitaires Android (comme les CursorAdapter) s'attendent à ce qu'une colonne d'ID soit présente dans la base de données et soit nommée _id. Si votre table a une clé primaire ou un identifiant unique autre que _id, il peut être judicieux de créer un alias _id pour elle ou de l'appeler directement _id.

Exercice: Base de données des inventeurs:
Objectif: Construire une base de données comprenant une table Inventeur qui contiendra des informations sur certains inventeurs historiques. Cette table sera utilisée dans un quiz.

Étapes:
Classe Inventeur:

Créer une classe Inventeur pour modéliser les données.
Classe de gestion de la base de données:

Créer une sous-classe de SQLiteOpenHelper. Cette classe gérera la création, la mise à jour et les opérations sur la base de données.
Interaction avec la base de données via les activités:

Les activités vont interagir avec la base de données via la classe créée à l'étape 2.
### Singleton:
Un singleton est un patron de conception (design pattern) qui garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global à cette instance. Dans le contexte de SQLite, cela garantit une gestion centralisée et un accès uniforme à la base de données.

### Création et gestion de la base de données:
Méthodes importantes de la classe SQLiteDatabase:
execSQL: Utilisée pour les requêtes autres que INSERT ou SELECT (par exemple, CREATE TABLE).
insert: Pour insérer un enregistrement. Elle nécessite le nom de la table, null et un objet ContentValues contenant les données à insérer.
ContentValues fonctionne comme une Hashtable, où chaque paire clé-valeur représente un champ et sa valeur associée dans la table.

### Utilisation du Cursor:
Lorsqu'une requête est effectuée, le résultat est retourné sous forme d'un objet Cursor qui permet de parcourir les résultats.

Méthodes couramment utilisées avec Cursor:
moveToFirst(): Se positionne sur la première ligne du résultat.
moveToNext(): Passe à la ligne suivante.
isAfterLast(): Vérifie si le curseur est après la dernière ligne.
getInt(): Récupère la valeur d'un champ de type integer.

Introduction aux patrons de conception (Design Patterns):
Les patrons de conception sont des solutions éprouvées à des problèmes courants de conception rencontrés lors de la programmation. Ils offrent une structure réutilisable qui peut être adaptée à des situations spécifiques. Le but est d'offrir une solution robuste, optimale et réutilisable à des problématiques récurrentes.

## Le Modèle Singleton:
- Définition:
 Le Singleton est un patron de conception qui garantit qu'une classe n'a qu'une seule instance et offre un point d'accès global à cette instance. Il est utilisé lorsqu'on souhaite qu'un objet soit unique pour toute une application.

- Utilité:
Il est utilisé lorsque l'on a besoin d'un seul point de contrôle ou de coordination, comme une connexion à une base de données ou une interface de gestion de configuration.
Dans les applications Android, le Singleton est souvent utilisé en association avec des ressources système comme la connexion à une base de données SQLite.
Scénarios d'utilisation:
Jeu de stratégie militaire: Par exemple, il pourrait y avoir de nombreuses classes comme Avion, Artillerie, Soldat. Cependant, pour la classe PresidentEtatsUnis, il ne peut y avoir qu'un seul président à la fois. Ici, le Singleton garantit qu'il y a toujours un seul président.

- Pool de hockey: Alors qu'il peut y avoir de nombreuses instances pour des classes comme Participant, Joueur, pour la classe Pool qui regroupe les règles du pool (par exemple, un budget limité, un nombre limité de choix de gardiens), un Singleton serait approprié car il y a un seul ensemble de règles pour tout le projet.

- Singleton vs Classe Statique:
Bien que les deux concepts garantissent qu'il n'y ait qu'une seule instance, ils diffèrent dans leur utilisation et leurs avantages:

Interfaces et héritage: Un Singleton peut implémenter des interfaces et hériter d'autres classes, ce qui n'est pas le cas avec des classes entièrement statiques.

Variables: Un Singleton peut avoir à la fois des variables d'instance et des variables statiques, tandis qu'une classe statique ne peut avoir que des variables statiques.

Clonage: On peut cloner une instance Singleton, mais on ne peut pas cloner une classe statique.

Implémentation du Singleton en Java:
```java
public class GestionBD extends SQLiteOpenHelper {
    //instance unique de la classe Singleton GestionBD
    private static GestionBD instance;
    private SQLiteDatabase database;

    //pour limiter les risques que quelqu'un creer un autre objet de singleton
    //s'il y a en a deux le singleton n'a plus sa raison d'etre
    private GestionBD(Context context) {
        super(context, "biere", null, 1);

    }


    public static GestionBD getInstance(Context contexte) {
        if (instance == null)
            //si lìnstance est null alors je creer mon instence unique
            instance = new GestionBD(contexte);
        return instance;
    }

    //reste du code
}
```
Points importants:

Le constructeur est privé, ce qui empêche l'instanciation directe.

La méthode getInstance est synchronisée pour garantir que l'instance est créée une seule fois, même si plusieurs threads tentent d'y accéder simultanément.

L'utilisation du paramètre Context dans Android est courante car de nombreuses méthodes nécessitent un contexte. Cependant, lorsqu'on instancie le Singleton, il est recommandé d'utiliser getApplicationContext() pour éviter les fuites de mémoire.

### la méthode finish() dans Android:

Définition : La méthode finish() est utilisée pour terminer ou fermer l'activité actuelle.

Méthodes du cycle de vie :

- Lors de l'appel de finish(), les méthodes onPause(), onStop(), et finalement onDestroy() sont exécutées.
Ces méthodes permettent à l'activité de sauvegarder son état, d'arrêter les animations, de libérer des ressources, etc.
Pile d'activités (Back Stack) :

- L'activité est retirée de la pile d'activités de la tâche en cours.
Si l'activité en question est au sommet de la pile, l'activité précédente (s'il y en a une) redevient active.
Renvoi d'un résultat :

- Si l'activité a été lancée par une autre activité en utilisant startActivityForResult(), elle peut renvoyer un résultat à cette activité appelante avant d'être terminée.


example d'une classe bd
```java
public class GestionBD extends SQLiteOpenHelper {
    //instance unique de la classe Singleton GestionBD
    //dans ce cas Gestion bd peut etre remplacer par singleton instance
    private static GestionBD instance;
    private SQLiteDatabase database;

    //pour limiter les risques que quelqu'un creer un autre objet de singleton
    //s'il y a en a deux le singleton n'a plus sa raison d'etre
    private GestionBD(Context context) {
        super(context, "biere", null, 1);
    }
     // méthode de base pour un Singleton
   public static GestionBD getInstance(Context contexte) {
        if (instance == null)
            //si lìnstance est null alors je creer mon instence unique
            instance = new GestionBD(contexte);
        return instance;
    }
    // pour creer les tables et si necessaire ajouter les enregistrements/tuples initiaux
     //est appeler automatiquement une seule fois. soit lors de l'estalation de l'app sur le téléphone
    //si je fais une erreur de frappe dans le nom de la bd je dois delete le app dans l'emulateur et corriger la faute
        // si je  corrige la faute directement sa ne va pas marcher. Ou changer la version
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE biere(_id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT,microbrasserie TEXT,nbEtoiles REAL);");

        //pour populer nous meme la table
          ajouter(new Inventeur("Laszlo Biro", "Hongrie","Stylo à bille" 1938),db); 
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
    }
    public void ajouterBiere(Evaluation i){
        ContentValues cv = new ContentValues();
        cv.put("nom", i.getNom());
        cv.put("nbEtoiles",i.getEvaluation());
        cv.put("microbrasserie", i.getMicrobrasserie());
        database.insert("biere", null, cv);
    }
    public void ouvrireConnectionBd(){
        //tjrs mieux de faire cwritetable meme si on ne veut pas ecrire
        database = this.getWritableDatabase();
    }
    public void  fermerConnection(){
        database.close();
    }
    public Vector<String> retournerMeilleur(){
        Vector<String> v = new Vector<>();
        Cursor resultat = database.rawQuery("SELECT nom,microbrasserie, nbEtoiles  FROM biere ORDER BY nbEtoiles DESC LIMIT 3 ",null);
        //move to next va retourner faut si il y a rien apres, ne va jamais retourner null
        while (resultat.moveToNext()){
            //c'est a 0 car l,ensemble de resultat est slm une colonne sir on avait fait SELEct * il aurai fallu metre plus de paramettre selon la table
            v.add(resultat.getString(0));
        }
        //example
        String[] projection = {
                "nom",
                "microbrasserie",
                "nbEtoiles"
        };
        // Sort order
        String sortOrder = "nbEtoiles DESC";
        // Query the database
        Cursor resultat2 = database.query(
                "biere",      // The table to query
                projection,   // The columns to return
                null,         // The columns for the WHERE clause
                null,         // The values for the WHERE clause
                null,         // Group by
                null,         // Having
                sortOrder,    // Sort order dans une variable string ou direct en string
                "3"           // Limit
        );
        return v;
    }

    public boolean aBonneReponse(String nomInventeur, String invention){

        //toujours faire un tableau meme s'il y a un seul arguement
        //l'ordre est important
        String[] args = {nomInventeur,invention};

        //SELECT * FROM inventeur WHERE nom = nomInventeur AND invention = invention",
        //? pour des variable
        Cursor c = database.rawQuery("SELECT * FROM inventeur WHERE nom = ? AND invention = ?",args);

        //si retourne vrai on a trouver un tuple ou le nom et l'invention sont dans la la liste
        return c.moveToFirst();
    }
}
```