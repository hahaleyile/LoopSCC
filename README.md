# LoopSCC

LoopSCC is a loop summarization tool capable of producing loop summaries represented by Z3 expressions, which are semantically equivalent to the loops being analyzed. Currently, LoopSCC supports integer addition and subtraction operations through a custom `INT` data type. Further support can be added by defining additional data types and operations.

## Build and Run

LoopSCC is written in Python 3, and we have tested it under Python 3.12. The dependencies for LoopSCC can be installed using the following command:

```
pip install -r requirements.txt
```

LoopSCC is provided as a library, and it needs to be invoked by writing custom code. The code in `expr1`, `expr2`, and `tests` folders demonstrate how to use LoopSCC, all of which can be run directly with Python.

## Usage

Using the `speed_pldi09_fig1` program from `expr1` as an example, we will demonstrate how to use LoopSCC.

First, you need to define the integer variables to be used as symbolic variables using the `INT.define_int` function. The argument is the display name of the symbolic variable and can be defined freely.

Then, use the `CFG.define_loop` function to define the loop structure, which follows the following syntax:

```
assign: tuple(INT, INT)
sequence: tuple(assigns)
body: list[sequence | choice]
choice: list[branches]
branch: tuple(condition, body)
loop: CFG(condition, body)
condition: list[list[constraints]]
```

`condition` represents the loop condition or branch condition in disjunctive normal form (DNF). The first list's elements represent the disjuncts (clauses), and each element within a clause represents a conjunctive constraint.

For example, the loop condition in the example program is defined as `[[x < 100], [y > 0]]`, meaning the loop condition is `(x < 100) || (y > 0)`. The condition for the second branch is defined as `[[x >= 100, y > 0]]`, representing the branch condition `(x >= 100 && y > 0)`. Conditional statements provide limited support for integer multiplication, division, and modulus operations.

The `body` of the loop consists of `sequence` and `choice`, where `sequence` represents a sequence structure, and `choice` represents a choice structure, all contained within a single list. By expanding sequentially, the loop program can ultimately be transformed into the format required by LoopSCC.

Once the input format is obtained, create instances of the `SPath_Graph` and `Summarizer` classes and call the `summarize` method to generate the loop summary.

LoopSCC provides three interfaces for further processing of loop summaries:

| Interface            | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| `solver_check_trace` | Checks whether the solver contains conditions can satisfy the specific SCC sequence execution. |
| `solve`              | Computes the output data for given input data. This interface calls `solver_check_trace`, adding the initial input data as conditions to the solver. Only one execution sequence is feasible, as guaranteed. |
| `check_after_loop`   | Checks whether the conditions after loop execution can be satisfied. |

## Experiment Section

The source code, input data, and results of various tools used in the experiments are available in the `experiments` folder. The source code for the test cases in Experiment 1 is stored in the `raw_files` folder, and we generated 1000 random input data for each test case, which are stored in the `input` path. Each tool records its results for every input data of each test case, which can be found in the `output` path. Additionally, Experiment 2 provides only the processed files run by LoopSCC, while the other tools follow the instructions at [SV-COMP 2024](https://sv-comp.sosy-lab.org/2024/results/results-verified/META_ReachSafety.table.html#/) for their execution. Details of the experimental setup can be found in the main body of the paper.

 