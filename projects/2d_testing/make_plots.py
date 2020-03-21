import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = 'data/raw_data.txt'

def main():

    # Load data from file into DataFrame
    df = pd.read_csv(DATA_FILE, sep='\t', header=None, names=['x', 'y'])

    # Plot the data
    plot = df.plot.scatter(x='x', y='y')

    # Save the plot
    plot.get_figure().savefig('plots/scatter.png')
    

if __name__ == '__main__':
    main()
