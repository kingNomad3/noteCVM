# Introduction
- Les "Intents" sont un mécanisme fondamental dans le développement Android permettant la communication entre différents composants, notamment les activités. Ils peuvent être utilisés pour démarrer une nouvelle activité, démarrer un service, envoyer un message à un Broadcast Receiver, etc.

## 1. Création d'un Intent
Pour créer un nouvel Intent pour démarrer une activité, vous devez spécifier l'activité actuelle et l'activité que vous souhaitez démarrer.

Exemple :

```java
Intent i = new Intent(DepartActivity.this, ArriveeActivity.class);
```
- DepartActivity.this est le contexte, représentant l'activité actuelle.
- ArriveeActivity.class est l'activité que vous souhaitez démarrer.

## 2. Démarrage d'une activité avec un Intent
- Après avoir créé un Intent, vous pouvez utiliser la méthode startActivity() pour démarrer la nouvelle activité.

Exemple :

```java
startActivity(i);
```
## 3. Terminer une activité
- Si vous souhaitez fermer l'activité en cours et revenir à l'activité précédente (comme mentionné dans le bouton Enregistrer de la deuxième activité), utilisez la méthode finish().

Exemple :

```java
finish();
```
## 4. Passer des informations entre les activités
- Les Intents permettent également de passer des informations d'une activité à une autre.

#### 4.1. Pour envoyer des informations :
```java
i.putExtra("nom", ecric);
```
"nom" est la clé sous laquelle la donnée est stockée.
ecric est la donnée que vous souhaitez passer à la nouvelle activité.

### 4.2. Pour recevoir des informations :
```java
String data = getIntent().getStringExtra("nom");
```
- getIntent() récupère l'intention qui a démarré cette activité.
- getStringExtra("nom") récupère la donnée stockée sous la clé "nom".

## 5. Conclusion
Les "Intents" sont essentiels pour naviguer entre les activités et partager des données entre elles. Comprendre leur fonctionnement et leur utilisation est crucial pour tout développeur Android.

Exemple

```java
 private class Ecouteur implements AdapterView.OnClickListener{
    @Override
    public void onClick(View v) {
        if (v == Evaluation){
            Intent i = new Intent(MainActivity.this,AjouterActivity.class);
            startActivity(i);
        }else if (v == MeilleurBiere){
             Intent i = new Intent(MainActivity.this,MeilleurActivity.class);
            startActivity(i);
        }
    }
}
```
## Dialogue
- Lorsque vous êtes dans une classe Dialog (ou toute autre classe qui n'est pas directement une Activity), vous ne pouvez pas utiliser la référence this pour indiquer le contexte courant comme vous le feriez dans une Activity. Vous devez plutôt vous référer au contexte passé au dialogue.

Problème:
Vous avez utilisé le code suivant dans votre classe Dialog pour lancer une Activity:

```java
Intent i = new Intent(MenuAlert.this, MainActivity.class);
startActivity(i);
```
Solution:
Il faut remplacer ce code par :

```java
Intent i = new Intent(getContext(), MainActivity.class);
getContext().startActivity(i);
```
Explication:
- getContext() vous permet de récupérer le contexte qui a été transmis au dialogue.
Ensuite, vous utilisez ce contexte pour démarrer l'Activity.
C'est une erreur courante que de vouloir utiliser directement this dans des classes qui ne sont pas directement des Activity. Il faut toujours se rappeler d'utiliser le bon contexte.