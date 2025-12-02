import json
from pathlib import Path
import time
import tracemalloc
from contextlib import contextmanager
from dataclasses import dataclass, asdict

LEADERBOARD_FILENAME = "efficiency_leaderboard.json"

@dataclass
class EfficiencyRecord:
    day: int
    part: int
    runtime_ms: float
    peak_memory_kb: float
    timestamp: float

def get_day_folder(day: int) -> Path:
    day_folder = Path("aoc_solutions") / f"day_{day}"
    if not day_folder.exists():
        raise FileNotFoundError(f"Day folder for day {day} does not exist.")
    return day_folder

def load_efficiency_leaderboard(file_path: Path) -> list[EfficiencyRecord]:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return [EfficiencyRecord(**record) for record in data]
    except FileNotFoundError:
        return []

def save_efficiency_record(record: EfficiencyRecord, file_path: Path) -> None:
    """Save the efficiency record to the leaderboard file."""
    leaderboard = load_efficiency_leaderboard(file_path)

    if check_record_is_pb(record, leaderboard):
        leaderboard.append(record)
        with open(file_path, "w") as f:
            json.dump([asdict(rec) for rec in leaderboard], f, indent=4)
    else:
        print("Record is not a personal best; not saving.")

def is_record_more_efficient(new_record: EfficiencyRecord, existing_record: EfficiencyRecord) -> bool:
    """Determine if new_record is more efficient than existing_record based on runtime and memory usage."""
    if new_record.runtime_ms < existing_record.runtime_ms:
        return True
    if new_record.runtime_ms == existing_record.runtime_ms:
        return new_record.peak_memory_kb < existing_record.peak_memory_kb
    return False

def check_record_is_pb(record: EfficiencyRecord, leaderboard: list[EfficiencyRecord]) -> bool:
    """Check if the given record is a personal best compared to the leaderboard."""
    for existing_record in leaderboard:
        if (existing_record.day == record.day and
            existing_record.part == record.part):
            if not is_record_more_efficient(record, existing_record):
                return False
    return True

def print_leaderboard(day: int) -> None:
    """Print the efficiency leaderboard for the given day, grouped by part."""
    file_path = get_day_folder(day) / LEADERBOARD_FILENAME
    leaderboard = load_efficiency_leaderboard(file_path)

    if not leaderboard:
        print(f"No records for Day {day}.")
        return

    for part in (1, 2):
        part_records = [r for r in leaderboard if r.part == part]
        print(f"Efficiency Leaderboard for Day {day} - Part {part}:")
        if not part_records:
            print("  No records.")
            continue

        for record in sorted(part_records, key=lambda r: (r.runtime_ms, r.peak_memory_kb)):
            print(f"  {record.runtime_ms:.2f} ms, {record.peak_memory_kb:.2f} kb at {time.ctime(record.timestamp)}")

@contextmanager
def measure_efficiency(day: int, part: int):
    """Context manager to measure efficiency of a code block."""
    tracemalloc.start()
    start_time = time.perf_counter()
    error = None
    try:
        yield
    except Exception as e:
        error = e
    finally:
        end_time = time.perf_counter()
        _, peak = tracemalloc.get_traced_memory()
        peak_memory_kb = peak / 1024
        tracemalloc.stop()

        if error:
            print(f"An error occurred, not saving efficiency record.")
        else:
            # Save the efficiency record
            record = EfficiencyRecord(
                day=day,
                part=part,
                runtime_ms=(end_time - start_time) * 1000,
                peak_memory_kb=peak_memory_kb,
                timestamp=time.time()
            )
            print(f"Run completed in {record.runtime_ms:.2f} ms, peak memory {record.peak_memory_kb:.2f} kb.")
            save_efficiency_record(record, get_day_folder(day) / LEADERBOARD_FILENAME)

