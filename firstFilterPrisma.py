import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from transformers import pipeline

# Pour avoir une détection stable
DetectorFactory.seed = 0

# Charger le fichier Excel
df = pd.read_excel("C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\FilterPhase1Prisma.xlsx")

# 1. Supprimer les doublons dans la colonne Title
df = df.drop_duplicates(subset=["Title"], keep="first")

# 2. Garder uniquement les publications entre 2017 et 2025
df = df[df["Year"].between(2017, 2025)]

# 3. Supprimer les titres qui ne sont pas en anglais
def is_english(title):
    try:
        return detect(title) == 'en'
    except LangDetectException:
        return False

df = df[df["Title"].apply(is_english)]

# 4. Classification automatique des titres
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Définir les labels de la classification
labels = ["Computer Science & Engineering", "Other"]

def classify_title(title):
    result = classifier(title, labels)
    # Retourne True si le titre appartient au label CS&E avec confiance > 0.5
    return result["labels"][0] == "Computer Science & Engineering" and result["scores"][0] > 0.5

df = df[df["Title"].apply(classify_title)]

# Sauvegarder le fichier nettoyé
df.to_excel("C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\publications_cleaned.xlsx", index=False)

print("✅ Nettoyage et classification terminés. Résultat enregistré dans publications_cleaned.xlsx")
