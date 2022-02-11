from .models import Book

import pandas as pd


def main():
    df = pd.read_csv("dataset.csv")
    # print(df.shape)
    for index, row in df.iterrows():
        book = Book(index, row[1], row[2], row[3], row[4], row[5])
        book.save()
        # break
