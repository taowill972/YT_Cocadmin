# 🎬 Déployer une app en prod est enfin devenu facile avec cet outil

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=63D29lhtqoY](https://www.youtube.com/watch?v=63D29lhtqoY)  
> **Date de publication** : 20250928  
> **Durée** : 00:19:12  
> **Identifiant vidéo** : `63D29lhtqoY`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé

Déployer des applications en production de manière simple, robuste et économique reste un défi récurrent pour les développeurs et administrateurs systèmes. Contrairement aux plateformes PaaS managées (Heroku, Vercel) qui imposent des surcoûts et des limitations, l'utilisation de serveurs dédiés nus (« bare-metal » ou VPS) offre une liberté totale mais complexifie la mise en œuvre de la CI/CD, de la gestion des certificats SSL et du provisionnement de bases de données.

La solution présentée réside dans l'utilisation de **Docploy**, un outil open source auto-hébergé qui s'installe via une unique commande et configure automatiquement l'environnement conteneurisé (Docker et Docker Swarm). Il fait office de PaaS personnel en s'interfinçant directement avec les principaux gestionnaires de code source (GitHub, GitLab, Bitbucket) ou des registres de conteneurs. Il automatise le build via des Dockerfiles, gère le reverse proxy, automatise l'émission de certificats SSL via Let's Encrypt, et simplifie le déploiement de services complémentaires (bases de données SQL et NoSQL).

Pour les équipes DevOps et les administrateurs systèmes, cet outil change la donne en comblant le fossé entre la complexité des orchestrateurs lourds (Kubernetes pur) et le manque de flexibilité des hébergeurs cloud managés. Il permet de s'affranchir des pipelines CI/CD complexes pour de petites et moyennes architectures, tout en conservant une maîtrise totale de l'infrastructure sous-jacente et des coûts d'hébergement.

---

### 🛠️ Outils, Modèles & Logiciels Présentés

* **Docploy** : Interface open source auto-hébergée de gestion et de déploiement d'applications conteneurisées, combinant la simplicité d'un PaaS et la liberté d'un serveur dédié.
* **Docker / Docker Swarm** : Moteur de conteneurisation et outil d'orchestration léger utilisé sous le capot pour isoler et exécuter les services et applications.
* **GitHub / GitLab / Bitbucket** : Plateformes de gestion de code source connectées à Docploy pour déclencher des déploiements automatisés sur événement (`push`).
* **Dockerfile** : Fichier de configuration décrivant les instructions de construction (build) de l'image de l'application à partir du code source.
* **Let's Encrypt** : Autorité de certification automatisée utilisée par Docploy pour générer et renouveler des certificats SSL/TLS valides et sécuriser le trafic HTTPS.
* **Bases de données (PostgreSQL, MongoDB, MariaDB, Redis, MySQL)** : Systèmes de gestion de bases de données déployables en un clic sous forme de services conteneurisés isolés.
* **Heroku / Vercel** : Solutions PaaS propriétaires et managées du marché, contrastant par leurs coûts et contraintes avec l'approche auto-hébergée de Docploy.

---

### 🔑 Points Clés & Enseignements Stratégiques

* **Installation universelle minimaliste** : Une seule ligne de commande suffit pour amorcer l'infrastructure complète sur un serveur vierge (installation de l'interface, de Docker et du moteur d'orchestration).
* **Affranchissement des contraintes PaaS** : L'utilisation de serveurs loués auprès d'hébergeurs économiques permet de réduire drastiquement les coûts par rapport aux offres cloud managées traditionnelles.
* **Isolation par projets et services** : La structure permet de cloisonner plusieurs applications et services hétérogènes (frontend, backend, bases de données) sur une seule et même machine hôte.
* **Sources de déploiement multiples** : Flexibilité totale dans l'importation du code source (dépôts Git distants, registres de conteneurs, archives ZIP ou images pré-buildées).
* **Automatisation native de la CI/CD** : Déclenchement automatique des builds et des mises en production sur simple `push` Git, éliminant la nécessité de configurer des pipelines complexes (Jenkins, GitHub Actions avancées).
* **Filtres de chemins de surveillance (*Watch Paths*)** : Possibilité de restreindre les déclenchements de déploiement aux modifications de répertoires spécifiques au sein du dépôt de code.
* **Standardisation via Dockerfile** : Adoption d'un standard universel de conteneurisation garantissant la reproductibilité des environnements de staging et de production.
* **Gestion automatique du reverse proxy et du routage** : Association transparente des noms de domaines personnalisés aux ports internes des conteneurs applicatifs (ex: redirection du trafic HTTP/HTTPS vers le port applicatif 5000).
* **Automatisation SSL/TLS intégrée** : Résolution des challenges Let's Encrypt nativement par l'outil pour garantir une sécurisation HTTPS immédiate et valide des services exposés.
* **Provisionnement instantané de bases de données** : Déploiement en un clic de services de bases de données relationnelles ou NoSQL pré-configurés (MongoDB, PostgreSQL, etc.) avec gestion des variables d'environnement.
* **Bonne pratique - Gestion des secrets** : Ne jamais coder en dur les identifiants de bases de données ou les chaînes de connexion dans le code source ; utiliser systématiquement les variables d'environnement injectées par l'interface de l'outil.
* **Erreur critique à éviter** : Négliger la persistance des données lors du déploiement de conteneurs de bases de données ; s'assurer que les volumes Docker sont correctement rattachés pour éviter toute perte de données en cas de redémarrage ou de mise à jour du conteneur.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:27]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je suis tombé sur le meilleur moyen de déployer une application en production. À la base, je voulais tester tous les différents outils qui permettent de déployer des applications en prod, mais il y en a un qui est largement au-dessus de tous les autres, et cet outil, c'est DocPloy. Premièrement, une des choses que j'ai aimées, c'est simplement l'installation. C'est simplement une seule commande. Et ça, ça va non seulement t'installer DocPloy, qui est une interface qui va te permettre de déployer tes applications, et ça va aussi t'installer Docker, et même Docker soit, mais on verra pourquoi par la suite, pour pouvoir déployer un ou plusieurs services, une ou plusieurs applications sur ton serveur.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant le site officiel de Dokploy et son interface d'administration (UI).

**Contenu textuel & Code** : Commande shell d'installation (`curl -sSL https://dokploy.com/install.sh | sh`) et paramètres de configuration du fournisseur de code source (GitHub Account, Repository, Branch, Trigger Type).

**Action / Démonstration** : Présentation du script d'installation automatisée de Dokploy et de l'interface de liaison avec les dépôts Git pour le déploiement d'applications.

![Page d'accueil du site web Dokploy affichant la commande d'installation rapide avec curl.](../screenshots/63D29lhtqoY/63D29lhtqoY_000014_seg1.jpg)
*📸 00:00:14 — Page d'accueil du site web Dokploy affichant la commande d'installation rapide avec curl.*

![Interface d'administration de Dokploy montrant la configuration des providers (GitHub, GitLab, Bitbucket, etc.) et des dépôts pour le déploiement.](../screenshots/63D29lhtqoY/63D29lhtqoY_000021_seg1.jpg)
*📸 00:00:21 — Interface d'administration de Dokploy montrant la configuration des providers (GitHub, GitLab, Bitbucket, etc.) et des dépôts pour le déploiement.*

---

### ⏱️ `[00:00:27 - 00:00:46]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc évidemment, contrairement à des SaaS comme Heroku ou Vercel, il va falloir avoir son propre serveur. Mais l'avantage, c'est que tu peux trouver n'importe où, prendre un hébergeur pas cher et avoir ton propre serveur. Une fois qu'on a installé Docploy, on se retrouve sur cette interface. On va venir pouvoir créer un projet. Parce que même si on n'a qu'un seul serveur, maintenant on peut déployer autant de projets et d'applications différentes sur notre serveur.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface Web de l'outil de déploiement Docploy avec une modale de création de projet.

**Contenu textuel & Code** : Formulaire "Add a project" avec les champs "Name" (saisi: Vandelay Industries) et "Description", ainsi qu'un bouton "Create".

**Action / Démonstration** : Configuration et création d'un nouveau projet dans l'interface de gestion Docploy.

![Interface Web de gestion Docploy affichant une modale pour ajouter un nouveau projet (nom et description).](../screenshots/63D29lhtqoY/63D29lhtqoY_000041_seg2.jpg)
*📸 00:00:41 — Interface Web de gestion Docploy affichant une modale pour ajouter un nouveau projet (nom et description).*

---

### ⏱️ `[00:00:46 - 00:01:09]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ici, mon projet, je vais l'appeler jeu2048. Vous allez savoir pourquoi juste après. Et donc, j'ai mon projet. Et dans un projet, je vais avoir différents services. Parce qu'une application, elle peut avoir différents morceaux. va y avoir l'application en elle-même, l'application Python, en Node.js ou en Java. Donc on va venir ici faire créer un service et ça va être une application. Mon application ici, c'est une application Node, donc je vais l'appeler Node, ce qui fait que mon app sera jeu 2048 Node.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion d'infrastructure / PaaS self-hosted (Coolify v0.24.12)

**Contenu textuel & Code** : Projet nommé 'jeu-2048', menu de création de services avec les types de ressources disponibles (Application, Database, Compose, Template, AI Assistant)

**Action / Démonstration** : Navigation dans l'interface pour ajouter un nouveau service de type Application au projet jeu-2048

![Interface de gestion de projet (type Coolify) montrant la création d'un service au sein du projet 'jeu-2048' avec un menu déroulant affichant les options 'Application', 'Database', 'Compose', 'Template' et 'AI Assistant'.](../screenshots/63D29lhtqoY/63D29lhtqoY_000103_seg3.jpg)
*📸 00:01:03 — Interface de gestion de projet (type Coolify) montrant la création d'un service au sein du projet 'jeu-2048' avec un menu déroulant affichant les options 'Application', 'Database', 'Compose', 'Template' et 'AI Assistant'.*

---

### ⏱️ `[00:01:11 - 00:01:34]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc j'ai créé mon application. Maintenant, comment est-ce que je fais pour pouvoir récupérer mon application en elle-même, le code de mon application pour que ça tourne sur mon serveur ? Eh bien, je vais venir ici dans mon appli. C'est un des premiers trucs que j'ai trouvé incroyable dans Doploy, qui est un outil open source d'ailleurs, je ne vais pas préciser. On va pouvoir récupérer son application depuis différentes sources. Ça peut être depuis GitHub. Donc moi, j'ai déjà ajouté mon compte GitHub, mais si ce n'est pas le cas, c'est juste deux, trois clics pour connecter Dockploy à GitHub.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de l'outil open-source Doploy avec menu latéral (Projects, Monitoring, Docker, Swarm, etc.) et section Provider.

**Contenu textuel & Code** : Sélection des providers de code (GitHub, GitLab, Bitbucket, Gitea, Docker, Git, Drop), champs pour le compte GitHub, le dépôt, la branche, le chemin de build (Build Path), le type de déclenchement (Trigger Type : On Push), et les chemins surveillés (Watch Paths).

**Action / Démonstration** : Présentation et explication de la configuration de la source du code pour l'application dans Doploy, permettant de lier un dépôt distant au serveur.

![Interface de configuration de Doploy montrant la sélection des fournisseurs de code source (GitHub, GitLab, Bitbucket, Gitea, Docker, Git, Drop) et les paramètres de dépôt.](../screenshots/63D29lhtqoY/63D29lhtqoY_000122_seg4.jpg)
*📸 00:01:22 — Interface de configuration de Doploy montrant la sélection des fournisseurs de code source (GitHub, GitLab, Bitbucket, Gitea, Docker, Git, Drop) et les paramètres de dépôt.*

---

### ⏱️ `[00:01:34 - 00:01:53]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et c'est la même chose si on utilise GitLab, si on utilise Bitbucket ou un autre type de repo. Ça peut aussi être un conteneur Docker. Donc je peux le pointer directement vers un registri Docker, comme par exemple Docker Hub ou quelque chose comme ça. Ça peut être un repo Git perso ou on peut même dropper directement un zip avec mon code dedans. Donc là, vraiment, il y a plein, plein, plein de façons différentes de dropper son code là-dedans.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:53 - 00:02:11]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Dans mon cas, ça va être GitHub. Donc je vais prendre mon compte, je vais choisir mon repo. Donc mes repos, ça va être 2048. Je vais choisir ma branche. En général, ça va être main, mais peut-être que je vais avoir une autre branche que je vais déployer. Donc moi ici, je vais choisir une branche qui s'appelle Dockerfile. Là ici, le chemin de bulle, c'est à quel endroit on va se mettre pour pouvoir builder notre application.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:11 - 00:02:34]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que notre code, il faut le builder, il faut le construire, il faut peut-être le compiler, il faut peut-être installer des modules, juste comme ça. Ou il faut peut-être créer une image Docker, on va voir juste après. Ensuite, ce qui est vraiment cool, c'est qu'on peut choisir le type de déclenchement. déclenchement. Donc à quel moment est-ce que notre application va être déployée ? Parce que je peux le faire manuellement mais je peux aussi faire en sorte que automatiquement dès qu'il y a un commit sur telle ou telle branche, eh bien ça déploie la nouvelle version automatiquement sur mon serveur.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Plateforme de PaaS/déploiement Dokploy (version v0.24.12) avec son menu latéral (Projects, Monitoring, Schedules, Docker, Swarm).

**Contenu textuel & Code** : Paramètres de liaison GitHub : compte, dépôt ("2048-mern"), branche ("dockerfile"), chemin d'accès (" / "), type de déclencheur ("On Push") et encadré d'avertissement sur les ressources système recommandées pour le build (4+ Go de RAM et 2+ CPU).

**Action / Démonstration** : Explication de la configuration de l'intégration continue (CI/CD), spécifiquement le choix du déclencheur ("Trigger Type") automatique lors d'un push de code sur le dépôt.

![Interface d'administration de Dokploy affichant la configuration d'un déploiement (dépôt GitHub 2048-mern, branche dockerfile, et Trigger Type réglé sur On Push).](../screenshots/63D29lhtqoY/63D29lhtqoY_000222_seg7.jpg)
*📸 00:02:22 — Interface d'administration de Dokploy affichant la configuration d'un déploiement (dépôt GitHub 2048-mern, branche dockerfile, et Trigger Type réglé sur On Push).*

---

### ⏱️ `[00:02:34 - 00:02:55]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ce qui peut être un petit peu plus casse-tête à faire si je dois faire de la CI-CD. Là j'ai même pas besoin, je peux juste choisir ici on push. Donc quand je vais faire un push sur mon réponse git, ça va partir en prod sur mon serveur. Et je peux aussi mettre un watch path. Donc c'est à dire que je peux surveiller un chemin dans lequel je vais faire des modifications. C'est à dire que si je fais des modifications en dehors de ce chemin-là, ça ne va pas déclencher une mise en prod.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Dokploy (dashboard de déploiement et d'hébergement open-source).

**Contenu textuel & Code** : Configuration du dépôt Git (2048-mern), sélection de la branche (dockerfile), trigger type réglé sur 'On Push' et champ Watch Paths.

**Action / Démonstration** : Configuration des options de déploiement automatique sur push Git sans passer par une configuration CI/CD complexe.

![Interface de configuration de déploiement (Dokploy) montrant les paramètres du dépôt Git, la branche, le type de déclenchement (On Push) et les chemins surveillés (Watch Paths).](../screenshots/63D29lhtqoY/63D29lhtqoY_000244_seg8.jpg)
*📸 00:02:44 — Interface de configuration de déploiement (Dokploy) montrant les paramètres du dépôt Git, la branche, le type de déclenchement (On Push) et les chemins surveillés (Watch Paths).*

---

### ⏱️ `[00:02:55 - 00:03:27]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est encore grave stylé aussi. Ensuite on peut se dire bon bah ok on va construire mon application, mais ça dépend de l'application. Si c'est une application en Java, ça ne se construit pas de la même manière qu'une application en Python. Et bah ici encore une fois on a différents types de builds. On a des Dockerfiles qui est une des façons les plus pratiques de construire une application. Si tu n'as jamais utilisé, je te recommande de t'y mettre, il serait temps. Mais si par exemple tu étais sur Heroku et bah voilà. Si par exemple c'est juste un site web statique, tu peux faire un un site web statique. Si tu es un appli en Rails, tu peux utiliser des Rails pack. Et donc ici, nous, on va utiliser un Dockerfile. Donc il y a vraiment plein de façons différentes de

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de déploiement (type Coolify ou plateforme PaaS similaire) avec un menu latéral (Projects, Monitoring, Docker, Swarm) et un panneau de configuration central.

**Contenu textuel & Code** : Liste des options de type de build : "Dockerfile", "Railpack (New)", "Nixpacks", "Heroku Buildpacks", "Paketo Buildpacks", et "Static", ainsi qu'un champ "Publish Directory".

**Action / Démonstration** : Explication et démonstration des différentes méthodes de construction et de packaging d'application (Buildpacks vs Dockerfile) selon le langage utilisé.

![Interface graphique de configuration d'un projet montrant les différentes options de type de build ("Build Type") disponibles pour packager une application.](../screenshots/63D29lhtqoY/63D29lhtqoY_000311_seg9.jpg)
*📸 00:03:11 — Interface graphique de configuration d'un projet montrant les différentes options de type de build ("Build Type") disponibles pour packager une application.*

---

### ⏱️ `[00:03:27 - 00:03:52]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> construire ton application. Là, ici, le chemin de mon Dockerfile, ça va simplement être Dockerfile. Donc là, je vais vous montrer l'application pour le coup. C'est une petite application que j'aime bien utiliser en exemple et qui a un fichier ici Dockerfile. Et le fichier Dockerfile, il va utiliser l'appli Node. On va venir copier tous les fichiers de mon repo et les mettre dans usr.src.app qui va être l'endroit où on va exécuter notre application. Donc c'est ça ce fichier là qui va être utilisé.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web GitHub (dépôt de code source).

**Contenu textuel & Code** : Fichier Dockerfile montrant les instructions : FROM node:23-slim, COPY, WORKDIR, RUN npm install, EXPOSE 5000 et CMD ["npm", "run", "start"].

**Action / Démonstration** : Présentation et explication du contenu du fichier Dockerfile utilisé pour packager l'application Node.js.

![Interface GitHub affichant le contenu d'un fichier Dockerfile pour une application Node.js.](../screenshots/63D29lhtqoY/63D29lhtqoY_000339_seg10.jpg)
*📸 00:03:39 — Interface GitHub affichant le contenu d'un fichier Dockerfile pour une application Node.js.*

---

### ⏱️ `[00:03:52 - 00:04:25]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Quel est le contexte de mon Dockerfile ? Donc si par exemple je faisais dans ma ligne de commande docker-build. Et bien point c'est le contexte, c'est-à-dire le dossier actuel. Donc là pareil ça va être point, on peut le laisser par défaut. Et le build stage, si on a des multi-stage build, c'est pas mon cas donc j'ai pas besoin de le mettre. Si tu sais pas c'est quoi, c'est que tu l'utilises pas donc il n'y a pas vraiment besoin de savoir. Donc on a quand même quelque chose d'assez puissant qui permet de nous faire de la CSID, de construire des images Docker etc. sans être trop compliqué, sans avoir un milliard d'options qui ne sert à rien, etc. C'est-à-dire que même les options, si je ne sais pas exactement ce que c'est, à partir du moment où je laisse par défaut, ça me convient. Et donc là, ici, si je fais sauvegarder, hop, j'ai sauvegardé, je peux venir

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:25 - 00:04:59]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> ici faire déployer. Et donc là, est-ce que je n'ai sûr ? Ok. Et j'ai mon déploiement qui est en cours. Donc là, ce qui est en train de se passer, c'est que deploy va aller chercher sur mon repo GitHub, il est connecté à mon compte GitHub. Donc si on a un compte privé, évidemment, on peut quand même avoir accès. Il va récupérer mon repo, il va builder avec le Dockerfile et d'ailleurs on peut voir ce qu'il est en train de faire ici avec Vue. Il récupère mon repo, il se met dedans et il build le Dockerfile et le build ensuite cette image là qu'il a buildé, il va la lancer sur mon serveur. Une fois que ça c'est fait, il a créé l'image et il bouge. Donc là mon application

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web Dokploy, console de logs de déploiement.

**Contenu textuel & Code** : URL Webhook, logs de build Docker, étapes 'Cloning Repo', 'Build dockerfile', 'Source Type: github'.

**Action / Démonstration** : Suivi et explication du processus de déploiement automatisé depuis GitHub vers le serveur Dokploy.

![Interface de déploiement Dokploy montrant le statut 'Running' d'un build Node.js et l'URL du webhook Git.](../screenshots/63D29lhtqoY/63D29lhtqoY_000434_seg12.jpg)
*📸 00:04:34 — Interface de déploiement Dokploy montrant le statut 'Running' d'un build Node.js et l'URL du webhook Git.*

![Logs en temps réel du déploiement Dokploy affichant le clonage du dépôt GitHub, le build Docker et les étapes de build d'une application Node.js.](../screenshots/63D29lhtqoY/63D29lhtqoY_000451_seg12.jpg)
*📸 00:04:51 — Logs en temps réel du déploiement Dokploy affichant le clonage du dépôt GitHub, le build Docker et les étapes de build d'une application Node.js.*

---

### ⏱️ `[00:04:59 - 00:05:35]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> elle est déployée, elle tourne déjà sur mon serveur. Si je vais dans Docker ici, je vois ici que j'ai un conteneur qui tourne depuis 50 secondes qui s'appelle jeu 2048 node blablabla. Donc là ça tourne. Maintenant comment est-ce que je fais pour y accéder ? Je reviens dans mon application ici et je vais dans Domaine. Première chose c'est que mon serveur il a une adresse IP qui est accessible depuis l'internet donc je pourrais accéder avec l'adresse IP mais bon c'est pas très pratique. Donc ce que je vais faire, ce que j'ai déjà fait, c'est que j'ai créé un nom de domaine qui s'appelle Coca0 et j'ai créé le sous-domaine 2048.coca0 et je l'ai pointé vers l'adresse IP de mon serveur, l'adresse IP publique de mon serveur. Ce qui fait qu'ici dans Domaine,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Console d'administration DNS Cloudflare

**Contenu textuel & Code** : - Domaine configuré : coca0.xyz
- Enregistrement A : Nom `2048` pointant vers `3.84.117.28` (statut "Proxied" activé)
- Enregistrement CNAME : pointant vers une cible spécifique

**Action / Démonstration** : Configuration des enregistrements DNS et du routage réseau pour permettre l'accès public au conteneur Docker "jeu 2048" déployé sur le serveur via un sous-domaine dédié.

![Interface d'administration Cloudflare montrant la configuration des enregistrements DNS (DNS Records) pour le domaine coca0.xyz, avec un enregistrement de type A pour le sous-domaine 2048 pointant vers l'adresse IP 3.84.117.28.](../screenshots/63D29lhtqoY/63D29lhtqoY_000526_seg13.jpg)
*📸 00:05:26 — Interface d'administration Cloudflare montrant la configuration des enregistrements DNS (DNS Records) pour le domaine coca0.xyz, avec un enregistrement de type A pour le sous-domaine 2048 pointant vers l'adresse IP 3.84.117.28.*

---

### ⏱️ `[00:05:35 - 00:06:08]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je peux faire ajouter un domaine. Mon domaine ça va être 2048.cocas0.xyz. Ça va être quoi le chemin ? Parce que peut-être que j'ai une application qui s'attend à avoir un chemin slash api ou quelque chose comme ça. Bon là dans mon cas c'est pas le cas, mais si je voulais ce serait pratique que je puisse le faire. Et on a le port qu'on va vouloir taper dans le conteneur. Donc là si on regarde en fait dans mon application, pour le coup il se trouve que mon app elle est coûte sur le port 5000. Donc je peux venir ici et dire ok tu vas envoyer les requêtes qui rentre, tu vas les envoyer sur le port 5000. Mais Docploi, il va écouter sur les ports HTTP pour

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:08 - 00:06:43]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> pouvoir avoir vraiment un vrai site web. Donc il va écouter sur le port 80 en HTTP, mais il va aussi écouter sur le port 443 en HTTPS si j'ai besoin d'avoir des HTTPS qui est quand même un minimum. Donc ce que je peux faire, je peux acheter un domaine, je peux acheter d'ailleurs autant de domaines que ce que je veux. Remettre encore 2048.coca0.xyz, encore le port 5000 parce qu'on va toujours dans le même conteneur, sauf que cette fois-ci, je peux dire ok, je vais écouter en HTTPS sur le port 443 et je vais choisir ici Let's Encrypt ou même un provider custom si on veut, pour pouvoir aller générer un certificat. Donc Doploy va résoudre le challenge que Let's Encrypt va lui envoyer pour pouvoir récupérer un certificat SSL qui est valide pour le domaine

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de déploiement (type PaaS ou reverse proxy dashboard)

**Contenu textuel & Code** : Champs de configuration visibles : Host (2048.coca0.xyz), Path (/), Internal Path (/), Strip Path (désactivé), Container Port (5000), option HTTPS pour l'approvisionnement automatique de certificat SSL.

**Action / Démonstration** : Configuration d'un sous-domaine et association d'un conteneur applicatif sur le port interne avec option de génération de certificat HTTPS.

![Interface de configuration d'un service (reverse proxy/PaaS) montrant le paramétrage du nom de domaine, des chemins et du port conteneur.](../screenshots/63D29lhtqoY/63D29lhtqoY_000626_seg15.jpg)
*📸 00:06:26 — Interface de configuration d'un service (reverse proxy/PaaS) montrant le paramétrage du nom de domaine, des chemins et du port conteneur.*

---

### ⏱️ `[00:06:43 - 00:07:16]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> 2048.coca.min.xyz. Et ensuite quand je vais sur mon domaine en HTTPS, ça fonctionne avec le certificat que j'ai récupéré de Let's Encrypt. Donc quand je viens ici en SSL, j'ai bien ma connexion qui est sécurisée et j'ai bien un certificat qui est valide. Donc ça déjà, c'est déjà pas mal. Maintenant notre application, ok elle fonctionne mais jusqu'à présent c'est juste un site statique. Donc là j'ai une partie ici qui récupère les highscores et qui ne fonctionne pas parce que j'ai pas de passe de données pour pouvoir sauvegarder mes scores. Donc la plupart des applications vont avoir besoin de plus que juste l'application en elle-même, elles vont avoir

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant l'application web 2048.

**Contenu textuel & Code** : Jeu 2048 v1 avec score et message d'erreur : "Failed to load high scores: HTTP error! Status: 500".

**Action / Démonstration** : Test de l'application web et constat d'une erreur HTTP 500 liée au chargement des meilleurs scores.

![Interface du jeu 2048 v1 affichant une grille avec des nombres et une erreur HTTP 500 au niveau des meilleurs scores.](../screenshots/63D29lhtqoY/63D29lhtqoY_000708_seg16.jpg)
*📸 00:07:08 — Interface du jeu 2048 v1 affichant une grille avec des nombres et une erreur HTTP 500 au niveau des meilleurs scores.*

---

### ⏱️ `[00:07:16 - 00:07:53]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> besoin de services comme par exemple des passes de données. Donc je vais revenir ici dans mon projet et je vais rajouter un service. Et là dans les services qu'est-ce qu'on a ? Soit Compose parce que d'ailleurs je ne vais pas montrer mais si j'avais un fichier Docker Compose avec toutes les listes des services que j'avais besoin et pas boum je le mettrais dedans, on en parlera même plus, ça serait réglé. On a une section template ici avec plein d'applications pré-configurées qu'on pourrait déployer donc si on veut avoir un homelab et puis déployer des petits services, des petites applications open source ça peut être cool. Mais dans le cas de mon application je voudrais déployer une base de données et donc là ça me propose directement d'utiliser soit Postgre, soit MongoDB, soit MariaDB, soit Redis, soit MySQL ce qui est dans 99% des gals les bases de données

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de type PaaS/Coolify (projets, services, déploiements).

**Contenu textuel & Code** : Menus contextuels de création de services (Application, Database, Compose, Template, AI Assistant) et bibliothèque de templates open-source.

**Action / Démonstration** : Exploration des différentes options de services disponibles pour enrichir le projet en cours de configuration.

![Interface de gestion de projet montrant le menu d'ajout de service avec les options Application, Database, Compose, Template et AI Assistant.](../screenshots/63D29lhtqoY/63D29lhtqoY_000725_seg17.jpg)
*📸 00:07:25 — Interface de gestion de projet montrant le menu d'ajout de service avec les options Application, Database, Compose, Template et AI Assistant.*

![Catalogue de templates open-source permettant de déployer rapidement des applications préconfigurées comme Ackee, Activepieces, Actual Budget ou AdGuard Home.](../screenshots/63D29lhtqoY/63D29lhtqoY_000735_seg17.jpg)
*📸 00:07:35 — Catalogue de templates open-source permettant de déployer rapidement des applications préconfigurées comme Ackee, Activepieces, Actual Budget ou AdGuard Home.*

![Vue de la console du projet avec le menu déroulant pointant sur l'option 'Database' lors de la création d'un service.](../screenshots/63D29lhtqoY/63D29lhtqoY_000744_seg17.jpg)
*📸 00:07:44 — Vue de la console du projet avec le menu déroulant pointant sur l'option 'Database' lors de la création d'un service.*

---

### ⏱️ `[00:07:53 - 00:08:27]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> que je vais utiliser. Moi pour le coup mon application a besoin d'une base de données MongoDB. Là je vais lui donner un nom, je vais l'appeler MyMongo et donc ici ça va être Gio 2048 MyMongo. Je peux lui spécifier un utilisateur donc on va mettre ici username, très sécurisé et password comme password. Voilà je ne le dis ta personne. Je peux choisir l'image parce que ça va être une image Docker donc si je veux une version spécifique je vais pouvoir lui dire mais par défaut elle va me prendre la version aussi ce qui me va très bien. Et je vais faire ici dans Mongo. Il faut que je clique sur Déploy pour le lancer. Est-ce que vous êtes sûr ? Confirmez.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de déploiement et de gestion (type PaaS/Coolify).

**Contenu textuel & Code** : Liste des services du projet 'jeu-2048' incluant 'my-mongo' et 'node', menu latéral de navigation (Projects, Monitoring, Docker, Swarm, etc.).

**Action / Démonstration** : Validation de la création d'une base de données MongoDB pour l'application Node.js du jeu 2048.

![Interface de gestion de projet montrant les services 'my-mongo' et 'node' dans l'environnement 'jeu-2048' avec la notification 'Database Created'.](../screenshots/63D29lhtqoY/63D29lhtqoY_000819_seg18.jpg)
*📸 00:08:19 — Interface de gestion de projet montrant les services 'my-mongo' et 'node' dans l'environnement 'jeu-2048' avec la notification 'Database Created'.*

---

### ⏱️ `[00:08:27 - 00:08:48]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et c'est en train de démarrer mon conteneur qui contient ma base de données MongoDB. Maintenant, il reste une dernière petite chose à faire, c'est que mon application, il faut qu'elle communique avec ma base de données. Là, ici, mon déploiement a tout bien marché, etc. Donc, il faut que je revienne dans mon application ici. Et mon application, elle prend des variables d'environnement. Donc, si on vient dans mon application ici, si ton application est à peu près bien faite, elle va prendre des variables d'environnement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Dokploy (dashboard de gestion de conteneurs).

**Contenu textuel & Code** : Paramètres de déploiement du projet my-mongo, port interne MongoDB (27017), hôte interne et boutons d'action (Deploy, Reload, Stop, Open Terminal).

**Action / Démonstration** : Explication de la configuration réseau et des identifiants du conteneur MongoDB pour permettre la communication avec l'application.

![Interface de gestion Dokploy montrant les paramètres de déploiement d'un conteneur MongoDB ("my-mongo") avec les boutons Deploy, Reload, Stop et les informations d'identification internes.](../screenshots/63D29lhtqoY/63D29lhtqoY_000838_seg19.jpg)
*📸 00:08:38 — Interface de gestion Dokploy montrant les paramètres de déploiement d'un conteneur MongoDB ("my-mongo") avec les boutons Deploy, Reload, Stop et les informations d'identification internes.*

---

### ⏱️ `[00:08:48 - 00:09:07]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc là ici, la variable d'environnement me dit que c'est mongo-uri. Et donc mongo-uri égale blablabla. Donc je vais utiliser cette variable d'environnement pour pouvoir dire à mon application où se connecter, quelle base de données se connecter. Et donc si je vais dans mon mongo ici, je peux revenir vite fait ici, et ça me donne directement internal connection URL.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant de la documentation markdown et l'interface d'administration Dokploy.

**Contenu textuel & Code** : `MONGO_URI=mongodb://login:password@mongohostname:27017/databasename` et interface Dokploy avec les paramètres du conteneur my-mongo (port 27017, identifiants, URL de connexion).

**Action / Démonstration** : Explication de la configuration de la chaîne de connexion MongoDB via la variable d'environnement MONGO_URI dans Dokploy.

![Documentation ou fichier affichant l'utilisation de la variable d'environnement MONGO_URI pour connecter l'application à MongoDB.](../screenshots/63D29lhtqoY/63D29lhtqoY_000853_seg20.jpg)
*📸 00:08:53 — Documentation ou fichier affichant l'utilisation de la variable d'environnement MONGO_URI pour connecter l'application à MongoDB.*

![Interface de gestion Dokploy montrant les paramètres de déploiement et les identifiants internes d'un conteneur MongoDB ("my-mongo").](../screenshots/63D29lhtqoY/63D29lhtqoY_000902_seg20.jpg)
*📸 00:09:02 — Interface de gestion Dokploy montrant les paramètres de déploiement et les identifiants internes d'un conteneur MongoDB ("my-mongo").*

---

### ⏱️ `[00:09:07 - 00:09:28]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc là, si je l'affiche ici, pareil, de dite à personne, je peux directement copier ma connection string, c'est comme ça que ça s'appelle, qui me permet de me connecter à ma base de données. Et donc je peux revenir ici et juste simplement coller ma connection string. Mon nom de utilisateur, c'est username. Mon password, c'est password. Et ensuite, le nom d'hôte, c'est le nom du conteneur qui s'appelle jeu2048-mongo, blablabla, avec le port ici, 27017.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:29 - 00:10:05]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc là, boum, boum, boum, mon application va pouvoir se connecter. Je viens sauvegarder. Évidemment, il faut que je redéploie pour que mon conteneur redémarre avec les nouvelles variables d'environnement pour pouvoir se connecter à la base de données. Et donc si je fais un redéploiement ici, est-ce que vous êtes sûr ? Hop, hop, hop. J'ai un deuxième déploiement qui est en cours. je peux voir où est-ce que ça en est. Ça va me reconstruire mon conteneur, me le relancer, bien mettre la bonne variable environnement, etc. Et donc là ici, c'est déployé. Donc encore une fois, un truc que je trouve assez stylé, c'est qu'on peut voir les logs. Et bien je vois ici que j'ai mes logs. Mon application, elle a bien démarré. C'est bien connecté sur le port 5000 et j'ai

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:10:05 - 00:10:38]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> bien ici mon GoDB connecté. Donc c'est bien connecté à la base de données que j'ai donnée dans la connection string. Alors qu'avant ici, j'avais des erreurs qui me disaient je n'arrive pas à me connecter et il essaie de se reconnecter toutes les 10 secondes à une base de données qui n'existe pas. Et donc là en théorie si je reviens sur mon application et ben là à partir de maintenant je peux jouer un petit peu on voit que ça fait des highscores et donc si je rafraîcie je vois que j'ai mes highscores qui ont été enregistrés parce que mon application à chaque fois que je fais un score l'enregistre dans ma base de données et peut les récupérer une fois que mes scores sont enregistrés. Donc là déjà là on est bien. Là on est bien. J'ai mon application qui est déployée

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant une application web interactive (jeu 2048 v1).

**Contenu textuel & Code** : Interface utilisateur du jeu 2048 avec affichage du score (576), plateau de jeu avec tuiles (2, 4, 8, 16, 32, 64), bouton "Nouvelle partie" et section "Meilleurs Scores".

**Action / Démonstration** : Démonstration de l'application web fonctionnelle après correction de la connexion à la base de données.

![Interface web du jeu 2048 v1 montrant la grille de tuiles chiffrées et les scores, illustrant l'application fonctionnelle connectée à la base de données.](../screenshots/63D29lhtqoY/63D29lhtqoY_001022_seg23.jpg)
*📸 00:10:22 — Interface web du jeu 2048 v1 montrant la grille de tuiles chiffrées et les scores, illustrant l'application fonctionnelle connectée à la base de données.*

---

### ⏱️ `[00:10:38 - 00:11:12]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> sur mon serveur. Je n'ai pas eu à taper aucune ligne de commande, j'ai juste à cliquer un petit peu, configurer un petit peu et c'est déployé. Maintenant, on a quelques petites choses supplémentaires qu'on a besoin quand on déploie en production. Premièrement, le fait qu'on ait un redémarrage automatique en cas de crash, eh bien ça, c'est déjà pris en compte parce que ça utilise Docker Swarm sous le capot et donc si mon application crash, eh bien elle va automatiquement être redémarrée. Le conteneur va être redémarré. Donc ça déjà, c'est cool. Deuxièmement, on veut être capable de voir qu'est ce qui se passe. Donc on a vu ici qu'on avait accès à nos logs, ce qui est super important mais on a aussi accès à du monitoring donc savoir qu'est ce que consomme

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUNE

**Action / Démonstration** : Explication orale de la configuration de déploiement en production sans manipulation visible à l'écran.

---

### ⏱️ `[00:11:12 - 00:11:47]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> mon application mes différents services qui composent mon application et qu'est ce qu'ils consomment en termes de mémoire en termes de cpu en termes d'io etc et donc on a un petit graph qui s'affiche ici qui est assez cool pour savoir si jamais ça consomme plus ou bien un petit bug ou quoi et ben on peut on peut voir où est ce qu'on en est on a également des backups donc là dans le cas dans l'application ça n'avait pas de sens de faire des backups mais dans le cas de ma base de données par exemple ça fait du sens de pouvoir avoir des backups donc je pourrais connecter un bucket S3, pareil sur le fournisseur de bucket de type S3 que je veux et avoir automatiquement des sauvegardes sans encore une fois avoir la moindre ligne de code à faire. Ensuite on a comme je t'ai

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface graphique de gestion (Panneau de monitoring de type PaaS/PPL avec menu latéral incluant Projects, Monitoring, Schedules, Traefik, Docker, Swarm, Requests).

**Contenu textuel & Code** : Graphiques et métriques de performance : CPU Usage (0.11%), Memory Usage (48.25 MiB / 7.75 GiB), Block I/O et Network I/O, avec infobulle temporelle sur le graphique mémoire.

**Action / Démonstration** : Présentation et explication du module de supervision des ressources serveur et des services applicatifs pour détecter les pics de consommation ou les bugs.

![Tableau de bord de monitoring affichant l'utilisation des ressources (CPU, mémoire, I/O disque et réseau) d'une application.](../screenshots/63D29lhtqoY/63D29lhtqoY_001121_seg25.jpg)
*📸 00:11:21 — Tableau de bord de monitoring affichant l'utilisation des ressources (CPU, mémoire, I/O disque et réseau) d'une application.*

---

### ⏱️ `[00:11:47 - 00:12:06]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> montré le déploiement automatique donc c'est à dire que tout un pipeline de CACD en fait sans avoir à faire de pipeline de CACD, sans avoir à utiliser GitLab CI ou des GitHub Action ou quoi que ce soit. Si on se souvient dans mon application ici j'avais dit que je pouvais déployer les nouvelles versions directement quand je faisais un push. Donc je peux venir ici et faire auto-deploy.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Dokploy (dashboard PaaS/DevOps)

**Contenu textuel & Code** : Configuration du dépôt (2048-mern), branche 'dockerfile', et Trigger Type configuré sur 'On Push'.

**Action / Démonstration** : Explication du mécanisme de déploiement automatique intégré sans utiliser de pipeline CI/CD externe (comme GitLab CI ou GitHub Actions).

![Interface web de Dokploy montrant la configuration du déploiement avec le dépôt GitHub, la branche, et le déclencheur défini sur 'On Push'.](../screenshots/63D29lhtqoY/63D29lhtqoY_001201_seg26.jpg)
*📸 00:12:01 — Interface web de Dokploy montrant la configuration du déploiement avec le dépôt GitHub, la branche, et le déclencheur défini sur 'On Push'.*

---

### ⏱️ `[00:12:06 - 00:12:39]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc à partir de maintenant, dès qu'il y a une modification qui va être faite et qui va être pushée sur GitHub, ça va partir en prod directement. Donc on peut venir dans mon application ici. Là, je vais dans mon fichier index par exemple. Je vais venir faire une petite modification et c'est plus la version 0, c'est boom version 2. Commit change, commit change. Et là, quand je veux venir dans mon application. Si je viens dans déploiement, j'ai un nouveau déploiement qui est en cours en ce moment. Il est en train de récupérer la dernière version de mon application, recréer une nouvelle

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web GitHub et tableau de bord de la plateforme de déploiement Dokploy.

**Contenu textuel & Code** : Code source HTML (balises meta, liens CSS, titre "2048 v0") et liste des déploiements avec statuts (Running, Done) et hash de commits.

**Action / Démonstration** : Modification du code source sur GitHub pour illustrer le déclenchement d'un déploiement automatique en production visible sur Dokploy.

![Visualisation du fichier index.html du projet 2048-mern sur l'interface GitHub, montrant la structure du code HTML avec la version v0.](../screenshots/63D29lhtqoY/63D29lhtqoY_001214_seg27.jpg)
*📸 00:12:14 — Visualisation du fichier index.html du projet 2048-mern sur l'interface GitHub, montrant la structure du code HTML avec la version v0.*

![Tableau de bord Dokploy affichant l'onglet Deployments avec un déploiement en cours (Running) suite à un webhook ou un push Git.](../screenshots/63D29lhtqoY/63D29lhtqoY_001231_seg27.jpg)
*📸 00:12:31 — Tableau de bord Dokploy affichant l'onglet Deployments avec un déploiement en cours (Running) suite à un webhook ou un push Git.*

---

### ⏱️ `[00:12:39 - 00:13:13]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> image Docker qui contient ma dernière version de mon application. Et boum, là ça a fonctionné. J'ai récupéré tout ça, etc. Et ça a redéployé la nouvelle image qui a été recréée avec la nouvelle version de mon appli. Et donc si je viens dans mon application ici et que je rafraîchis la page, et bah hop je récupère la nouvelle version la V2. Donc ça sans rien configurer, sans même se connecter une seule fois sur le serveur, si ce n'est juste la ligne de commande qui installe d'oploy, c'est déjà grave stylé. Mais c'est pas fini, ça va encore plus loin parce qu'imagine que mon application devient populaire, j'ai de plus en plus de trafic, de plus en plus d'utilisateurs,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant l'interface graphique de l'application déployée.

**Contenu textuel & Code** : Interface utilisateur du jeu 2048 avec mention explicite de la version "v2" et tableau des meilleurs scores.

**Action / Démonstration** : Test et validation du déploiement en rafraîchissant l'application dans le navigateur pour confirmer la prise en compte de la nouvelle version (V2).

![Interface web du jeu 2048 affichant la version V2 après le redéploiement réussi de l'application via conteneur Docker.](../screenshots/63D29lhtqoY/63D29lhtqoY_001256_seg28.jpg)
*📸 00:12:56 — Interface web du jeu 2048 affichant la version V2 après le redéploiement réussi de l'application via conteneur Docker.*

---

### ⏱️ `[00:13:13 - 00:13:35]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> les gens ils kiffent le 2048, ça devient viral carrément, et bah je vais avoir beaucoup plus de charge sur mon serveur et jusqu'à ce que potentiellement mon serveur soit saturé. Et Et donc j'aimerais bien pouvoir répartir la charge sur différents serveurs pour pouvoir scaler, rajouter différents serveurs et que tous ces serveurs servent mon application. Accessoirement, ça me sert aussi en termes de haute disponibilité parce que si j'ai qu'un seul serveur et qu'il tombe en panne, bon bah j'ai plus de site.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucun

**Contenu textuel & Code** : Aucun

**Action / Démonstration** : Explication orale du besoin de répartition de charge et de scalabilité horizontale.

---

### ⏱️ `[00:13:35 - 00:13:55]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et c'est ça qui pour moi a fait la grosse différence avec d'autres outils comme par exemple Coolify qui est assez cool aussi comme outil qui est assez similaire. Mais en plus d'avoir une interface qui est un petit peu moins logique, un petit peu moins facile à utiliser, quelques petits bugs, etc. ne règle pas du tout ce problème de scalabilité, c'est-à-dire déployer l'application sur plusieurs serveurs. Et Docploy, pour faire ça, il utilise Docker Swarm.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Site web Coolify (plateforme open-source de self-hosting / alternative à Heroku/Netlify).

**Contenu textuel & Code** : Page de présentation de Coolify mentionnant les fonctionnalités de déploiement et la liste des sponsors.

**Action / Démonstration** : Présentation et comparaison critique de l'outil Coolify par rapport à d'autres solutions de gestion d'infrastructure.

![Capture d'écran montrant le site web de Coolify avec le logo officiel et les informations de l'outil de déploiement self-hosted.](../screenshots/63D29lhtqoY/63D29lhtqoY_001340_seg30.jpg)
*📸 00:13:40 — Capture d'écran montrant le site web de Coolify avec le logo officiel et les informations de l'outil de déploiement self-hosted.*

---

### ⏱️ `[00:13:56 - 00:14:15]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc Docker Swarm, c'est un orchestrateur qui permet d'héberger des conteneurs Docker sur plusieurs serveurs, les partager sur différents serveurs. Donc si je viens sur Docker ici, j'ai la liste de mes conteneurs. Et si je viens ici dans Swarm, je vois que j'ai deux nœuds parce que j'ai ajouté un nœud à mon cluster Swarm. Pareil, je n'ai pas eu de configuration de fou à faire ici.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord d'administration (UI web de gestion de conteneurs / orchestrateur) avec menu latéral de navigation.

**Contenu textuel & Code** : Vue d'ensemble de Docker Swarm (Docker Swarm Overview) affichant 2 total nodes, 2/2 active nodes online, 1/2 manager nodes, et le détail des deux nœuds (ip-172-31-83-141 Leader et ip-172-31-87-173 Worker avec versions du moteur 28.3.3, 2 Cores et 7.75 Go de RAM).

**Action / Démonstration** : Présentation et explication du statut des nœuds d'un cluster Docker Swarm dans une interface de supervision.

![Interface graphique de gestion montrant le tableau de bord Docker Swarm avec deux nœuds actifs.](../screenshots/63D29lhtqoY/63D29lhtqoY_001405_seg31.jpg)
*📸 00:14:05 — Interface graphique de gestion montrant le tableau de bord Docker Swarm avec deux nœuds actifs.*

---

### ⏱️ `[00:14:15 - 00:14:43]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je suis juste allé dans Manage Cluster, ajouter un node, et il me dit hop, tu as juste à ruiner cette commande-là et cette commande-là. Donc deux commandes, c'est plus compliqué une, mais c'est quand même assez simple. Et donc ça va installer Docker sur mon serveur. Et la deuxième va activer le mode Swarm et joindre le cluster de la première machine, la machine principale qui va être le manager. Et donc ce que ça me donne comme possibilité, c'est que maintenant, si je reviens dans mon petit projet 2048, imaginons que je veux scaler mon application Node, je ne veux plus que ça tourne une fois, mais que je veux que ça tourne cinq fois par exemple.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de cluster (type Dashboard PaaS / Docker Swarm UI).

**Contenu textuel & Code** : Dashboard avec le menu latéral (Projects, Monitoring, Docker, Swarm) et la vue principale listant les services du projet "jeu-2048".

**Action / Démonstration** : Navigation dans l'interface pour présenter l'ajout d'un nœud au cluster et la gestion des services.

![Interface d'administration web montrant la gestion d'un cluster avec un projet nommé "jeu-2048" et des services déployés ("my-mongo", "node").](../screenshots/63D29lhtqoY/63D29lhtqoY_001436_seg32.jpg)
*📸 00:14:36 — Interface d'administration web montrant la gestion d'un cluster avec un projet nommé "jeu-2048" et des services déployés ("my-mongo", "node").*

---

### ⏱️ `[00:14:43 - 00:15:03]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je peux venir ici dans Node, venir dans Avancer, Et ici, réplique. Je peux choisir de monter jusqu'à 5, 6, le nombre que je fais. Ici, ça me demande de choisir un registre. Donc un registre. Moi, j'ai déjà ajouté un ici. Je l'ai appelé My Registry. Comment est-ce que j'ai fait ? Je suis simplement allé dans Registry. Et j'ai fait Ajouter un nouveau registre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:15:03 - 00:15:23]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> J'ai mis un nom, un nom d'utilisateur. Et l'URL, je peux vous montrer ici. Et donc, ce que j'ai utilisé ici, c'est le Docker Hub, qui est un registre public. Je peux avoir deux ou trois images privées, si tu veux, en gratuit. Mais il y a plein de services différents qui permettent d'héberger des images Docker. Docker Hub, c'est un des plus basiques, mais ça pourrait même être sur GitHub directement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucun outil, terminal ou logiciel affiché.

**Contenu textuel & Code** : Aucun code, commande ou métrique visible.

**Action / Démonstration** : Explication orale du concept de registre public (Docker Hub) et des images Docker.

---

### ⏱️ `[00:15:23 - 00:15:46]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> GitHub a son propre registre ou sur GitLab ou sur plein d'autres endroits où on peut avoir un registre. Et pourquoi est-ce qu'on a besoin de ça ? Parce que si j'ai plusieurs serveurs et que je construis mon image Docker sur un des serveurs, cette image-là, elle est juste sur le serveur qu'il a construit et pas sur les autres serveurs de mon cluster. Parce que ce n'est pas une image qui est publique. Donc ce qu'il faut, c'est pouvoir non seulement construire cette image, mais ensuite aller l'uploader sur un registre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Panneau de configuration web de gestion de cluster avec menu latéral (Projects, Monitoring, Docker, Swarm) et paramètres de service.

**Contenu textuel & Code** : Champs de configuration 'Cluster Settings' avec les options 'Replicas' (réglé à 5), 'Select a registry' (sélectionné sur 'my-registry'), et la gestion des limites de ressources (Memory Limit, CPU Limit et réservations).

**Action / Démonstration** : Présentation de la configuration d'un service Docker Swarm, explication de la nécessité d'utiliser un registre centralisé partagé entre les différents nœuds d'un cluster pour synchroniser les images de conteneurs.

![Interface de configuration d'un cluster montrant les paramètres de réplication et la sélection d'un registre de conteneurs.](../screenshots/63D29lhtqoY/63D29lhtqoY_001534_seg35.jpg)
*📸 00:15:34 — Interface de configuration d'un cluster montrant les paramètres de réplication et la sélection d'un registre de conteneurs.*

---

### ⏱️ `[00:15:46 - 00:16:06]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ensuite, mes autres serveurs de mon cluster pourront tous récupérer cette image de la même source. Et donc mon application pourra tourner sur tous les nœuds de mon cluster, même si ce n'est pas ce nœud-là en particulier qui a construit l'image à la base. Donc là, j'ai mis 5 répliques, mon registre, sauvegarder. D'ailleurs, ici, ça me dit, maintenant que tu as sauvegardé pour tes 5 répliques, il faut juste que tu redeployes, parce que c'est un nouveau déploiement dans Swarm.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Coolify (Dashboard de gestion DevOps / Docker Swarm)

**Contenu textuel & Code** : Paramètres de cluster Docker Swarm, champ 'Replicas' défini à 5, sélection du registre 'my-registry', et message d'avertissement concernant le redéploiement.

**Action / Démonstration** : Configuration du nombre de répliques et du registre d'images pour le service dans le cluster Docker Swarm.

![Interface web de gestion de conteneurs (Coolify) affichant les paramètres du cluster Docker Swarm avec le réglage du nombre de répliques et du registre.](../screenshots/63D29lhtqoY/63D29lhtqoY_001601_seg36.jpg)
*📸 00:16:01 — Interface web de gestion de conteneurs (Coolify) affichant les paramètres du cluster Docker Swarm avec le réglage du nombre de répliques et du registre.*

---

### ⏱️ `[00:16:07 - 00:16:28]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc je viens ici faire dans Général et Deploy. Boum, boum. Donc là, ça va me refaire un nouveau déploiement, me reconstruire une nouvelle image. Mais cette fois-ci, l'uploader sur mon repo sur le Docker Hub. Donc là, je vois qu'il a créé l'image, mais il est maintenant en train de la pusher vers Docker Hub. Donc là, si je viens dans mon compte Docker Hub, je vois qu'il y a une nouvelle image qui a été créée.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de déploiement / console de logs cloud (style Coolify ou similaire) avec affichage de la sortie standard d'un build et d'un push Docker.

**Contenu textuel & Code** : Logs détaillant les étapes de build : export to image, writing image, naming, authentification (Login Succeeded), puis le push des différentes couches (layers) vers le registre distant (docker.io/cocadmin/jeu2048-node-n3lcfs:latest), se terminant par le message "Docker Deployed: Success".

**Action / Démonstration** : Surveillance et explication en direct du processus de reconstruction de l'image conteneurisée et de son téléversement (upload/push) vers le dépôt Docker Hub.

![Interface de déploiement affichant les logs de construction et de publication d'une image Docker sur Docker Hub, avec une pastille vidéo du présentateur en bas à gauche.](../screenshots/63D29lhtqoY/63D29lhtqoY_001623_seg37.jpg)
*📸 00:16:23 — Interface de déploiement affichant les logs de construction et de publication d'une image Docker sur Docker Hub, avec une pastille vidéo du présentateur en bas à gauche.*

---

### ⏱️ `[00:16:28 - 00:16:51]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Coqadmin, jeu 2048, node, blablabla. Il y a juste moins d'une minute. Donc cette image-là, si elle est en public, tout le monde peut accéder. Et si elle est en privé, il n'y a que moi ou les différents nodes de mon cluster qui vont pouvoir accéder en utilisant le mot de passe que j'ai renseigné ici quand j'ai créé mon registre. Donc là maintenant que j'ai mis 5 répliques, ça va me démarrer 5 fois le conteneur avec mon application Node dedans et ça va me balancer mon trafic entre mes 5 conteneurs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur Web, interface Docker Hub et formulaire de configuration de registre.

**Contenu textuel & Code** : URL de registre docker.io, identifiant utilisateur "cocadmin", et champs de configuration de mot de passe.

**Action / Démonstration** : Explication de la visibilité publique ou privée d'une image Docker et configuration des accès pour un cluster de nœuds.

![Interface Docker Hub affichant le dépôt public pour le jeu 2048 sous le compte cocadmin.](../screenshots/63D29lhtqoY/63D29lhtqoY_001634_seg38.jpg)
*📸 00:16:34 — Interface Docker Hub affichant le dépôt public pour le jeu 2048 sous le compte cocadmin.*

![Formulaire de configuration d'un registre externe (External Registry) avec champs de nom, nom d'utilisateur, mot de passe et URL du registre.](../screenshots/63D29lhtqoY/63D29lhtqoY_001640_seg38.jpg)
*📸 00:16:40 — Formulaire de configuration d'un registre externe (External Registry) avec champs de nom, nom d'utilisateur, mot de passe et URL du registre.*

---

### ⏱️ `[00:16:51 - 00:17:18]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Chaque conteneur va recevoir un cinquième du trafic. J'ai que 2 serveurs, donc d'équivalent ça ne me sert pas à grand chose d'en avoir 5. Mais si je rajoutais des serveurs à mon cluster, je pourrais distribuer ces différents conteneurs sur mes différents serveurs et donc avoir plus de capacités et répondre à plus de requêtes à la fois. Un petit truc qui m'a un petit peu déçu, sur cette partie-là, c'est que techniquement, si je viens ici dans mes logs et que je regarde ici, je vois que j'ai que trois conteneurs qui sont en train de tourner.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Dokploy (tableau de bord de gestion de conteneurs et de cluster).

**Contenu textuel & Code** : Panneau d'administration de Dokploy affichant les onglets Environment, Domains, Preview Deployments, Schedules, Volume Backups, Deployments, Logs, ainsi qu'une section "Cluster Settings" avec un champ Replicas réglé sur 5.

**Action / Démonstration** : Explication de la distribution du trafic et de la configuration des réplicas (mise à l'échelle) au sein d'un cluster de serveurs.

![Interface de l'outil Dokploy montrant la configuration d'un nœud, les onglets de gestion et les paramètres de cluster avec le réglage du nombre de réplicas à 5.](../screenshots/63D29lhtqoY/63D29lhtqoY_001711_seg39.jpg)
*📸 00:17:11 — Interface de l'outil Dokploy montrant la configuration d'un nœud, les onglets de gestion et les paramètres de cluster avec le réglage du nombre de réplicas à 5.*

---

### ⏱️ `[00:17:19 - 00:17:40]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc là, je me disais, c'est bizarre, j'en ai demandé cinq, mais j'en ai que trois. Ils sont où les deux autres ? Pareil ici, si je vais dans Docker, je vois que j'ai que trois conteneurs qui tournent ici. Donc pareil, c'est un peu bizarre. Mais en fait, ce qui se passe, c'est que ça a quand même bien fait ce que j'ai demandé. C'est juste que dans l'interface ici de DocPloy, je peux voir que les conteneurs qui tournent sur la machine qui fait tourner Docploy et pas les conteneurs qui tournent ailleurs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:17:40 - 00:18:04]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais si je vais sur les serveurs en question, donc là à droite, j'ai mon serveur Docploy, je vois mon service ici, je node blablabla, qui a bien 5 répliques. Et si je fais Docker PS, je vois que j'ai 3 conteneurs les mêmes qu'on voit dans l'interface de Docploy ici. Donc là, hop 2 minutes, hop 2 minutes, hop 2 minutes, c'est mes 3. Mais si je vais sur mon autre serveur et que je fais Docker PS, j'ai les 2 autres qui font que j'ai bien 5 répliques.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:18:04 - 00:18:29]` | Segment #42

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc j'ai bien 2 conteneurs et c'est bien la même image qu'au admin slash jeu 2048, blablabla. Donc, ça fonctionne, mais dans l'interface, ça peut prêter un peu à confusion parce qu'on se dit, c'est bizarre, j'en ai que trois. Puis en plus de ça, on ne peut voir que les métriques et les logs de juste ceux qui tournent sur la machine de plug. Donc, c'est un petit bémol, mais cette fonctionnalité de fait de pouvoir scaler horizontalement, c'est quelque chose que j'ai retrouvé dans aucun autre outil que j'ai testé ou du moins aucun autre outil qui est simple.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucune interface affichée.

**Contenu textuel & Code** : Aucun contenu technique, code ou métrique visible.

**Action / Démonstration** : Explication orale de la configuration des conteneurs par le créateur face caméra.

---

### ⏱️ `[00:18:30 - 00:18:49]` | Segment #43

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Tu as d'autres orchestrateurs qui peuvent faire ça, évidemment, mais ils sont beaucoup plus compliqués à utiliser. Alors que là, même si je ne sais même pas ce que c'est Docker Swarm, ça va quand même marcher. J'ai testé énormément de solutions alternatives. J'ai testé Doge, Portainer, Coolify, Nomad, Kamal, Swarm, et même les classiques Kubernetes ou Docker Compose.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucun outil, terminal ou console n'est affiché à l'écran.

**Contenu textuel & Code** : Aucun code, commande ou architecture visible (plans purement face-caméra).

**Action / Démonstration** : Explication verbale par le créateur sur les différents orchestrateurs de conteneurs testés (Docker Swarm, Kubernetes, Nomad, etc.).

---

### ⏱️ `[00:18:49 - 00:19:11]` | Segment #44

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et pour moi, Doploie a de loin le meilleur rapport entre simplicité, avec l'interface où il y a vraiment tout, quelques clics, pas trop de trucs compliqués, et d'avoir quand même toutes les fonctionnalités nécessaires qu'on a besoin pour pouvoir aller avoir une application solide en production. Si tu veux apprendre les différentes outils et méthodes DevOps avec moi, je fais quelques fois par an des formations en petits groupes. Je te laisse ce lien en description si jamais ça t'intéresse. Et si tu veux toi même savoir comment faire une application qui scale, je te laisse aller voir cette vidéo.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web / outil de présentation sur écran externe.

**Contenu textuel & Code** : Diapositive titrée "Philosophie DevOps" avec des questions textuelles.

**Action / Démonstration** : Explication théorique sur la philosophie DevOps sans manipulation technique directe à l'écran.

---

