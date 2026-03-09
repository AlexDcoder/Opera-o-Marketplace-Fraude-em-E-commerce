import pandas as pd

def outlier_iqr(df, coluna):
    """
    Detecta outliers usando a técnica IQR.
    Retorna o DataFrame limpo e um DataFrame apenas com os outliers.
    """
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    # Filtros
    outliers_mask = (df[coluna] < limite_inferior) | (df[coluna] > limite_superior)
    
    df_outliers = df[outliers_mask]
    df_limpo = df[~outliers_mask]
    
    print(f"Coluna: {coluna}")
    print(f"Outliers removidos: {len(df_outliers)}")
    print(f"Limites: {limite_inferior:.2f} a {limite_superior:.2f}\n")
    
    return df_limpo, df_outliers