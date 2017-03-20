import matplotlib.pyplot as plt
from numpy import min, max, searchsorted, zeros, int, array, arange

def plot2hist(dist1, dist2, BlAreaCut_, fan_range, bl_range, text_label):
    plt.figure(1, figsize=(18,7))
    plt.subplot(121)
    fh = plt.hist(dist1, bins = 100, range = fan_range,  alpha=0.75, color = 'red', log=True)
    plt.ylabel('Number markins')
    plt.xlabel('Size, pixels')
    plt.title("Fans size distribution ") # + str(season3.obsid[season3.index[k]]) + ' L_s =' + str(Ls) )
    plt.xlim((0, fan_range[1]))
    plt.ylim((1,1e3))
    plt.text(1, 700, text_label)

    plt.subplot(122)
    bh = plt.hist(dist2,  bins = 100, range = bl_range, alpha=0.75, color = 'blue', log=True)
    if BlAreaCut_:
        plt.xlabel('Size, pixels^2')   
        plt.xticks(arange(0, 1e6, 5e5))  
    else:
        plt.xlabel('Size, pixels')
        
    plt.xlim((0, bl_range[1]))
    plt.ylabel('Number markins')
    plt.title("Blotches size distribution ") #+ str(season3.obsid[season3.index[k]]) )
    #plt.ylim((1,1e3))
    
def plot2seasons(ls1, dist11, dist12, ls2, dist21, dist22, labe1_str, labe2_str, 
                 title_str, plt1_title, plt2_title, x_str, y_str):
    plt.figure(1, figsize=(18,7))
    plt.figtext(0.1,1,title_str, fontsize=20)
    plt.subplot(121)
    plt.plot(ls1, dist11, '*', ms = 12, color='blue', label=labe1_str, alpha=0.75)
    plt.plot(ls1, dist12, 'o', ms = 10, color = 'red', label=labe2_str)
    Ymax = array( [dist11.max(), dist11.max(), dist21.max(), dist22.max() ])
    Ymin = array( [dist11.min(), dist11.min(), dist21.min(), dist22.min() ])
    #plt.ylim((Ymin.min() - Ymin.min()*0.1, Ymax.max() + Ymax.max()*0.1))
    #plt.xlim((170,270))
    plt.legend(loc='upper left', fontsize=20)
    plt.xlabel(x_str, fontsize=20)
    plt.ylabel(y_str, fontsize=20)
    plt.title(plt1_title, fontsize=20)
    plt.xticks(arange(170,280,10))
    plt.grid(True)

    plt.subplot(122)
    plt.plot(ls2, dist21, '*', ms = 12, color='blue', alpha=0.75)
    plt.plot(ls2, dist22, 'o', ms = 10, color = 'red')
    #plt.ylim((Ymin.min() - Ymin.min()*0.1, Ymax.max() + Ymax.max()*0.1))
    #plt.xlim((170,270))
    plt.xlabel(x_str, fontsize=20)
    plt.ylabel(y_str, fontsize=20)
    plt.title(plt2_title, fontsize=20)
    plt.xticks(arange(170,280,10))
    plt.grid(True)
    
def plot2taste(x_all, xlbl, ylbl, plot_lbls, plot_title):
    my_color = ['red', 'blue', 'green', 'orange', 'grey']
    
    x = x_all[:,0]
    y = x_all[:,1]    
    
    #plt.close('all')
    plt.clf()
    plt.title(plot_title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    
    plt.xlim(0, x[x.argmax()])
    
    plt.ylim(min(y) - 100 , max(y) + 0.1*max(y))
    
    if len(x_all.shape) > 1: 
        
        for i in range(1, x_all.shape[1]):
            y = x_all[:,i]
            plt.plot(x[:x.argmax()], y[:x.argmax()], color = my_color[i], label = plot_lbls[i])
    else:
        plt.plot(x, y, color ='blue', label = plot_lbls)
    plt.legend(loc='upper center', shadow=True) 
    plt.show()

#make plot with flat tops
def for_flat_tops_plot(x,y, dx):
    y_new = zeros(x.size*2)
    x_new = zeros(x.size*2)
    for i in range(x.size):
        y_new[i*2] = y[i]
        y_new[i*2 +1] = y[i]
        x_new[i*2] = x[i] - dx*0.5
        x_new[i*2+1] = x[i] + dx*0.5
    return x_new, y_new

def my_way_1plot(x, y, xlbl, ylbl, plotlbl):    
    fig, axes = plt.subplots(1,1, figsize=(20, 20))
    ax = plt.subplot(111) 
    ax.plot(x, y,'r', label=plotlbl)
    ax.legend(loc = 'lower right', fontsize = 20)
    ax.set_ylabel(ylbl, fontsize = 20)
    ax.set_xlabel(xlbl, fontsize = 20)
    x0 = int(x[0])
    xE = int(x[-1])
    dX = (xE-x0)//10
    ax.set_xticklabels(range(x0, xE, dX))
    ax.xaxis.set_tick_params(labelsize=18)
    ax.yaxis.set_tick_params(labelsize=18)
    ax.grid()