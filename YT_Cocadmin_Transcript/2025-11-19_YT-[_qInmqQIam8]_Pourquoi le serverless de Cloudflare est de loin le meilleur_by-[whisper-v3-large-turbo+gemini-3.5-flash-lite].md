# 🎬 Pourquoi le serverless de Cloudflare est de loin le meilleur

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=_qInmqQIam8](https://www.youtube.com/watch?v=_qInmqQIam8)  
> **Date de publication** : 20251119  
> **Durée** : 00:19:01  
> **Identifiant vidéo** : `_qInmqQIam8`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Pourquoi le serverless de Cloudflare est de loin le meilleur**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Linux & Outils Systèmes** : Administration système, automatisation et surveillance.
- **Conteneurisation & Cloud** : Déploiement et gestion d'environnements résilients.

### 🔑 Points Clés & Enseignements Stratégiques
- Maîtriser les fondamentaux réseau et système pour diagnostiquer efficacement les pannes.
- Privilégier les architectures simples et observables en environnement de production.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:19]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Lire les blogs techniques, c'est un des meilleurs moyens de faire sa veille technologique. Mais on ne va pas se mentir, c'est difficile de trouver les bons et parfois c'est un petit peu chiant à lire. Mais récemment, je suis tombé sur cet article du blog de Cloudflare qui est « Éliminer les démarrages à froid 2 ». Et en fait, j'ai trouvé ça intéressant parce que j'étais déjà tombé, il n'y a pas si longtemps, sur « Éliminer les démarrages à froid », la version 1 de 2020.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:20 - 00:00:42]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je pense que ça peut te donner des idées dans tes futurs projets et donc je t'ai fait un petit résumé. Ça parle des cold starts, des démarrages à froid. Et des démarrages à froid de quoi ? Des fonctions serverless. Donc juste très très rapidement, c'est quoi le serverless ? En gros tu fais une application, même pas une application, une toute petite fonction, donc un morceau d'application, et tu te casses pas la tête avec les serveurs ou quoi, tu veux juste l'envoyer à ton fournisseur cloud, que ce soit AWS, Azure ou dans ce cas-ci Cloudflare.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:42 - 00:01:02]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et eux ce qu'ils vont faire c'est qu'ils vont la faire tourner sur une machine, donc ça c'est la machine, ils vont la faire tourner en même temps que des fonctions d'autres clients. Ce qui fait qu'ils peuvent mesurer juste le temps que passe ta fonction à être exécutée et te facturer juste pendant ce temps-là. Ce qui fait que quand tu reçois une requête, tu payes. Quand tu reçois plein de requêtes, ça scale automatiquement parce qu'ils le rajoutent sur plein de machines.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:03 - 00:01:30]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc tu payes pareil pour toutes ces requêtes. Mais quand tu reçois zéro requête, tu payes rien. Donc ce qui fait que dans certains cas, ça peut être très avantageux d'utiliser ce système de serverless. Soit parce que tu as des charges qui varient énormément, soit parce que parfois tu as très peu de charges et donc tu finis par payer presque rien, des fractions de centimes, si tu as juste quelques requêtes par jour. Donc déjà, première petite spécificité, là ici, ce schéma, c'est le serverless classique qu'on peut retrouver par exemple chez AWS avec Lambda, où on a notre application qu'on va donner.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:30 - 00:01:50]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et on va avoir un runtime par exemple JavaScript, mais ça peut être Python, ça peut être autre chose. C'est quelque chose qu'on choisit. Et ça va être tourné dans un conteneur, un conteneur Docker. Et donc pour chacune des fonctions serverless, AWS, ils vont démarrer un conteneur qui chacun va contenir la fonction, l'application, mais va contenir aussi le runtime. Ce qui fait qu'ils peuvent mettre pas mal de fonctions sur le même serveur.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:50 - 00:02:11]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et pour chacune des applications Node, il y a le runtime qui est dupliqué un petit peu ici. Il me semble d'ailleurs que sur AWS, ils n'utilisent pas des conteneurs directement, ils utilisent Firecracker qui est une espèce de micro-VM. Donc c'est un peu entre des conteneurs et des VM. La différence, c'est que chez Cloudflare, toutes les fonctions de tous les clients, ils tournent sur le même runtime. Et donc ça fait qu'ils peuvent en paquer beaucoup plus sur le même serveur.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:12 - 00:02:46]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc ils peuvent charger moins cher parce qu'ils ont besoin de moins de serveurs pour faire le même travail. L'inconvénient, c'est qu'il y a moins d'isolation entre les applications. L'isolation ici, elle est gérée directement par le runtime. Ils ont un runtime custom, ils n'utilisent pas Node directement, c'est un truc custom qu'ils ont fait, qui utilise la fonction des isolate. C'est une fonction qui est de base dans V8 qui permet d'avoir une fonction qui a droit à un certain nombre de ressources de mémoire, etc. mais qui ne pourra jamais accéder aux ressources des autres fonctions. Ils ont rajouté quelques petites autres sauces magiques pour pouvoir isoler encore plus, pour avoir une meilleure sécurité parce que tu ne veux vraiment pas qu'un client puisse accéder à l'application d'un autre client. Donc ils ont fait

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:46 - 00:03:12]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> en sorte que ça soit assez robuste. Et donc l'avantage c'est qu'ils en ont beaucoup plus, donc c'est beaucoup moins cher pour l'utilisateur. L'inconvénient, c'est qu'on est obligé d'utiliser notre JS, alors que sur Lambda, on peut utiliser d'autres home times comme Python, comme Java, comme ce que tu veux. Et le deuxième inconvénient, c'est potentiellement qu'il y a plus de chances qu'ils aient des problèmes de sécurité qu'avec des micro-VM, où là, ça va être vraiment très difficile de sortir d'un conteneur qui est dans une micro-VM.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:12 - 00:03:37]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais jusqu'ici, ça va, ça se passe bien. Et donc, c'est quoi ce fameux problème de call start ? Imaginons que ça, c'est un serveur, et que chaque rond ici, c'est une fonction d'un client différent. Des fonctions, en fait, ils en ont plein. Ils en ont plus que ce qu'ils peuvent faire tenir sur les serveurs. Parce qu'il y a plein de fonctions qui sont là, mais qui ne sont pas utilisées très souvent, mais elles doivent quand même être prêtes à être exécutées au moment où il y a une requête qui arrive.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:37 - 00:04:01]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc ce qu'ils font, c'est qu'ils ont des fonctions qui sont « chaudes », c'est-à-dire qu'elles sont chargées directement dans le serveur, dans la RAM du serveur, et ils ont des fonctions qui sont froides, des « cold ». Et donc ces fonctions-là restent peut-être sur le disque, ou du moins elles ne sont pas chargées en mémoire. Ce qui fait que si moi j'ai une fonction qui est sur kokamine.com et sa fonction elle est chaude, elle est déjà en RAM, je fais ma requête, boum, je reçois ma réponse instantanément parce que ma fonction est déjà chargée en mémoire.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:01 - 00:04:19]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Si par contre ça fait longtemps que je n'ai pas fait de requête sur kokamine.com et donc du coup ma fonction ici elle a été mise de côté, elle est froide, et bien je vais faire ma requête sur kokamine.com. Là le serveur il va dire la fonction pour kokamine.com je ne l'ai pas, donc il faudrait que je l'ai trouvé, il faut que je la compile, et il faut que je la charge en mémoire, et ensuite seulement je pourrais répondre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:19 - 00:04:42]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc, c'est ça le fameux problème de cold start, c'est que ce temps qu'il faut pour prendre tout ça, parfois ça prend beaucoup de temps. Et comme pendant ce temps-là, notre utilisateur-là, il est en train d'attendre que sa page est charge, ça ne peut pas prendre plus en seconde, il faut que ça prenne max 100 millisecondes. Sachant que 100 millisecondes, c'est juste le temps pour récupérer ma fonction ici. Si ma fonction, une fois qu'elle est chargée, elle est chaude, elle prend du temps pour s'exécuter parce qu'elle fait du travail, elle calcule les choses, elle va chercher des éléments dans ma base de données, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:43 - 00:05:13]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> s'ajoutent à tout ce temps de processing que ma fonction va devoir faire. Donc on veut minimiser ce temps-là au minimum, on veut qu'il soit imperceptible. Dans l'idéal, on veut qu'il n'y ait aucune différence entre un appel de fonction qui est froid et un appel de fonction qui est chaud. Et donc c'est ça qu'ils expliquent dans leur article ici, éliminer les démarrages à froid. Avant de vous montrer ce qu'ils ont fait dans la version 2, je vais leur parler vite fait de ce qu'ils ont fait à la base pour pouvoir éliminer les colstar, c'est-à-dire ne plus en avoir du tout. Et ensuite on va comprendre pourquoi est-ce qu'ils ont dû refaire une une deuxième passe parce qu'ils n'en ont plus mais ils continuent de les éliminer, c'est bizarre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:13 - 00:05:44]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc la manière dont il définit ici le call start, c'est qu'on a notre worker, cette machine qui va faire le travail, il faut qu'elle ait récupéré le script, donc elle est récupérée par le réseau depuis un stockage. Donc ça prend du temps pour télécharger le script. Une fois qu'on a téléchargé le script, il faut le compiler pour pouvoir l'exécuter rapidement, il faut le charger en mémoire avant de pouvoir l'exécuter et à ce moment-là on va pouvoir commencer à exécuter vraiment le code qu'il y a dans la fonction. Mais toute cette période qui est ici avant, c'est ça le cold start. C'est du temps qui s'ajoute en plus du temps de processing de la fonction.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:44 - 00:06:10]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Idéalement on voudrait que ce temps ici soit à zéro. Donc on se pourrait se dire bon bah le temps de téléchargement on peut pas faire grand chose, on peut augmenter la vitesse du réseau, mais si j'imagine que chez CloudFair c'est déjà assez haut. Le temps de compilation on peut mettre un meilleur CPU à la limite mais bon pareil j'imagine qu'ils ont déjà des machines assez balètes. Donc comment on peut faire pour éliminer ce temps de boot ? Donc on peut pas l'éliminer mais on peut faire en sorte qu'il soit imperceptible. Comment est-ce qu'on peut faire ? Notre navigateur ici, il fait une requête à Cloudflare. Il lui dit ok je veux que kokanmik.com ou luxemple.com.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:10 - 00:06:45]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Quand il fait cette requête, cette requête est là en HTTPS. Et comme cette requête en HTTPS, pour pouvoir chiffrer la connexion, il y a un échange qui va se faire entre le navigateur et entre le serveur de Cloudflare. Et cet échange là, il prend quelques allers-retours. Il y a le premier paquet qui va être le client Hello, ensuite on va recevoir une réponse qui va être le serveur Hello, ensuite on va envoyer une clé, ensuite à partir de là on va s'accorder sur une clé que mon navigateur et le serveur vont pouvoir utiliser et à ce moment là seulement une fois qu'on a une clé qu'on peut chiffrer les données et bah je peux envoyer ma requête qui va être chiffré maintenant et à ce moment là qu'un fer peut aller voir cette requête là à quelle fonction ça

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:45 - 00:07:05]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> correspond chargé cette fonction si jamais les pas déjà en mémoire la compilée la mettre en mémoire exécuté le code qui a dans cette fonction et enfin envoyer la réponse au navigateur donc Donc ils se sont dit, peut-être que ce qu'on pourrait faire, c'est que techniquement, exemple.com, ici on le sait dès le départ, dans la première requête que nous fait le client.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:06 - 00:07:25]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc peut-être qu'on pourrait utiliser tout ce temps-là, où on est en train d'attendre que la connexion SSL se fasse, ça prend quand même un certain temps. Donc peut-être que ce temps-là, on pourrait l'utiliser pour pouvoir améliorer notre temps de démarrage. Et donc c'est exactement ce qu'ils ont fait. Leur serveur, dès qu'il va recevoir le premier paquet qui demande hello.com, directement ils vont aller demander au runtime d'aller récupérer la fonction et de la compiler, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:25 - 00:07:45]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ce qui fait que le temps que la négociation SSL, le uncheck SSL finisse, s'ils sont assez rapides, une fois qu'ils reçoivent la requête qui est faite pour cette fonction-là, eh bien la fonction est déjà chargée en mémoire ici. Et donc on peut directement envoyer la réponse. Ce qui fait que si ma requête est chargée en mémoire, c'est rapide. Et si elle n'est pas chargée en mémoire, eh bien c'est quand même rapide. C'est imperceptible le temps de chargement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:45 - 00:08:09]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce qu'on a utilisé ce temps de négociation SSL avant que la requête soit envoyée. Et donc, fin du game, ils ont éliminé les cold starts. Et donc ils ont un peu le Graal, ils vont avoir une fonction qui va être toujours à la tête rapide, même si elle n'est pas déjà chargée en mémoire. Donc pourquoi est-ce qu'ils ont fait un deuxième article où ils disent « éliminer les démarrages à froid 2, fragmenter et conquérir ? » En fait, à l'époque, ils avaient effectivement éliminé le problème de Code Start, mais ça c'était en 2020.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:10 - 00:08:30]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Maintenant on est en 2025, donc il y a eu pas mal de petits changements qui ont été faits entre temps. Le premier, c'est que la taille des scripts, elle est passée de 1 MO à 5 MO, et même jusqu'à 10 MO pour les utilisateurs payants. Ce qui fait que juste le temps qu'il faut pour aller télécharger ce script, Déjà, il a pu faire x5, x10. Donc, ça rajoute pas mal de temps. En plus de ça, la taille du script autorisé est passée de 1 MO à 3 MO pour les utilisateurs gratuits.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:30 - 00:08:52]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, c'est-à-dire qu'il y a encore plus de personnes qui ont utilisé les workers de CloudFair et peuvent aussi utiliser des plus gros scripts. Il y a plus de codes à exécuter. Donc, ce qui fait que ça prend plus de temps à télécharger, mais ça prend aussi plus de temps à compiler parce qu'il y a juste plus de scripts, plus de codes à compiler et à mettre en mémoire. Ce qui veut dire que le travail qu'on a à faire ici, télécharger et compiler, ça prend plus de temps. Il y a des moments où ces étapes-là, et bien a commencé à prendre plus de temps que le Uncheck SSL.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:52 - 00:09:13]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> En plus de ça, à l'époque, le protocole qui était le plus utilisé pour pouvoir chiffrer les données, c'était TLS 1.2. Et aujourd'hui, celui qui est le plus utilisé, c'est TLS 1.3. Et TLS 1.3, au lieu d'avoir plusieurs allers-retours comme ça, et bien on en a juste un seul, voire même zéro dans certains cas. Ce qui fait que non seulement on a plus de choses à faire ici, mais en plus de ça, le temps qu'on a ici, il a été réduit.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:13 - 00:09:34]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc, dans de plus en plus de cas, ils ont commencé à perdre la course entre guillemets. et donc le call start a commencé à revenir. Il y a des fonctions qui commençaient à mettre plus de temps à répondre quand ça faisait longtemps qu'elles n'étaient pas exécutées. Donc là, ils se sont dit, il faut qu'on trouve une nouvelle technique. Et une des optimisations qu'ils ont voulu essayer, c'est que dans la data center, imaginons qu'on a plusieurs serveurs et que moi, j'ai mon utilisateur ici, voilà, je dessine très bien.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:34 - 00:10:00]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Imaginons que ça fait longtemps que je n'ai pas appelé ma fonction et donc du coup, elle est froide. Et tout de coup, je fais un appel. Premier appel, il arrive ici, sur un serveur au hasard. Il y a un load balancer qui me fait arriver sur ce serveur numéro 1 ici. le serveur numéro 1, il va chercher ma fonction, il a compil, il la met ici. Ça a pris du temps, j'ai un call start. On va dire bon c'est pas très grave parce que maintenant toutes les requêtes que je vais faire à partir de maintenant, elles vont être chaudes et ça va mieux aller. Mais le problème c'est que ici, il y a un autre balancer qui répartit la requête.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:00 - 00:10:35]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et on n'en voit pas tout le temps sur les mêmes machines. Donc quand je vais faire une nouvelle requête ou un autre utilisateur va faire une autre requête, eh ben potentiellement elle va arriver sur un autre serveur. Et ce autre serveur là n'a pas la fonction en mémoire. Il faut que lui aussi il aille la chercher, etc. Et donc là je vais avoir un autre call start ici. Et donc ce qui fait qu'en fait il ya des serveurs il y en a plein il ya plein même plein de différentes régions donc ce qui fait que une fonction qui est un peu utilisé mais pas énormément et ben elle peut se retrouver à être tout le temps tout le temps en call start parce que à chaque fois qu'il ya une nouvelle requête car il elle arrive sur un nouveau serveur et ce qui peut être encore pire c'est que le temps que je fasse une requête ici là que ça soit en call start ensuite je fais une autre quête

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:35 - 00:10:54]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> là j'arrive sur un autre serveur c'est encore en call start si c'est assez infréquent ça se peut que que quand je fasse une troisième requête, imaginons que je retombe sur le même premier, comme ça fait assez longtemps que je n'ai pas fait de requête, celle-là ici, elle est devenue encore entre-temps en call start parce que ça l'a effacée, parce que le serveur l'a enlevé de la mémoire, parce que ça fait plus d'une heure que je n'ai pas reçu de requête.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:54 - 00:11:12]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc si on avait la malchance d'être un de leurs clients qui était un peu dans cette zone grise, qui ont par exemple peut-être 20 requêtes par heure ou quelque chose comme ça, ça se peut que chacune des requêtes soit en call start parce que même si les fonctions sont chargées sur les serveurs, le temps qu'on retombe sur un même serveur, il s'est déjà passé plus d'une heure et donc la fonction est repartie en call storage. Ça arrive de plus en plus fréquemment.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:12 - 00:11:36]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pour certains des clients, ça arrive encore plus fréquemment parce que le plus ça arrive, le plus ça arrive, si tu veux. Donc ils se sont dit, ce qu'on pourrait faire, c'est que quand un utilisateur fait une requête, il y a un call start. Bon, ben voilà, il faut qu'on aille chercher ma fonction en call start. On vient, on la pompinoise et on la met. Mais la prochaine fois qu'on fait une requête, on pourrait faire en sorte que le loadbouncer sache sur quel serveur la fonction est déjà chargée et l'envoyer en priorité sur ce serveur-là.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:36 - 00:11:59]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> De cette manière, on ne va pas éliminer le code start, mais on va beaucoup diminuer la probabilité que ça arrive. En particulier pour ces utilisateurs qui n'ont pas énormément de requêtes. Donc on va vous dire, ok, c'est simple, on met ça en place et c'est bon, c'est fini. Le souci, c'est que comment est-ce que le load balancer fait pour savoir sur quel serveur a quelle fonction ? Parce que non seulement les fonctions bougent, c'est-à-dire qu'à un moment la fonction va être ici, mais ensuite elle va être là-bas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:00 - 00:12:20]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et en plus de ça, les serveurs aussi bougent. À un moment, il y a un serveur qui va être ajouté, à un moment il y a un serveur qui va être enlevé, un moment où il y a un serveur où il y a la fonction dessus qui va être enlevée, donc la fonction va se remettre là-bas. Donc en fait, ça bouge tout le temps. Donc si on fait ça un peu naïvement, on va se retrouver comme un peu avec une table ici, on va voir l'application 2 qui va être sur le serveur 2, l'application 13 qui est sur le serveur 0, l'application 31 qui est sur le serveur 1, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:20 - 00:12:42]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que ce qu'on veut, c'est répartir les fonctions de manière un peu équitable sur tous les serveurs. Ok, donc il n'y a pas de souci, ce qu'on pourrait faire, une solution facile, c'est d'utiliser le modulo. Donc là, on a trois serveurs, Donc on va utiliser la fonction modulo3. Et donc en fonction de l'ID de notre fonction, ça va nous répondre à un chiffre entre le serveur 0, le serveur 1 ou le serveur 2. Et comme ça, je vais répartir exactement équitablement toutes mes fonctions en un tiers, un tiers, un tiers.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:42 - 00:13:04]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Évidemment, ils n'ont pas trois serveurs, ils ont peut-être 300 000, mais le principe reste le même. Le petit souci avec ça, c'est que là, jusque-là, ça fonctionne. Si je fais 123 modulo3, ça me donne 0. Donc cette fonction va être sur le serveur 0. Là, sur l'application 13, je fais 13 modulo3, pareil, ça me donne 0. Donc la fonction 13, elle va être sur le serveur 0 aussi. 31 modulo 3 ça me donne 1 donc je vais être sur le serveur 1, 2 modulo 3 ça me donne 2, je vais être sur le serveur 2.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:04 - 00:13:23]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc on voit que ça me répartit quand même assez équitablement mes fonctions à travers mes trois serveurs. Le petit souci c'est que qu'est ce qui se passe quand on ajoute un serveur ? Là ici je me retrouve avec un quatrième serveur qui s'appelle serveur 3 parce qu'on a commencé de 0. Et bah maintenant mon application ici 1, 2, 3, si je fais 123 modulo 3 ça me donne 3 au lieu de 0.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:24 - 00:13:44]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc ça veut dire que cette application là elle était sur le serveur 0, il faut maintenant qu'on l'envoie sur le serveur 3. Là, l'application 13, 13 modules 3, maintenant ça donne 1. Donc en fait, celle-là, pareil, elle était sur le serveur 0, il faut qu'on l'envoie sur le 1, etc. Donc on voit que ce n'est pas vraiment très pratique parce que si on est dans un environnement cloud où on a tout le temps des machines qui s'ajoutent et qui s'enlèvent, notre calcul va être différent à chaque fois et je ne veux pas avoir à bouger mes fonctions de serveur à chaque fois.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:44 - 00:14:04]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que si je fais ça, si j'enlève mes fonctions d'un serveur pour le mettre sur l'autre, il faut que je le recompile, le re-télécharge, etc. Et je retombe dans le même problème que je veux exactement éviter. Donc pour éviter ça, ils vont utiliser un anneau de hachage cohérent. Donc c'est un algorithme qui est un petit peu différent, qui est le même concept, mais qui va faire en sorte que quand on ajoute ou qu'on enlève des serveurs, ça n'impacte pas toutes les fonctions. Ça n'impacte juste les fonctions qu'il y avait sur ce serveur-là qui a disparu.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:04 - 00:14:25]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ou juste les fonctions qui doivent être déplacées sur le nouveau serveur pour garder une distribution homogène. Mais il reste un petit problème. C'est qu'avant, les fonctions étaient beaucoup plus petites. Elles étaient limitées à 1 MO. Mais maintenant, elles peuvent être beaucoup plus grosses à 10 MO. Et contrairement à du caching classique, quand on a par exemple un CDN qui met en cache des images, des fichiers CSS, JavaScript, etc., un fichier de 10 mégas va prendre 10 fois plus de ressources qu'un fichier de 1 mégas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:26 - 00:14:45]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc si j'ai 100 mégas de capacité, je peux soit mettre 10 fichiers de 10 mégas ou alors 1000 fichiers de 1 mégas ou alors 2 fichiers de 500 mégas. Et donc ce que je veux dire, c'est que c'est assez facile de répartir les différents fichiers sur différents serveurs en fonction de la capacité qu'on a. Le problème avec des scripts, c'est qu'un script de 10 mégas, il peut consommer moins de ressources qu'un script de 1 mégas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:46 - 00:15:19]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça dépend de ce que fait la fonction. Et donc si on répartit les fonctions de manière équilibrée fonction de leur taille, on peut se retrouver avec des serveurs qui n'ont eu pas de chance, qui ont plein de petites fonctions mais qui consomment énormément de ressources. Et de la même manière, on peut se retrouver avec des serveurs qui ont quelques grosses fonctions mais qui ne sont pas super utilisées et qui n'utilisent pas tant de retours que ça. Et donc on va avoir des serveurs qui vont être surchargés et des serveurs qui ne font rien de l'autre côté. Donc on va éviter ça. Et donc pour éviter ça, une des solutions, c'est d'avoir du délestage de charge. C'est-à-dire que le système doit être capable de supporter le fait que si un serveur, il est trop chargé, c'est-à-dire qu'il a trop de travail à faire, il doit être capable de pouvoir dire non je ne supporte pas cette requête là,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:20 - 00:15:40]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> va la faire sur un autre serveur. Parce que sinon on va être vraiment trop trop déséquilibré entre les différents serveurs. La première possibilité c'est que le serveur qui reçoit la requête, il trouve le serveur qui a vraiment cette fonction en charge en mémoire, il lui demande ok est-ce que tu es chaud pour pouvoir l'exécuter, est-ce que tu as de la dispo ? Lui lui dit si oui ou non, si il lui dit oui ok il lui envoie la requête, il exécute et puis voilà.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:40 - 00:16:00]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc l'exécution se fait assez rapidement. Et si jamais non le serveur il est trop surchargé, et bien dans ce cas-là, le serveur qui a envoyé la requête, il va lui-même aller chercher la fonction en call storage, lui-même la charge en mémoire, et comme ça, on va se retrouver avec deux serveurs qui peuvent exécuter cette fonction et donc plus de charge, parce que ça veut dire qu'on a plus de requêtes, et donc on doit la déployer sur plusieurs serveurs pour pouvoir la servir plus rapidement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:00 - 00:16:34]` | Segment #42

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Petit inconvénient avec cette technique, c'est que si à chaque fois je dois demander au serveur s'il est prêt ou pas, la majorité du temps, je vais perdre un aller-retour entre les deux serveurs. Là, on parle peut-être d'une milliseconde, parce que tout ça, c'est en interne, mais c'est du temps qui est perdu. En fait ils se sont dit ok mais la plupart du temps, 90% du temps quand je vais demander à un serveur d'exécuter ma fonction et bah il va le faire. C'est que dans les rares cas où il est surjet où il ne va pas le faire. Donc est-ce qu'on ne pouvait pas envoyer la requête sans confirmation ? Il lui dire juste fais ça. Et puis si jamais il ne peut pas le faire, il me dira de cette manière là, je lui envoie ok exécute cette fonction. Soit il exécute direct et donc du coup j'ai économisé un petit

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:34 - 00:16:58]` | Segment #43

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> alerte au. Soit dans les rares cas où c'est pas le cas et le serveur est surchargé et bah le serveur me répond. Le serveur qui a reçu la requête de l'utilisateur, il va charger la fonction sur lui-même À ce moment-là, on va avoir un call start. Mais maintenant que la fonction est chargée sur deux serveurs, il y a encore moins de chances d'avoir un call start derrière. Si vous voulez tout lire, je vous mettrai le lien. Ils partent un peu dans un délire où ils expliquent qu'ils ont un protocole custom qui s'appelle CaptainProtoRPC, qui va tout gérer ça automatiquement pour eux, le fait de réessayer automatiquement, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:58 - 00:17:28]` | Segment #44

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce qu'ils ont plein de cas bizarres où un worker peut aller déclencher un autre worker, qui lui-même peut déclencher un autre worker. Donc ça devient encore plus compliqué que ce que je viens de vous expliquer là. Et donc, les résultats. Qu'est-ce qui s'est passé une fois qu'ils ont mis ça en place ? Et ben là c'est assez intéressant parce qu'il dit ok, une fois que le déploiement est terminé, seulement 4% des requêtes du trafic ont été fragmentées ou chardées en anglais. Autrement dit, 96% des requêtes d'entreprises sont adressées à des savoir-worker dont la charge est telle qu'il est nécessaire d'en exécuter plusieurs instances dans un centre de données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:17:28 - 00:18:02]` | Segment #45

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc là ce qu'ils veulent dire c'est que toutes les optimisations qu'ils viennent de faire là, elles vont s'appliquer seulement à 4% des requêtes. Parce qu'il y a 96% des requêtes qui tombent sur des fonctions où il y a assez de trafic pour qu'elles soient déjà répliquées dans assez d'endroits pour qu'il n'y ait jamais de cold start. Donc on va dire qu'ils sont fait chier à faire tout ça pour pouvoir optimiser seulement 4% des requêtes. En fait ce qui est intéressant, c'est que même si ça concerne que 4% des requêtes, globalement sur tous leurs serveurs, il y a eu 10 fois moins d'expulsions des workers. Donc une expulsion de worker, c'est une fois quand un worker est là depuis trop longtemps, on ne sait rien faire, on l'enlève de la mémoire. Et donc si on a eu 10 fois moins d'expulsions, ça veut aussi dire qu'on a eu 10 fois moins de création, et donc

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:18:02 - 00:18:22]` | Segment #46

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> 10 fois moins de fonctions qu'on a dû servir à froid. Ce qui veut dire qu'ils ont diminué leur leur taux de requête à froid de fois 10. Et donc là, ils disent, pour le trafic entreprise, notre taux de requête chaude est passé de 99,9% à 99,99%. Donc on peut se dire, c'est juste 0,09%. En fait, ils ont par 10 du nombre de requêtes qui sont faites à froid. Donc dans la première étape, ce qu'ils ont fait en 2020, ils ont réduit au maximum le temps que ça prenait.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:18:22 - 00:18:55]` | Segment #47

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ils ont presque réussi à éliminer, ou du moins rendre imperceptible le problème de cold start. Et dans les modifications qu'ils viennent de faire récemment, en 2025, ils ne pouvaient pas vraiment le réduire plus que ça, mais ils ont réduit par 10 le pourcentage de chance que ça arrive. Tu sais que ce genre de vidéo, c'est vraiment pas pour tout le monde, c'est déjà un peu plus technique. Mais s'il y a assez de monde à qui ça plaît, j'essaierai d'en faire un peu plus. Mais si tu vois encore plus profondément comment fonctionne une requête depuis ton navigateur vers un serveur, et ça en fonction de si tu as un HTTP 1, HTTP 2, HTTP 3, ou même TLS 1.2, 1.3, etc., je te suggère d'aller voir cette vidéo, si elle est sortie, je sais pas encore, je pense peut-être qu'elle va sortir d'ici une semaine ou deux,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:18:55 - 00:19:00]` | Segment #48

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> ou peut-être que si tu as de la chance, elle est déjà sortie. Et si c'est pas encore le cas, je te mettrai une autre vidéo qui est très intéressante aussi.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

