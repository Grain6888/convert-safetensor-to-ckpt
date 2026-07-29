param(
    [Parameter(Mandatory=$true)]
    [string]$InputDir,

    [string]$OutputDir
)

if (-not $OutputDir) {
    $OutputDir = $InputDir
}

try {
    uv run convert_safetensors_batch.py $InputDir $OutputDir
} catch {
    Write-Error "An error occurred: $_"
    exit 1
}
