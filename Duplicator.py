import pandas as pd

# List of Excel files
files = [
    "C:\\Users\\Oumaima.TAYYARAT\\Documents\\PismaGuide\\googleScholar_export.xlsx",
    "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\PismaGuide\\IEEE_export.xlsx",
    "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\PismaGuide\\ScienceDirect_Export.xlsx",
    "C:\\Users\\Oumaima.TAYYARAT\\Downloads\\PismaGuide\\scopus_export.xlsx"
]

# Dictionary to store normalized titles with their file and row info
title_index = {}

# Function to normalize titles
def normalize_title(title):
    return ' '.join(str(title).lower().strip().split())

# Loop through each file
for f in files:
    df = pd.read_excel(f)
    df = df.reset_index()
    
    for idx, row in df.iterrows():
        norm_title = normalize_title(row['Title'])
        if norm_title not in title_index:
            title_index[norm_title] = []
        title_index[norm_title].append((f, row['index'] + 2))  # +2 for Excel row

# Check for duplicates
duplicates = {title: locations for title, locations in title_index.items() if len(locations) > 1}

# Convert to DataFrame for export
dup_list = []
for title, locs in duplicates.items():
    for file_path, row_num in locs:
        dup_list.append({
            "Title": title,
            "File": file_path,
            "Row": row_num
        })

dup_df = pd.DataFrame(dup_list)
dup_df.to_excel("C:/Users/Oumaima.TAYYARAT/Downloads/duplicates_report.xlsx", index=False)

print(f"✅ Found {len(duplicates)} duplicated titles. Report saved to duplicates_report.xlsx")
