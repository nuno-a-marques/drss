# -------------------------------------------------------------------------
# ----------------     SCRIPT TO PROCESS PRS RUNS -------------------------

# import data
import pandas as pd

# procedures
def numberModels(x, tt):
    #print(tt)
    if tt=='validation':
        nrows=1600
    else:
        nrows=2500
    row_number = x.name
    model_id = row_number//nrows + 1         # !!!  hard coded  !!!
    return model_id

# params list
window_length   =  100
decision_freq   =  200

test_type       = 'validation'
instance_number = 6

# data reading
#  example file name   detailedPerformance 100 200 validation i6.txt
data = pd.read_csv(  f'detailedPerformance {window_length} {decision_freq} {test_type} i{instance_number}.txt',header=None,delimiter=';')
data.rename(columns={   0: 'instance', 1: 'rule', 2: 'flex',
                        3: 'util', 4: 'allow', 5: 'seed',
                        6: 'tard', 7: 'flow', 8: 'maxqueue',
                        9: 'runtime', 10: 'aborted'}, inplace=True)
data['model_id'] = data.apply(numberModels, tt=test_type, axis='columns', raw=False, result_type='reduce')

# check
check = data[data.aborted != False]
control = check.shape[0]
if control > 0:
    print('some replication did not go until the end')

# pivot
table = pd.pivot_table(     data,
                            values='tard',
                            index=['util', 'allow'],
                            columns=['model_id'],
                            aggfunc="mean",
                            fill_value=0)

#print(table)

if test_type=='validation':
    utilisations = [0.83, 0.87, 0.93, 0.96]
    allowances   = [2.5 , 3.5 , 5.0 , 7.0 ]
else:
    utilisations = [0.80, 0.85, 0.90, 0.95, 0.97]
    allowances   = [2   , 3   , 4   , 6   , 8   ]

for util in utilisations:
    for allow in allowances:
        values = table.loc[(util, allow)]
        #print(values)
        for id in table.columns:
            #print(id)
            print(f'{window_length},{decision_freq},{instance_number},{util},{allow},{id},{values[id]}')
        del id
    del allow
del util

# clean environment
del window_length, decision_freq, test_type, instance_number
del data
del table
del check, control
del utilisations, allowances
del values

# --------------------------------------------------------------------------
# debug


