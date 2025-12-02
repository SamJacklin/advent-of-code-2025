# Advent of Code 2025

Here are my solutions to Advent of Code 2025. Rather than going for speed (which I gave a go last year), I decided to focus on execution efficiency.

The metrics I've chosen to capture for this focus includes runtime (ms) and peak memory usage (kb).

For each day, I've created a leaderboard that records the time of the attempt and the metric results. To keep the repository clean, I've only kept the optimal solutions.

Below is a summary of the metric results of the best performing solutions for each day:

## Performance Summary

<!-- efficiency-table-start -->
Day | P1 Runtime (ms) | P1 Memory (KB) | P2 Runtime (ms) | P2 Memory (KB)
--- | --------------- | ------------- | --------------- | -------------
1 | 3.185 | 209.3 | 4.844 | 209.3
2 | 2014.589 | 2.5 | 15727.221 | 3.0
<!-- efficiency-table-end -->

## Usage

I've created a Makefile for ease of running. 

To run the solution code for a given day and part simply run:

```
make run <day> <part>
```

To create a template for a new day, simply run:
```
make newday DAY=<day>
```