# Les expressions régulières

L'utilisation d'expressions régulières est une méthode puissante pour comparer des chaînes de caractères en utilisant des motifs correspondants.

Une expression régulière est une chaîne / modèle suivant les conventions ci-dessous :

## Modèles (pour un caractère ou un nombre)

- `[abc]`: a, b, ou c
- `[^abc]`: Tous les caractères sauf a, b, ou c (négation)
- `[a-zA-Z]`: a à z, ou A à Z (ensemble)
- `[a-d[m-p]]`: a à d, ou m à p : [a-dm-p] (union)
- `[a-z&&[def]]`: d, e, ou f (intersection)
- `[a-z&&[^bc]]`: a à z, sauf b et c : [ad-z] (soustraction)
- `[a-z&&[^m-p]]`: a à z, mais pas m à p : [a-lq-z] (soustraction)

## Modèles généraux (pour un caractère)

- `.`: Tout caractère n'importe quoi
- `\d`: Un chiffre : [0-9]
- `\D`: Tout sauf un chiffre : [^0-9]
- `\s`: Un caractère blanc : [ \t\n\x0B\f\r]
- `\S`: Tout sauf un caractère blanc : [^\s]
- `\w`: Un caractère (lettre ou chiffre) : [a-zA-Z_0-9]
- `\W`: Tout sauf un caractère (lettre ou chiffre) : [^\w]

## Multiplicateurs

- `X?`: X : 0 ou 1 fois seulement
- `X*`: X : 0 ou plusieurs fois
- `X+`: X : 1 ou plusieurs fois
- `X{n}`: X : exactement n fois
- `X{n,}`: X : au moins n fois
- `X{n,m}`: X : au moins n fois et au plus m fois

**Note:** En Java, le caractère `\` est un caractère d'échappement. Pour utiliser les modèles de caractères, on doit donc utiliser `\\`. On construit une chaîne composée des différents symboles ci-dessus et on compare la chaîne à vérifier (entrée par l’utilisateur) avec le modèle à l’aide de la méthode `matches`.

**Exemple:**

```java
String modele = "..\\d";
System.out.println("nana".matches(modele));  // false

String modele = "..\\d";
System.out.println("na9".matches(modele));  // true
```

# Les expressions régulières (Exercices de base + Pattern, Matcher)

## 1. Vrai ou Faux ?

A) `String un = "allo";` 
   `un.matches("\\d{4}");` 
   - Faux

B) `String deux = " dede";`
   `deux.matches("\\s{1,}[a-e]{2,5}");`
   - Vrai

C) `String trois = "343---";`
   `trois.matches("...\\w\\w\\w");`
   - Faux

D) `String quatre = "2222";`
   `quatre.matches("22");`
   - Faux

E) `String cinq = "sage";`
   `cinq.matches("\\s.{3}");`
   - Faux

F) `String six = "éric";`
   `six.matches("\\w{4}");`
   - Faux (à cause de l'accès sur le "é")

G) `String six = "éric";`
   `System.out.println(six.matches("[\\wé]{4}"));`
   - Vrai

H) Une expression régulière permettant de représenter tout matricule du collège ?
   - `\\d{7}`

I) Une expression régulière pouvant représenter n'importe quel nombre entier positif?
   - `[1-9][0-9]{0,}` ou `[1-9][0-9]*`    
   - Pour positif, négatif ou nul ? `[-]?` ou `-?` ou `-?[1-9]\\d*|0`

J) Une expression régulière pouvant contenir une lettre majuscule suivie de deux astérisques ?
   - `[A-Z]\\*{2}`

## 2. Classes Pattern, Matcher

Les trois principales classes du package `java.util.regex` :

- **Pattern:**
  - La classe Pattern représente une version compilée d’une expression régulière.
  - Elle n’a pas de constructeur; on crée un objet Pattern à l’aide de la méthode statique compile :
    ```java
    Pattern p = Pattern.compile("\\d{5}");
    ```

- **Matcher:**
  - La classe Matcher permet d’obtenir un objet qui interprétera le Pattern (l’expression régulière) et d'y appliquer des méthodes.
  - Comme Pattern, on ne peut pas créer un objet Matcher avec un constructeur, on doit utiliser la méthode matcher de la classe Pattern :
    ```java
    Matcher m = p.matcher("123456666633");
    ```

  - Méthodes à utiliser sur le Matcher : `matches`, `find`, `reset`
    ```java
    m.matches();  // faux car 123456666633 ne correspond pas à 5 chiffres
    m.find();     // vrai car tu peux trouver 5 chiffres dans 123456666633
    m.find();     // vrai car tu peux trouver 5 chiffres à la suite de l’autre 5 chiffres
    m.find();     // faux car il ne reste qu’un chiffre
    m.reset();    // retourne au début
    ```

- **PatternSyntaxException:**
  - Lancée lorsque la syntaxe de l’expression régulière n’est pas correcte.

## 3. Autres méthodes pour travailler avec une chaîne de caractères

- Méthode `split` de la classe String :
  ```java
  String[] tab = "asdf4pa4osi".split("\\d");
  for (int i = 0; i < tab.length; i++)
      System.out.println(tab[i]);
