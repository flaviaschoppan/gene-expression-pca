import pandas as pd
import numpy as np

def log2_transform(matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Apply log2(x + 1) transformation to stabilize variance and compress scale.

    This transformation is standard in expression analysis pipelines and helps:
    - reduce skewness
    - stabilize variance
    - make data more suitable for linear methods like PCA

    Input:
        rows = genes
        columns = samples
    
    Output:
        Log2-transformed matrix with same shape.
    """
    
    log_matrix = np.log2(matrix + 1)

    return log_matrix