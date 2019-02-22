import logging
import pandas as pd

log = logging.getLogger(__name__)
df, df_head = '', ''

class Count:
    def val_leb(self):
        log.info("Preparing data for calculation.")
        values = [0]*self.df_head
        label = [0]*self.df_head
        for i in range(0, self.df_head):
            values[i] = self.df.iloc[i]
            label[i] = self.df.index[i] + ": " + str(values[i])
        both = [i for i, _ in enumerate(values)]
        return values, label, both

    def top_action(self, data):
        log.info("Counting top 5 actions for FSE.")
        self.df_head = data.action.value_counts().head(5).count()
        self.df = data.action.value_counts()
        return df_head, df
    
    def mean_actions(self, data):
        log.info("Counting mean value of actions for FSE.")
        return str(data.action.value_counts().mean())

    def dd_mean_dc(self, data):
        log.info("Counting mean value of domains per data center.")
        return str(data.data_center.value_counts().mean())

    def sum_storage(self, data):
        log.info("Summing used storage.")
        return str(data.storage_used_MB.value_counts().sum())

    def dd_data_center(self, data):
        log.info("Counting domains per data center.")
        self.df_head = data.data_center.value_counts().head().count()
        self.df = data.data_center.value_counts()
        return df_head, df

    def fse_data_center(self, data):
        log.info("Counting actions per data center.")
        self.df_head = data.datacenter.value_counts().head().count()
        self.df = data.datacenter.value_counts()
        return df_head, df

    def continent(self, data):
        log.info("Counting actions per continent.")
        self.df_head = data.continent.value_counts().count()
        self.df = data.continent.value_counts()
        return df_head, df

    def app_inferred(self, data):
        log.info("Counting top 5 most used apps.")
        self.df_head = data.app_inferred.value_counts().head(5).count()
        self.df = data.app_inferred.value_counts()
        return df_head, df

    def hours(self, data):
        log.info("Counting activity each hour.")
        self.df_head = data.timestamp.dt.hour.value_counts().count()
        self.df = data.timestamp.dt.hour.value_counts()
        return df_head, df