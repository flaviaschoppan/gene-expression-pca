"""
Gene Expression PCA Pipeline

This script orchestrates a minimal and explicit exploratory pipeline for
gene expression data, including normalization, transformation and PCA-based
inspection of global sample structure.

Pipeline steps:
1. Load raw counts and metadata
2. Normalize counts to CPM (Counts Per Million)
3. Apply log2(x + 1) transformation
4. Run PCA on processed expression matrix
5. Save PCA coordinates as a CSV artifact
6. Generate PCA scatterplot colored by experimental condition

The goal is not biological interpretation, but structural and numerical
inspection of the dataset before any downstream analysis.
"""

from pipeline.io import load_counts, load_metadata
from pipeline.normalization import cpm
from pipeline.transform import log2_transform
from pipeline.pca import run_pca
from pipeline.plots import plot_pca


def main():
    # ------------------------------------------------------------------
    # Step 1 — Load raw data
    # ------------------------------------------------------------------
    print("Loading raw counts and metadata...")
    counts = load_counts("data/raw/counts.csv")
    metadata = load_metadata("data/raw/metadata.csv")
    print("✓ Step 1 finished: raw data loaded\n")

    # ------------------------------------------------------------------
    # Step 2 — CPM normalization
    # ------------------------------------------------------------------
    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 2 finished: CPM normalization applied\n")

    # ------------------------------------------------------------------
    # Step 3 — Log2 transformation
    # ------------------------------------------------------------------
    print("Applying log2 transformation...")
    log_matrix = log2_transform(cpm_matrix)
    print("✓ Step 3 finished: log2 transformation applied\n")

    # ------------------------------------------------------------------
    # Step 4 — PCA
    # ------------------------------------------------------------------
    print("Running PCA...")
    coords_df, explained_variance = run_pca(log_matrix, n_components=2)
    print("✓ Step 4 finished: PCA computed\n")

    # ------------------------------------------------------------------
    # Step 5 — Save PCA coordinates
    # ------------------------------------------------------------------
    print("Saving PCA coordinates...")
    coords_df.to_csv("outputs/matrices/pca_coordinates.csv")
    print("✓ Step 5 finished: PCA coordinates saved to outputs/matrices/\n")

    # ------------------------------------------------------------------
    # Step 6 — Generate PCA plot
    # ------------------------------------------------------------------
    print("Generating PCA plot...")
    plot_pca(
        coords_df=coords_df,
        metadata=metadata,
        outpath="outputs/figures/pca.png"
    )
    print("✓ Step 6 finished: PCA plot saved to outputs/figures/\n")

    # ------------------------------------------------------------------
    # Final report
    # ------------------------------------------------------------------
    print("Explained variance ratio:")
    for i, v in enumerate(explained_variance, start=1):
        print(f"  PC{i}: {v:.3f}")

    print("\nPipeline finished successfully.")


if __name__ == "__main__":
    main()
