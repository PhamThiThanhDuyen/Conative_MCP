[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Push-Location $repoRoot

try {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        throw 'Git is required.'
    }
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        throw 'Python 3.10 or newer is required.'
    }

    $pythonVersion = python -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
    $parts = $pythonVersion.Split('.')
    if ([int]$parts[0] -lt 3 -or ([int]$parts[0] -eq 3 -and [int]$parts[1] -lt 10)) {
        throw "Python 3.10 or newer is required; found $pythonVersion"
    }

    Write-Host "Python: $pythonVersion"
    python 05-scripts/validate_skill_size.py
    if ($LASTEXITCODE -ne 0) {
        throw "Skill size validation failed with exit code $LASTEXITCODE"
    }

    python 02-skills/test-design/testcase-matrix-design/scripts/validate_testcase_design.py 06-demo/search-ui-function/02-testcase-matrix.md
    if ($LASTEXITCODE -ne 0) {
        throw "Search demo validation failed with exit code $LASTEXITCODE"
    }

    $submoduleStatus = git submodule status -- 00-sources/product-docs
    if ($LASTEXITCODE -ne 0 -or -not $submoduleStatus) {
        throw 'Product Docs submodule is unavailable. Run git submodule update --init --recursive.'
    }
    if ($submoduleStatus.StartsWith('-')) {
        throw 'Product Docs submodule is not initialized. Run git submodule update --init --recursive.'
    }

    Write-Host "Submodule: $submoduleStatus"
    Write-Host 'Kit verification completed successfully.'
}
finally {
    Pop-Location
}
