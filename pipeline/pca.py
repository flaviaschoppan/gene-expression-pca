import pandas as pd
from sklearn.decomposition import PCA


def run_pca(matrix: pd.DataFrame, n_components: int = 2):
    """
    Run PCA on expression matrix to inspect global sample structure.

    Input:
        matrix: rows = genes, columns = samples

    The matrix is transposed internally because PCA is applied to samples.

    Output:
        coords_df: DataFrame with PCA coordinates (PC1, PC2, ...)
        explained_variance: array with variance explained per component
    """

    # ---------------------------------------------------------
    # Transpose: now rows = samples, columns = genes
    # ---------------------------------------------------------
    X = matrix.T

    # ---------------------------------------------------------
    # Fit PCA
    # ---------------------------------------------------------
    pca = PCA(n_components=n_components)
    coords = pca.fit_transform(X)

    # ---------------------------------------------------------
    # Build DataFrame with sample names
    # ---------------------------------------------------------
    coords_df = pd.DataFrame(
        coords,
        index=X.index,
        columns=[f"PC{i+1}" for i in range(n_components)]
    )

    return coords_df, pca.explained_variance_ratio_
