"""Simple D&D d20 dice roller with advantage/disadvantage support."""

from __future__ import annotations

import argparse
import secrets
from typing import List


def roll_d20() -> int:
    """Roll a single d20 and return the result (crypto-strong)."""
    return secrets.randbelow(20) + 1


def roll_with_advantage() -> int:
    """Roll two d20s and take the higher (advantage)."""
    return max(roll_d20(), roll_d20())


def roll_with_disadvantage() -> int:
    """Roll two d20s and take the lower (disadvantage)."""
    return min(roll_d20(), roll_d20())


def _positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("count must be a positive integer")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Roll a D&D-style d20.")
    parser.add_argument(
        "-n",
        "--count",
        type=_positive_int,
        default=1,
        help="Number of times to roll (default: 1)",
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=("normal", "advantage", "disadvantage"),
        default="normal",
        help="Roll normally, with advantage, or with disadvantage",
    )
    return parser.parse_args()


def roll_many(count: int, mode: str) -> List[int]:
    rollers = {
        "normal": roll_d20,
        "advantage": roll_with_advantage,
        "disadvantage": roll_with_disadvantage,
    }
    roller = rollers[mode]
    return [roller() for _ in range(count)]


def main() -> None:
    args = parse_args()
    results = roll_many(args.count, args.mode)
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")


if __name__ == "__main__":
    main()
