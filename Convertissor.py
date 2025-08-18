# ==========================================================
# PART 1 : Convert a Scopus CSV export to Excel
# ==========================================================
import pandas as pd

# Path to the exported Scopus CSV file
fichier_csv = "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\export2025.08.15-07.31.27.csv"
# Path where the Excel file will be saved
fichier_xlsx = "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\IEEE_export.xlsx"

# Read the CSV file while respecting quotes (to avoid splitting authors by commas inside quotes)
df = pd.read_csv(fichier_csv, quotechar='"')

# Save as a clean Excel file
df.to_excel(fichier_xlsx, index=False)

print(f"✅ Excel file created: {fichier_xlsx}")


# ==========================================================
# PART 2 : Convert a Google Scholar CSV export to Excel
# ==========================================================
import pandas as pd

# Input and output paths
input_csv = "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\citations (1).csv"
output_xlsx = "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\googleScholar_export.xlsx"

# Read the CSV file (the 'python' engine is more tolerant with irregular CSV formatting)
df = pd.read_csv(input_csv, engine="python")

# (Optional) Light cleaning of column names and values
df.columns = [c.strip() for c in df.columns]  # Remove extra spaces from column names
for col in df.columns:
    if df[col].dtype == object:  # Apply only on text columns
        df[col] = df[col].astype(str).str.strip()  # Remove spaces before/after text

# Export to Excel
df.to_excel(output_xlsx, index=False)
print("✅ Exported to ->", output_xlsx)


# ==========================================================
# PART 3 : Convert a plain text file (ScienceDirect export) into Excel
# ==========================================================
import re
import pandas as pd

# Load the raw text file containing references
with open("C:\\Users\\Oumaima.TAYYARAT\\Downloads\\ScienceDirect_citations_1755442728891.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split articles by double newlines (each article is separated by blank lines)
raw_articles = [a.strip() for a in text.split("\n\n") if a.strip()]

# Initialize a list to store extracted data
data = []

# Loop through each article and extract metadata using regex patterns
for article in raw_articles:
    authors = re.search(r"^(.*?)\,\n", article, re.S)
    title = re.search(r",\n(.*?)\,\n", article, re.S)
    journal = re.search(r"\n(.*?),\nVolume", article, re.S)
    volume = re.search(r"Volume\s+([\w\d]+)", article)
    issue = re.search(r"Issue\s+([\w\d]+)", article)
    pages = re.search(r"Pages\s+([\d–-]+)", article)
    year = re.search(r"\n(\d{4}),", article)
    doi = re.search(r"(https:\/\/doi\.org\/[^\s]+)", article)
    
    # Append extracted values into a dictionary (one per article)
    data.append({
        "Authors": authors.group(1).strip() if authors else "",
        "Title": title.group(1).strip() if title else "",
        "Journal": journal.group(1).strip() if journal else "",
        "Volume": volume.group(1) if volume else "",
        "Issue": issue.group(1) if issue else "",
        "Pages": pages.group(1) if pages else "",
        "Year": year.group(1) if year else "",
        "DOI": doi.group(1) if doi else ""
    })

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("C:\\Users\\Oumaima.TAYYARAT\\Downloads\\ScienceDirect_Export.xlsx", index=False)

print("✅ Conversion finished: ScienceDirect_Export.xlsx generated")
