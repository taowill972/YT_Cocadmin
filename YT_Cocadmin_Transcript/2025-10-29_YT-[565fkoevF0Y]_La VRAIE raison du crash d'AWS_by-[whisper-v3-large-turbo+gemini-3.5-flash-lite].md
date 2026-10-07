# 🎬 La VRAIE raison du crash d'AWS

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=565fkoevF0Y](https://www.youtube.com/watch?v=565fkoevF0Y)  
> **Date de publication** : 20251029  
> **Durée** : 00:17:21  
> **Identifiant vidéo** : `565fkoevF0Y`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **La VRAIE raison du crash d'AWS**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.

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
> On a entendu parler partout, Amazon était d'Inde, donc tout le monde était d'Inde, donc c'était le bordel. Et puis, en tant que sysadmin, on était tranquille parce qu'on n'avait plus besoin de travailler. On pouvait juste dire, ah bah c'est pas ma faute, Amazon est d'Inde, vous voyez, tout ne marche pas, donc c'est normal. Mais ce que moi je trouve vraiment intéressant, c'est de savoir qu'est-ce qui s'est passé exactement. À la base, le problème venait de DynamoDB, on va voir un petit peu plus en détail juste après.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:19 - 00:00:38]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais ça a eu des effets de bord sur plein plein plein d'autres services, ce qui fait que t'as plein de sites qui fonctionnaient plus. Et c'était limité à la région US East 1, qui est la toute première région qu'AWS a mis en service. Et donc en fait Amazon est divisé en régions et chaque région est divisée en zones de disponibilité. Par exemple la région Paris ici qui n'est pas exactement à Paris.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:38 - 00:00:57]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Elle est divisée en plusieurs data centers qui sont indépendants les uns des autres. Pour éviter les effets de bord. Pour que s'il y a un problème dans un data center ça n'affecte pas en théorie les autres data centers. Et si jamais il y a une météorite qui tombe et que ça explose les trois data centers qui sont dans cette région là. En théorie tu peux avoir ton infrastructure qui est rondondée dans des régions qui sont à côté. Et ce qui fait que ton service va rester disponible.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:57 - 00:01:16]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais en pratique, ce n'est pas toujours le cas parce que c'est quand même assez chiant et il y a quand même quelques inconvénients à mettre son service dans différentes régions. Parce que ça veut dire que toutes tes bases données, par exemple, elles doivent se répliquer à travers le monde. Tu dois faire transférer pour synchroniser des données à travers le monde aussi, donc ça coûte beaucoup plus cher. Tu dois aussi avoir une infrastructure un peu partout, donc ça coûte plus cher aussi.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:16 - 00:01:37]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, il faut vraiment en avoir besoin. Ce qui fait que tu as beaucoup d'entreprises qui, même si c'était une seule région, ils étaient impactés. En plus de ça, c'est la plus ancienne et donc la plus grosse. et donc celle qui a le plus gros impact quand il y a un souci dedans. Donc là, ils disent que ça a affecté DynamoDB, mais ils se disent aussi que ça a affecté aussi les NLB, les Network Cloud Balancer, les répertiteurs de charges, mais aussi les instances de C2.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:37 - 00:02:10]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc on va essayer de comprendre pourquoi, parce que tout ça est un peu connecté, même si à la base, ce n'est pas censé avoir de rapport. Le souci a commencé à minuit au Pacifique, et pour commencer, pour comprendre le problème, ils expliquent comment fonctionne le système derrière, sous le capot. Le service DynamoDB, c'est un service de base de données non relationnelle qui est beaucoup utilisé parce qu'il est facile à utiliser, il est géré et donc il est utilisé par beaucoup d'entreprises même par Amazon eux-mêmes en interne pour pouvoir faire fonctionner toute la plateforme et donc les applications pour se connecter à cette base de données elles ont besoin d'utiliser un nom de domaine qui va résoudre en adresse IP donc tu vas avoir ton DNS ici, service de DNS, celui qui résout entre

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:10 - 00:02:32]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> l'adresse IP blablabla.dynamoDB.aws.com en adresse IP donc comme c'est beaucoup utilisé beaucoup de personnes qui créent des bases de données qui suppriment des bases de données des bases de données qui scalent et donc pour pouvoir faire ça le système est découplé ça Ça veut dire qu'on a un système ici qui sert à planifier. Il appelle ça le planificateur. C'est celui qui va recevoir toutes les requêtes du système pour pouvoir faire des changements dans le nom de domaine des bases de données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:32 - 00:02:53]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et en fait, quand tu cliques pour faire un changement, le changement n'est pas fait instantanément. Il arrive dans ce système de planification. Ce système de planification, il peut répondre à l'utilisateur en disant « Ok, j'ai pris en compte ta requête, mais je ne l'ai pas encore fait. » Donc en gros, c'est en statut pending, c'est en cours. Ce système, il va générer une configuration. Tac, voilà, c'est censé représenter une configuration. Et ensuite, ces configurations vont être appliquées par des DNS enactors.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:53 - 00:03:16]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> L'actors, ça veut dire que c'est lui qui va vraiment faire le travail, qui va modifier la configuration DNS. Donc, tu vas avoir tes enactors ici. Et en fait, eux, tu en as plein. Tu en as plusieurs parce que, pareil, il y a beaucoup de travail à faire, beaucoup de modifications à faire. Et donc, on peut potentiellement en ajouter ou en enlever en fonction de la charge qu'il y a, etc. Et donc, la manière normale dont fonctionne le système, c'est que quand il y a une nouvelle configuration qui arrive, le système génère une nouvelle configuration.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:16 - 00:03:35]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le connecteur, par exemple celui-là, il récupère la configuration. Il vérifie que cette configuration est bien plus récente que la configuration qui existe déjà dans mon système DNS. Si c'est le cas, il applique la nouvelle configuration sur le DNS. Et ensuite, il va enlever les vieilles configurations du DNS. Et ce qui fait qu'on se retrouve dans le dernier état.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:35 - 00:03:55]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça, c'est dans le meilleur des cas, dans le cas qui fonctionne et qui a fonctionné tout le temps, tous les jours, 7 jours sur 7 jusqu'à 7 semaines. Là, le problème a eu lieu, c'est qu'on avait une nouvelle configuration qui est arrivée. les annecteurs ont commencé à distribuer la nouvelle configuration un petit peu partout. Sauf un, il y en a un qui était un petit peu en galère. Lui par exemple ici, il a récupéré la nouvelle configuration.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:55 - 00:04:14]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Il a bien vérifié que cette configuration était bien plus récente que la configuration qui est actuellement sur les DNS. Mais en essayant de l'appliquer, il n'y arrivait pas. Parce que ça se peut qu'il y avait un autre annecteur en ce moment-là qui était en train de faire une modification. Et donc il réessayait un petit peu en boucle. Et donc ça tout seul, ce n'est pas trop un problème. Parce que bon, il va réessayer. Au bout d'un moment, ça ne va finir pas fonctionner.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:14 - 00:04:32]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le problème c'est que ça a augmenté énormément les chances d'avoir une waste condition. Donc ça c'est un type de bug qui arrive quand tu as un système qui est distribué. Donc tu as plusieurs machines qui font des choses en même temps. Ou dans la plupart des cas les systèmes font ce qu'on veut. Mais il peut y avoir dans certains cas si les choses arrivent vraiment dans un ordre précis. Là ça ne fait pas ce qu'on veut et ça génère un bug. Et c'est ce qui est arrivé là. Pendant que lui il essaie de mettre sa configuration.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:32 - 00:04:59]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Tu as une nouvelle configuration ici qui est arrivée. Parce qu'il y a des modifications qui sont faites tout le temps. Les gens ils créent, ils modifient, ils enlèvent des bases de données tout le temps. Et donc tu as un autre acteur qui l'a récupéré. lui regarde la configuration ici, il se dit ok, elle est bien plus ancienne que celle que j'ai en ce moment, donc il n'y a pas de soucis. Il vient rajouter sa configuration dans le DNS ici. Juste exactement après ce moment-là, pas de chance, un acteur qui essayait de rajouter sa configuration, finalement il arrive à appliquer sa configuration, et donc elle vient écraser la configuration qui vient d'être mise juste avant.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:00 - 00:05:18]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Il a effectivement fait sa vérification que sa configuration était plus récente, mais il l'a fait avant de recommencer 10 fois. Et le temps qu'il recommence 10 fois, ce n'est plus le cas, sa configuration est devenue trop ancienne. Et lui, une fois qu'il a appliqué sa configuration, et bien ce qu'il fait, c'est qu'il efface les anciennes configurations. Et quand il regarde les configurations qui sont appliquées, il voit que celles-là et celles-là sont anciennes, et donc il les efface.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:18 - 00:05:37]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc on est entré dans une race condition. Si les choses se font exactement au mauvais endroit, au mauvais moment, à la milliseconde près, et bien on arrive à ce bug-là, où on se retrouve avec rien du tout. Aucune configuration DNS. Ce qui fait que quand j'ai une application qui essaye d'accéder à ma base de données MongoDB, il essaye de résoudre le nom de domaine, et le nom de domaine, il ne correspond à rien.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:37 - 00:05:55]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le DNS, il dit non, ça n'existe pas. Même si la base de données elle elle est bien toujours là, elle répond, elle a toujours ses données etc. Et bien notre application ici elle peut pas y accéder. Et ça, ça va déclencher pas mal de problèmes en cascade. Parce que maintenant le DNS il est dans un état qui est vraiment bizarre, inconnu avec aucune entrée DNS. Donc c'est pour ça qu'il y a eu besoin d'une intervention manuelle.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:55 - 00:06:15]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pour pouvoir corriger ce problème c'est pas si compliqué. Il faut juste récupérer ok c'est quoi la dernière version, l'appliquer sur les serveurs DNS. Et puis boum ça revient. Et donc effectivement ils ont corrigé ça assez rapidement. Et au bout de pas si longtemps que ça, ça a pris deux heures et demie. ils ont restauré le DNS et tout fonctionnait correctement pour DynamoDB. Le souci, c'est que pendant ce temps-là, on a Amazon EC2.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:15 - 00:06:36]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc EC2, c'est le service de machines virtuelles. Ce système, il utilise lui aussi DynamoDB en tant que base de données pour pouvoir faire les modifications, créer des nouvelles machines, supprimer les anciennes. À partir du moment où DynamoDB a commencé à ne plus être disponible, ça a commencé à bugger. Les gens n'étaient plus capables de pouvoir démarrer des nouvelles machines. En soi, ce n'était pas trop grave parce que toutes les machines qui étaient là déjà existantes, elles continuent à fonctionner.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:36 - 00:06:58]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est juste que dans le cas où on voulait ajouter une nouvelle machine ou faire une modification d'une machine existante ou les supprimer, là, ça fonctionnait. Et ça, ça peut causer des problèmes quand on utilise un service d'AWS qui s'appelle l'autoscaling qui permet d'automatiquement ajouter des machines quand la charge devient plus importante sur nos serveurs. Ce qui fait que si on a plus d'utilisateurs sur notre application, ça va rajouter des machines pour pouvoir absorber la charge supplémentaire.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:59 - 00:07:20]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais là, dans ce cas-là, on ne pouvait pas démarrer des nouvelles machines. Donc, ça peut causer des interruptions ou du moins des ralentissements dans certaines applications qui essayaient de scaler à ce moment-là. Donc on peut se dire, bon, arrivé 2h30, là, ça a dû se remettre à marche parce que DynamoDB était réparé. Mais ils disent, après avoir résolu les problèmes de DynamoDB à 2h30, les utilisateurs ont continué de voir des erreurs dans le lancement de nouvelles instants.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:20 - 00:07:53]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Au fait, là aussi, le système est découplé. En fait, c'est le cas partout. Parce qu'en un système qui a beaucoup de charges et que la charge peut varier beaucoup, tu ne veux pas directement qu'un utilisateur fasse une demande et que directement ça fasse la modification sur ton système. Tu veux en fait que l'utilisateur fasse une demande sa demande aille dans une file d'attente ça s'ajoute ici et ensuite tu vas avoir un programme qui va récupérer les demandes et qui va les effectuer sur notre système et de cette manière là l'utilisateur lui il a une réponse tout de suite quand il fait la demande de modification on peut tout de suite lui dire ok on a bien pris en compte ta demande de modification et de temps en temps on peut récupérer le statut

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:53 - 00:08:13]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> de cette modification pour savoir quand est-ce que ça a été fait et c'est le cas quand on va sur la double S et qu'on crée une machine on voit que la machine elle apparaît dans notre dashboard mais elle est en état pending ou en creating et en train de se configurer, etc. Donc ça, c'est évidemment indispensable quand c'est des actions qui prennent beaucoup de temps à faire parce que sinon, l'utilisateur, il va cliquer et si ça prend 45 secondes avant de lui répondre que la machine est là, c'est une expérience utilisateur qui est pourrie.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:13 - 00:08:42]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Même si c'est quelque chose qui est rapide, qui prend juste 100 millisecondes, c'est quand même utile d'utiliser ce système de fil d'attente parce que quand soudainement, tu as plein d'utilisateurs qui commencent à arriver et à faire des demandes de modification, même si ça prenait que 100 millisecondes avant, et bien là, ça peut prendre beaucoup plus de temps et donc on peut quand même répondre vite aux utilisateurs. Et en plus de ça, on peut scaler, Donc, si on voit que dans la liste d'attente, il y a beaucoup de demandes, on peut rajouter ici des workers, des programmes qui vont aller plus vite pour aller vider la file d'attente plus rapidement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:43 - 00:09:07]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, ça pour dire que dans EC2, c'est comme ça que ça fonctionne. On a notre utilisateur ici qui demande la création d'une instance. Il veut une EC2 ? Point d'interrogation. Et notre système ici, notre demande, elle est dans une liste d'attente ici. On a notre petit programme qui va prendre la requête quand il a le temps de le faire et qui va ensuite aller voir dans les machines disponibles pour pouvoir créer la machine et ensuite redire à l'utilisateur que sa machine est bien créée.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:07 - 00:09:36]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc ça, ça fonctionne bien, il n'y a pas de souci. Même s'il y a un peu plus de requêtes d'utilisateurs, les requêtes vont s'additionner un petit peu ici. Mais finalement, quand la demande va redescendre ou quand on va ajouter des programmes ici, ça va finir par redescendre. Mais là, le problème, c'est que pendant deux heures, trois heures, toutes les requêtes ici, elles ne pouvaient pas être exécutées. Ce qui fait que ça s'est tellement accumulé que même quand c'est revenu, il y avait tellement tellement de requêtes dans le backlog que même en rajoutant des programmes ici, il y en avait tellement que c'était impossible à rattraper.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:36 - 00:09:57]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ou du moins peut-être que ça aurait pris trois jours pour rattraper toutes les requêtes. Parce qu'en plus du nombre de requêtes qu'on va avoir normalement dans l'espace de 2-3 heures, en fait on a beaucoup plus que ça parce que les gens voient que ça ne marche pas, donc ils réessayent. Parfois tu as des bots qui réessayent aussi parce qu'ils sont codés comme ça. Et donc tu te retrouves à devoir régler les requêtes non seulement des 2-3 dernières heures, mais peut-être x10 parce que les gens ont réessayé, réessayé, réessayé, réessayé pendant tout ce temps-là.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:57 - 00:10:20]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc c'est pour ça que les gens voyaient des erreurs insufficient capacity. Le système leur disait non, je ne peux pas rajouter de nouvelles machines parce que je n'ai pas de capacité. En vrai, il y avait de la capacité, mais le système qui créait de nouvelles machines était tellement saturé qu'il disait qu'il n'avait plus de capacités. Et donc ce qu'ils ont fait pour fixer ça, c'est que premièrement, ils ont trottled, donc ils ont limité le nombre de requêtes que les gens pouvaient faire pour éviter que la liste d'attente continue de grossir.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:20 - 00:10:45]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que même s'il y a quelques machines qui démarrent, il y a trop de demandes de modifications qui sont rajoutées par rapport à ce qu'on peut traiter en temps réel. Donc ce qu'ils ont fait, c'est qu'ils ont tout simplement, comme on dit d'habitude dans l'outre-boot, c'est qu'ils ont redémarré certains de ces systèmes pour pouvoir vider les listes d'attente. Parce que la plupart de ces demandes-là de modifications, de création et d'effacement de machines virtuelles, la plupart c'était par exemple des demandes de suppression de machines qui n'existaient déjà plus, parce que c'est un script qui voulait créer une machine, mais comme il a réessayé, il a demandé 100 fois.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:45 - 00:11:05]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc au lieu d'attendre que la liste d'attente se vide par elle-même, ce qui peut ne jamais arriver parce qu'il y a tellement de requêtes dessus, et bien ils ont juste vidé la liste d'attente en gros. Et donc cette combinaison de vider la liste d'attente et de limiter le nombre de requêtes maximum que chaque utilisateur peut faire a fait qu'au final on a pu retrouver un état stable. Mais en fait non. Ça c'est le système qui permet de créer des machines virtuelles.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:05 - 00:11:27]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et en fait, tu as un autre système qui s'appelle le Network Manager qui permet lui, une fois que la machine est créée, de lui affecter sa configuration réseau. De lui dire ok, tu vas être dans tel VPC, c'est-à-dire tu vas être connecté à tel autre groupe d'instance, tu vas avoir tel règle de firewall, tu peux accéder à telle route, telle route, etc. Et ce système avait exactement le même souci. Il avait un backlog énorme de rétats réseaux à affecter à toutes les machines.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:27 - 00:11:46]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et il n'arrivait pas à rattraper toute la liste d'attente qu'il avait. Donc, ils ont appliqué les mêmes techniques pour pouvoir résoudre ce problème-là. Et à 10h du matin, donc on est déjà à 10-11h plus tard, et seulement à ce moment-là, ça a commencé à redevenir correct. En fait, c'est redevenu utilisable probablement un petit peu avant. Mais on était un peu dans un état où les gens avaient quand même un petit peu d'erreurs, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:46 - 00:12:05]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais de moins en moins. Une heure après, ils ont enlevé les limites. Et donc comme ça, on pouvait à nouveau recréer autant d'instances qu'on voulait. Mais ce n'est pas fini. Parce qu'il y a aussi les NLB qui ont été affectés. En gros, tu as deux types de load balancer chez AWS. C'est les NLB et les ALB. Les ALB, c'est plus pour les applications. Par exemple, une API, une application web, un site web, des choses comme ça.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:05 - 00:12:29]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et on a le NLB qui vont être plus pour si on a une application qui est accessible via TCP, via UDP, quelque chose comme ça, qui n'est pas un protocole HTTP en gros. Et bien, on peut utiliser un NLB pour pouvoir balancer la charge entre différents serveurs. Une de ces fonctionnalités, c'est de vérifier que chacune des machines est dans un état qui permet de répondre. Et donc, on a notre load balancer ici, qui balance le trafic entre plusieurs machines, comme ça.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:29 - 00:13:02]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et bien, si mon utilisateur, lui, il envoie des requêtes qu'à un seul endroit, au load balancer, le load balancer, il distribue sur des serveurs au hasard, mais en plus des requêtes des utilisateurs, il envoie aussi des requêtes de health check, une requête pour savoir si la machine en question, elle répond. Si une machine en question qui pour une raison ou pour une autre, elle arrête de répondre ou elle répond pas assez vite Et bah le load balancer, il va la considérer qu'elle est unhealthy, qu'elle est pas en bonne santé Et donc il va arrêter de lui envoyer du trafic Et donc comme ça pour l'utilisateur, c'est transparent parce que son trafic va être envoyé toujours sur une machine qui fonctionne correctement

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:02 - 00:13:35]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et après on peut avoir d'autres systèmes qui vont automatiquement effacer cette machine Et recréer une nouvelle qui fonctionne à nouveau Et à ce moment là le load balancer va continuer à lui renvoyer du trafic Donc tout ça c'est bien, sauf que dans notre cas ici le système de health check il a commencé à bugger un petit peu parce que parfois il arrivait à accéder à l'instance et parfois il n'arrivait pas et donc il s'est retrouvé dans un état où il y avait beaucoup d'instances qui étaient considérées comme unhealthy c'est-à-dire qui ne rentrent pas en bonne santé qu'elles ne répondent pas correctement même si au final peut-être que l'instance en elle-même elle est correcte mais le fait que sa configuration réseau soit pas bonne ou que cette instance elle n'arrive pas à accéder

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:35 - 00:13:54]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> à une base de données derrière ça a déclenché un failover quand un NLB détecte qu'il y a trop d'erreurs dans une des zones de disponibilité et bien il va complètement enlever toutes les machines de cette zone de disponibilité. Le problème c'est que ça aggravait encore plus le problème qu'il y avait sur EC2. Toutes les machines qui étaient dans cette zone de disponibilité ont été considérées comme indisponibles même si ce n'était pas forcément tous le cas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:54 - 00:14:27]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc ça a augmenté énormément la charge sur les autres machines qui sont dans les autres zones de disponibilité. Donc là imaginons que j'ai deux zones de disponibilité, une à gauche et une à droite. Si celle à droite ici j'ai trop de machines qui bug, qui répondent, qui répondent pas, et bien le load balancer il va dire ok dans cette zone de disponibilité là c'est le bordel. et bah on va tout enlever et il va complètement arrêter d'envoyer du trafic ici. Ce qui fait que quelque part c'est bon pour l'utilisateur parce qu'il va pas avoir des requêtes qui vont finir par arriver sur des serveurs qui bug mais ce qui se fait qu'on se retrouve là dans notre exemple on avait cinq serveurs on se retrouve avec plus que deux donc en temps normal ça peut ne pas être un

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:27 - 00:14:45]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> trop gros problème parce qu'on peut juste ici rajouter des nouveaux serveurs dans les autres zones de disponibilité sauf que souvenez-vous on peut plus redémarrer des nouvelles machines parce que EC2 est en train de bugger aussi. Ce qui fait que bah ici notre application elle commence à ralentir et à faire plein d'erreurs parce qu'elle n'a qu'une fraction des serveurs qu'elle devrait avoir pour pouvoir servir toutes les requêtes des utilisateurs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:14:45 - 00:15:04]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc pour pouvoir régler ce souci là, ce qu'ils ont fait c'est qu'ils ont désactivé les Health Check Failover des NLB pour éviter que ça arrive, pour éviter d'aggraver le problème. Et ça c'est quelque chose qu'on retrouve pas mal dans tout ce qu'ils ont fait. Ils n'ont pas essayé tout de suite de régler le problème parce qu'ils savent que parfois le problème peut prendre du temps à régler.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:04 - 00:15:25]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ils essayent de savoir qu'est-ce qu'on peut faire pour mitiger, qu'est-ce qu'on fait pour pouvoir le plus rapidement possible se retrouver dans un état qui est proche de fonctionnel. Quitte à faire des choses qui sont temporaires, désactiver certaines fonctionnalités pour au plus vite retrouver de l'uptime. Et comme ça, ça nous laisse du temps pour pouvoir fixer le vrai problème. Ensuite, ils donnent la liste de tous les autres services qui ont été impactés parce qu'évidemment, et la plupart des services vont utiliser aussi EC2.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:26 - 00:15:45]` | Segment #42

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc là, par exemple, SQS qui est un service de liste d'attente justement de QE. Les lambdas utilisent EC2, donc ça a été affecté. On a EKS, le service de Kubernetes, un service qui a été affecté parce que ça utilise aussi des machines EC2. Et donc, même si le problème venait à la base de DynamoDB, même si toi, ton application utilisait juste des lambdas, par exemple, eh bien, tu as quand même été affecté.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:45 - 00:16:04]` | Segment #43

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc maintenant que c'est réglé, OK, tout est rentré dans l'ordre, c'est fini. Non, pas tout à fait, parce qu'il faut faire en sorte maintenant que ça ne réarrive plus dans le futur. Parce que même si c'est rare et que c'est une reste condition qui arrive vraiment une fois sur un milliard, bon, là, pour le coup, c'est arrivé. Premièrement, c'est qu'ils ont désactivé le planeur et l'anacteur, l'automation, juste temporairement. Ils vont le réactiver, mais avant de le réactiver, ils vont fixer la reste condition.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:04 - 00:16:24]` | Segment #44

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ils vont faire en sorte que si l'anacteur doit réessayer, au moment où il réessaye, il faut qu'il revérifie si le plan est bien plus récent que celui qui va écraser. Pour NLB, ils vont ajuster un petit peu le mécanisme de failover de manière à ce que ça n'enlève pas trop trop de machine d'un coup et donc limiter l'effet qu'un seul NLB peut avoir dans le failover.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:24 - 00:16:48]` | Segment #45

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pour EC2, il faut faire des modifications dans la manière dont ce système qui affecte les machines sur le hardware. Comme ça, si jamais il y a un souci, le système peut retomber dans un état normal un peu plus rapidement et surtout automatiquement. Sans qu'il y ait besoin d'avoir une intervention manuelle, on va améliorer notre mécanisme de ralentissement et le rendre en fonction de la liste d'attente. Plus la liste d'attente va grossir, plus le ralentissement des requêtes utilisateurs va être agressif pour pouvoir essayer de revenir le plus rapidement possible en temps réel.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:16:48 - 00:17:06]` | Segment #46

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Au-delà du buzz de AWS et d'Inde, je trouve que c'est super intéressant de voir ces post-mortem parce qu'on peut à la fois voir d'où le problème vient et peut-être l'éviter sur notre propre système, voir comment est-ce qu'ils ont été fixés et aussi voir sous le capot comment fonctionne la grosse machine AWS. Quelques fois par an, je fais une formation avec un petit groupe de personnes pour pouvoir apprendre les différents outils pilés du DevOps.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:17:06 - 00:17:20]` | Segment #47

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, si ça t'intéresse, je te mets un petit lien dans la description. Et en attendant, la prochaine formation, qui est je ne sais pas encore quand, vu que je suis en train d'en faire une en ce moment, je te conseille de regarder cette vidéo qui explique comment faire une infrastructure tellement solide qu'elle peut résister même à ce type de problème où toute une région AWS ne fonctionne plus.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

