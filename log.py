import numpy as np
import pandas as pd
import os
import json

class MyLogger:
    def __init__(self):
        with open("./settings.json",'r') as rf: 
            self.settings = json.load(rf)
            rf.close()
        self.filedir =self.settings["logging"]["loggingfile"]
        if not os.path.exists(self.filedir):
            # create
            new_df = pd.DataFrame(columns=self.settings["logging"]["columns"])
            self.df = new_df
        else:
            self.df = pd.read_csv(self.filedir,index_col=False)
        
        self.names = set(list(self.df["Name"]))
        
        self.status_dct = {
           1:'Win',
           0:'Draw',
           -1:'Loss',
        }

    
    def put(self,name,status):
        if name in self.names:
            row_idx = self.df[self.df["Name"]==name].index
            col_idx = self.status_dct[status]
            val = self.df.loc[row_idx,col_idx]
            self.df.loc[row_idx,col_idx] = val+1
        else:
            self.df.loc[len(self.df)] = {
                "Name":name,
                "Win":0,
                "Draw":0,
                "Lose":0
            }
            
            row_idx = self.df[self.df["Name"]==name].index
            col_idx = self.status_dct[status]
            val = self.df.loc[row_idx,col_idx]
            self.df.loc[row_idx,col_idx] = val+1
        
    def get(self,name):
        if name in self.names:
            return np.array(self.df.values)[:,1:]
            return self.df[self.df["Name"]==name].values[0][1:]
        else:
            return [-1,-1,-1]
    def save(self):
        self.df.to_csv(self.filedir,index=0)
    
    def gettop3(self):
        values = np.array(self.df.values)[:,1:]
        scores = values[:,0]*0+values[:,1]*1+values[:,2]*3
        
        
    
    
if __name__=="__main__":
    logger = MyLogger()
    #logger.put('Alan',1)
    #logger.put('Yuang',1)
    print(logger.get('Alan'))
    #logger.get('Alan')
    logger.save()
                