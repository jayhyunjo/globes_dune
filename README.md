# globes_dune
DUNE sensitivity study using GLoBES (https://www.mpi-hd.mpg.de/personalhomes/globes/index.html).

Originally written by Xuyang Ning (xning@bnl.gov).

Requires GLoBES v3.2.18 to run.

## Performance Studies (Reproduction)
This repository has been updated to evaluate CP Violation and Mass Ordering sensitivity for various DUNE detector performance scenarios (TDR, Q1, Q, Q3, L1) as described in [arXiv:2503.04432](https://arxiv.org/abs/2503.04432).

### 1. CP Violation Sensitivity (5 Scenarios)
Evaluates DUNE's sensitivity to $\delta_{CP}$ assuming a 336 kt$\cdot$MW$\cdot$yr exposure.
- **Run Command**: `python3 plot_cp_5scenarios.py` (uses existing `dune_dcp_*_336.dat` files).
- **Tool**: `dune.c` computes the sensitivity.

### 2. Mass Ordering Sensitivity (Figure 6)
Reproduces Figure 6 from [arXiv:2503.04432], showing MO sensitivity vs $\delta_{CP}$ for 50/50 and 100% FHC scenarios.
- **Run Command**: `python3 plot_fig6.py` (uses existing `mo_fig6_*.dat` files).
- **Tool**: `dune_mo_5050.c` and `dune_mo_100fhc.c` generate the data.

### 3. Mass Ordering (5 Scenarios)
- **Run Command**: `python3 plot_mo_5scenarios.py`.

## Main Entrypoints
- `dune.c`: Evaluates DUNE’s sensitivity to $\delta_{CP}$ (CP Violation).
- `dune_mo_5050.c` / `dune_mo_100fhc.c`: Evaluates Mass Ordering sensitivity for Figure 6.
- `run_scenarios.py`: A python pipeline that orchestrates GLoBES execution and plotting across calorimeter scenarios.

## Compilation and Running
To compile the GLoBES C simulations:
```bash
gcc dune.c myio.c -o dune -lglobes -lm
gcc dune_mo_5050.c myio.c -o dune_mo_5050 -lglobes -lm
gcc dune_mo_100fhc.c myio.c -o dune_mo_100fhc -lglobes -lm
```

To run a specific binary directly, pass the output tag:
```bash
./dune dune_dcp_test.dat
```

Batch/Automated Execution:
- `all.sh` combined with `process.sh <tag>` allows you to quickly modify smearing includes and process the binaries in batch.
- `run_scenarios.py` orchestrates the entire sequence (configuration, GLoBES execution, and python plotting) dynamically. 

Conventions (Refer to [Phys. Rev. D 111, 032007](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.032007)):
- Tag `ori` is the original result in DUNE. Other tags typically represent different reconstruction methods (Q1 to Q3, L1).
- `0-2` are for Q1 to Q3.
- `3` is for Q4 (not shown in the paper).
- `4` is for L1.

Outputs (e.g., `dune_dcp_{tag}.dat`) can be drawn using `plot.cc` or Python scripts.

## Directory Structure
- **`eff/`**: Contains pre-simulated event selection efficiencies and background rejection rates for various interaction modes.
- **`flux/`**: Houses the DUNE neutrino and antineutrino beam flux profiles (neutrino energy spectra inputs). This defines the unoscillated energy spectra of the beam ($\Phi(E)$).
- **`smr/`**: Includes parameter files and migration matrices defining energy "smearing", simulating how true neutrino energy degrades into reconstructed energy across different readouts.
- **`xsec/`**: Holds neutrino interaction cross-sections ($\sigma(E)$) for nominal Charged Current and Neutral Current interactions (e.g., from GENIE).

## Runtime Simulation Flow
1. **Scenario Configuration:** A user (or wrapping scripts) swaps out smearing matrix files within `smr/` and updates systematic uncertainties tracking inside `definitions.inc`.
2. **GLoBES Initialization:** The C executable loads `DUNE_GLoBES.glb`. This central file pulls in configurations from `definitions.inc`, `flux/`, `xsec/`, `eff/`, and `smr/`.
3. **Simulation Mapping:** GLoBES multiplies the raw beam spectra by interaction rates and applies the oscillation formulas to generate a "True" expected event spectrum. It then applies acceptance efficiencies and the energy resolution matrices to map the energies to the reconstructed bins.
4. **Minimization and Systematics:** GLoBES uses `chiMultiExp` to apply the fixed normalization errors from `definitions.inc`, allowing the internal fitter to dynamically float the signal and background predicted rates to find the minimum possible $\chi^2$ significance.
5. **Data Generation:** It serializes the $\Delta \chi^2$ evaluations into `.dat` files logging sensitivity.
6. **Post-Processing:** Scripts parse the generated `.dat` arrays and output comparative visual histograms.

## Handling of Systematic Uncertainties

This codebase collapses systematic uncertainties into simple normalization errors without propagating complex covariance matrices for specific flux beams or nuclear targets. The nominal simulation data in `flux/` and `xsec/` are used *only* for computing the nominal event rates before effects are applied, not the uncertainties themselves.

### Identifying and Tracking Systematics
Systematics are defined in two primary files:
1. **`definitions.inc`**: Defines the physical fractional magnitudes of the systematic uncertainties.
    - Signal uncertainties (e.g., `ERR_NUE_SIG = 0.02` for 2% on electron neutrino appearance).
    - Background uncertainties (e.g., `ERR_NUMU_BG = 0.05` for 5% on background muon neutrinos).
2. **`syst_list.inc`**: Maps these defined scalars into system objects that the GLoBES C-engine internal parser understands.

These scalars cannot be directly backtracked to localized flux or xsec parameters individually because they operate as global uniform pulls.

### The Role of `chiMultiExp`
The `chiMultiExp` function is the core $\chi^2$ evaluation routine. It performs the following:
1. **Baseline $\chi^2$:** Uses a Poisson log-likelihood ratio to compare simulated "expected" versus "observed" event rates per energy bin.
2. **Pull Parameters:** Introduces nuisance parameters (pulls) for every systemic uncertainty defined, shifting the predictions up or down by the assigned percentages.
3. **Penalty Term:** Penalizes the $\chi^2$ for pulling these parameters away from zero using a Gaussian penalty.
4. **Minimization:** Finds the worst-case scenario (minimum possible $\chi^2$ difference) by minimizing across all highly-correlated sub-channels simultaneously (e.g., integrating appearance and disappearance limits together).
