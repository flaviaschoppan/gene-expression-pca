# Gene Expression PCA Pipeline

This repository implements a minimal, explicit and reproducible exploratory pipeline for gene expression data analysis.

The goal of this project is to formalize the typical first steps of a transcriptomics analysis workflow:

- Load a gene expression count matrix
- Normalize counts to make samples comparable
- Apply log-transformation for numerical stabilization
- Perform PCA (Principal Component Analysis)
- Inspect the global structure of the samples

This project is **not** intended to perform differential expression analysis or biological interpretation.  
Its focus is strictly on **data preparation, numerical conditioning and exploratory structure inspection**.

---

## Planned pipeline steps

1. Load raw counts and sample metadata
2. Normalize counts (CPM)
3. Apply log2(x + 1) transformation
4. Run PCA on samples
5. Generate PCA plot colored by condition
6. Save numerical results and figures as pipeline artifacts

---

## Project structure

```text
gene-expression-pca/
├── data/
│   └── raw/
├── pipeline/
├── outputs/
│   ├── figures/
│   └── tables/
├── run_pipeline.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Status

This project is under active development.
The pipeline structure and modules will be implemented step by step.


## Conceptual focus

> Before interpreting biology, you must understand the numerical structure of your data.

This repository is designed as a didactic and structural example of how exploratory transcriptomics pipelines are organized in practice.