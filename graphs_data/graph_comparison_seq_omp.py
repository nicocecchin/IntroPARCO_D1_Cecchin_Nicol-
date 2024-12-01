import pandas as pd
import matplotlib.pyplot as plt


def plot_speedup_efficiency(seq_file, openmp_file):
    seq_df = pd.read_csv(seq_file)
    seq_df.columns = seq_df.columns.str.strip()
    openmp_df = pd.read_csv(openmp_file)
    openmp_df.columns = openmp_df.columns.str.strip()

    seq_avg = seq_df.groupby('n')['seconds_for_transposition'].mean().reset_index()
    seq_avg = seq_avg.rename(columns={'seconds_for_transposition': 'avg_seq_time'})

    openmp_avg = openmp_df.groupby(['n', 'threads'])['seconds_for_transposition'].mean().reset_index()
    openmp_avg = openmp_avg.rename(columns={'seconds_for_transposition': 'avg_openmp_time'})

    merged_df = pd.merge(openmp_avg, seq_avg, on='n', how='inner')

    merged_df['speedup'] = merged_df['avg_seq_time'] / merged_df['avg_openmp_time']
    merged_df['efficiency'] = merged_df['speedup'] / merged_df['threads']

    thread_counts = sorted(merged_df['threads'].unique())

    plt.figure(figsize=(10, 6))
    for t in thread_counts:
        thread_data = merged_df[merged_df['threads'] == t]
        plt.plot(thread_data['n'], thread_data['speedup'], marker='o', label=f'{t} Thread(s)')
    plt.title('Speedup vs Matrix Size')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Speedup')
    plt.grid(True)
    plt.legend(title='Thread Count')
    plt.xscale('log') 
    plt.savefig('speedup_vs_matrix_size.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    for t in thread_counts:
        thread_data = merged_df[merged_df['threads'] == t]
        plt.plot(thread_data['n'], thread_data['efficiency'], marker='o', label=f'{t} Thread(s)')
    plt.title('Efficiency vs Matrix Size')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Efficiency')
    plt.grid(True)
    plt.legend(title='Thread Count')
    plt.xscale('log')  
    plt.savefig('efficiency_vs_matrix_size.png')
    plt.show()


plot_speedup_efficiency('sequential_results_time.csv', 'openmp_results_time.csv')
