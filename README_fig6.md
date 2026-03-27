# Reproduction of Figure 6 from the Paper

## Overview

This directory contains code to reproduce Figure 6 from the paper "Physics Case for an Accelerated Beam Timeline in DUNE: Enabling an Early-2030s Determination of the Neutrino Mass Ordering" (arXiv:2503.xxxxx).

Figure 6 shows the mass ordering sensitivity (Δχ² = χ²_IO - χ²_NO) as a function of the true CP phase δ_CP, with 68% and 95% uncertainty bands.

## Files Created

### Configuration Files
- `definitions_fig6_5050.inc` - Exposure parameters for 50/50 FHC-RHC split (0.75+0.75 yr, 12 kt)
- `definitions_fig6_100fhc.inc` - Exposure parameters for 100% FHC (1.5 yr, 12 kt)
- `DUNE_GLoBES_fig6_5050.glb` - GLoBES configuration for 50/50 scenario
- `DUNE_GLoBES_fig6_100fhc.glb` - GLoBES configuration for 100% FHC scenario

### C Programs
- `dune_mo_5050.c` - Mass ordering calculation for 50/50 split
- `dune_mo_100fhc.c` - Mass ordering calculation for 100% FHC

### Python Scripts
- `run_scenarios.py` - Runs GLoBES simulations and computes uncertainty bands
- `plot_fig6.py` - Generates the reproduction of Figure 6

### Output Files
- `mo_fig6_5050.dat` - Raw Δχ² data for 50/50 scenario
- `mo_fig6_5050_bands.dat` - Data with 68% and 95% uncertainty bands
- `mo_fig6_100fhc.dat` - Raw Δχ² data for 100% FHC scenario
- `mo_fig6_100fhc_bands.dat` - Data with 68% and 95% uncertainty bands
- `figure6_reproduction.pdf` - Final figure (PDF)
- `figure6_reproduction.png` - Final figure (PNG)

## How to Run

### 1. Compile the C programs

```bash
make dune_mo_5050
make dune_mo_100fhc
```

### 2. Run simulations and generate plots

```bash
python3 run_scenarios.py
python3 plot_fig6.py
```

Or simply run both steps together:

```bash
python3 run_scenarios.py && python3 plot_fig6.py
```

## Parameters Used

Based on NuFit 4.0 and the paper specifications:

- **Oscillation parameters:**
  - sin²θ₁₂ = 0.310
  - sin²θ₁₃ = 0.0224
  - sin²θ₂₃ = 0.58 (higher octant)
  - Δm²₂₁ = 7.39×10⁻⁵ eV²
  - |Δm²₃₂| = 2.451×10⁻³ eV² (Normal Hierarchy)

- **Exposure:** 21.6 kt·MW·yr = 12 kt × 1.2 MW × 1.5 yr
  - Scenario (a): 0.75 yr FHC + 0.75 yr RHC
  - Scenario (b): 1.5 yr FHC only

- **Systematic uncertainties:**
  - νₑ signal: 2%
  - νμ signal: 5%
  - Various backgrounds: 5-20%

## Uncertainty Band Calculation

The 68% and 95% uncertainty bands are computed using the Gaussian approximation mentioned in the paper:

- For a given Δχ², the distribution is approximated as Gaussian with:
  - Mean = Δχ²
  - Standard deviation σ = 2√(Δχ²)

- Bands:
  - 68% band: [Δχ² - σ, Δχ² + σ]
  - 95% band: [Δχ² - 2σ, Δχ² + 2σ]

## Results Summary

### 50/50 FHC-RHC Split
- Peak Δχ² ≈ 39 (√Δχ² ≈ 6.3σ) at δ_CP ≈ -101°
- 100% of δ_CP range has > 3σ sensitivity
- 47.5% of δ_CP range has > 5σ sensitivity

### 100% FHC
- Peak Δχ² ≈ 61 (√Δχ² ≈ 7.8σ) at δ_CP ≈ -104°
- 100% of δ_CP range has > 3σ sensitivity
- 68.3% of δ_CP range has > 5σ sensitivity

## Notes

- The reproduction does not include T2K and NOvA excluded regions (as requested)
- The plot shows two panels side by side matching the paper's layout
- All calculations assume Normal Ordering (NO) as the true hypothesis
- The fit tests both NO and Inverted Ordering (IO) hypotheses

## References

Paper: "Physics Case for an Accelerated Beam Timeline in DUNE: Enabling an Early-2030s Determination of the Neutrino Mass Ordering"
