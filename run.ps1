param(
    [Parameter(Mandatory=$true)]
    [string]$InputDir,

    [string]$OutputDir
)

if (-not $OutputDir) {
    $OutputDir = $InputDir
}

uv run convert_safetensors_batch.py $InputDir $OutputDir
