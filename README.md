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
