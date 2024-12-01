import pandas as pd
import matplotlib.pyplot as plt

def create_plots_from_csv(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  
    df_mean = df.groupby('n').agg({'seconds_for_checksym': 'mean', 'seconds_for_transposition': 'mean'}).reset_index()
    

    plt.figure(figsize=(10, 6))
    plt.plot(df_mean['n'], df_mean['seconds_for_checksym'], marker='o', label='Seconds for Checksym', color='b')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Average Time for Checksym (seconds)')
    plt.title('Average Time for Checksym vs Matrix Size (Sequential)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_mean['n'], df_mean['seconds_for_transposition'], marker='o', label='Seconds for Transposition', color='r')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Average Time for Transposition (seconds)')
    plt.title('Average Time for Transposition vs Matrix Size (Sequential)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')  
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig("transpose_seq.png")
    plt.show()

file_path = 'sequential_results_time.csv'
create_plots_from_csv(file_path)
