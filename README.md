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
2 | 1984.406 | 2.5 | 4603.621 | 2.5
3 | 0.646 | 29.6 | 2.393 | 29.5
4 | 10.657 | 25.9 | 113.531 | 599.3
5 | 3.687 | 96.1 | 1.272 | 53.4
6 | 5.929 | 281.8 | 36.421 | 450.3
7 | 8.308 | 37.0 | 4.010 | 39.6
8 | 16236.942 | 88963.5 | 74335.824 | 88963.4
9 | 414.339 | 86.1 | 13167.858 | 105860.3
10 | 880454.158 | 17410624.9 | 1072.982 | 2368.8
11 | 1.068 | 208.7 | 3.010 | 291.8
12 | 9.723 | 103.0 | - | -
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