import matplotlib.pyplot as plt
import numpy as np

def binomial_coeff(n, k):
    coeff = 1
    for i in range(min(k, n - k)):
        coeff *= (n - i)
        coeff /= (i + 1)
    return int(coeff)

def plot_pascals_triangle(rows):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    for row in range(rows):
        for col in range(row + 1):
            x = col - row / 2
            y = -row
            coeff = binomial_coeff(row, col)
            ax.add_patch(plt.Circle((x, y), 0.3, color='skyblue', ec='black', lw=1.5))
            ax.text(x, y, str(coeff), ha='center', va='center', fontsize=10)

    plt.xlim(-rows / 2, rows / 2)
    plt.ylim(-rows, 1)
    plt.show()

rows = 5  # Number of rows in Pascal's Triangle
plot_pascals_triangle(rows)
