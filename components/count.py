import pandas as pd

df, df_head = '', ''

class Count:
    def val_leb(self):
        values = [0]*self.df_head
        label = [0]*self.df_head
        for i in range(0, self.df_head):
            values[i] = self.df.iloc[i]
            label[i] = self.df.index[i] + ": " + str(values[i])
        both = [i for i, _ in enumerate(values)]
        return values, label, both

    def action(self, data):
        print("Counting data...\n")
        self.df_head = data.action.value_counts().head(5).count()
        self.df = data.action.value_counts()
        return df_head, df
    
    def mean_actions(self, data):
        return str(data.action.value_counts().mean())

    def mean_dc(self, data):
        return str(data.data_center.value_counts().mean())

    def sum_storage(self, data):
        return str(data.storage_used_MB.value_counts().sum())

    def data_center(self, data):
        print(f"Counting dc for ...\n")
        self.df_head = data.data_center.value_counts().head(5).count()
        self.df = data.data_center.value_counts()
        return df_head, df

    def continent(self, data):
        self.df_head = data.continent.value_counts().count()
        self.df = data.continent.value_counts()
        return df_head, df

    def tfe(self, data):
        self.df_head = data.target_file_extension.value_counts().head(5).count()
        self.df = data.target_file_extension.value_counts()
        return df_head, df

    def app_inferred(self, data):
        self.df_head = data.app_inferred.value_counts().head(5).count()
        self.df = data.app_inferred.value_counts()
        return df_head, df

    def domain_status(self, data):
        print(f"Counting dc ...\n")
        self.df_head = data.domain_status.value_counts().head(5).count()
        self.df = data.domain_status.value_counts()
        return df_head, df