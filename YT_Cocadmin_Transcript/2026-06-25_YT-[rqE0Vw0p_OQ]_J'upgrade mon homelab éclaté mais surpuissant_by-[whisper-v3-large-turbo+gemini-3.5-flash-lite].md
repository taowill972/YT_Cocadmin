# 🎬 J'upgrade mon homelab éclaté mais surpuissant

> **Chaîne** : [cocadmin](https://www.youtube.com/@cocadmin)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=rqE0Vw0p_OQ](https://www.youtube.com/watch?v=rqE0Vw0p_OQ)  
> **Date de publication** : 20260625  
> **Durée** : 00:09:10  
> **Identifiant vidéo** : `rqE0Vw0p_OQ`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **J'upgrade mon homelab éclaté mais surpuissant**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.

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
> Mon infra est de plus en plus stylé mais elle est aussi de pire en pire en même temps. Je viens d'ajouter un nouveau serveur avec 36 coeurs, 512 Go de RAM. Je vais l'ajouter en cluster avec le serveur de 256 Go de RAM que j'ai déjà en plus de mon NAS de 56 Tera pour mes vidéos, mes données perso. Mais tout ça c'est bien beau mais ça sert à rien si j'ai des coupeurs d'électricité tout le temps. Et comme par hasard, la dernière fois c'était le jour de l'ouverture de ma formation.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:22 - 00:00:43]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et en plus de ça, moi j'étais littéralement à l'autre bout du monde donc je pouvais pas facilement venir redémarrer, refixer mes serveurs. Et comme toutes ces servages, je les utilise pendant ma formation pour pouvoir donner des machines virtuelles aux apprenants. Donc au final, même si ça finit par revenir, le temps que je fixe tout, etc., je passe un tuyau pour un con. Donc pour régler ce problème, je pensais ajouter un UPS pour Uninterruptible Power Supply. Le problème, c'est que c'est assez cher, assez encombrant, assez lourd.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:00:43 - 00:01:04]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et en plus de ça, ça ne tient pas vraiment très longtemps la charge. En général, un UPS, c'est peut-être comme 5 minutes, 10 minutes, quelque chose comme ça. Et les coupures que j'ai, parfois, ça dure 1h, 3h, 4h, on ne sait pas. Mais je me suis dit maintenant, il y a pas mal de grosses batteries au lithium qui ont des grosses capacités, qui ne coûtent pas si cher et qui ont des fonctionnalités d'UPS. Et donc je me suis dit que c'était beaucoup plus rentable et surtout ça allait faire en sorte que toute mon infra allait pouvoir rester up même si le courant coûte pendant 1h, 2h, 3h.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:04 - 00:01:24]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc j'ai pris une de ces grosses batteries que j'ai trouvées en promo qui n'était pas trop trop chère, qui a 2000Wh et comme mes serveurs consomment entre 100 et 200W chaque, ça veut dire que je peux tourner facile 4-5h avec de la marge. Et n'est pas une nécessité aussi longue, c'est quand même beaucoup plus rare. Donc depuis que j'ai installé ça, je n'ai plus trop de soucis. J'ai juste ajouté une deuxième plus petite batterie pour tout ce qui est mon équipement réseau, mon routeur, mon modem, etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:24 - 00:01:44]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce que ce n'est pas dans la même pièce. Qui, elle, fait 500 Wh, ce qui est un petit peu overkill pour deux modems routeurs qui consomment 5 Wh chacun. Donc là, pour le coup, ça peut tenir facilement une journée pour pouvoir alimenter l'Internet. Donc, ça a réglé mon souci de coupure d'électricité. Mais tout ça, ça ne sert à rien si, au final, c'est pour perdre l'Internet toutes les 5 minutes. Comme c'est une connexion normale, pas d'entreprise, de temps en temps, il y a des petites coupures, le modem, il redémarre, l'IPL change, des trucs comme ça.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:01:44 - 00:02:06]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et à chaque fois que ça, ça arrive, comme j'ai mon infrastructure chez moi, les gens ne peuvent plus accéder. Moi, je ne peux plus accéder à mes serveurs, même s'ils sont bien alimentés en électricité. Parfois, c'est des petites coupures de 2-3 minutes le temps que le modem rostar. Mais parfois, c'est juste une coupure complètement inexpliquée pendant 2h, 3h avant que magiquement, ça revienne. Et ça, je n'y peux rien. C'est vraiment aléatoire. Je suis à la merci de mon opérateur. C'est pour ça que je me suis dit qu'avec une connexion 5G, il y a peut-être un peu moins de chances que si ma connexion principale est affectée.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:06 - 00:02:25]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> En 5G, je peux potentiellement me connecter à une antenne qui est un peu plus loin si celle qui est proche, elle est déconnectée. Mais maintenant que j'ai deux connexions, comment est-ce que je fais pour utiliser les deux en même temps pour pouvoir switcher quand il y a un problème sur l'une ? J'ai commencé à regarder les routeurs, les switches, et je ne trouvais rien pour moins de 400, 500 balles. Même juste pour un switch qui soit juste assez intelligent pour pouvoir changer de connexion quand il y a un problème sur l'une.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:25 - 00:02:55]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et c'est là que je me suis dit, en fait un switch ou un routeur, en fait c'est juste un ordinateur avec beaucoup de ports Ethernet et qui fait passer le trafic d'un port à l'autre. Et des ordinateurs, j'en ai plein chez moi. Donc j'ai ressorti un Zima Blade, qui est un espèce de Raspberry Pi mais avec un processeur Intel donc quand même un petit peu plus de puissance et surtout ce qui est très intéressant c'est qu'il y a un port PCI Express donc ça m'a permis d'acheter une carte réseau avec 4 ports 2.5 gigabits et pouvoir le brancher directement dans mon Zimablade ce qui fait que ça me donne un handi avec 5 ports dont 4 2 fois et demi plus rapides que ce que j'avais déjà ici ce qui pour mon réseau local, pour accéder à mon NAS etc.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:02:55 - 00:03:15]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> est quand même assez pratique par contre ça m'a pris pas mal de temps pour pouvoir comprendre un petit peu comment le configurer parce que c'est Linux dessus, c'est pas un OS spécial pour faire du routage Donc j'ai dû passer pas mal de temps à bidouiller avec les IP tables, les bridges, etc. Et au final, pour faire le failover, c'est-à-dire le changement de connexion en cas de problème, j'ai cherché un peu ce qui existait déjà, mais j'ai rien trouvé qui avait l'air vraiment très simple. Donc j'ai simplement inventé une solution simple en bash.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:16 - 00:03:34]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est juste un petit script de 10 lignes qui fait des pings en passant spécifiquement par une des connexions Internet. Et si cette connexion Internet-là principale, elle ne marche plus pendant plus que quelques pings, eh bien on va changer les routes pour que l'Internet passe à travers la deuxième connexion. Bon, petite démo. Là, je vais avoir une vidéo qui tourne. Je la réfrèche pour que ça tourne. Là, je vois les logs de mon truc. Et là, je vois mon ping.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:35 - 00:03:55]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, je vais carrément venir ici. Et je vais couper le net. J'enlève la fibre. Carrément. Plus de fibre. Là, c'est rouge. Il galère. Après, tu vois, ça peut faire un peu. Ça a repris. Et donc là, tu vois mon ping. Avant, il était à 3 millisecondes.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:03:55 - 00:04:20]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Là, maintenant, il est à 30 millisecondes. Parce que je suis en 5G. mais du coup ma vidéo elle continue de tourner tranquille et ça continue de buffer. Normalement si je me mets là, tac, je peux continuer à regarder YouTube. J'ai même pas vu de coupure. J'ai eu une coupure quand même, mais une histoire de peut-être 20 secondes, quelque chose comme ça. Mais pour ce que je fais et pour l'accès aux machines virtuelles qui sont dans mes serveurs, qui a un accès par HTTP, par SSH, j'ai pas besoin d'une méga connexion, donc ça suffit largement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:20 - 00:04:41]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le seul petit bémol, c'est que j'ai pas réussi à saturer complètement les ports 2.5 gigabits Parce qu'en fait, le port PCI Express de la Zimablade, c'est un vieux PCI Express qui est limité à 2 gigabits. Donc en fait, je ne pourrais jamais dépasser les 2 gigabits entre ma carte réseau. Le maximum que j'ai, c'est 1.9 quelque chose. Je suis quand même content parce que c'est quand même le double de ce que j'avais avant. Et ça m'a juste coûté le prix de la carte réseau au lieu d'avoir acheté un Switch super cher.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:41 - 00:04:59]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Maintenant que j'ai des résistés et l'Internet sont redondés, il me restait quand même un gros souci. Parce que mon NAS, c'était juste un ancien Raspberry avec deux disques externes branchés en USB. Les performances étaient catastrophiques à cause du processeur du Raspberry et à cause du fait parce que je passe par l'USB. Et en plus de ça, j'avais pris deux disques pour pouvoir faire un arrêt 1. Comme ça, si j'ai un disque qui pète, je conserve toujours mes données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:04:59 - 00:05:18]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Sauf que je n'ai jamais mis en place. Et le but à la base, c'était de migrer mon NAS depuis ce Raspberry Pi en USB à l'arrache sur le Zima Blade en branchant les disques durs en SATA et en faisant le setup RAID qui va bien, etc. Sauf que maintenant, j'utilise le Zima Blade comme routeur. Mais au final, avoir les deux sur la même machine, ça ne pose pas trop de soucis. Parce que le fait d'être un routeur, ça ne consomme pas vraiment beaucoup de ressources.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:18 - 00:05:36]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais le fait d'être aussi un NAS, finalement ça m'arrange parce que ça fait que j'ai besoin d'un port de moi pour aller brancher mon NAS. Parce que mon NAS c'est le routeur. Donc au final c'était pas une si mauvaise idée. Maintenant j'ai du RAID 1 donc je peux perdre un disque et toujours garder mes données. Mais le RAID à la base c'est pas vraiment un backup. Parce que si j'ai un souci électrique ou une inondation ou que juste simplement j'efface mes données sans faire exprès, bah je perds tout d'un coup.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:36 - 00:05:55]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc c'est pour ça qu'il faut un backup externe. Le plus simple c'est de l'avoir dans le cloud mais tout l'intérêt c'était justement de se barrer de Google Drive. Du coup j'ai utilisé AirClone pour pouvoir synchroniser mes données chaque jour avec Internext qui est justement le sponsor de la vidéo. Contrairement à d'autres fournisseurs de Stockage Cloud, ils font du chiffrement de bout en bout. Ça veut dire que le chiffrement se fait sur ton navigateur sans même qu'ils aient accès à la clé. Et donc même s'ils avaient envie, ils ne pourraient jamais déchiffrer tes données.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:05:55 - 00:06:20]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> En plus c'est open source et c'est chiffré avec un algorithme post-quantique pour résister même aux futures attaques des ordinateurs quantiques. Pour éviter de devoir payer tous les mois, ils ont une offre à vie qui est assez rentable par rapport à tout ce que j'ai déjà dépensé dans Google Drive et iCloud. Parce que même si c'est des petites sommes, parfois ça me fait un peu mal au cœur de me dire que je vais devoir payer ça jusqu'à la fin de ma vie. Donc si comme moi tu veux un backup hors site, ou si tu veux juste stocker tes données pour qu'elles restent privées et sans payer tous les mois, je te mets mon lien dans la description, ça te donne 87% de réduction sur le plan à vie.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:20 - 00:06:43]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est le prix le plus bas que tu pourras jamais trouver. Maintenant du côté matos, on commence à être bon. Mais du côté logiciel, c'était encore plus le bordel. Je pense qu'un des pires exemples, c'est que ma plateforme PaperLab que j'utilise pour pouvoir fournir des VM aux étudiants de mes formations, elle tournait sur un de mes serveurs. Et le problème, c'est qu'elle tournait juste sur ce serveur-là. Pas d'autres environnements, pas d'environnement de dev, pas de moyens vraiment de coder sur mon ordi, parce que j'avais juste mis en place un VS Code Server sur mon serveur.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:06:43 - 00:07:01]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc, quand je faisais des modifications, j'ajoutais des fonctionnalités, je corrigais des bugs, etc., j'avais aucun autre moyen de tester que de programmer direct en prod. Et donc, la moindre virgule que j'ajoutais dans un fichier, ça provoquait une interruption de service instantanément. C'était pas si grave que ça, parce qu'en général, je fais ça l'après-midi, ce qui est tard dans la nuit en France, mais c'est quand même loin d'être idéal.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:01 - 00:07:22]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc l'idéal, ça serait d'avoir un deuxième serveur que je puisse utiliser en environnement dev. Sauf que comme je fais tourner beaucoup de machines virtuelles dessus, ça veut dire qu'il faut un serveur quand même balèze. Et la RAM aujourd'hui, ça coûte vraiment trop cher et moi, je suis un crevard. Donc j'ai essayé de trouver une autre solution et c'est là que je suis tombé sur Colima, qui est à la base un espèce de remplacement à Docker Desktop. Donc ça va faire tourner une machine virtuelle qui va te permettre de faire tourner des conteneurs sur ton Mac.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:22 - 00:07:43]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc en général, on fait tourner des conteneurs avec Docker, donc c'est pour ça que c'est un remplacement à Docker. Sauf que ce n'est pas simplement compatible avec Docker. C'est aussi compatible avec Kubernetes et avec Incus. Et c'est Incus ou LXD que moi j'utilise pour faire tourner Paperlab, pour faire tourner les machines virtuelles et les conteneurs des étudiants. Donc ça veut dire qu'avec Colima, je peux à la fois avoir Docker, à la fois avoir Kubernetes et à la fois avoir Incus sur mon Mac.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:07:43 - 00:08:06]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et donc je peux prendre le code de l'application Paperlab et le connecter directement avec mon cluster Incus qui tourne tout localement sur la machine. Donc ça veut dire que j'ai enfin un vrai environnement de développement local sur mon arti, sur mon Mac. Donc maintenant je peux faire des modifications sans risquer de tout péter à chaque fois que j'appuie sur la rentrée. Il y a encore pas mal de choses qui ne vont pas dans mon infra. Les choses que j'aimerais mettre en place derrière, c'est du CICD pour pouvoir faire en sorte que, automatiquement, mon code de mon application soit testé et déployé automatiquement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:06 - 00:08:25]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Que ce ne soit pas moi qui aille déployer manuellement en me connectant sur le serveur. J'aimerais aussi avoir de l'infra à ce code parce que quand j'ai eu le problème de la coupure d'électricité, j'ai dû en urgence prendre un serveur sur le cloud, tout remettre en place, Paperlab dessus. Et tout ça, c'était en SSH manuellement. Donc, c'est vraiment pourri. Idéalement, je voudrais juste lancer un script avec Ansible ou avec Docker Compose et que tout se déploie automatiquement en une commande.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:25 - 00:08:44]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> J'aimerais aussi rajouter du clustering, du backup, parce que je n'ai toujours pas vraiment de backup de ma base de données. Une vraie gestion des logs, parce qu'encore une fois, l'ajustion des logs que je fais en ce moment, c'est juste aller voir les logs en essessage sur la machine. Et plein d'autres choses, j'aimerais bien avoir du 10 gigabits, j'aimerais même avoir un cache SSD pour mon NAS, potentiellement mettre à jour la SimaBlade pour quelque chose d'un petit peu plus puissant.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:08:44 - 00:09:04]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et j'aimerais bien aussi me débarrasser de toutes ces prises toutes pourrutes là, et faire tout passer en USB. J'ai des multiprises dans des multiprises dans des multiprises, c'est vraiment, c'est affreux. Donc parmi tout ce qui reste à fixer, dites-moi ce qui vous intéresse le plus et peut-être que je ferai un épisode 2. En attendant, si tu es développeur et que tu veux te mettre aux outils DevOps, je fais une formation qui utilise cette infra justement 2-3 fois par an avec un tout petit groupe.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

### ⏱️ `[00:09:04 - 00:09:06]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc si ça t'intéresse, je te laisse le lien dans la description.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra sans interface informatique partagée.

**Contenu textuel & Code** : Explications orales des concepts, architectures et retours d'expérience.

**Action / Démonstration** : Démonstration pédagogique et mise en perspective technique.

---

