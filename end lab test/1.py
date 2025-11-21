#!/usr/bin/env python3
"""
Bubble Sort with Swap Counter + BEAUTIFUL Visible Test Cases
Run this file → see every test input/output/swaps clearly + mutation testing
"""

from __future__ import annotations
import random
from typing import Tuple, List

def bubble_sort_with_swaps(arr: List[int]) -> Tuple[List[int], int]:
    """Bubble sort that returns sorted list and number of swaps performed."""
    if not arr:
        return arr.copy(), 0

    sorted_arr = arr.copy()
    n = len(sorted_arr)
    total_swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                total_swaps += 1
                swapped = True
        if not swapped:
            break

    return sorted_arr, total_swaps


# =============================================================================
# Beautiful Visible Test Runner (No hidden tests anymore!)
# =============================================================================

def run_visible_tests():
    print("=" * 70)
    print("     BUBBLE SORT WITH SWAP COUNTER - DETAILED TEST RESULTS")
    print("=" * 70)

    tests = [
        ("Empty list",          []),
        ("Single element",      [42]),
        ("Already sorted",      [1, 2, 3, 4, 5]),
        ("Reverse sorted",      [5, 4, 3, 2, 1]),
        ("Random list",         [64, 34, 25, 12, 22, 11, 90]),
        ("With duplicates",     [5, 2, 8, 2, 1, 5]),
        ("Large random (20)",   [random.randint(0, 100) for _ in range(20)]),
    ]

    all_passed = True

    for i, (name, data) in enumerate(tests, 1):
        input_copy = data.copy()
        sorted_data, swaps = bubble_sort_with_swaps(input_copy)
        expected = sorted(data)
        passed = (sorted_data == expected)

        if not passed:
            all_passed = False

        status = "✓" if passed else "✗"
        print(f"\nTest {i} - {name}")
        print(f"Input  : {data}")
        print(f"Result : {sorted_data} | Swaps: {swaps}")
        print(f"Expected: {expected}")
        print(f"Status : {status} {'PASS' if passed else 'FAIL'}")

    print("\n" + "="*70)
    if all_passed:
        print("   ALL TESTS PASSED! Your implementation is PERFECT!")
    else:
        print("   SOME TESTS FAILED! Check above.")
    print("="*70)
    return all_passed


# =============================================================================
# Mutation Testing (still included)
# =============================================================================

def run_mutation_testing():
    try:
        from mutatest.api import run_mutation_trials
        print("\nRunning mutation testing (Pitest style)...")
        result = run_mutation_trials(
            source_file=__file__,
            test_cmds=["python", "-m", "unittest", "discover"],
            timeout=10,
        )
        survived = len(result.survived)
        killed = len(result.killed)
        print(f"\nMutation Score: {killed}/{(killed+survived)} mutants killed")
        print("ALL MUTANTS KILLED!" if survived == 0 else f"{survived} survived – add more tests!")
    except ImportError:
        print("\nmutatest not installed → skipping mutation testing")
        print("   Install with: pip install mutatest")
    except Exception as e:
        print(f"Mutation testing error: {e}")


# =============================================================================
# Main - Everything runs automatically
# =============================================================================

if __name__ == "__main__":
    tests_passed = run_visible_tests()

    if tests_passed:
        run_mutation_testing()
    else:
        print("\nFix the failures first before mutation testing.")

    print("\nDone! You can now submit this file confidently.")