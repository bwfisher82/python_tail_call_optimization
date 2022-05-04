import config

from stack_util import stack_size
from recursion_util import recurse, tail_recursive


def factorial(n: int) -> int:
    config.stack_depth = stack_size()
    return 1 if n == 0 else n * factorial(n - 1)


def tail_call_factorial(n: int, accumulator: int = 1) -> int:
    config.stack_depth = stack_size()
    return accumulator if n == 0 else tail_call_factorial(n - 1, accumulator * n)


def recursion_without_tail_calls() -> None:
    config.stack_depth = None
    factorial(config.DEPTH)


def recursion_with_tail_calls_no_optimization(accumulator: int = 1) -> None:
    config.stack_depth = None
    tail_call_factorial(config.DEPTH, accumulator)


@tail_recursive
def recursion_with_tail_calls_manual_optimization(n: int, accumulator: int = 1) -> int:
    if n - 1 == 0: return accumulator
    recurse(n - 1, accumulator=accumulator * n)


def main() -> None:
    recursion_without_tail_calls()
    print(f"Stack Depth, Recursion Without Tail Calls: {config.stack_depth}")
    recursion_with_tail_calls_no_optimization()
    print(f"Stack Depth, Recursion With Tail Calls: {config.stack_depth}")
    recursion_with_tail_calls_manual_optimization(config.DEPTH_LARGE)
    print(f"Stack Depth, Recursion With Tail Calls, Manually Optimized: {config.stack_depth}")


if __name__ == "__main__":
    main()
