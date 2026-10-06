# 🎬 Cette techno sur ton cv vaut +600€/mois

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=s1YBeSDnGnY](https://www.youtube.com/watch?v=s1YBeSDnGnY)  
> **Date de publication** : 20251209  
> **Durée** : 00:13:35  
> **Identifiant vidéo** : `s1YBeSDnGnY`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Cette techno sur ton cv vaut +600€/mois**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Linux & Outils Systèmes** : Administration système, automatisation et surveillance.
- **Conteneurisation & Cloud** : Déploiement et gestion d'environnements résilients.

### 🔑 Points Clés & Enseignements Stratégiques
- Maîtriser les fondamentaux réseau et système pour diagnostiquer efficacement les pannes.
- Privilégier les architectures simples et observables en environnement de production.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:20]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Moi je sais que maîtriser quelques technos DevOps pour un développeur, c'est OP. Mais en vrai, c'est plus un sentiment que quelque chose que je peux prouver concrètement. Ce qui serait bien, ce serait que je fasse un dashboard qui soit public, qui puisse récupérer un maximum d'offres d'emploi et pour chaque type de poste, qui peut montrer quelle technologie est la plus en demande et surtout celle qui paye le plus. Et comme ça, je pourrais mathématiquement prouver que connaître le DevOps, ça rapporte beaucoup plus.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:20 - 00:00:39]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ou pas parce que ça se trouve, en voyant les chiffres, ça sera pas le cas. Cette vidéo est sponsorisée par Bright Data, ce qui va pas mal m'aider dans mon projet, mais je vous en reparle tout à l'heure. Donc le premier truc qu'on doit faire, c'est récupérer le maximum d'offres d'emploi. Et ça, ça s'appelle du scrapping. Et il y a deux, trois façons différentes de scrapper des sites. Le premier cas, c'est simplement récupérer le contenu de la page et puis extraire les données qu'on a besoin.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:39 - 00:01:01]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça, c'est rarement le cas parce que maintenant, la plupart des sites, ils sont dynamiques, ils vont afficher une page qui est vide au début, puis ensuite, ils vont ajouter petit à petit les offres d'emploi dans la page. Ce qui fait que si on récupère juste le code de la page, les offres ne sont pas dedans. La deuxième chose qu'on peut faire, c'est trouver l'API que le site web utilise pour pouvoir récupérer les offres d'emploi. Et donc ça, en fouillant un petit peu dans le code de la page pour pouvoir savoir comment le site fonctionne, en général, on peut trouver d'où est-ce que le site récupère ces informations.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:01 - 00:01:21]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ensuite, on peut attaquer directement cette API. Et c'est beaucoup plus simple parce qu'on a les données déjà bien formatées pour pouvoir travailler dessus. Mais parfois, il y a des sites qui font en sorte que justement, ce ne soit pas super bien formaté, la page se charge en plusieurs morceaux, et après, chaque morceau est modifié, etc. Donc c'est un peu compliqué à récupérer. Et donc à ce moment-là, il faut utiliser une autre technique, c'est-à-dire carrément utiliser un navigateur, comme Chrome par exemple, pour pouvoir aller sur le site.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:21 - 00:01:41]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le JavaScript va faire tout ce qu'il a besoin pour pouvoir charger et afficher la page. Et une fois qu'elle est affichée, qu'elle est bien construite et affiche toutes les données qu'on veut, et bien là c'est beaucoup plus facile de pouvoir récupérer les éléments, récupérer tous les jobs dessus. Mais du coup c'est un petit peu plus compliqué. Il faut faire un script qui va aller récupérer exactement les bons éléments. Ces éléments peuvent bouger dans la page. Ton script peut marcher aujourd'hui mais dans une semaine ça ne remarche plus.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:41 - 00:02:16]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que les noms des éléments ont bougé ou ont été renommés ou des choses comme ça. Donc cette manière est un petit peu plus chiante. Et ça consomme beaucoup plus de ressources parce que tu as tout un navigateur qui est là pour pouvoir générer la page. Donc c'est beaucoup plus chiant. Et le premier site sur lequel j'ai essayé de récupérer des offres d'emploi, c'est Indeed, ce qui est un des plus connus. Et sur Indeed, c'était chaud. Parce que justement, ils sont dans ce cas-là. Les Cetob, ils récupèrent les jobs d'une API, mais cette API, c'est pas vraiment une API pour pouvoir bien coder. Donc du coup, il aurait fallu utiliser la deuxième technique, celle d'avoir un navigateur qui rend dans la page pour pouvoir récupérer les éléments, etc. Mais chez Indeed, ils sont un petit peu vicieux parce que parmi la liste de jobs, ils rajoutent des éléments qui ressemblent à des offres d'emploi mais qui n'en sont pas. Donc c'était casse-tête. Mais moi, quand je me suis cru malin,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:16 - 00:02:38]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> je me suis dit Indeed ils ont une application mobile. Et assez souvent les applications mobiles elles vont accéder à une API qui est différente que celle qui est utilisée pour des navigateurs. Parce que forcément c'est affiché différemment. Donc si ça récupère les éléments qui sont faits pour être affichés sur un grand écran sur un navigateur, sur un mobile ça va être pourri. Et donc j'ai installé l'appli, j'ai inspecté le trafic pour pouvoir voir ce que ça récupérait et ça récupère quand même exactement le même format que celui qui est affiché sur les navigateurs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:38 - 00:03:11]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc retour au point de départ. Donc là avant de commencer à moi-même coder mon scrapper etc parce que ça allait me casser un peu la tête, je regarde un petit peu sur GitHub pour voir ce qui se fait et je tombe sur un projet qui s'appelle Job Spy, qui est un petit script en petit ton qui permet directement de récupérer les oeuvres d'emploi de Indeed. Et donc je le teste et bizarrement ça marche du premier coup. Mais ça marche mais c'est quand même assez lent parce que ça doit faire la recherche, afficher la liste des emplois, aller sur chacune des pages d'emploi pour pouvoir récupérer les informations de quand ça a été posté, la description, etc. Et donc ce qu'on pourrait faire, c'est simplement faire beaucoup plus de requêtes beaucoup plus vite pour pouvoir récupérer les jobs beaucoup plus rapidement. Et si je fais ça de chez moi, je risque de me faire ban et après là ça va

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:11 - 00:03:35]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> commencer à être encore plus compliqué pour récupérer les oeuvres d'emploi. Mais c'est là où je me je me suis souvenu que dans un ancien projet, j'avais commencé à regarder différentes services pour pouvoir utiliser des proxys, et j'étais tombé sur Bright Data. Et un des services qui propose, c'est justement d'avoir plein de proxys, plein d'adresses IP partout dans le monde, très facilement. Donc je crée mon compte, je récupère un proxy, et juste en deux, trois clics, et en modifiant juste une seule ligne dans mon script, ça me permet de passer par 20 adresses IP différentes, et donc de récupérer le contenu 20 fois plus vite, et en étant 20 fois moins susceptible de me faire cramer.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:35 - 00:04:08]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et même si jamais je me fais bloquer une des idées IP, comme je peux l'avoir presque à l'infini, c'est plus du tout un problème. Et donc comme ça je récupère quelques centaines d'offres d'emploi et maintenant il faut que je les affiche. Donc je fais un petit frontend, je vibe code ça à l'arrache avec Codex et honnêtement avec Tchadjpt 5.1 ça marche vraiment bien. J'ai pas trop trop besoin de fouiller dans le code, juste de temps en temps il fait des trucs un petit peu bizarres mais tant que je suis là pour le recadrer, le garder dans le droit chemin, ça se passe bien. Et ça permet quand même d'aller beaucoup beaucoup plus vite que si c'était moi qui devais coder du frontend parce que c'est pas du tout pas du tout ma spécialité. Et je pense que la clé c'est de lui donner des tâches qui

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:08 - 00:04:40]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> sont de la bonne taille. Si elle lui donne une trop grosse tâche et qu'il n'y a pas assez de détails, et bien ça lui donne beaucoup trop d'opportunités de faire son truc qui va finir par soit pas marcher, soit être vraiment bizarre, soit bourré de failles de sécurité. Mais si on sait exactement ce qu'on veut faire, les outils qu'on veut utiliser, la bonne manière de faire, etc. Et bien en lui donnant juste des petits morceaux de tâche, ça permet d'avancer, itérer, essayer des choses très très rapidement. Donc maintenant il faut quand même plus de données que ça parce que j'ai quelques centaines de jobs mais c'est pas assez statistiquement significatif. J'aimerais en avoir le plus possible et je sais que sur LinkedIn il y a beaucoup d'offres d'emploi aussi. Et LinkedIn c'est presque encore pire que Indie, ça fait 50 000 requêtes à 50

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:40 - 00:05:06]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> trucs différents, c'est impossible de comprendre ce qui se passe et comment est-ce que la page est générée. Mais là encore une fois, en regardant les différentes fonctionnalités de Bright Data, je vois qu'ils ont des scrappers managés qui sont déjà faits. Donc là ça gare bien parce que j'ai pas de code à faire, j'ai pas besoin de le maintenir. Si jamais la page de LinkedIn elle change, mon scrapper va toujours marcher. Et je profite toujours de l'infrastructure de Bright Data, qui permet non seulement d'avoir plein de proxys et pas me faire bannir mon IP, mais aussi potentiellement de résoudre les captchas et toutes les mesures anti-robots qu'il y a sur plein de sites maintenant.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:06 - 00:05:24]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et en regardant, je me rends compte qu'ils avaient aussi un scrapper manager pour Indeed. Donc ça permettrait d'avoir un seul pipeline, un seul outil pour pouvoir récupérer mes données sur plein de sites différents et en même temps de garder le même format de données, même si ça vient de différents sites. Donc maintenant j'ai un peu plus de job, j'en ai à peu près 1000 et quelques. La première statistique que je peux faire, c'est regarder le nombre d'offres d'emploi postées en fonction du temps.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:24 - 00:05:58]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais comme j'ai récupéré juste les offres des dernières quelques semaines, peut-être un mois, c'est pas encore une métrique qui est très utile. Mais si je maintiens mon projet à petit à petit, ce que j'aimerais bien faire, je vais pouvoir voir dans le temps l'évolution du nombre d'offres d'emploi en fonction du temps. Mais ce qui m'intéressait à la base, c'était de voir les différents mots clés qu'il y avait dans les offres d'emploi pour savoir lesquels revenaient le plus souvent. Et donc je retourne sur mon petit codex et je lui demande de faire un petit script qui va extraire la description de chacun des jobs pour trouver certains mots clés comme Docker, Kubernetes, Ansible et donc de créer une nouvelle base de données qui contient non seulement le titre de job, la description et aussi toutes les technologies qui sont mentionnées dans l'offre d'emploi.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:58 - 00:06:29]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et maintenant je peux calculer le nombre de fois où ces mots clés y reviennent. Par exemple je peux prendre toutes les offres qui ont le mot clé Java dedans. Il y a des grandes chances pour que ce soit une offre de développement en Java. Et pour toutes ces offres-là, comptez le nombre de fois où revient chacune des technologies que j'ai trouvées. Donc combien de fois il y a Spring, combien de fois il y a SQL, combien de fois il y a Docker, combien de fois il y a Ansible. Et après je demande de faire un petit tableau et pour tous les langages, de me donner les technologies qui reviennent le plus souvent. Et donc là, on peut commencer à voir des choses intéressantes. Par exemple, pour les postes de développeurs Java, on voit que Spring revient dans 44% des offres d'emploi. Donc ça veut dire que c'est quelque chose qui est extrêmement demandé.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:29 - 00:07:02]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ce qui paraît logique parce que c'est un des frameworks Java les plus populaires. Mais ensuite en second on retrouve Angular. Et moi j'aurais pas pensé que Angular était beaucoup utilisé pour les développeurs Java. J'imagine que ça revient plus dans des postes de développeurs full stack qui vont faire un backend en Java et qui vont faire un frontend en Angular. Et ensuite parmi toutes les autres technologies qu'il y avait dans les offres d'emploi, on voit que DevOps revient dans 34% des jobs. C'est-à-dire qu'il y a quand même un tiers des jobs en Java qui demandent d'avoir des skills en DevOps. Ensuite on voit la même chose pour Git. Bon là ça c'est à peu près logique, j'imagine que 100% des jobs Java vont demander d'avoir un git. Mais derrière on a CI-CD, pareil pour un tiers encore. Et Docker, SQL et Kubernetes

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:02 - 00:07:26]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> reviennent eux aussi pour à peu près un tiers des jobs. Donc si on prend Kubernetes par exemple, si on assume que dans ces jobs-là qui ont mentionné spécifiquement Kubernetes, ça veut dire qu'ils ont besoin de quelqu'un qui connaît ça. Si on n'est pas au moins un tout petit peu familier avec Kubernetes, il y a un job sur trois sur lequel on n'aura pas exactement le bon profil. Évidemment en tant que développeur Java c'est plus important de connaître Spring que connaître Kubernetes, mais ça permet déjà de savoir en fonction de ce qu'on connaît déjà qu'est-ce qu'on peut rajouter pour avoir exactement le bon profil qui est recherché par les entreprises.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:26 - 00:07:47]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Maintenant qu'on a ça, c'est déjà pas mal, mais moi j'aimerais bien mettre un chiffre exact en euros pour pouvoir savoir exactement combien me rapporte chaque technologie. Le problème c'est que sur LinkedIn et sur Indeed, il n'y a très souvent pas les salaires. Mais il y a un autre site sur lequel il y a un peu plus d'informations qui s'appelle FreeWork, qui est un peu plus pour les freelances à la base. Mais l'avantage c'est que dans les offres freelance, très souvent il y a le TGM, c'est le tarif qu'on te paye à la journée.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:47 - 00:08:07]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et avec ça on va savoir exactement combien les entreprises sont prêts à payer en plus pour avoir quelqu'un qui connaît telle ou telle technologie. Ce qui est cool, c'est que Freework, ils ont une API privée. Privé parce que ce n'est pas vraiment une API que tu es censé utiliser, mais en tout cas, c'est l'API qui est utilisée par le site web, qui est très facile à utiliser, qui formate bien les données, etc. Donc, je retourne sur Bright Data. Ils n'ont pas de scrappeurs préfets dédiés pour Freework.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:07 - 00:08:30]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Par contre, ce qui est cool, c'est qu'ils ont un outil qui permet d'en générer un. J'ai juste à donner l'URL de Freework avec la liste des jobs que je vais récupérer et une petite description de ce que j'ai besoin, le titre des jobs, la date de publication, c'est quoi les salaires, etc. Et en deux minutes, ça me génère un script qui utilise toute l'infrastructure de Bride Data pour pouvoir scraper ce site-là. Avec encore une fois, tous les avantages d'être dans Bride Data, la résolution des captchas, l'utilisation des proxys, le fait d'avoir un seul outil pour pouvoir récupérer sur différents sites, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:30 - 00:08:52]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et là, je récupère d'un coup un petit peu plus de 1000 jobs, donc ce Freework a quand même pas mal d'offres. Après, c'est normal pour des offres freelance, j'imagine qu'il y en a un peu plus. Et donc, je rajoute tout ça dans ma base de données, qui contient déjà mes offres de LinkedIn et de Indeed. Sauf que maintenant, j'ai aussi des informations sur les salaires. Et donc, je peux retourner modifier mon front-end. Et ensuite je peux prendre toutes les offres de développeurs Java, calculer c'est quoi la moyenne de salaire de toutes les offres qui ne mentionnent pas Kubernetes, et calculer toutes les moyennes de salaire qui contiennent Kubernetes.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:52 - 00:09:17]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et je peux afficher la différence entre les deux. Et ça si je le fais pour toutes les technos, on va pouvoir savoir exactement lesquelles sont les plus demandées, et lesquelles rapportent le plus. Donc comme je vous ai dit, cette vidéo est sponsorisée par Braille Data, et avant même qu'ils me contactent, j'avais déjà prévu d'utiliser leurs services. Et pour ce projet ça m'a énormément simplifié la tâche. Parce que moi ce qui m'intéressait surtout c'était analyser la data, trouver les informations pertinentes etc. Mais toute la partie technique du scrapping, gérer les captchas, éviter les blocages d'IP, passer par des proxys, etc. C'est la partie qui est un peu plus casse-tête.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:17 - 00:09:50]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et pour ça, Brianata, ça m'a simplifié la vie à tous les niveaux. D'abord sur l'infrastructure, parce qu'ils ont une infinité de proxys que tu peux payer à la demande. Pour mon projet, ça m'a coûté juste quelques centimes pour pouvoir récupérer mes données à travers plein d'adresses IP différentes. Ensuite, j'ai testé leurs scrappers qui sont managés, et ça, c'était quand même assez stylé. Parce que par exemple, pour LinkedIn, en juste 2-3 clics, j'avais déjà récupéré 800 jobs. Sans ça, j'aurais dû galérer à faire un script, à me faire bloquer etc. Ça m'aurait cassé la tête. Et une autre fonctionnalité que j'ai découvert en faisant cette vidéo, c'est qu'ils ont aussi un MCP pour pouvoir connecter un agent IA pour qu'il puisse parcourir le web et récupérer les données en temps réel. Donc moi j'ai vraiment

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:50 - 00:10:26]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> bien aimé. Je vous conseille d'aller jeter un œil si vous avez des datas à récupérer. Et avec le lien dans la description, tu as droit à des crédits offerts pour pouvoir tester ça gratuitement. Donc là sur mes jobs Zava par exemple, on voit que Spring, bon ok c'est demandé dans la moitié des jobs, mais la différence de salaire c'est juste 3%. C'est-à-dire qu'on s'attend à ce que tu saches Spring mais n'ont pas forcément te payer beaucoup plus pour ça. Par contre on remarque que toutes les offres qui contiennent DevOps, elles sont payées en moyenne 11% de plus que les offres qui contiennent pas DevOps. Donc ça peut être intéressant à savoir. Pareil pour CI-CD et Docker, on n'est pas loin aussi des 10%. Si on veut savoir si c'est significatif, là pour les offres Java, j'ai 700 offres qui contiennent Java quelque part dans la description. Et pour Docker par exemple,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:26 - 00:10:53]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> sur 154 jobs qui contiennent des salaires, il y en a 43 qui mentionnent Docker et il y en a 111 qui ne mentionnent pas Docker. Et ceux qui ne mentionnent pas Docker payent en moyenne 431 euros, et ceux qui mentionnent Docker payent en moyenne 470 euros. Donc là ça veut dire que pour quelqu'un qui est développeur Java freelance, le fait de savoir Docker, ça lui fait gagner en moyenne 600 balles le plus par mois. C'est quand même pas négligeable. Là ici pour Python, on voit que DevOps est numéro 1. Donc DevOps est un des termes qui revient le plus souvent dans les offres pour Python. Mais par contre ce qu'il faut garder en tête, c'est les statistiques de co-occurrence.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:53 - 00:11:12]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ça veut dire que c'est aussi possible qu'il y ait des offres d'emploi pour un poste de DevOps qui comprennent le terme Python. Ce qui ferait du sens parce que dans le DevOps en général, quand on a des petits scripts à faire, très souvent ça va être en Python. Mais toutes les offres d'emploi que j'ai récupérées, c'est les offres d'emploi que j'ai récupérées avec le terme développeur. Donc l'écrasante majorité seront des offres de développeurs. À moins qu'il y ait des offres qui s'appellent développeurs experts DevOps.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:12 - 00:11:47]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> En tout cas, s'il y en a, il ne devrait pas y en avoir beaucoup. Pour JavaScript, ici on voit que React est demandé dans 40% des jobs et ça booste ton salaire de 20%. Donc là, c'est une énorme différence. Si tu es développeur JavaScript et que tu ne fais pas de React, c'est chaud pour toi. On peut aussi voir que par exemple, les jobs JavaScript, en moyenne sont payés 446 euros par jour et 52 000 euros par an. Et les offres en TypeScript sont en moyenne à 450 euros par jour, un petit peu plus, et 54 000 euros par an, donc un petit peu plus. Mais comme on peut voir, je me base plus sur les TGM que sur les salaires annuels parce que là, par exemple, j'ai que 9 jobs

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:11:47 - 00:12:20]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> avec un salaire. Ce n'est pas encore super super fiable. Mais j'espère qu'avec le temps, en récupérant les offres d'emploi chaque semaine, dans quelques mois, j'aurai des stats avec des salaires annuels qui seront un petit peu plus fiables. Et toujours pour JavaScript, on voit que Docker n'est demandé que dans un quart des jobs, donc ça permet quand même de s'ouvrir a pas mal de jobs en plus. Mais la différence de salaire est énorme avec 15% de salaire en plus. Pareil en Go, très probablement ça va être plus des offres plus DevOps que plus de développement Go pur. Parce que c'est là où on retrouve quand même pas mal d'outils. DevOps, Terraform, Prometheus, Linux, Docker, etc. Donc peut-être que dans une prochaine version, je ferai la même chose mais pour les postes plus d'infrastructures, d'administrateur système, d'expert DevOps,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:20 - 00:12:55]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> expert cloud, etc. Pour Kotlin qui est du développement mobile, on voit pareil, AWS plus 16%, Kubernetes plus 18%. Donc là évidemment pour du développement mobile Android, souvent ça va être soit du Java, soit du Kotlin. Donc on voit que Java est très très demandée, 62% des jobs. Donc c'est quelque chose qu'il faut absolument en savoir, mais c'est pas quelque chose qui va payer énormément plus. Alors que le fait en tant que développeur mobile de savoir se débrouiller un petit peu en AWS ou en Kubernetes, ça booste énormément ton salaire. Plus 18%, plus 16% pour AWS. Là c'est carrément 1600 euros en plus par mois pour un développeur Kotlin qui a la

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:12:55 - 00:13:30]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> spécialité Kubernetes. Donc ça vaut le coup quand même de s'y mettre. Donc même si les différences de salaire sont plus basées sur les DGM que sur les salaires annuels, je pense que c'est quand même une bonne indication pour comprendre ce qui est demandé et les technologies pour lesquelles les entreprises sont prêtes à payer beaucoup plus. Encore merci à Brydata. Et si jamais ça t'a motivé à apprendre des technologies DevOps, quelques fois par an je fais une petite formation en groupe pour apprendre ces technologies comme Docker, Kubernetes, AWS, Terraform, Prometheus, Ansible, tout ça en juste 6 semaines et avec des projets concrets que tu pourras rajouter sur ton CV pour pouvoir avoir exactement le profil parfait. Si tu veux rejoindre la prochaine session, je te mets un petit lien dans l'inscription. Et si tu veux mieux comprendre exactement à

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:13:30 - 00:13:34]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> quoi sert chaque outil DevOps, je te laisse avoir cette vidéo qui explique tout ça.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

