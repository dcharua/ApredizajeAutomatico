import json
import numpy as np
import pandas as pd


class Stats:
    def __init__(self, df):
        self.df = df

    def get_stats(self, column):
        base_stats = {}

        # Check if column is numeric.
        if pd.to_numeric(self.df[column], errors="coerce").notnull().all():
            base_stats["mean"] = self.df[column].mean()
            base_stats["median"] = self.df[column].median()
            base_stats["max"] = self.df[column].max()
            base_stats["min"] = self.df[column].min()
            base_stats["var"] = self.df[column].var()
            base_stats["sem"] = self.df[column].sem()

        base_stats["shape"] = str(self.df[column].shape)

        return json.dumps(base_stats)
