#!/usr/bin/env bash

INPUT_DIR="$1"
OUTPUT_DIR="$2"

if [ -z "$INPUT_DIR" ]; then
  echo "Error: input directory is required."
  echo "Usage: ./run.sh <input_dir> [output_dir]"
  exit 1
fi

if [ -z "$OUTPUT_DIR" ]; then
  OUTPUT_DIR="$INPUT_DIR"
fi

try {
    uv run convert_safetensors_batch.py "$INPUT_DIR" "$OUTPUT_DIR"
} catch {
    echo "An error occurred: $?" >&2
    exit 1
}
