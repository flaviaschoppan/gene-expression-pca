import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global aesthetics style for diagnostic plots
sns.set_theme(style="whitegrid", context="talk")

def plot_pca(coords_df: pd.DataFrame, metadata: pd.DataFrame, outpath: str):
    """
    Plot PCA scatterplot clored by experimental condition.

    Parameters
    ----------
    coords_df : pd.DataFrame
        DataFrame with PCA coordinates.
        Index = sample names
        Columns = PC1, PC2, ...
    
    metadata : pd.DataFrame
        DataFrame with sample metadata.
        Index = sample names
        Must contain a column named 'condition'.
    
    outpath : str
        Path where the figure will be saved.
    """

    # Merge PCA coordinates with metadata
    df = coords_df.join(metadata)

    plt.figure(figsize=(7,6))

    sns.scatterplot(
        data=df, 
        x="PC1", 
        y="PC2", 
        hue="condition", 
        s=100
    )

    plt.title("PCA of expression matrix")
    plt.xlabel("PC1")
    plt.ylabel("PC2")

    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()