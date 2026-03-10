"""
Validation script: compare the DUNE-default (ori) GLoBES result against
the DUNE TDR (arXiv:2002.03005, Fig. 5.17) at the standard exposure.

Exposure: 336 kt·MW·yr  =  40 kt × (3.5 ν + 3.5 ν̄) yr × 1.2 MW
  → definitions.inc: NUTIME = NUBARTIME = 3.5, LAMASS = 40
  → flux/Beam.inc:   @power = 11.0  [×10^20 POT/yr, ≡ 1.2 MW @ 120 GeV]

Oscillation parameters (dune.c / dune_hie.c):
  sin²θ₁₂ = 0.310  (θ₁₂ = 0.59 rad)
  sin²θ₁₃ = 0.0224 (θ₁₃ = 0.15 rad)
  sin²θ₂₃ = 0.581  (θ₂₃ = 0.866 rad)
  Δm²₂₁   = 7.39 × 10⁻⁵ eV²
  |Δm²₃₁| = 2.451 × 10⁻³ eV²  (Normal Hierarchy assumed true)

Smearing: ori = app_nue_sig.txt / app_nuebar_sig.txt  (DUNE TDR matrices)

Input files:
  dune_dcp_ori_336.dat  — CP violation sensitivity  (dune.c output)
  dune_hie_ori_336.dat  — Mass ordering sensitivity (dune_hie.c output)

Outputs: verify_tdr.pdf, verify_tdr.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def load_dat(fname):
    """Load two-column GLoBES output: (delta_CP_deg, sqrt|Delta_chi2|)."""
    data = np.loadtxt(fname, comments="#")
    return data[:, 0], data[:, 1]


fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.subplots_adjust(left=0.07, right=0.97, top=0.88, bottom=0.13, wspace=0.27)

sig_levels = [3.0, 5.0]

# ------------------------------------------------------------------ #
# Left panel: CP Violation Sensitivity
# ------------------------------------------------------------------ #
ax = axes[0]

x336, y336 = load_dat("dune_dcp_ori_336.dat")
ax.plot(x336, y336, color="royalblue", lw=2.0, ls="-",
        label=r"DUNE default  (ori)  336 kt$\cdot$MW$\cdot$yr")

for sig in sig_levels:
    ax.axhline(sig, color="dimgray", ls=":", lw=0.9, alpha=0.7)
    ax.text(175, sig + 0.12, f"{sig:.0f}$\\sigma$",
            ha="right", va="bottom", fontsize=8.5, color="dimgray")

ax.set_xlim(-180, 180)
ax.set_ylim(0, 10)
ax.set_xlabel(r"True $\delta_{\rm CP}$ (degrees)", fontsize=13)
ax.set_ylabel(r"$\sqrt{|\Delta\chi^2|}$", fontsize=13)
ax.set_title("CP Violation Sensitivity  (DUNE default, NH true)", fontsize=12)
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(45))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.tick_params(which="both", direction="in", top=True, right=True)
ax.legend(loc="upper center", fontsize=10, framealpha=0.85)

# Print summary statistics
frac3 = np.sum(y336 > 3.0) / len(y336) * 100
frac5 = np.sum(y336 > 5.0) / len(y336) * 100
print(f"CP 336 kt*MW*yr: peak={y336.max():.2f} sigma  >3sigma: {frac3:.0f}%  >5sigma: {frac5:.0f}%")

# ------------------------------------------------------------------ #
# Right panel: Mass Ordering Sensitivity
# ------------------------------------------------------------------ #
ax = axes[1]

xh336, yh336 = load_dat("dune_hie_ori_336.dat")
ax.plot(xh336, yh336, color="royalblue", lw=2.0, ls="-",
        label=r"DUNE default  (ori)  336 kt$\cdot$MW$\cdot$yr")

for sig in sig_levels:
    ax.axhline(sig, color="dimgray", ls=":", lw=0.9, alpha=0.7)
    ax.text(175, sig + 0.3, f"{sig:.0f}$\\sigma$",
            ha="right", va="bottom", fontsize=8.5, color="dimgray")

ax.set_xlim(-180, 180)
ax.set_ylim(0, 30)
ax.set_xlabel(r"True $\delta_{\rm CP}$ (degrees)", fontsize=13)
ax.set_ylabel(r"$\sqrt{|\Delta\chi^2|}$", fontsize=13)
ax.set_title("Mass Ordering Sensitivity  (DUNE default, NH true)", fontsize=12)
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(45))
ax.yaxis.set_major_locator(ticker.MultipleLocator(4))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.tick_params(which="both", direction="in", top=True, right=True)
ax.legend(loc="upper center", fontsize=10, framealpha=0.85)

print(f"MO 336 kt*MW*yr: min={yh336.min():.2f} sigma  max={yh336.max():.2f} sigma")

# Shared parameter annotation at top
param_text = (
    r"$\sin^2\theta_{12}=0.310,\ \sin^2\theta_{13}=0.0224,\ "
    r"\sin^2\theta_{23}=0.581$   "
    r"$\Delta m^2_{21}=7.39\times10^{-5}\ {\rm eV}^2,\ "
    r"|\Delta m^2_{31}|=2.451\times10^{-3}\ {\rm eV}^2\ ({\rm NH})$"
)
fig.text(0.5, 0.97, param_text, ha="center", va="top", fontsize=8,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8))

fig.savefig("verify_tdr.pdf", dpi=150)
fig.savefig("verify_tdr.png", dpi=150)
print("\nSaved: verify_tdr.pdf  verify_tdr.png")
