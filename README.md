# convert-safetensors-to-ckpt

A simple utility that converts a `.safetensors` file into a `.ckpt` file (PyTorch checkpoint).

Some old tools may not support the newer `.safetensor` file format. This utility allows converting data to the old `.ckpt` format.

## Usage

### Single File Conversion

To convert a single `.safetensors` file to a `.ckpt` file, use `convert_safetensors_to_ckpt.py`.

```sh
./convert_safetensors_to_ckpt.py my-model-file.safetensors my-model-file.ckpt
```

### Batch Directory Conversion

To convert all `.safetensors` files in a directory to `.ckpt` files, use `convert_safetensors_batch.py`. You can specify an optional output directory.

#### Using Python Script Directly

```sh
./convert_safetensors_batch.py input_directory [output_directory]
```

- `input_directory`: Directory containing the `.safetensors` files.
- `output_directory`: Optional. Relative path to save the converted `.ckpt` files. If not specified, files are saved in the same directory as the original `.safetensors` files.

#### Using PowerShell Script

```ps1
./run.ps1 -InputDir input_directory [-OutputDir output_directory]
```

- `-InputDir`: Directory containing the `.safetensors` files.
- `-OutputDir`: Optional. Relative path to save the converted `.ckpt` files. If not specified, files are saved in the same directory as the original `.safetensors` files.

#### Using Shell Script

```sh
./run.sh input_directory [output_directory]
```

- `input_directory`: Directory containing the `.safetensors` files.
- `output_directory`: Optional. Relative path to save the converted `.ckpt` files. If not specified, files are saved in the same directory as the original `.safetensors` files.

## Example

Convert all `.safetensors` files in the `models` directory and save the resulting `.ckpt` files in a `converted_models` subdirectory:

```sh
./convert_safetensors_batch.py models converted_models
```

Or using the shell script:

```sh
./run.sh models converted_models
```

Or using the PowerShell script:

```ps1
.\run.ps1 -InputDir models -OutputDir converted_models
```

`
