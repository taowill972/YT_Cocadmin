# 🎬 J'ai tracké tous les salaires des dev

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=Wv3ARXImFUg](https://www.youtube.com/watch?v=Wv3ARXImFUg)  
> **Date de publication** : 20260618  
> **Durée** : 00:08:29  
> **Identifiant vidéo** : `Wv3ARXImFUg`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **J'ai tracké tous les salaires des dev**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Linux & Outils Systèmes** : Administration système, automatisation et surveillance.
- **Conteneurisation & Cloud** : Déploiement et gestion d'environnements résilients.

### 🔑 Points Clés & Enseignements Stratégiques
- Maîtriser les fondamentaux réseau et système pour diagnostiquer efficacement les pannes.
- Privilégier les architectures simples et observables en environnement de production.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:21]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça c'est un site qui traque tous les salaires des devs en fonction des langages et des technos que j'ai créé il y a quelques mois. Mais le premier petit souci c'est que déjà ça traque que Paris. Et surtout au niveau infras c'est à moitié infaillible mais c'est aussi à moitié éclaté. Donc premièrement ce que je voulais faire c'était ajouter d'autres régions. Non seulement pour qu'on ait une meilleure idée des différences de salaire entre les régions. Mais aussi pour avoir plus de statistiques et plus fiable. Donc pour la partie scrapping ça n'a pas été trop trop compliqué à mettre à jour.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:21 - 00:00:56]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que j'ai utilisé le MCP de Bright Data qui sponsorise la vidéo on en reparlera plus tard. Donc j'ai juste dû faire 2-3 pompes pour lui dire ok bah fais moi la liste des régions Et puis à partir de maintenant pour chacune des régions tu vas récupérer toutes les offres d'emploi que tu peux trouver sur Indeed, LinkedIn et Freework Et comme parfois on a des fauchettes de salaires qui sont affichées Et bah ça nous donne une bonne idée de quel langage, quelle technologie, quelle région paye le plus Donc ça c'est cool mais comme maintenant on traque 15 régions au lieu de juste une Et bah ça fait 15 fois plus d'appels sur des serveurs Et donc c'est à peu près 15 fois plus lent à récupérer les données Donc forcément je me suis dit que j'allais paralléliser ça pour pouvoir faire plus de requêtes en même temps Pour que ça arrive plus vite Mais le petit souci, c'est que déjà je fais pas mal de requêtes pour avoir la liste des jobs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:56 - 00:01:14]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ensuite, je fais une requête par job pour pouvoir récupérer un peu plus d'infos. Et ça sur trois sites différents. Donc quand tu multiplies par 15, tu multiplies par 15 les chances de te faire bannir ton IP. Donc ça, c'est un des nombreux soucis qu'on peut avoir quand on scrape des données. Donc là, ce que j'ai fait, c'est que j'ai simplement utilisé des proxys de NetData qui vont en fait me donner plein d'adresses IP différentes pour qu'à chaque fois que je fasse une requête, ça passe à travers une nouvelle IP.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:14 - 00:01:33]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Comme ça, je suis tranquille et je ne me fais jamais cramer. Donc maintenant, c'est cool parce que j'ai beaucoup plus d'infos. Donc j'avais déjà les salaires par langage et par technologie, mais maintenant ils sont un petit peu plus précis. Mais j'ai aussi pu rajouter ces statistiques par région pour savoir quelle région paye le plus ou le moins, en fonction de quelle technologie, avec différentes cartes, différents graphiques, pour pouvoir calculer aussi le nombre d'offres d'emploi en fonction des régions.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:33 - 00:01:56]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pour voir aussi non seulement les salaires par langage, mais aussi le nombre d'offres d'emploi, parce que t'as des technos qui payent beaucoup plus que les autres, mais s'il n'y a jamais d'offres, ça sert à rien. Pour aussi potentiellement savoir si peut-être qu'il y a des régions où certaines technologies sont plus valorisées que d'autres. Donc maintenant le site a beaucoup plus d'infos, de statistiques, de graphiques, etc. Mais faut bien que je l'héberge quelque part et pas quelque part qui va cracher dès que je vais sortir cette vidéo et qu'il va y avoir direct des centaines ou des mille personnes qui vont cliquer dessus en même temps.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:56 - 00:02:15]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc celle-là j'ai mis en place une affra incassable mais à la fois ultra fragile en même temps. Mais juste avant ça je vais trop parler vite fait du sponsor de la vidéo, Braille Data, que j'avais déjà utilisé dans la première version du projet. Et honnêtement sans ça je pense que j'aurais jamais commencé. Parce que scraper les sites c'est vraiment une galère. Entre naviguer entre les pages, nettoyer les données, éviter les bannes. Tout qui pète parce que tous les trois jours il y a une virgule qui change sur les sites.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:15 - 00:02:35]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ça sur trois sites différents en même temps donc laisse tomber. Alors que là, j'ai utilisé leur scrapper managé. Donc en gros, si je veux récupérer les offres d'emploi de LinkedIn, ils me donnent une API toute faite. Et si demain, LinkedIn décide de déplacer le salaire et de le mettre à droite au lieu d'à gauche, bah, c'est pas mon problème. C'est Bright Data qui va mettre à jour leur scrapper et moi, j'ai rien à toucher. Au niveau infrat, comme je t'ai dit, moi, comme je scrappe une quinzaine de régions, j'ai énormément de chances de me faire ban.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:35 - 00:02:55]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et si je me fais ban mon IP de chez moi et que je peux plus aller sur LinkedIn, c'est quand même un petit peu chiant. Alors que là, avec leur proxy résidentiel, j'ai plus du tout à me soucier de ça. Ça me coûte littéralement quelques centimes par jour pour scraper tous les jobs de toutes les régions des trois différentes plateformes. Et surtout, je peux récupérer mes données beaucoup plus vite. En plus de ça, ils ont un MCP pour les agents IA. Et donc, ça permet de récupérer n'importe quelle donnée, n'importe quel site sans rien avoir à coder.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:55 - 00:03:27]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, c'est vraiment une solution tout en un pour tout ce qui est scrapping de données. Donc, si tu as des données à récupérer pour ton projet, je te recommande d'essayer Bright Data. Et avec le lien dans la description, tu as 15 dollars offerts. Ce qui est largement assez pour tester gratuitement un petit ou même un moyen projet. Et donc, pourquoi mon infra est infaillible ? Parce qu'en fait, je n'ai pas d'infra. j'utilise Cloudflare Pages qui est assez utile pour héberger des sites statiques et comme c'est hébergé par Cloudflare c'est redondé et mis en cache dans le monde entier, c'est super rapide, ça scale automatiquement et en plus c'est gratuit. Donc ce qui fait que le site il a quasi aucune chance de tomber. Et donc pourquoi est-ce que je dis que c'est quand même un peu éclaté ? C'est parce que quand je récupère tous ces jobs je les enregistre dans une base de données

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:27 - 00:04:01]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> et si j'ai une base de données je peux pas avoir un site statique. Et donc au départ j'avais ma base de données, j'avais mon backend mais les données qui sont affichées sur le site elles sont pareilles pour tout le monde et elles changent pas jusqu'au lendemain. Donc au final ce que j'ai fait c'est que je continue à enregistrer les jobs dans une base de données, mais chaque jour je génère une page qui est statique qui contient toutes les informations qu'on va avoir dans la page et c'est ce fichier statique là que j'envoie chez Cloudflare et qui est servi à tout le monde. Le souci avec ça c'est que le script qui fait tout ça il tournait sur une VM de test qui tourne sur une machine de test chez moi dans mon placard ici. Donc autant dire que le truc est down toutes les deux semaines, il n'y a pas de backup, il n'y a rien quoi. Donc pour fixer ça j'ai passé le script de scrapping

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:01 - 00:04:35]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> et de génération de la page sur GitHub Action qui est l'outil de CICID de GitHub et je l'ai configurer pour que chaque jour il lance ses étapes là de récupérer les données et générer la page et l'envoyer sur Cloudflare. Donc comme ça en théorie ça va marcher tous les jours. En théorie parce que GitHub en ce moment ils sont pas super up. Donc ça règle mon problème de fiabilité de mon pipeline et ça règle aussi mon problème de backup parce que du coup ma base de données c'est un fichier SQLite qui est dans mon repo et donc comme ça j'ai pas besoin de caisser la tête avec un backup non plus. Le souci encore avec ça c'est que maintenant que je scrape les 15 régions j'ai 15 fois plus de données et donc ma base de données est grossie de plus en plus. Et donc maintenant base

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:35 - 00:05:08]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> données fait 50, 60, 70 MO. Ce qui dépasse la limite de ce qu'on peut avoir dans un repo sur GitHub. Donc pour régler ce problème là, ce que j'ai fait c'est que j'ai utilisé Git LFS qui est un système qui va permettre de déporter ce fichier là dans un système de stockage différent. Comme ça Git va juste utiliser un pointeur vers ce fichier là et comme ça ton repo il reste d'une taille raisonnable. Et la limite de Git LFS dans GitHub je crois que c'est 1 giga donc ça me laisse quand même un petit peu le temps de voir venir. Donc là maintenant on a toutes les régions donc c'est par exemple tu es en Bretagne et je peux voir les différences de technologies qui sont les plus en demande en fonction de ton langage. Mais ce que j'ai surtout rajouté c'est la partie salaire.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:08 - 00:05:43]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc là on peut voir que ça fait juste quelques semaines que j'ai commencé à récupérer les données donc on avait juste Paris avant et puis maintenant on commence à avoir de plus en plus pour les régions. Et des trucs qui sont un petit peu bizarres. Donc par exemple quand on va voir les salaires moyens par langage, si on regarde les salaires et qu'on classe par le salaire en CDI, et bien là on voit que PHP est numéro 1. C'est à dire que PHP paye le mieux et quand même de loin. Par contre si on classe en termes de salaire par freelance, on voit que PHP est dernier. PHP est le moins bien payé en salaire freelance. Donc à la base je me suis dit peut-être que c'est parce qu'il n'y a pas assez d'offres d'emploi avec des salaires mais j'ai plus de 1000 offres d'emploi

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:43 - 00:06:16]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> pour développeurs PHP dans la base de données donc normalement ça devrait quand même être assez statistiquement significatif. Donc il y a potentiellement quelque chose à fouiller là-dedans. Peut-être que je ne sais pas, peut-être qu'il y a une plus grosse demande de PHP mais en freelance dans une certaine région ou quelque chose comme ça je sais pas mais c'est potentiellement quelque chose à creuser maintenant ici on voit les salaires par langage mais aussi en fonction de combien il y a d'offres donc c'est à dire que les points qui sont les plus en haut à droite c'est ceux qui à la fois beaucoup d'offres et à la fois des bons salaires et ceux qui sont en bas à gauche ça veut dire que c'est les moins bons salaires et en plus il y a pas beaucoup d'offres et donc idéalement on voudrait éviter ceux qui sont ici donc dans les pires on a php qui est le

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:16 - 00:06:53]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> moins bon salaire il ya quand même un certain nombre d'offres mais c'est pas le best mais encore une fois ça c'est les salaires en freelance donc potentiellement que le graphe serait peut-être inversé si j'avais fait ce graphe là avec les salaires cdi et on voit qu'on a aussi kotlin et peut-être potentiellement swift qui est un petit peu en dessous de la limite et dans les meilleurs entre guillemets on va avoir python qui est un petit peu plus payé que la moyenne et qui a quand même beaucoup beaucoup d'offres d'emploi après faut quand même garder en tête une chose c'est que entre le mieux payé qui est c++ mais il n'y a pas beaucoup d'offres donc c'est comme un peu niche. Et le moins bien payé qui est PHP, il y a peut-être 15% de différence entre le mieux

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:53 - 00:07:27]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> payé et le moins bien payé. Potentiellement ça veut dire que ça vaut peut-être pas le coup de choisir son langage en fonction de combien ça paie. Je vous ai mis la même chose pour la technologie, je vous laisserai aller voir si ça vous intéresse. Et ensuite pour les régions, donc on voit que Paris a les meilleurs salaires freelance à 453 euros par jour en moyenne et deuxième c'est Occitanie à 425. Mais on voit qu'il n'y a pas une si grosse différence, a peut-être 5% de différence. Si par exemple à Marseille le coût de la vie est peut-être 20% 30% moins qu'à Paris, peut-être que ça vaut le coup de gagner 5% moins. Donc à parer quelque chose qui est assez intéressant. Apparemment si on est en Bourgogne, c'est

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:27 - 00:08:02]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> pas la fête. Les salaires sont la moitié moins, moins que moitié moins la moyenne de la France. Ça n'a peut-être pas le coup d'aller là-bas, spécifiquement pour trouver un job en tech. Ensuite on recevait les salaires par langage, par région, pour voir si potentiellement des petites différences ici. Et comme d'habitude, on a les différentes technologies qui sont intéressantes à savoir en tant que développeur de tel ou tel langage. Donc par exemple, si on est développeur Java, tu vois que le CSED et le DevOps vont en moyenne augmenter ton salaire de 3%. Donc on va dire ok, ce n'est pas une si grosse augmentation. Mais par contre, le nombre d'offres d'emplois auxquelles tu peux appliquer si tu as ça sur ton CV, c'est plus de 36%. Pareil si tu

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:02 - 00:08:28]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> développeurs Python, l'appareil DevOps, ça n'affecte pas vraiment ton salaire mais par contre, ça te rajoute 40% d'opportunités en plus. Ça permet de savoir exactement les technologies qui sont les plus en demande pour un développeur. Ce qui fait que maintenant mon site a beaucoup plus de data dans beaucoup plus de régions. Il y a aussi beaucoup plus de statistiques, de graphiques, c'est aussi beaucoup plus fiable non seulement au niveau des chiffres, des statistiques qu'on affiche mais aussi au niveau de l'infra, au niveau du pipeline de déploiement, etc. Donc si tu veux savoir comment j'ai commencé à mettre en place le projet, à galérer un peu avec les scrappers, etc. Je te laisse aller voir cette vidéo.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

