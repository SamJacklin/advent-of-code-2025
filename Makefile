PYTHON := uv run python

# First arg = DAY, second arg = PART
run:
	@if [ "$(word 2,$(MAKECMDGOALS))" = "" ]; then \
	    echo "Usage: make run DAY PART"; exit 1; \
	fi
	$(PYTHON) -m aoc_solutions.day_$(word 2,$(MAKECMDGOALS)).solution_p$(word 3,$(MAKECMDGOALS))

%:
	@:

newday:
	@if [ -z "$(DAY)" ]; then \
		echo "Usage: make newday DAY=<number>"; \
		exit 1; \
	fi
	$(PYTHON) scripts/new_day_generator.py $(DAY)