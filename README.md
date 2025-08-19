# Systematic Review – AR Maintenance

## Description
This project automates the processing and analysis of scientific publications on Augmented Reality (AR)-assisted maintenance. It includes data import from different databases, duplicate removal, consolidation into a single file, as well as extraction and filtering according to PRISMA criteria.

## Project Structure

### 1. **Import and Conversion**
Export files from different databases are converted to uniform format (Excel/CSV) to facilitate analysis.

* **Source files:**
   * `googleScholar_export.xlsx`
   * `IEEE_export.xlsx`
   * `ScienceDirect_Export.xlsx`
   * `scopus_export.xlsx`
* **Code:** `Convertissor.py`
* **Output:** Excel files ready for processing.

### 2. **Duplicate Removal and Consolidation**
Duplicate publications between different sources are removed and all data is combined into a **single file**.

* **Code:** `Duplicator.py` and `mergeUnique.py`
* **Output:** `merged_unique_FullDatabase.xlsx`

### 3. **PRISMA Filtering**
Publications are filtered step by step according to PRISMA criteria:

1. **Title-based filtering**
   * **Code:** `firstFilterPrisma.py`
   * **Output:** `publications_AR_maintenance_abstractTitle.xlsx`

2. **Title and abstract filtering**
   * **Output:** `publications_cleaned.xlsx`

3. **Introduction and conclusion filtering**
   * **Output:** `publications_AR_maintenance_IntroductionConclusion.xlsx`

Non-selected publications are stored in `publications_non_AR_maintenance.xlsx`.

### 4. **Additional Files**
* `duplicates_report.xlsx`: report on removed duplicates.
* `titres_non_trouves.xlsx`: list of  non-retrieved titles.
* `Capture d'écran 2025-08-17 192843.png`:  visualization.

## Installation

1. Install Python (>= 3.8)
2. Install required libraries:

```bash
pip install pandas openpyxl
```

## Usage

1. Place database exports in the main folder.
2. Run `Convertissor.py` to unify files.
3. Run `Duplicator.py` and `mergeUnique.py` to remove duplicates and merge.
4. Apply PRISMA filters with `firstFilterPrisma.py` and follow the filtering steps by title, abstract, then introduction/conclusion.

## Output Files

| File | Description |
|------|-------------|
| `merged_unique_FullDatabase.xlsx` | Complete consolidated database after duplicate removal |
| `publications_AR_maintenance_abstractTitle.xlsx` | Publications after title-based filtering |
| `publications_cleaned.xlsx` | Publications after title and abstract filtering |
| `publications_AR_maintenance_IntroductionConclusion.xlsx` | Final publications after full-text filtering |
| `publications_non_AR_maintenance.xlsx` | Excluded publications with reasons |
| `duplicates_report.xlsx` | Detailed duplicate removal report |

## PRISMA Compliance

This workflow follows PRISMA 2020 guidelines for systematic reviews, ensuring:
- **Transparency:** All filtering steps are documented and traceable
- **Reproducibility:** Automated scripts ensure consistent application of criteria
- **Reporting:** Detailed logs of inclusion/exclusion decisions at each stage

## Contact

For questions about methodology or technical implementation, please refer to the main systematic review publication or open an issue in this repository.
