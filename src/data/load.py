import pandas as pd

def load_data(path):
    train = pd.read_csv(f'{path}/train.csv')
    test = pd.read_csv(f'{path}/test.csv')

    return train, test
