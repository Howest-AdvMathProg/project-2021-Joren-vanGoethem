import pandas as pd
import json
import numpy as np
pd.set_option('display.max_columns', 500)


class DataHandler():
    def __init__(self, backend, config):
        self._backend = backend
        self._config = config

        self._df = pd.read_csv(config["dataset"]).replace(np.nan, 'unkown', regex=True)

    def get_columns(self):
        return list(self._df.columns)
    
    def get_rows(self, count:int = 10):
        return self._df.head(count)

    def search_all(self, query:str, exact=False):
        columns = list(self._df.columns)
        df = None
        if exact:
            for column in columns:
                if isinstance(df, pd.DataFrame): 
                    df = pd.concat([df,self._df[self._df[column] == query]])
                else: 
                    df = self._df[self._df[column] == query] 
        else:
            for column in columns:
                if self._df[column].dtypes == object:
                    df = self._df.loc[self._df[column].str.contains(query, case=False)]
        return df

    def search_column(self, column:str, query:str, exact=False):
        if exact:
            return self._df[self._df[column] == query]
        else:
            if self._df[column].dtypes == object:
                return self._df[self._df[column].str.contains(query, na=False, case=False)]


    def search_columns(self, columns, queries):
        tempdf = self._df
        if len(columns) == len(queries):
            for query in list(zip(columns,queries)):
                if self._df[column].dtypes == object:
                    tempdf = tempdf[tempdf[query[0]].str.contains(query[1], na=False, case=False)]
        elif len(queries) == 1:
            for column in columns:
                if self._df[column].dtypes == object:
                    tempdf = tempdf[tempdf[queries].str.contains(queries, na=False, case=False)]
        return tempdf

# test = DataHandler()

# alles hier onder werkt

# result = test.search_column('title', 'days')
# print(result)

# result = test.search_columns(['title', 'country'], 'belgium') 
# print(result.head())

# result = test.search_all('a')
# print(result.head())
