"""
CP Violation Sensitivity: 4 scenarios overlaid (3.5+3.5 yr = 336 kt*MW*yr).
Compares: DUNE TDR (ori), Q1, Q3, L1.
Exposure: 40 kt, 3.5+3.5 yr, 1.1e21 POT/yr, baseline 1284.9 km.
Reference: arXiv:2503.04432 Fig. 2 (left) and TDR arXiv:2002.03005 Fig. 5.17.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

files = {
    "DUNE TDR": "dune_dcp_ori_336.dat",
    "Q1":       "dune_dcp_Q1_336.dat",
    "Q3":       "dune_dcp_Q3_336.dat",
    "L1":       "dune_dcp_L1_336.dat",
}

colors     = {"DUNE TDR": "black",      "Q1": "royalblue", "Q3": "forestgreen", "L1": "crimson"}
linestyles = {"DUNE TDR": "-",          "Q1": "--",         "Q3": "-.",          "L1": ":"}
linewidths = {"DUNE TDR": 2.0,          "Q1": 2.0,          "Q3": 2.0,           "L1": 2.0}

def load(fname):
    d = np.loadtxt(fname, comments="#")
    return d[:, 0], d[:, 1]

fig, ax = plt.subplots(figsize=(7, 5.5))
fig.subplots_adjust(left=0.11, right=0.97, top=0.93, bottom=0.12)

for label, fname in files.items():
    x, y = load(fname)
    ax.plot(x, y, color=colors[label], ls=linestyles[label],
            lw=linewidths[label], label=label, zorder=3)

# significance lines
for sig, ytxt in [(3.0, 0.12), (5.0, 0.12)]:
    ax.axhline(sig, color="dimgray", ls="--", lw=0.8, alpha=0.6, zorder=1)
    ax.text(178, sig + ytxt, f"{sig:.0f}$\\sigma$",
            ha="right", va="bottom", fontsize=8, color="dimgray")

ax.set_xlim(-180, 180)
ax.set_ylim(0, 9)
ax.set_xlabel(r"True $\delta_{\rm CP}$ (degrees)", fontsize=13)
ax.set_ylabel(r"$\sqrt{|\Delta\chi^2|}$", fontsize=13)
ax.set_title(
    r"CP Violation Sensitivity  —  336 kt$\cdot$MW$\cdot$yr  (3.5$\nu$ + 3.5$\bar{\nu}$ yr, 40 kt)",
    fontsize=11)
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(45))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.tick_params(which="both", direction="in", top=True, right=True)
ax.legend(loc="upper center", fontsize=11, framealpha=0.85,
          ncol=2, columnspacing=1.2, handlelength=2.2,
          bbox_to_anchor=(0.5, 0.99))

# parameter annotation — bottom center, away from legend
ax.text(0, 0.38,
        r"$\sin^2\theta_{12}=0.310,\ \sin^2\theta_{13}=0.0224,\ \sin^2\theta_{23}=0.581$" + "\n"
        r"$\Delta m^2_{21}=7.39\times10^{-5}\ {\rm eV}^2,\ |\Delta m^2_{31}|=2.451\times10^{-3}\ {\rm eV}^2\ ({\rm NH})$",
        fontsize=7.5, va="bottom", ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.85))

fig.savefig("cp_4scenarios_336.pdf", dpi=150)
fig.savefig("cp_4scenarios_336.png", dpi=150)
print("Saved: cp_4scenarios_336.pdf / .png")

print("\n--- Summary (3.5+3.5 yr, 336 kt*MW*yr) ---")
print(f"{'Scenario':<12} {'Peak sigma':>12} {'Peak dCP':>12} {'>3s frac':>10} {'>5s frac':>10}")
for label, fname in files.items():
    x, y = load(fname)
    pk = y.max()
    px = x[np.argmax(y)]
    f3 = 100 * np.mean(y > 3)
    f5 = 100 * np.mean(y > 5)
    print(f"{label:<12} {pk:>12.2f} {px:>+12.1f} {f3:>9.1f}% {f5:>9.1f}%")
