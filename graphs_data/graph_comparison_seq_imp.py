import pandas as pd
import matplotlib.pyplot as plt

def calculate_means(df, group_by_column, target_column):
    return df.groupby(group_by_column)[target_column].mean()

seq_times_file = "sequential_results_time.csv"
implicit_times_file = "implicit_results_time.csv"
seq_cache_misses_file = "sequential_results_perf.csv"
implicit_cache_misses_file = "implicit_results_perf.csv"

seq_times = pd.read_csv(seq_times_file)
implicit_times = pd.read_csv(implicit_times_file)
seq_cache_misses = pd.read_csv(seq_cache_misses_file)
implicit_cache_misses = pd.read_csv(implicit_cache_misses_file)

seq_times.columns = seq_times.columns.str.strip()
implicit_times.columns = implicit_times.columns.str.strip()
seq_cache_misses.columns = seq_cache_misses.columns.str.strip()
implicit_cache_misses.columns = implicit_cache_misses.columns.str.strip()

seq_transpose_means = calculate_means(seq_times, 'n', 'seconds_for_transposition')
implicit_transpose_means = calculate_means(implicit_times, 'n', 'seconds_for_transposition')

speedup = seq_transpose_means / implicit_transpose_means

seq_cache_misses_means = calculate_means(seq_cache_misses, 'n', 'cache_misses')
implicit_cache_misses_means = calculate_means(implicit_cache_misses, 'n', 'cache_misses')

cache_miss_reduction = seq_cache_misses_means / implicit_cache_misses_means

plt.figure(figsize=(10, 6))
speedup.plot(marker='o', label="Speedup (Sequential / Implicit)", logx=True)
plt.title("Speedup of Implicit Execution Compared to Sequential")
plt.xlabel("Matrix Size (n)")
plt.ylabel("Speedup")
plt.legend()
plt.grid()
plt.savefig("speedup_plot.png")
plt.show()

plt.figure(figsize=(10, 6))
cache_miss_reduction.plot(marker='o', color='orange', label="Cache Miss Reduction (Sequential / Implicit)", logx=True)
plt.title("Cache Miss Reduction of Implicit Execution Compared to Sequential")
plt.xlabel("Matrix Size (n)")
plt.ylabel("Cache Miss Reduction")
plt.legend()
plt.grid()
plt.savefig("cache_misses_reduction_plot.png")
plt.show()
