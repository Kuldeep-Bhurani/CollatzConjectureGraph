import matplotlib.pyplot as plt


# def Plot(x, y, z):
def Plot(x, n):
    plt.plot(x)
    # plt.plot(y)
    # plt.plot(z)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title(
        f'Collatz Conjecture Graph of {n}')
    plt.show()
