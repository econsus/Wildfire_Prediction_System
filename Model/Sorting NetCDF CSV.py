import pandas as pd

slhf=pd.read_csv('slhf_2023.csv')
sshf=pd.read_csv('sshf_2023.csv')
#var_out_ind=pd.read_csv('Variables_without_index.csv')
#hvc=pd.read_csv('hvc_csv.csv')
#lvc=pd.read_csv('lvc_csv.csv')

def sort_csv(csv,sorting_by):
    df=csv.sort_values(sorting_by)
    return df

slhf_sorted=sort_csv(slhf,['time','latitude','longitude'])
sshf_sorted=sort_csv(sshf,['time','latitude','longitude'])
#hvc_sorted=sort_csv(hvc,['time','latitude','longitude'])
#lvc_sorted=sort_csv(lvc,['time','latitude','longitude'])

#df=pd.concat([slhf_sorted,sshf_sorted['sshf']],axis=1,join='outer')
ds=pd.concat([slhf_sorted['slhf'],sshf_sorted['sshf']],axis=1,join='outer')
#ds=pd.concat([var_out_ind,lvc_sorted['cvl']],axis=1,join='outer')

print(ds.head())

#df.to_csv('Variables_with_index.csv')
ds.to_csv('Variable_without_index.csv',index=False,index_label=False)
