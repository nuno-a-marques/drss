# Dispatching rule selection systems for dynamic jobs shops

#### Scope of the repository
The purpose of this github repository is to enable anyone to test their dispatching rule selection systems in a dynamic job shop simulator.

In this page, the focus goes towards the practical side, more precisely, setting the code, running the models, and processing the results.
If one desires more in-depth information, it can be found in the working paper or in the presentation.
[working-paper](drs-for-dfjssp/paper-1.pdf) [slideshow](drs-for-dfjssp/slideshow-1.pdf)

#### Table of Contents

[TOC]

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
| *O<sub>j</sub>* | Number of operations per job | U(2,14) | U(2,14) |
| *p<sub>jo</sub>* | Processing times of operations | U(1,*ptMax*): *ptMax*={50,100} | U(1,*ptMax*): *ptMax*={50,100,200} |
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

##### Reference values, validation

| u | a  | ptMax |  Reference | | u | a | ptMax | Reference |
| :-------------: |:--------------:|:------------:|---------------:|------------:|:---------------:|:---------------:|:---------------:|---------------:|
| 0.83 |2.5 |50 |331823 | | 0.83 |2.5 |100 |590031 |
| 0.83 |3.5 |50 |108854 | | 0.83 |3.5 |100 |176085 |
| 0.83 |5.0 |50 |10837 | | 0.83 |5.0 |100 |13666 |
| 0.83 |7.0 |50 |302 | | 0.83 |7.0 |100 |343 |
| 0.87 |2.5 |50 |578357 | | 0.87 |2.5 |100 |1020988 |
| 0.87 |3.5 |50 |293228 | | 0.87 |3.5 |100 |478362 |
| 0.87 |5.0 |50 |60361 | | 0.87 |5.0 |100 |80757 |
| 0.87 |7.0 |50 |3991 | | 0.87 |7.0 |100 |4297 |
| 0.93 |2.5 |50 |1208267 | | 0.93 |2.5 |100 |2126587 |
| 0.93 |3.5 |50 |870462 | | 0.93 |3.5 |100 |1456940 |
| 0.93 |5.0 |50 |416861 | | 0.93 |5.0 |100 |624458 |
| 0.93 |7.0 |50 |95647 | | 0.93 |7.0 |100 |116017 |
| 0.96 |2.5 |50 |1680673 | | 0.96 |2.5 |100 |2944442 |
| 0.96 |3.5 |50 |1329707 | | 0.96 |3.5 |100 |2248914 |
| 0.96 |5.0 |50 |783862 | | 0.96 |5.0 |100 |1238100 |
| 0.96 |7.0 |50 |276994 | | 0.96 |7.0 |100 |370385 |

##### Reference values, test

| u | a  | ptMax |  Reference | | u | a | ptMax | Reference | | u | a | ptMax | Reference |
| :-------------: |:--------------:|:------------:|---------------:|------------:|:---------------:|:---------------:|:---------------:|---------------:|---------------:|:---------------:|:---------------:|:---------------:|---------------:|
| 0.80 |2 |50 |369241 | | 0.80 |2 |100 |681827| | 0.80 |2 |200 |1318873 |
| 0.80 |3 |50 |119671 | | 0.80 |3 |100 |201698| | 0.80 |3 |200 |369831 |
| 0.80 |4 |50 |21719 | | 0.80 |4 |100 |33211| | 0.80 |4 |200 |56527 |
| 0.80 |6 |50 |98 | | 0.80 |6 |100 |138| | 0.80 |6 |200 |172 |
| 0.80 |8 |50 |7 | | 0.80 |8 |100 |16| | 0.80 |8 |200 |48 |
| 0.85 |2 |50 |621761 | | 0.85 |2 |100 |1130057| | 0.85 |2 |200 |2163763 |
| 0.85 |3 |50 |322463 | | 0.85 |3 |100 |547952| | 0.85 |3 |200 |1004930 |
| 0.85 |4 |50 |116701 | | 0.85 |4 |100 |176537| | 0.85 |4 |200 |306929 |
| 0.85 |6 |50 |5697 | | 0.85 |6 |100 |6172| | 0.85 |6 |200 |8488 |
| 0.85 |8 |50 |50 | | 0.85 |8 |100 |34| | 0.85 |8 |200 |54 |
| 0.90 |2 |50 |1046847 | | 0.90 |2 |100 |1889954| | 0.90 |2 |200 |3594317 |
| 0.90 |3 |50 |725368 | | 0.90 |3 |100 |1241692| | 0.90 |3 |200 |2296481 |
| 0.90 |4 |50 |428998 | | 0.90 |4 |100 |678579| | 0.90 |4 |200 |1199313 |
| 0.90 |6 |50 |80044 | | 0.90 |6 |100 |98732| | 0.90 |6 |200 |155712 |
| 0.90 |8 |50 |7247 | | 0.90 |8 |100 |6589| | 0.90 |8 |200 |7401 |
| 0.95 |2 |50 |1749588 | | 0.95 |2 |100 |3113202| | 0.95 |2 |200 |5858747 |
| 0.95 |3 |50 |1407777 | | 0.95 |3 |100 |2416214| | 0.95 |3 |200 |4470124 |
| 0.95 |4 |50 |1064130 | | 0.95 |4 |100 |1749864| | 0.95 |4 |200 |3152303 |
| 0.95 |6 |50 |428072 | | 0.95 |6 |100 |615217| | 0.95 |6 |200 |1031406 |
| 0.95 |8 |50 |122761 | | 0.95 |8 |100 |146724| | 0.95 |8 |200 |217069 |
| 0.97 |2 |50 |2154590 | | 0.97 |2 |100 |3785902| | 0.97 |2 |200 |7074386 |
| 0.97 |3 |50 |1782232 | | 0.97 |3 |100 |3086554| | 0.97 |3 |200 |5707281 |
| 0.97 |4 |50 |1416460 | | 0.97 |4 |100 |2360131| | 0.97 |4 |200 |4291922 |
| 0.97 |6 |50 |671327 | | 0.97 |6 |100 |1020995| | 0.97 |6 |200 |1748243 |
| 0.97 |8 |50 |252311 | | 0.97 |8 |100 |322718| | 0.97 |8 |200 |506110 |

#### Benchmark
