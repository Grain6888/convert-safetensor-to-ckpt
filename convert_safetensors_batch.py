#!/usr/bin/env python3

import os
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
    input_path = normalize_path(input_dir)

    assert input_path.exists(), f"Error: 入力ディレクトリが存在しません: {input_path}"

    print(f"[INFO] Input:  {input_path}")

    # safetensors を再帰的に収集
    safetensors_files = list(input_path.rglob("*.safetensors"))
    total = len(safetensors_files)

    assert total > 0, (
        "Error: 入力ディレクトリに safetensors ファイルが見つかりませんでした"
    )

    print(f"[INFO] 変換対象ファイル数: {total}")

    for idx, safepath in enumerate(safetensors_files, start=1):
        print_progress(idx, total)

        # safetensors があるディレクトリ
        safedir = safepath.parent

        # output 未指定 → safetensors と同じディレクトリ
        if output_dir is None:
            ckpt_dir = safedir
        else:
            # output 指定 → safedir/output_dir の相対パス
            ckpt_dir = safedir / output_dir

        ckpt_dir.mkdir(parents=True, exist_ok=True)

        ckpt_path = ckpt_dir / safepath.with_suffix(".ckpt").name

        if ckpt_path.exists():
            print(f"[SKIP] {ckpt_path} は既に存在します")
            continue

        convert_safetensors_to_ckpt(str(safepath), str(ckpt_path))
        print(f"[DONE] {ckpt_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert .safetensors to .ckpt")
    parser.add_argument(
        "input_dir", type=str, help="Input directory containing .safetensors files"
    )
    parser.add_argument(
        "output_dir", type=str, nargs="?", help="Relative output directory (optional)"
    )
    args = parser.parse_args()

    # output_dir が None の場合は safetensors と同じディレクトリに出力
    convert_directory(args.input_dir, args.output_dir)
