# IntroPARCO D1


## Description
This repo is the collection of codes related to the project "Parallel Matrix Transposition: Exploring Implicit
and Explicit Parallelism with OpenMP". The following are the instruction to replicate the results presented in the report.

Disclaimer: I used **WSL** (Windows subsystem for Linux) on my local machine to run all the codes (i. e. python codes for the graphs), to this tutorial uses Linux commands.
To run the Python files you need to have Python installed. Version and requested modules are specified in the report.


## Environment setup
The first thing you have to do is clone this repo on your computer. Inside the repo there are two folders and this **README.md**:
- **codes_and_jobs**: is the folder where the three C++ implementations are, together with the PBS files to run the jobs in the cluster.
- **graphs_data**: is the folder where you will put the CSV results files once the jobs will be complete. There are also the python files that generate the graphs.

To perfectly replicate this project, you need to have access to the HPC cluster of the University of Trento, and login in it, either being connected to the university wifi or using the VPN.


## Load into HPC cluster
You should now open the terminal and navigate it up to the repository folder. Now to load every C++ code and the PBS job submissions you have to use the command
```
scp /codes_and_jobs/* your.username@hpc.unitn.it:/home/your.usename/codes_and_jobs/
```
in the terminal. You will be asked to put your unitn password. Then the copy to the cluster will be completed.


## Jobs submission
Move now to the cluster terminal, thet by now should point to your home directory. Use 
```
cd codes_and_jobs
```
to enter the directory you just copied into the cluster. Now you can start to submit the jobs.

### Sequential implementation
These two jobs will compile the C++ code *matrix_transp_seq.cpp*
- We submit the job described in *job_submission_seq_time.pbs*, that will provide us a CSV file with the times of the functions *checkSym* and      *matTranspose*. This job will run in the **short_cpuQ**. to run the job use this code in the cluster terminal (pointing inside *codes_and_jobs*):
    ```
    qsub job_submission_seq_time.pbs
    ```
- We submit the job described in *job_submission_seq_perf.pbs*, that will provide us a CSV file with the times of the functions *checkSym* and      *matTranspose*, together with the number of cache misses of every run of the code. This job will run in the **short_cpuQ**. to run the job use this code in the cluster terminal (pointing inside *codes_and_jobs*):
    ```
    qsub job_submission_seq_perf.pbs
    ```

### Implicit parallelization implementation
These two jobs will compile the C++ code *matrix_transp_imp.cpp*
- We submit the job described in *job_submission_imp_opt_time.pbs*, that will provide us a CSV file with the times of the functions *checkSym* and      *matTranspose*. This job will run in the **short_cpuQ**. to run the job use this code in the cluster terminal (pointing inside *codes_and_jobs*):
    ```
    qsub job_submission_imp_opt_time.pbs
    ```
- We submit the job described in *job_submission_imp_opt_perf.pbs*, that will provide us a CSV file with the times of the functions *checkSym* and      *matTranspose*, together with the number of cache misses of every run of the code. This job will run in the **short_cpuQ**. to run the job use this code in the cluster terminal (pointing inside *codes_and_jobs*):
    ```
    qsub job_submission_imp_opt_perf.pbs
    ```
### Explicit parallelization implementation with OpenMP
This job will compile the C++ code *matrix_transp_imp.cpp*
- We submit the job described in *job_submission_omp_time.pbs*, that will provide us a pbs file with the times of the functions *checkSym* and      *matTranspose*, using 1, 2, 4, 8, 16 and 32 threads. This job will run in the **short_cpuQ**. to run the job use this code in the cluster terminal (pointing inside *codes_and_jobs*):
    ```
    qsub job_submission_omp_time.pbs
    ```

You can check at any time the status of your jobs using the command
```
qstat -u your.username
```

## Data collection and graphs
Once you are sure that **every** job has finished in the cluster, use this command on your local terminal (that by now should be pointing inside the directory *IntroPARCO_D1_Cecchin_Nicolò*, if not, be sure to get there before continuing) to download every CSV output file.
```
scp your.username@hpc.unitn.it:/home/your.username/codes_and_jobs/*.csv ./graphs_data/
```
### Graphs 
The following instructions are for the graphs included in the report. There are more python files that provide graphs for other data, but in this README it will only be explained how to create the graphs of the report.
Once again, be sure to have all the CSV file inside the directory. Then, use this command to enter the graphs directory:
```
cd graphs_data
```
Then use this commands to get the graphs:
- **Sequential transposition time**
    ```
    python3 graph_seq_time.py
    ```
- **Implicit transposition time**
    ```
    python3 graph_imp_time.py
    ```
- **OpenMP transposition time**
    ```
    python3 graph_omp_time.py
    ```
- **Speedup of implicit compared to sequential / Reduction of cache misses of implicit compared to sequential**
    ```
    python3 graph_comparison_seq_imp.py
    ```
- **Speedup of OpenMP compared to sequential / Efficiency opf OpenMP per thread**
    ```
    python3 graph_comparison_seq_omp.py
    ```

## Conclusion
That was all for what concerned the data collection and processing.