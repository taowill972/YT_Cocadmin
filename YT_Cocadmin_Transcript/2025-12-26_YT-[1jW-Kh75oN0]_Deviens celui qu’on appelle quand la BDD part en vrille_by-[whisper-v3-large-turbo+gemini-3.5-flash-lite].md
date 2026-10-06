# 🎬 Deviens celui qu’on appelle quand la BDD part en vrille

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=1jW-Kh75oN0](https://www.youtube.com/watch?v=1jW-Kh75oN0)  
> **Date de publication** : 20251226  
> **Durée** : 00:16:52  
> **Identifiant vidéo** : `1jW-Kh75oN0`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Deviens celui qu’on appelle quand la BDD part en vrille**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Linux & Outils Systèmes** : Administration système, automatisation et surveillance.
- **Conteneurisation & Cloud** : Déploiement et gestion d'environnements résilients.

### 🔑 Points Clés & Enseignements Stratégiques
- Maîtriser les fondamentaux réseau et système pour diagnostiquer efficacement les pannes.
- Privilégier les architectures simples et observables en environnement de production.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:27]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Les bases de données c'est toujours ce qui est le plus difficile à scaler dans une application, mais je vais te donner une douzaine de techniques qui vont choquer ton équipe quand tu vas les mettre en place. La première chose à faire si notre base de données commence à saturer un petit peu, elle reçoit trop de requêtes, c'est simplement de lui envoyer moins de requêtes. Et une des meilleures façons de faire ça, c'est en dehors de la base de données, dans notre application ici, si on a notre application ici qui envoie des requêtes à notre base de données, ce qu'on peut faire c'est mettre en place un CDN pour Content Delivery Network, et ça va être un service que tu vas venir mettre devant ton application, et qui va être répliqué à travers le monde.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:27 - 00:00:55]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est pour ça que c'est un network, parce qu'en fait, c'est plein de machines qui sont un petit peu partout. Et ce qui va se passer, c'est que tes utilisateurs, au lieu d'aller taper directement ton serveur, ils vont aller taper ce delivery network. Et la machine qu'ils vont taper, elle va être proche du CSEU, donc du coup, ça va être plus rapide. Et ensuite, cette machine-là, elle va venir taper son serveur qui va venir faire la requête. Mais ça, c'est la première fois. La seconde fois qu'un utilisateur va venir faire une requête, comme le CDN, il a déjà la réponse, parce que pour la plupart des pages, elles ne vont pas changer toutes les 5 minutes, et bien le CDN peut directement répondre à ton utilisateur, sans même avoir demandé à ton serveur, et donc du coup, sans même avoir à faire une requête de base de données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:56 - 00:01:17]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc juste avec ça, on peut déjà drastiquement diminuer la charge sur ta base de données. Donc on peut servir beaucoup plus d'utilisateurs sans même devoir toucher à notre base de données. Ensuite, si même avec ça, ta base de données est toujours super lente à répondre, ce qu'il va falloir faire, c'est mesurer qu'est-ce qui la rend lente exactement. Donc premièrement, on va devoir définir qu'est-ce qu'on veut dire par lent. Parce que suivant le service, suivant l'application, peut-être qu'une seconde, ça peut être rapide, mais ça peut être aussi super lent.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:17 - 00:01:37]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc ça, dans le jargon, on appelle ça une SLO pour Service Level Objectif. Ça va être notre objectif en interne pour pouvoir dire, « Ok, ça c'est lent et ça c'est rapide. » Par exemple, en tant qu'équipe, on va décider que notre base de données, c'est bien si dans 95% des temps, elle répond en dessous de 200 millisecondes. On appelle ça le P95. On peut aussi parfois utiliser le P90, P99, ça dépend un petit peu de ce qu'on a besoin.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:38 - 00:01:57]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Une fois qu'on a fait ça, on va pouvoir configurer un slow log. Ça veut dire que dans ma base de données, je vais aller la configurer pour lui dire « À partir de maintenant, toutes les requêtes qui prennent plus qu'un certain temps, tu vas me les enregistrer dans un log. » Ça va simplement être un fichier de log qui va contenir les requêtes qui ont été faites par quel utilisateur, sur quelle base de données et combien de temps elles ont pris. Comme ça, on peut de temps en temps aller voir dans ce fichier, voir qu'est-ce qui prend du temps.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:57 - 00:02:19]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et comme ça, c'est ça qu'on peut pouvoir optimiser. Ça ne sert à rien d'optimiser des requêtes qui sont déjà rapides. Comme ça, ça permet de se concentrer sur les plus lentes en premier. Maintenant qu'on sait lesquelles sont les plus lentes, on va pouvoir savoir comment les optimiser. Et donc, si par exemple, dans ma base de données, imaginons une application à un système de blog et donc du coup, j'ai des utilisateurs et j'ai des posts. On peut fausser des articles ou des commentaires. Et j'ai remarqué que quand je fais une requête pour pouvoir récupérer ces posts, c'est à ce moment là que c'est long.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:19 - 00:02:41]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que peut-être que j'ai beaucoup de postes ou que j'ai beaucoup d'utilisateurs ou les deux. Je vais pouvoir créer un index ici. Et cet index, en fait, c'est comme une table secondaire qui va directement garder la liste des postes pour chaque utilisateur. Comme ça, quand je demande l'utilisateur 42, je sais directement, sans aller chercher nulle part dans la base de données, la liste de tous les postes qu'il a fait. Parce que sans ça, j'ai ma liste d'utilisateurs et j'ai ma liste de postes qui sont dans deux tables séparées.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:41 - 00:03:14]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et si je n'ai pas cet index-là, il faut que je regarde tous les postes un par un pour savoir si le propriétaire de ce poste c'est l'utilisateur numéro 42 ou pas. Donc je dois passer à travers tout. Mais avec un index j'ai directement la liste donc c'est mille fois plus rapide. Mais on peut encore aller plus loin. On peut faire ce qu'on appelle des covering index et ça va être le même concept des index sauf que au lieu de faire ça pour juste les id des utilisateurs on va aussi sauvegarder dans cette table secondaire le titre et le contenu du poste. Ce qui fait que quand je vais demander la liste des postes pour l'utilisateur numéro 42 non seulement j'ai la liste de tous les postes qui ont été créés par l'utilisateur 42 mais en plus de ça, dans les postes, ça va contenir le titre et le corps directement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:15 - 00:03:34]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc la base de données, elle n'a pas besoin d'aller faire une sous-requête secondaire pour aller chercher tout ce qu'elle a besoin. Tout est déjà là dans l'index. Et si dans nos requêtes qu'on fait à nos bases de données, on demande à ordonner les résultats, par exemple les trier par ordre de création, s'il y a beaucoup de résultats, c'est quelque chose qui peut prendre beaucoup de temps dans la base de données parce qu'une fois qu'elle a récupéré toutes les infos, il faut qu'ensuite elle les regarde un par un pour pouvoir les mettre dans le bon ordre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:34 - 00:03:58]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc encore une fois, à la création de notre index, on peut aussi spécifier un ordre. Comme ça quand on va demander la liste des postes créés par l'utilisateur 42, non seulement je les ai déjà, mais ils sont déjà triés par ordre de création. Donc ma base de données n'a aucun travail à faire, elle a juste d'apprendre et me renvoyer la réponse. En plus de ça, une bonne pratique quand on réorganise la liste des postes, c'est de mettre une limite. Comme ça ma base de données n'a pas besoin de récupérer toute la liste et de tout réordonner l'ordre des articles pour qu'ensuite moi j'en affiche juste les 10 premiers.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:58 - 00:04:30]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Autant directement dans ma requête, dire combien j'en ai besoin, et comme ça ma base de données a moins de travail à faire. Maintenant que j'ai ajouté mes index, si ça ne suffit toujours pas, un petit gain facile que je peux avoir, c'est l'ajout d'un pooler. Et le pooler, ce qu'il va faire, c'est qu'il va agréger toutes les connexions. Parce que si chaque requête de mes utilisateurs génère une connexion à ma base de données, et que chacun de mes différents serveurs, parce que si j'ai besoin de scaler, souvent, je vais avoir beaucoup de serveurs devant ma base de données, se connecte individuellement à ma base de données, chaque connexion consomme un petit peu de mémoire. Et si on a beaucoup de serveurs, beaucoup de requêtes, beaucoup de connexions, ce petit peu de mémoire se multiplie jusqu'à ce qu'on consomme beaucoup de mémoire sur notre base de données. Et cette mémoire-là,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:30 - 00:04:49]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> c'est la mémoire qu'on aurait pu utiliser pour pouvoir mettre des informations en cache, répondre plus rapidement aux setters, et donc potentiellement ça ralentit un petit peu ma base de données. Donc le fait de rajouter cette étape intermédiaire ici, notre puller, lui, va se connecter à la base de données, il va maintenir juste un petit nombre de connexions à la base de données, juste assez pour pouvoir faire plusieurs requêtes en même temps, et tous mes serveurs ici, ils vont se connecter à mon puller.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:49 - 00:05:07]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Comme ça, la mémoire qui est utilisée pour pouvoir maintenir la connexion ouverte, elle est prise par le puller, et elle n'est pas prise dans la base de données, et donc la base de données peut respirer un petit peu. Maintenant, si même ça, ça ne suffit toujours pas, tu continues à recevoir un max de requêtes malgré avoir mis les index, etc. Ça continue à être lent parce que tu as vraiment trop de charges, trop d'utilisateurs, trop de serveurs. Ce que je te souhaite, évidemment.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:07 - 00:05:26]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ce qu'il va falloir faire maintenant, c'est optimiser les requêtes. Parce que jusqu'à présent, on a juste optimisé le côté de la base de données. Et l'exemple ici, ça serait, imaginons, je récupère une liste d'utilisateurs, un certain nombre d'utilisateurs. Donc ça ici, ça va générer une requête qui va en retourner plusieurs utilisateurs. Jusque là, c'est pas trop grave. Et ensuite, pour chacun de ces utilisateurs, je vais faire la requête pour pouvoir récupérer la liste de ces posts.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:26 - 00:05:45]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais si j'ai 1000 utilisateurs que je récupère, je vais faire 1000 requêtes à ma base de données. Et donc ça va être un long va-et-vient entre mon serveur applicatif et ma base de données. Et comme on passe par le réseau à chaque fois, même si c'est le réseau interne, c'est 2-3 millisecondes qui s'ajoutent à chaque fois, à chaque fois, à chaque fois, à chaque fois. Et si on le fait 1000 fois, c'est direct 2 secondes qui s'ajoutent au temps de réponse de mon application. Et là du coup, on est beaucoup plus loin que les 200 millisecondes qu'on avait décidé à départ.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:46 - 00:06:12]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> À la place, ce que je pourrais faire, c'est utiliser une jointure. Et donc en fait, je fais faire une seule requête qui effectivement va récupérer plus de données, mais je ne veux pas faire des va-et-vient réseaux sans cesse entre mon application et ma base de données. C'est ma base de données qui va pouvoir utiliser plein d'optimisation en interne pour pouvoir faire cette jointure potentiellement bien plus rapidement que ce que mon programme pourrait faire. Et ensuite, moi quand je récupère mes résultats, chaque utilisateur a déjà la liste de ses postes qui sont attachés et j'ai juste un aller-retour au niveau du réseau et c'est beaucoup plus efficace, beaucoup plus optimisé.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:13 - 00:06:33]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Malgré ça, ça ne suffit toujours pas. Ton application est vraiment vraiment trop populaire. Une solution que tu peux utiliser, c'est de batcher les requêtes. Ce n'est pas dans tous les cas qu'on peut, mais parfois ce qu'on peut faire, c'est vraiment on a beaucoup de requêtes. Au lieu qu'à chaque fois qu'on a un utilisateur qui fasse une demande, un utilisateur ou une application, ça peut être n'importe quoi, et qu'à chaque fois on aille dans notre base de données pour pouvoir récupérer l'information, parfois ça vaut le coup d'attendre un petit peu.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:34 - 00:06:53]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Imaginons que j'ai 100 demandes par seconde de mes utilisateurs. Je pourrais attendre par exemple 100 000 secondes, donc un dixième de seconde, et comme ça en un dixième de seconde, j'ai le temps de récupérer 10 requêtes d'utilisateurs. Et donc quand je vais faire ma requête à ma base de données ici, au lieu de la faire juste pour un seul utilisateur, je vais la faire pour 10 utilisateurs directement. Ma base de données va travailler 10 fois plus, mais je vais faire qu'un seul aller-retour entre ma base de données et mon serveur ici.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:54 - 00:07:14]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc encore une fois, je gagne un petit peu de temps au niveau du réseau. Et ça allège un petit peu ma base de données parce qu'elle n'a qu'une seule requête à faire. Et donc la requête, elle a besoin de la préparer, d'aller chercher dans les index, d'aller chercher la donnée, la récupérer, etc. Là, il y a plein de choses qu'elle peut faire juste une seule fois, comme c'est qu'une seule requête. même s'il y a plus de données à aller chercher, elle a besoin de la préparer qu'une seule fois, etc. Maintenant que mes requêtes sont optimisées, ça peut être intéressant d'optimiser le moteur de ma base de données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:14 - 00:07:32]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce qu'il y a plein de petits paramètres que je peux ajuster pour qu'elles fonctionnent un petit peu mieux. Et on appelle ça du tuning de base de données, comme son nom l'indique. Comme on va tuner une voiture pour qu'elle soit un petit peu plus performante, on peut aussi faire ça pour notre moteur de base de données. Donc ça, ça demande d'avoir une barbe un petit peu longue, de sortir sa casquette d'administrateur de base de données. Mais je peux te donner quand même un petit top 3 qui va faire la plupart du travail.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:32 - 00:07:53]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le premier paramètre, ça va être WorkMem. Donc là, je parle pour PostgreSQL, qui est une des bases de données SQL les plus populaires. Il y a des équivalents si tu utilises d'autres moteurs de bases de données. Mais forcément, comme chaque moteur est différent, la manière de les optimiser varie un petit peu. Et donc, le premier paramètre, ça va être WorkMem. C'est en fait la mémoire qui est utilisée par requête. Quand une requête arrive dans la base de données, la base doit aller chercher des données à droite à gauche.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:53 - 00:08:14]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Peut-être qu'elle doit aller mélanger les reordonnées, etc. Et donc, elle a besoin de mémoire pour faire ça. Et WorkMem, c'est la quantité de mémoire qui est allouée pour chacune des requêtes qui rentrent dans la base de données. Et ça pour l'optimiser, c'est en fonction du nombre de requêtes concurrentes qui rentrent dans ma base de données, qu'on peut savoir à peu près combien on va donner. On peut aussi regarder dans les logs de notre base de données, et si on a des erreurs OOM, c'est-à-dire que ma base de données n'arrive pas à répondre à la requête parce qu'elle n'a pas assez de mémoire, c'est peut-être que j'ai besoin d'augmenter ce paramètre-là.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:14 - 00:08:35]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça peut arriver aussi parfois que si on veut faire du reporting ou quelque chose comme ça, et on fait une requête qui, on sait qu'elle est un peu grosse, mais on la fait qu'une fois par semaine, une fois par mois, quelque chose comme ça, et bien on peut venir temporairement augmenter cette valeur-là pour que la requête puisse passer, et ensuite on va la redescendre. Parce que si jamais il y a une grosse requête qui est générée par erreur ou par un bug ou quelque chose comme ça, ça ne bouffe pas la mémoire de toutes les autres requêtes concurrentes qui tournent sur ma base de données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:36 - 00:08:59]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ensuite, Shared Buffer. En règle générale, on choisit de mettre 25% de la mémoire vive totale de notre machine. C'est la mémoire que la base de données va utiliser en cache pour garder un certain nombre d'informations frais pour ne pas avoir à aller les récupérer sur le disque dur. Mais dans le cas de Postgre, il va surtout se baser sur le cache du système de fichier. C'est-à-dire que Linux, quand on demande l'accès à un fichier, ce fichier-là, automatiquement, il va être mis en RAM, s'il y a assez de RAM disponible.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:59 - 00:09:21]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc PostgreSQL va utiliser ce système-là qui est natif dans Linux. Et donc c'est pour ça qu'il ne va pas forcément réserver la mémoire juste pour lui. On va juste réserver un quart de la mémoire. Et donc on va laisser les trois quarts de la mémoire libres. Comme ça, le système de fichier va pouvoir l'utiliser en tant que cache. Et donc quand on va accéder à ces fichiers, ça va être beaucoup plus rapide naturellement. Et c'est pour ça qu'on a ce paramètre-là ici, Effective Cache Size, qu'on recommande de mettre à peu près à 75% de la mémoire.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:22 - 00:09:51]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça ne veut pas dire que Postgre va prendre 75% de la mémoire, c'est juste une indication pour lui dire qu'il y a à peu près cette quantité de RAM-là qui va être disponible pour le cache et qui va être utilisée par le système de fichier. Une autre bonne pratique qui peut aider aussi, c'est de demander directement les champs qu'on a besoin dans notre requête. Ça, ça va moins être le cas si on utilise un ORM, mais si on est un peu à l'ancienne et qu'on fait ses requêtes manuellement, ou si même on utilise mal son ORM, il se peut que derrière, on fasse des requêtes qui demandent toutes les colonnes de ma table, alors que potentiellement j'avais besoin juste des titres parce que je suis pas en train d'afficher leur contenu, je suis juste en train d'afficher la liste de mes articles par exemple.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:51 - 00:10:11]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc ça c'est du travail qu'on fait faire à notre base de données pour rien. Deuxième chose, en particulier quand on doit réordonner les résultats, c'est de mettre des filtres. Donc dans ce cas-là c'est évident si on veut juste l'utilisateur numéro 69. Mais filtrer le plus possible ça va aider notre base de données à travailler sur un moins gros volume de données et donc être plus rapide. Et aussi comme on l'a dit tout à l'heure, de mettre des limites. Comme ça notre base de données, encore une fois, elle a moins de travail à faire.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:11 - 00:10:31]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Maintenant, si tu en es arrivé là, tu as ajouté un puller, tu as optimisé tes requêtes, tu as ajouté des index et c'est toujours super lent. Seulement, à ce moment-là, ça commence à devenir intéressant de rajouter du cache. Et pas avant. Parce qu'ajouter du cache, effectivement, ça va beaucoup booster la rapidité de récupération des résultats. Mais ça ajoute quand même aussi un peu de complexité à notre application. Parce que maintenant, elle va avoir un comportement qui va dépendre de est-ce que la donnée est enregistrée dans le cache ou pas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:31 - 00:10:50]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, ça devient plus difficile de débugger et plus difficile de voir qu'est-ce qui se passe exactement. Donc, c'est pour ça que c'est recommandé d'ajouter du cache que quand on a déjà bien optimisé le reste. Et donc ce qui va se passer, c'est que notre application va recevoir une requête. Et en fait, il y a plusieurs stratégies. Par exemple, quand un utilisateur vient faire une requête dans mon application, je vais d'abord aller regarder dans mon cache.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:50 - 00:11:08]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc en général, on va utiliser une autre base de données, mais de type clé-valeur en mémoire qui va juste utiliser la RAM. Et donc on aura beaucoup moins d'espace que dans une base de données qui va utiliser le disque dur. Mais par contre, ça va être beaucoup plus rapide parce que c'est en RAM, en mémoire vive. Et comme on a moins d'espace, on ne va pas tout stocker. Mais si on stocke les valeurs qui sont les plus fréquemment utilisées, ça va vraiment beaucoup accélérer.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:08 - 00:11:30]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc la première fois, mon application va venir vérifier si dans le cache mon information est dedans ou pas. Et si elle n'est pas dedans, elle va venir demander à ma base de données. Et quand on récupère la valeur de la base de données, on va avoir une troisième étape ici, où on va venir écrire cette valeur dans notre base de données de cache, comme Redis, Memcache ou Couchbase par exemple. Et après, il y a plein de stratégies différentes, dont les valeurs qu'on va garder dans notre base de données ici, on peut juste garder les dernières qui ont été utilisées.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:30 - 00:11:56]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Cette stratégie s'appelle LRU, pour List Recently Used. Quand notre base de cache est remplie, elle va devoir faire un petit peu de mémoire, elle va aller chercher ceux qui ont été le moins récemment utilisés, donc en fait les données les plus vieilles, et elle va les enlever. Et donc elle va garder que les plus récentes. C'est une stratégie. Une autre stratégie qu'on pourrait faire aussi, c'est regarder la fréquence d'accès de nos données. Si on sait que par exemple, on a notre top 100 utilisateurs qui utilisent 10 fois plus notre application que d'autres utilisateurs, on peut garder ces 100 utilisateurs-là les plus actifs dans notre cache.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:56 - 00:12:17]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Comme ça, même si c'est une fraction des utilisateurs que j'ai au total, comme c'est eux qui génèrent la majorité des requêtes, je vais libérer ma base de données ici de la majorité des requêtes. Ce qui fait que la deuxième fois que je vais venir pour récupérer des informations, s'ils sont déjà dans la base de données de cache, je vais les récupérer direct. Je n'ai même pas besoin de toucher à ma base de données. Et donc, encore une fois, ma base de données, elle travaille beaucoup moins et donc elle peut servir beaucoup plus de requêtes, beaucoup plus d'utilisateurs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:17 - 00:12:36]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais je te vois venir, tu vas me dire que ça ne suffit toujours pas. Il y a encore trop d'utilisateurs. Là, arrivé là, normalement, tu commences à t'approcher de la licorne. Et arrivé là, il nous reste plus d'autre choix que de scaler notre base de données. Et donc, on a deux façons de scaler une base de données. La première, c'est le scaling vertical. Ça veut dire simplement qu'on a une base de données qui est sur un certain type de machine. Et bien on va prendre une plus grosse machine.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:36 - 00:12:58]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est-à-dire une machine avec plus de RAM, plus de CPU, plus de disques durs, des disques durs plus rapides. Mais le scaling vertical, ça a une limite. Parce que premièrement, ça coûte assez cher d'avoir une plus grosse machine. Parce que plus je vais avoir des composants haut de gamme, plus ils vont coûter cher par rapport au gain de performance qu'ils me donnent. Si j'ai un processeur 32 coeurs et que je vais le remplacer par un processeur 64 coeurs, même si j'ai deux fois plus de coeurs, en général je vais payer beaucoup plus que deux fois le prix.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:58 - 00:13:24]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et le deuxième inconvénient, c'est qu'au bout d'un moment, quand j'ai pris la plus grosse machine du monde et que j'ai rempli tous les slots de RAM dans la machine, je ne peux plus scaler verticalement, c'est fini. Donc il faut que je trouve une nouvelle technique. Encore une fois, je suis encore bloqué. Après ça, ce qu'on peut faire, c'est du partitioning. Si par exemple, j'avais une table avec toutes mes listes des commandes et que j'ai tellement de commandes, je suis tellement riche, je suis Jeff Bezos des commandes, que ma base de données est trop lente quand je veux faire des requêtes dessus, je peux partitionner ma table des commandes.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:24 - 00:13:47]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est-à-dire que je vais la découper en plusieurs morceaux. Ensuite, je peux choisir par quoi est-ce que je les partitionne. Est-ce que je les partitionne en fonction des années, les commandes de 2024, de 2025, de 2026 ? Ou est-ce que je les partitionne en client, si j'ai un petit nombre de clients par exemple ? Ou en groupe d'utilisateurs ? Peut-être en catégorie des objets que je vends, quelque chose comme ça ? Idéalement, on veut choisir quelque chose qui va faire en sorte que les données vont bien se répartir à travers tous les morceaux, à travers toute notre partition.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:47 - 00:14:07]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Si par exemple, je fais des catégories des objets que je vends et que je vends 10 fois plus d'objets électroniques que de livres, je vais avoir une table qui est 10 fois plus grande que l'autre et ça ne va pas vraiment beaucoup m'aider. Alors que si je fais par année, par exemple, ça va bien être distribué entre chacune des années parce qu'en partant du principe que j'ai à peu près le même nombre de commandes par année. Par contre, si mon application, elle fait beaucoup plus de requêtes sur l'année en cours, bon, peut-être que ça va moins m'aider.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:08 - 00:14:31]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Peut-être que ça va être un petit peu moins efficace, mais ça va quand même m'aider parce que ma partition 2025, elle ne contient qu'un sous-groupe de toutes mes commandes. Ce qui fait que si je garde mes commandes sur les 20 dernières années, j'ai que 1 vingtième des données avec lesquelles je travaille. Donc, encore une fois, et donc ma base de données a beaucoup moins de travail. Mais ça, c'est encore une fois tout sur la même machine. Ça fait simplement partitionner mes données, découper mes données pour que je puisse travailler seulement sur un morceau de mes données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:31 - 00:14:50]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais je reste quand même limité par la machine sur laquelle je suis. Et donc à ce moment-là, il va falloir rajouter plus de machines. Et rajouter plus de machines, on appelle ça du scaling horizontal parce qu'à chaque fois, je rajoute une machine jamais à côté des unes des autres. Mais souvent dans les bases de données relationnelles comme MariaDB, MySQL, Postgre, ce n'est pas si simple que ça de juste rajouter des machines.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:50 - 00:15:08]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc ce qu'on fait pour commencer, c'est d'avoir une base de données primaire, et cette base de données primaire là, c'est la seule sur laquelle je vais faire des requêtes en écriture. Parce que très souvent les applications vont faire peu de requêtes en écriture par rapport au nombre de requêtes qu'elles vont faire en lecture. Je vais vous donner un exemple, si vous lisez à la liste des commentaires en dessous de ces vidéos, il y a 1000 fois plus de personnes qui vont lire les commentaires que des personnes qui vont créer un commentaire.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:08 - 00:15:28]` | Segment #42

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et créer un commentaire, c'est une requête en écriture, parce que j'enregistre un commentaire dans la base de données, alors que juste lire les commentaires, c'est une requête en lecture. Et donc très souvent, pour une requête en écriture, je peux en avoir 100 ou 1000 ou même 10 000 requêtes en lecture. Donc ça veut dire que ma base de données primaire ici, si elle reçoit juste les écritures, elle ne va pas recevoir tant de requêtes que ça. Et donc elle peut tenir la charge pendant quand même assez longtemps.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:28 - 00:15:50]` | Segment #43

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ce qu'on peut faire, c'est ajouter des répliques en lecture. Donc ça, ça va être des autres machines qui vont se synchroniser avec la base de données primaire et vont recevoir les nouvelles modifications depuis la base de données primaire à chaque fois qu'il y a une écriture. Et si mon application, elle a une requête en lecture, elle va venir contacter une des bases de données que j'ai en réplique de lecture ici. Et l'avantage c'est que les répliques de lecture, comme elles se synchronisent toutes vers une seule machine, je peux en ajouter autant que je veux.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:50 - 00:16:09]` | Segment #44

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça ne me gêne pas. Je peux en avoir 10, je peux en avoir 20. C'est simple d'en ajouter et d'en supprimer. Alors qu'au contraire, si j'avais une deuxième base de données primaire ici, il faut que les deux bases de données se synchronisent entre elles. Parce que si j'écris sur celle-là, il faut que ça se synchronise. Et si j'écris sur celle-là, il faut que ça se synchronise. Mais si j'en rajoute une troisième, il faut que celle-là se synchronise avec celle-là, puis celle-là avec celle-là, puis celle-là avec celle-là.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:10 - 00:16:32]` | Segment #45

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc, rapidement, le plus on en ajoute, le plus on a des synchronisations qui doivent se faire entre les bases de données, le plus souvent on va être bloqué en train d'attendre qu'une modification est en train de se répliquer sur toutes les machines en écriture. Si on n'attend pas que chaque écriture soit bien répliquée sur les autres bases de données primaires, je prends le risque que quand il y a une nouvelle requête qui vient d'arriver, de corrompre des données parce que je vais enregistrer des informations qui ne sont pas cohérentes avec ce qu'il y a dans une autre machine.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:33 - 00:16:52]` | Segment #46

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc, cette technique-là, elle me permet de facilement scaler mon nombre de requêtes en lecture, ce qui va être dans la majorité des cas, la majorité des requêtes que mon application va générer. Et donc maintenant que tu es capable de scaler à l'infini, que tu es un expert en base de données, que ton équipe t'est reconnaissante à jamais, si jamais tu veux savoir comment scaler ton application, ton infrastructure, il faut que tu ailles regarder cette vidéo.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

