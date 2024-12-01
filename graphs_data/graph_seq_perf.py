import pandas as pd
import matplotlib.pyplot as plt

def create_cache_misses_plot(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  

    df_mean = df.groupby('n').agg({'cache_misses': 'mean'}).reset_index()

    df_mean['cache_misses'] = df_mean['cache_misses'].astype(int)

    # Crea il grafico per 'cache_misses'
    plt.figure(figsize=(10, 6))
    plt.plot(df_mean['n'], df_mean['cache_misses'], marker='o', label='Cache Misses', color='g')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Average Cache Misses')
    plt.title('Average Cache Misses vs Matrix Size (Sequential)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

file_path = 'sequential_results_perf.csv'
create_cache_misses_plot(file_path)
