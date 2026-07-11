#!/usr/bin/env python3
"""CLI: readme-template"""
import sys, json, argparse
from datetime import datetime
def main():
    parser = argparse.ArgumentParser(description="Readme Template")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    r = {"tool": "readme-template", "v": "1.0.0", "author": "Jose Zuma"}
    print(json.dumps(r, indent=2) if args.json else f"{name} v1.0.0")
if __name__ == "__main__": main()
