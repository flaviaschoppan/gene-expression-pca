# Gene Expression PCA Pipeline

This repository implements a minimal, explicit, and reproducible exploratory pipeline for gene expression data, including normalization, transformation, and PCA-based inspection of sample structure.

The pipeline formalizes the standard numerical conditioning and exploratory steps used before any multivariate analysis of expression data, making the structure of the dataset explicit, inspectable, and reproducible.

It provides a clear, modular workflow to load expression matrices and metadata, apply normalization and transformation, compute PCA, and generate interpretable artifacts for downstream analysis.

---

## Overview

In gene expression analysis, raw or even normalized matrices are not immediately interpretable in high-dimensional space.

Before any differential analysis or modeling, it is standard practice to:

• Normalize expression values
• Transform the scale
• Reduce dimensionality
• Inspect the global structure of samples

This project formalizes that exploratory stage as a small, modular, and reproducible pipeline.

---

## What this pipeline does

1. Loads a raw gene expression count matrix and a metadata table  
2. Normalizes counts to CPM (Counts Per Million)  
3. Applies log2(x + 1) transformation  
4. Runs PCA on the processed matrix  
5. Saves PCA coordinates as a numerical artifact  
6. Generates a PCA scatter plot colored by experimental condition  

---

## Why this matters

Gene expression matrices:

    • Are high-dimensional (thousands of genes)
    • Are highly skewed
    • Contain strong scale effects and variance distortions
    • Cannot be inspected directly

PCA is not used here as a statistical test, but as a **geometric diagnostic tool**:

    • To inspect whether samples cluster by condition
    • To detect outliers or strange samples
    • To verify whether the data structure makes sense before any modeling

This exploratory step exists in virtually every serious transcriptomics workflow, but is often done in ad-hoc scripts and not formalized as a pipeline.

---

## What this project is NOT

• This is not a differential expression analysis  
• This is not a biological interpretation pipeline  
• This is not a production RNA-seq workflow  

It is strictly an **exploratory, structural, and methodological pipeline** for:

    • Preprocessing
    • Dimensionality reduction
    • Global structure inspection

---

## Conceptual focus

> "Before testing hypotheses, you must understand the geometry of your data."

This project focuses on:

    • Scale
    • Variance structure
    • Sample relationships
    • Numerical conditioning

    Not on biological conclusions.

---

## Project structure

```text
gene-expression-pca/
├── data/
│   └── raw/
│       ├── counts.csv
│       └── metadata.csv
├── pipeline/
│   ├── __init__.py
│   ├── io.py
│   ├── normalization.py
│   ├── transform.py
│   ├── pca.py
│   └── plots.py
├── outputs/
│   ├── matrices/
│   └── figures/
├── run_pipeline.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Outputs

The pipeline produces the following versionable artifacts:
```
outputs/matrices/pca_coordinates.csv
outputs/figures/pca.png
```

```pca_coordinates.csv``` contains the numerical PCA coordinates of each sample

```pca.png``` is the visual inspection plot colored by experimental condition

---

## How to run

Install dependencies:

```pip install -r requirements.txt```


Run the pipeline:

```python run_pipeline.py```


All outputs will be written to the outputs/ folder.

---

## Reproducibility

All steps in this pipeline are:

    • Explicit
    • Deterministic
    • Scripted
    • Modular
    • And produce versionable artifacts

The pipeline can be rerun at any time and will always produce the same results given the same inputs.

---

## Data note

The data used in this repository are synthetic and intended solely to demonstrate:

    • The numerical behavior of the pipeline
    • The structure of the workflow
    • The geometry of PCA on expression-like data
    • They do not represent real biological experiments.

## Position in the project sequence


This project sits conceptually between:

    • Pure preprocessing / QC
    and
    • Any real downstream statistical analysis

It represents the transition from:

    • "Preparing the data"
    to
    • "Inspecting the structure of the data in multivariate space"

---

## License

This project is released under the MIT License.

---