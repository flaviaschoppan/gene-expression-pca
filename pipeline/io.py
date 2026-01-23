import pandas as pd 

def load_counts(path: str) -> pd.DataFrame:
    """
    Load raw gene expression count matrix.

    Expected format: 
    • Rows = genes
    • Columns = samples
    • First Column = gene identifiers
    """
    counts = pd.read_csv(path, index_col=0)
    return counts

def load_metadata(path: str) -> pd.DataFrame:
    """
    Load sample metadata table.

    Expected format:
    • Rows = samples
    • Columns = experimental annotations (e.g. condition)
    • First Column = sample identifiers
    """
    metadata = pd.read_csv(path, index_col=0)
    return metadata