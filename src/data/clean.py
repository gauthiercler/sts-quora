import pandas as pd


def clean_set(input_filepath, output_filepath, filename):

    print(f'Loading {input_filepath}/{filename}')
    df = pd.read_csv(f'{input_filepath}/{filename}')

    df.dropna(inplace=True)

    print(f'Saving to {output_filepath}/{filename}')
    df.to_csv(f'{output_filepath}/{filename}', index=False)
