import pandas as pd
import matplotlib.pyplot as plt

def create_plots_for_threads(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  

    df_mean = df.groupby(['n', 'threads']).agg({'seconds_for_checksym': 'mean', 'seconds_for_transposition': 'mean'}).reset_index()

    plt.figure(figsize=(10, 6))
    for thread_count in df_mean['threads'].unique(): 
        df_thread = df_mean[df_mean['threads'] == thread_count]
        plt.plot(df_thread['n'], df_thread['seconds_for_checksym'], marker='o', label=f'{thread_count} Threads')

    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Average Time for Checksym (seconds)')
    plt.title('Average Time for Checksym vs Matrix Size for Different Threads (OpenMP)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    for thread_count in df_mean['threads'].unique(): 
        df_thread = df_mean[df_mean['threads'] == thread_count]
        plt.plot(df_thread['n'], df_thread['seconds_for_transposition'], marker='o', label=f'{thread_count} Threads')

    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Average Time for Transposition (seconds)')
    plt.title('Average Time for Transposition vs Matrix Size for Different Threads (OpenMP)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig("transpose_omp.png")
    plt.show()

file_path = 'openmp_results_time.csv'
create_plots_for_threads(file_path)
