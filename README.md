# Dispatching rule selection systems for dynamic jobs shops

#### Scope of the repository
The purpose of this github repository is to enable anyone to test their dispatching rule selection systems in a dynamic job shop simulator.

#### Dispatching rule selection system
In many real-world applications, such as manufacturing settings, uncertain events occur all the time, thus reactive methods are necessary.

In dynamic scheduling, dispatching rules (DRs) such as SPT and FIFO become quite popular as they make scheduling decisions quickly.

However, each dispacthing rule has preferential operating conditions, some are suitable when the job shop is loaded, others perform better when the job shop is emptier.

Therefore, dispatching rule selection systems (DRSSs) emerged in the literature. Their goal is to select DRs over time as conditions change. Two main types of systems emerged in the literature:

| DRSS type  | Description  |
| :----------------: |:-----------------:|
| PRS - Periodic Rule Selection    | Select a DR at fixed periods of time &Delta;t; Tackled with Supervised Learning |
| RTRS - Real time rule selection      | Select a DR every time a machine becomes idle; Tackled with Reinforcement Learning       |

#### Dynamic job shop instances
The dynamic job shop is a scheduling problem in which jobs arrive randomly over time to be processed in a pool of machines. Each job has a set of operations that must be processed in a given sequence, and each operation must be processed by a particular machine. In our work the goal is to optimize tardiness, i.e., the time jobs take beyond their due date.

The main parameters are the following:

|   | Parameter  | Validation | Test |
| :-------------: |:--------------:|:------------:|:---------------:|
| *M*    | Number of Machines | 20 | 20 |
| *J* | Number of Jobs | 2500 | 2500 |
| *O_j* | Number of operations per job | U(2,14) | U(2,14) |
| *p_jo* | Processing times of operations | U(1,*ptMax*): *ptMax*={50,100} | U(1,*ptMax*): *ptMax*={50,100,200} |
| *u* | Utilisation level | 0.83, 0.87, 0.93, 0.96 | 0.80, 0.85, 0.90, 0.95, 0.97 |
| *a* | Allowance factor | 2.5, 3.5, 5, 7 | 2, 3, 4, 6, 8 |
| nRep | Number of replications for each *u*, *a*, *ptMax* combination | 100 | 100|

#### Configuring the simulator

##### Specific guidelines for periodic rule selection models

##### Specific guidelines for real time rule selection models

#### Computing model performance
The software will output a file for each *ptMax*.
These files must be processed in the following manner to compute the tardiness score of each model:
1. Compute the average performance of each model for each *ptMax*, *u* and *a* combination;
2. Normalise the values computed in the previous step by the respective reference (see tables that follow);
3. Compute the geometric mean using the normalised values.




















