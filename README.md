# Nuxt-Tauri-Template

Un modèle de projet, servant de boilerplate pour créer mes futures applications web et bureau multiplateformes avec Nuxt.js et Tauri.

## Prérequis

- [pnpm](https://pnpm.io/) doit être installé sur votre système.
- [Rust](https://www.rust-lang.org/) (avec Cargo) doit être installé sur votre système.

## Installation

1. Clonez ce répertoire sur votre système local :

```bash
git clone https://github.com/MONCEF52341/Boilerplate-Nuxt-Tauri.git
```

2. Accédez au répertoire du projet :

```bash
cd nuxt-tauri-template
```

3. Installez l'interface de ligne de commande Tauri en utilisant pnpm :

```bash
pnpm i -g @tauri-apps/cli
```

4. Installez les dépendances du projet :

```bash
pnpm install
```

## Démarrage du développement

Pour lancer l'application en mode développement, utilisez la commande suivante :

En version Web:

```bash
pnpm run web
```

En version bureau:

```bash
pnpm run desktop
```

L'application sera accessible par défaut à l'adresse `http://localhost:3000`. Vous pouvez modifier l'adresse et le port dans le fichier `src-tauri/tauri.conf.json`.

## Création d'un bundle pour le serveur

Pour créer le bundle qui pourra etre lancé sur le serveur, utilisez la commande suivante :

```bash
pnpm run webbuild
```

## Création d'un exécutable

Pour créer un exécutable de votre application, utilisez la commande suivante :

```bash
pnpm run deskbuild
```

L'exécutable sera généré dans le répertoire `dist/`.

## Résolution des problèmes

Si vous rencontrez des problèmes avec les dépendances, vous pouvez essayer d'ajouter manuellement les dépendances Tauri en utilisant la commande suivante :

```bash
pnpm add @tauri-apps/api @tauri-apps/cli
```

## Personnalisation de l'application

Pour personnaliser votre application, vous pouvez modifier les champs suivants dans le fichier `src-tauri/tauri.conf.json` :

- `devPath` : L'adresse et le port utilisés pour l'application en mode développement.
- `productName` : Le nom de votre application.
- `version` : La version de votre application.
- `identifier` : L'identifiant de votre application. Il sera utilisé pour générer le nom du fichier exécutable.
- `title` : Le titre de la fenêtre de votre application.
- `allowlist` : Une liste blanche d'API système, de système de fichiers, de shell, de PATH, de presse-papiers, de notifications et de système de fenêtres auxquelles votre application aura accès.

Vous pouvez également modifier les icônes de votre application en remplaçant les fichiers dans le répertoire `src-tauri/icons/`. Un script est fourni pour convertir une image en icône.

## Build

Ce répertoire dispose d'un workflow qui compile le projet sur 4 architectures : Windows, MacOS (AArch64 et x86), et Ubuntu.
