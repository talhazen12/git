#!/usr/bin/env python3
"""A tiny command-line app."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple greeting app")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
