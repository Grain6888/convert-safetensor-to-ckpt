#!/usr/bin/env python3

import torch
from safetensors.torch import load_file


def convert_safetensors_to_ckpt(safetensors_path, ckpt_path):
    # Load the .safetensors file
    print(f"Loading safetensors file from: {safetensors_path}")
    state_dict = load_file(safetensors_path)

    # Wrap the state_dict under the expected structure
    print("Wrapping state_dict under 'state_dict' key...")
    ckpt = {"state_dict": state_dict}

    # Save the checkpoint as a .ckpt file
    print(f"Saving ckpt file to: {ckpt_path}")
    torch.save(ckpt, ckpt_path)
    print(f"Conversion complete: {ckpt_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert .safetensors to .ckpt")
    parser.add_argument(
        "safetensors_path", type=str, help="Path to the input .safetensors file"
    )
    parser.add_argument(
        "ckpt_path", type=str, help="Path to save the output .ckpt file"
    )
    args = parser.parse_args()

    convert_safetensors_to_ckpt(args.safetensors_path, args.ckpt_path)
