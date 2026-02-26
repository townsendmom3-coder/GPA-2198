import numpy as np
import pandas as pd

class OutlierDetector:
    def __init__(self, data):
        self.data = data

    def detect_outliers_iqr(self):
        Q1 = np.percentile(self.data, 25)
        Q3 = np.percentile(self.data, 75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return [x for x in self.data if x < lower_bound or x > upper_bound]

    def detect_outliers_z_score(self):
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        z_scores = [(x - mean) / std_dev for x in self.data]
        return [self.data[i] for i in range(len(z_scores)) if np.abs(z_scores[i]) > 3]