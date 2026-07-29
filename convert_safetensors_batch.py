#!/usr/bin/env python3

import os
import sys
from pathlib import Path

from convert_safetensors_to_ckpt import convert_safetensors_to_ckpt


def normalize_path(p: str) -> Path:
    return Path(os.path.expanduser(p))


def print_progress(current: int, total: int, bar_length: int = 30):
    ratio = current / total
    filled = int(bar_length * ratio)
    bar = "█" * filled + "░" * (bar_length - filled)
    percent = int(ratio * 100)
    print(f"[{bar}] {percent}% ({current}/{total})")


def convert_directory(input_dir: str, output_dir: str | None):
    try:
        input_path = normalize_path(input_dir)

        if not input_path.exists():
            raise FileNotFoundError(
                f"Error: Input directory does not exist: {input_path}"
            )

        print(f"[INFO] Input:  {input_path}")

        # Recursively collect safetensors files
        safetensors_files = list(input_path.rglob("*.safetensors"))
        total = len(safetensors_files)

        if total == 0:
            raise FileNotFoundError(
                "Error: No safetensor files found in the input directory"
            )

        print(f"[INFO] Conversion target files count: {total}")

        for idx, safepath in enumerate(safetensors_files, start=1):
            print_progress(idx, total)

            # Directory containing the safetensor file
            safedir = safepath.parent

            # Output directory not specified -> same as safetensor directory
            if output_dir is None:
                ckpt_dir = safedir
            else:
                # Output directory specified -> relative path
                ckpt_dir = safedir / output_dir

            ckpt_dir.mkdir(parents=True, exist_ok=True)

            ckpt_path = ckpt_dir / safepath.with_suffix(".ckpt").name

            if ckpt_path.exists():
                print(f"[SKIP] {ckpt_path} already exists")
                continue

            convert_safetensors_to_ckpt(str(safepath), str(ckpt_path))
            print(f"[DONE] {ckpt_path}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert .safetensors to .ckpt")
    parser.add_argument(
        "input_dir", type=str, help="Input directory containing .safetensors files"
    )
    parser.add_argument(
        "output_dir",
        type=str,
        nargs="?",
        default=None,
        help="Relative output directory (optional)",
    )
    args = parser.parse_args()

    # If output_dir is not specified, use the same directory as the safetensor files
    convert_directory(args.input_dir, args.output_dir)
