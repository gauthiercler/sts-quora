import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

def plot_confusion_matrix(y_true, y_pred, metric='recall'):

    if metric not in ['recall', 'precision']:
        metric = 'recall'
    cm = confusion_matrix(y_true, y_pred)
    cm = cm.astype(np.float) / cm.sum(axis=0 if metric == 'precision' else 1)[:, np.newaxis]

    df_cm = pd.DataFrame(cm, columns=np.unique(y_true), index = np.unique(y_true))
    df_cm.index.name = 'Actual'
    df_cm.columns.name = 'Predicted'

    plt.figure(figsize = (7,5))
    sn.set(font_scale=1.4)

    ax = sn.heatmap(df_cm, cmap="Blues", annot=True, annot_kws={"size": 16}, square=True)
    ax.set_title(metric)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)

    plt.show()
