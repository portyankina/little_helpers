import matplotlib.pyplot as plt
import numpy as np

def plot_CO2_candy_buzzel(Ls,CO2_m_lee, CO2_m_gen ):
    plt.figure(0)
    plt.title('Kaitain')
    plt.xlabel('Ls, deg')
    plt.ylabel('CO2 frost, kg/m2')
    plt.xlim(0, 360)
    plt.ylim([-10,800])
    plt.plot(Ls[0:526], CO2_m_lee[0:526],  color='black', label = 'slip slope', linewidth=2.0)
    # dimentions for buzzel plot [10000:16487]
    plt.plot(Ls[527:], CO2_m_lee[527:],  color='black', linewidth=2.0)

    plt.plot(Ls[:526], CO2_m_gen[:526], '--', color='black', label = 'windward slope', linewidth=2.0)

    plt.plot(Ls[527:], CO2_m_gen[527:], '--', color='black', linewidth=2.0)
    plt.legend(loc='upper center', shadow=True) 
    plt.show()

    #plt.savefig('/Users/Anya/Dropbox/DrB_Images/my_plots/Candy_paper_plotKaitain01.png', dpi=300)

def plot_Europa_anomaly(time, anomaly ):
    plt.figure(0)
    plt.title('Mean anomaly')
    plt.xlabel('et time, s')
    plt.ylabel('mean anomaly, deg')
    plt.ylim(0, 360)
    plt.plot(time, anomaly, '*', color='black')
    plt.show()

    #plt.savefig('/Users/Anya/Dropbox/DrB_Images/my_plots/Candy_paper_plotKaitain01.png', dpi=300)