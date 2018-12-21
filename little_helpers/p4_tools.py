import pandas as pd

def get_marking(line, cut=0.8):
    data = []
    for marking in ['fan_','blotch_']:
        m = line[line.index.str.startswith(marking)]
        data.append(m.rename_axis(lambda x: x[x.index('_')+1:]))
    fnotch = markings.Fnotch(line.fnotch_value, data[0], data[1])
    return fnotch.get_marking(cut)

def get_final_markings_counts(root, img_name, cut=0.5):
    # writing in dictionary here b/c later I convert it to pd.DataFrame
    # for which a dictionary is a natural input format
    d = {}
    d['obsid'] = img_name
    blotch_fname = root / '{}_blotches.csv'.format(img_name) #was _latlon
    d['n_blotches'] = len(pd.read_csv(str(blotch_fname)))
    fan_fname = root / '{}_fans.csv'.format(img_name) # was '{}_fans_latlons.csv'.format(img_name)
    d['n_fans'] = len(pd.read_csv(str(fan_fname)))
    
    return d

