[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$Destination,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$skillRoot = Join-Path $repoRoot '02-skills'

if (-not $Destination) {
    $codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
    $Destination = Join-Path $codexHome 'skills'
}

$destinationRoot = [IO.Path]::GetFullPath($Destination)
New-Item -ItemType Directory -Force -Path $destinationRoot | Out-Null

$skills = Get-ChildItem -LiteralPath $skillRoot -Recurse -Filter 'SKILL.md' -File |
    ForEach-Object { $_.Directory } |
    Sort-Object FullName -Unique

if (-not $skills) {
    throw "No SKILL.md files found under $skillRoot"
}

$installed = 0
$skipped = 0

foreach ($skill in $skills) {
    $name = $skill.Name
    $target = Join-Path $destinationRoot $name

    if (Test-Path -LiteralPath $target) {
        if (-not $Force) {
            Write-Warning "Skipping existing Skill: $name ($target)"
            $skipped++
            continue
        }

        $resolvedTarget = (Resolve-Path -LiteralPath $target).Path
        if (-not $resolvedTarget.StartsWith($destinationRoot, [StringComparison]::OrdinalIgnoreCase)) {
            throw "Refusing to replace a path outside the destination root: $resolvedTarget"
        }

        if ($PSCmdlet.ShouldProcess($resolvedTarget, 'Replace installed Skill')) {
            Remove-Item -LiteralPath $resolvedTarget -Recurse -Force
        }
    }

    if ($PSCmdlet.ShouldProcess($target, "Install Skill $name")) {
        Copy-Item -LiteralPath $skill.FullName -Destination $target -Recurse -Force
        Write-Host "Installed: $name"
        $installed++
    }
}

Write-Host "Skill installation complete: $installed installed, $skipped skipped."
Write-Host "Destination: $destinationRoot"
