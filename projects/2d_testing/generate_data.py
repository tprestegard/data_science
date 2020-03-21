import numpy as np

# Number of data points
N = 2000

# Range of x values
X_MIN = 0
X_MAX = 10

# Scale of jitter
JITTER_MAGNITUDE = 30

# Output file name
OUTPUT_FILE = './data/raw_data.txt'


# y = f(x)
def f(x):
    return 8*x + 37


# Main function
def main():
    # Seed the RNG
    np.random.seed(1)

    # X data points - uniform
    x = np.random.uniform(X_MIN, X_MAX, N)

    # Get Y data points
    y = f(x)

    # Add jitter (normally distributed)
    y += np.random.normal(0, JITTER_MAGNITUDE, N)

    # Write to a file
    np.savetxt(OUTPUT_FILE, np.c_[x, y], delimiter='\t', fmt='%0.9g')


if __name__ == '__main__':
    main()
