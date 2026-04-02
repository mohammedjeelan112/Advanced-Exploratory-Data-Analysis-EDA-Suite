import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class EDASuite:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def summary_stats(self):
        """Return descriptive statistics for numeric columns"""
        return self.df.describe().T

    def missing_values(self):
        """Return count of missing values per column"""
        return self.df.isnull().sum()

    def correlations(self, method="pearson"):
        """Return correlation matrix for numeric columns only"""
        numeric_df = self.df.select_dtypes(include=["int64", "float64"])
        return numeric_df.corr(method=method)

    def plot_histograms(self, save_dir="plots"):
        """Plot histograms for all numeric columns"""
        os.makedirs(save_dir, exist_ok=True)
        numeric_cols = self.df.select_dtypes(include=["int64", "float64"]).columns
        for col in numeric_cols:
            plt.figure(figsize=(6,4))
            sns.histplot(self.df[col], kde=True, bins=10)
            plt.title(f"Histogram of {col}")
            plt.tight_layout()
            plt.savefig(f"{save_dir}/{col}_hist.png")
            plt.close()

    def plot_correlation_heatmap(self, save_dir="plots"):
        """Generate and save a correlation heatmap for numeric columns"""
        import os
        import matplotlib.pyplot as plt
        import seaborn as sns

        os.makedirs(save_dir, exist_ok=True)

        # Select numeric columns only
        numeric_df = self.df.select_dtypes(include=["int64", "float64"])

        plt.figure(figsize=(8,6))
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(f"{save_dir}/correlation_heatmap.png")
        plt.close()