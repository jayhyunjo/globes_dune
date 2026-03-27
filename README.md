# DUNE GLoBES Sensitivity Studies

DUNE sensitivity study using GLoBES (https://www.mpi-hd.mpg.de/personalhomes/globes/index.html).
This repository contains tools to evaluate CP Violation and Mass Ordering sensitivity for various DUNE detector performance scenarios (TDR, Q1, Q, Q3, L1) as described in [arXiv:2503.04432](https://arxiv.org/abs/2503.04432).

## Core Capabilities

### 1. CP Violation Sensitivity (5 Scenarios)
Evaluates DUNE's sensitivity to $\delta_{CP}$ assuming a 336 kt$\cdot$MW$\cdot$yr exposure (3.5 yr neutrino + 3.5 yr antineutrino).

- **Data Generation**: `dune.c` computes the sensitivity. Compile with `gcc dune.c myio.c -o dune -lglobes -lm`.
- **Plotting**: `plot_cp_5scenarios.py` overlays the 5 performance scenarios.
- **Run Command**: `python3 plot_cp_5scenarios.py` (uses existing `dune_dcp_*_336.dat` files).

### 2. Mass Ordering Sensitivity (Figure 6 Reproduction)
Reproduces Figure 6 from [arXiv:2503.04432], showing MO sensitivity vs $\delta_{CP}$ for 50/50 FHC-RHC split and 100% FHC scenarios.

- **Data Generation**: `dune_mo_5050.c` and `dune_mo_100fhc.c`.
- **Plotting**: `plot_fig6.py` replicates the paper's aesthetics (True NO curve, 68/95% bands).
- **Run Command**: `python3 plot_fig6.py` (uses existing `mo_fig6_*.dat` files).

### 3. Mass Ordering (5 Scenarios)
- **Plotting**: `plot_mo_5scenarios.py` overlays MO sensitivity for the 5 scenarios.
- **Run Command**: `python3 plot_mo_5scenarios.py`.

## Directory Structure
- **`eff/`**: Event selection efficiencies and background rejection rates.
- **`flux/`**: DUNE neutrino and antineutrino beam flux profiles.
- **`smr/`**: Energy resolution "smearing" matrices for different scenarios (TDR, Q, L1).
- **`xsec/`**: Neutrino interaction cross-sections.
- **`definitions.inc` / `syst_list.inc`**: Definitions of systematic uncertainties and GLoBES χ² rules.

## Systematic Uncertainties
The simulation uses simple normalization errors (e.g., 2% on signal, 5-20% on backgrounds) managed via `glbChiMultiExp` and `glbChiAll`.
- **`definitions.inc`**: Physical magnitudes of uncertainties.
- **`syst_list.inc`**: Mapping of uncertainties to GLoBES systematic pulls.

