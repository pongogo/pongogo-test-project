#!/usr/bin/env python3
"""Sample main module for Pongogo E2E testing.

This file exists to provide a minimal Python project structure
that Pongogo can initialize and test against.
"""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    """Entry point for the sample project."""
    print(greet("Pongogo"))


if __name__ == "__main__":
    main()
