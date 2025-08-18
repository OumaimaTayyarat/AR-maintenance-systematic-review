import pandas as pd
import os

# Liste de fichiers Excel
files = [
    "C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\googleScholar_export_unique.xlsx",
    "C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\IEEE_export_unique.xlsx",
    "C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\ScienceDirect_Export_unique.xlsx",
    "C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\scopus_export_unique.xlsx"
]

dfs = []

for f in files:
    # Charger sans restriction
    df = pd.read_excel(f)

    # Normaliser les noms de colonnes
    df.columns = df.columns.str.strip().str.lower()

    # Renommer si nécessaire
    rename_map = {
        "authors": "Authors",
        "author": "Authors",
        "title": "Title",
        "publication": "Publication",
        "journal": "Publication",
        "year": "Year",
        "year published": "Year",
        "publication year": "Year",
        "publisher": "Publisher",
        "source": "Publisher"
    }
    df = df.rename(columns=rename_map)

    # Garder uniquement les colonnes standard
    expected_cols = ["Authors", "Title", "Publication", "Year", "Publisher"]
    for col in expected_cols:
        if col not in df.columns:
            df[col] = None  # si colonne absente, la créer vide
    
    df = df[expected_cols]

    dfs.append(df)

# Concaténer tous les fichiers
merged = pd.concat(dfs, ignore_index=True)

# Normaliser les titres et supprimer les doublons
merged["Title"] = merged["Title"].astype(str).str.lower().str.strip()
merged = merged.drop_duplicates(subset=["Title"], keep="first")

# Sauvegarde finale
output_file = "C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\merged_unique.xlsx"
merged.to_excel(output_file, index=False)

print(f"✅ Fichier final fusionné et sans doublons : {output_file}")
