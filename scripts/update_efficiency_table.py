import json
from dataclasses import dataclass
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

from aoc_solutions.efficiency_leaderboard import EfficiencyRecord, load_efficiency_leaderboard, LEADERBOARD_FILENAME


ROOT = Path(__file__).resolve().parents[1]
AOC_SOLUTIONS_DIR = ROOT / "aoc_solutions"
README_PATH = ROOT / "README.md"

TABLE_START = "<!-- efficiency-table-start -->"
TABLE_END = "<!-- efficiency-table-end -->"


def get_best_records_for_day(day_dir: Path) -> Dict[int, EfficiencyRecord]:
    """
    For a given day folder (aoc_solutions/day_X), load leaderboard.json
    and return best records per part:
      {1: BestRecord(...), 2: BestRecord(...)}
    """
    leaderboard_path = day_dir / LEADERBOARD_FILENAME
    leaderboard = load_efficiency_leaderboard(leaderboard_path)

    if not leaderboard:
        return {}

    best: Dict[int, EfficiencyRecord] = {}
    for record in leaderboard:
        if record.part not in (1, 2):
            continue
        if record.part not in best:
            best[record.part] = record
            continue
        if record.runtime_ms < best[record.part].runtime_ms:
            best[record.part] = record

    return best


def get_day_directories() -> List[Path]:
    """
    Return all aoc_solutions/day_* directories sorted by day number.
    """
    day_dirs: List[Path] = []
    for p in AOC_SOLUTIONS_DIR.iterdir():
        if p.is_dir() and p.name.startswith("day_"):
            # parse day number from 'day_X'
            try:
                day_num = int(p.name.split("_", 1)[1])
            except (IndexError, ValueError):
                continue
            day_dirs.append((day_num, p))

    day_dirs.sort(key=lambda tup: tup[0])
    return [p for _, p in day_dirs]


def build_table() -> str:
    """
    Build the markdown table summarizing best runtime/memory for each day.
    """
    rows: List[str] = []

    # Header
    rows.append(
        "Day | P1 Runtime (ms) | P1 Memory (KB) | P2 Runtime (ms) | P2 Memory (KB)"
    )
    rows.append(
        "--- | --------------- | ------------- | --------------- | -------------"
    )

    day_dirs = get_day_directories()
    for day_dir in day_dirs:
        best = get_best_records_for_day(day_dir)
        day_num = int(day_dir.name.split("_", 1)[1])
        if not best:
            rows.append(f"{day_num} | - | - | - | -")
            continue


        def fmt(part: int, field: str) -> str:
            rec: EfficiencyRecord | None = best.get(part)
            if rec is None:
                return "-"
            
            if field == "runtime_ms":
                return f"{rec.runtime_ms:.3f}"
            if field == "peak_memory_kb":
                return f"{rec.peak_memory_kb:.1f}"
            return "-"

        p1_rt = fmt(1, "runtime_ms")
        p1_mem = fmt(1, "peak_memory_kb")
        p2_rt = fmt(2, "runtime_ms")
        p2_mem = fmt(2, "peak_memory_kb")

        rows.append(f"{day_num} | {p1_rt} | {p1_mem} | {p2_rt} | {p2_mem}")

    return "\n".join(rows)


def update_readme() -> None:
    table_md = build_table()

    if not README_PATH.exists():
        raise SystemExit(f"README.md not found at {README_PATH}")

    text = README_PATH.read_text()

    if TABLE_START in text and TABLE_END in text:
        # Replace existing block
        before, rest = text.split(TABLE_START, 1)
        _, after = rest.split(TABLE_END, 1)
        new_text = (
            before
            + TABLE_START
            + "\n"
            + table_md
            + "\n"
            + TABLE_END
            + after
        )
    else:
        print("Table markers not found in README.md. Aborting.")
        return

    README_PATH.write_text(new_text)
    print("README.md efficiency table updated.")


if __name__ == "__main__":
    update_readme()