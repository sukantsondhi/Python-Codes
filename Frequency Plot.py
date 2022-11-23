import matplotlib.pyplot as plt

def fnplot(a):
    plt.plot(a)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.title('FIG 1')
    plt.show()

a=[1,1,2,2,2,3,4,4,5,6]
fnplot(a)
