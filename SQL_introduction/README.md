
````markdown
# Introduction à SQL

**SQL (Structured Query Language)** est un langage standard utilisé pour interagir avec les bases de données relationnelles. Il permet de créer des bases, des tables, d'insérer, de modifier, de supprimer et de lire des données.

Voici quelques commandes de base à connaître :

```sql
-- Créer une base de données
CREATE DATABASE ma_base;

-- Utiliser une base de données
USE ma_base;

-- Créer une table
CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    email VARCHAR(100)
);

-- Insérer des données
INSERT INTO utilisateurs (nom, email) VALUES ('Alice', 'alice@example.com');

-- Lire les données
SELECT * FROM utilisateurs;

-- Mettre à jour une donnée
UPDATE utilisateurs SET email = 'alice@nouveau.com' WHERE nom = 'Alice';

-- Supprimer une donnée
DELETE FROM utilisateurs WHERE nom = 'Alice';
````

Ces commandes permettent de manipuler facilement les données dans une base MySQL. Pour en apprendre plus, explorez les tutoriels SQL ou la documentation officielle.


## Installation de MySQL 8.0 sur Ubuntu 20.04 LTS

Ces instructions permettent d’installer MySQL 8.0 sur une machine Ubuntu 20.04 LTS (physique, VM ou WSL).  
**Note :** Les étapes peuvent varier légèrement selon la distribution ou version. En cas de problème, n’hésitez pas à rechercher des solutions spécifiques à votre environnement.

## Étapes d’installation

Ouvrez un terminal et exécutez les commandes suivantes :

```bash
# Mettre à jour la liste des paquets
sudo apt update

# Installer le serveur MySQL
sudo apt install mysql-server
````

> Pendant l'installation, MySQL sera installé sans demander de mot de passe root (authentification par socket sur Ubuntu par défaut).

## Vérifier la version installée

```bash
mysql --version
```

Vous devriez obtenir une sortie similaire à :

```
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

## Se connecter au serveur MySQL

```bash
sudo mysql
```

Vous verrez alors :

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

Pour quitter le client MySQL :

```sql
mysql> quit
Bye
```

## 📝 Notes supplémentaires

* Par défaut sur Ubuntu, MySQL utilise **l’authentification Unix Socket** pour l’utilisateur `root`. Cela signifie que vous devez utiliser `sudo mysql` pour vous connecter en tant que root.
* Pour définir un mot de passe root classique ou changer le mode d’authentification, vous pouvez le faire dans MySQL après l’installation.

---