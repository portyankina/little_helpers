import matplotlib.pyplot as plt
from numpy import min, max, searchsorted

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