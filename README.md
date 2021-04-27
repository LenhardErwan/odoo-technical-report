# Odoo Technical Report
CASTEL Jérémy - LENHARD Erwan - VERY-GRIETTE Milan

Odoo Technical Report est un module pour Odoo 14 qui permet de gérer des rapports techniques raccrochés à une commande.
Un rapport peut contenir plusieurs sous-rapports qui sont eux-mêmes composés de blocs de textes ou d'images.

# Execution
Pour lancer le serveur odoo, il faut se placer dans le répertoire home de gr1 puis exécuter:
`./odoo/odoo-bin`

# Connexion
Assurez-vous que le serveur est lancé, rendez-vous sur l'adresse : http://localhost:10000 et connectez-vous avec un des comptes disponibles :
|Nom de compte|Mot de passe|Groupe Reporter|
|-------------|------------|-------------|
|admin        |azertyuiop  |oui          |
|jeremy       |azertyuiop  |oui          |
|erwan        |azertyuiop  |oui          |
|milan        |borgar      |non          |

*Les utilisateurs avec le groupe **Reporter** peuvent modifier les rapports. Les autres utilisateurs ne peuvent que lire les rapports.

# Code Source
Le code source est disponible sur https://github.com/LenhardErwan/odoo-technical-report.
Organisation du répertoire :
```
odoo-technical-report
│   LICENSE
│   README.md
│   __init__.py
│   __manifest__.py
├─── models
│       tr_block.py
│       tr_globalreport.py
│       tr_report.py
│       __init__.py
├─── security
│       groups.xml
│       ir.model.access.csv
├─── static
│   └─── description
│           icon.png
└─── views
    │    tr_block.xml
    │   tr_global_report.xml
    │   tr_report.xml
```

Il s'agit d'un projet python usuel avec le manifest suivant:
```py
{
    'name': 'Technical Report',
    'description': 'Report manage intervention reports',
    'author': 'Castel Jeremy, Lenhard Erwan, Very-Griette Milan',
    'depends': ['base', 'account'],
    'data': [
			'security/groups.xml',
			'security/ir.model.access.csv',
			'views/tr_global_report.xml',
			'views/tr_report.xml',
			'views/tr_block.xml'
		],
    'application': True,
}
```
Le projet requiert les modules base et account. Le module account est utilisé pour créer le lien entre un rapport et une commande avec le `account.move`.

Le code source est divisé en trois parties.

## Models
Il s'agit des différents schémas de la base de données. Chaque fichier correspond à une nouvelle table.
Il y a les rapports, composés d'un nom, liés avec une commande et une liste de sous-rapports.
|GlobalReport|
|------------|
|name        |
|report_ids  |
|invoice_id  |

Les sous-rapports, définis par un nom, une date de publication et en lien avec une liste de blocs et un rapport.
|Report         |
|---------------|
|name           |
|date_published |
|block_ids      |
|globalreport_id|

Enfin, les blocs contiennent un texte, une image, un numéro d'ordre pour les trier ainsi que l'id du sous-rapport auxquels ils appartiennent. Le booléen `image_exists` est également ajouté durant l'exécution pour savoir si une image est visible dans le bloc. La méthode `compute_image` implémente cette vérification.
|Block    |
|---------|
|order    |
|image    |
|text     |
|report_id|

## Views
Les fichiers suivants définissent les vues de notre module, c'est-à-dire les interfaces qui seront présentées à l'utilisateur.
Dans notre cas, les vues sont au nombre de trois:

tr_global_report.xml
Cette vue est utilisée pour gérer les rapports globaux, c'est à dire la saisie d'un nom, le rattachement du rapport global à une commande ainsi que l'ajout de rapports.

tr_report.xml:
Ce fichier permet d'afficher le formulaire gérant les rapports.
On y entre un nom, une date et on peut de rajouter des blocs.

tr_block.xml:
C'est la vue affichée lorsque l'on visualise, ajoute ou modifie un bloc.
On peut y saisir un ordre, un texte et/ou une image.

## Security
Ce répertoire contient les règles de sécurité définies par le groupe Reporter.
Le fichier `groups.xml` permet de créer notre groupe Reporter et attribue tous les droits à un utilisateur admin:
```xml
<field name="name">Reporter</field>
<field name="users" eval="[(4, ref('base.user_admin'))]" />
```

Enfin, le tableur `ir.model.access.csv` définit les règles de création, d'écriture, de lecture et de suppression, que ce soit pour les utilisateurs simples ou les membres du groupe Reporter.

# Pistes d'amélioration
 - Visualisation d'une image dans les blocs
 - Support du format Markown ou BBCode dans les blocs de texte
 - Ajouter des personnes à un rapport
 - Affiner les régles de sécurité
 - Notification par mail
