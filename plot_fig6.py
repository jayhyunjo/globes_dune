#!/usr/bin/env python3
"""
Reproduce Figure 6 from Rout et al. (arXiv:2503.04432)
Mass Ordering Sensitivity vs δ_CP with 68% and 95% uncertainty bands
Two panels: (a) 50/50 FHC-RHC split, (b) 100% FHC
Includes both True NO and True IO curves
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Rectangle

def load_data(filename):
    """Load 3-column data: deltacp, delta_chi2_trueNO, delta_chi2_trueIO"""
    data = np.loadtxt(filename, comments='#')
    return {
        'deltacp': data[:, 0],
        'trueNO': data[:, 1],
        'trueIO': data[:, 2]
    }

def compute_bands(delta_chi2):
    """Compute 68% and 95% bands using Gaussian approximation.
    sigma = 2*sqrt(delta_chi2) per the paper's prescription."""
    sigma = 2 * np.sqrt(np.maximum(delta_chi2, 0.1))
    return {
        'lower_68': np.maximum(delta_chi2 - sigma, 0),
        'upper_68': delta_chi2 + sigma,
        'lower_95': np.maximum(delta_chi2 - 2*sigma, 0),
        'upper_95': delta_chi2 + 2*sigma
    }

def plot_panel(ax, data, title):
    """Plot one panel matching the paper's style"""
    dcp_pi = data['deltacp'] / 180.0  # Convert degrees to units of pi

    chi2 = data['trueNO']
    bands = compute_bands(chi2)

    # 95% band (yellow)
    ax.fill_between(dcp_pi, bands['lower_95'], bands['upper_95'],
                     alpha=0.25, color='#D4AA00', zorder=1)
    # 68% band (green)
    ax.fill_between(dcp_pi, bands['lower_68'], bands['upper_68'],
                     alpha=0.35, color='#4CAF50', zorder=2)
    # Central curve (black)
    ax.plot(dcp_pi, chi2, 'k-', linewidth=1.8, zorder=5)

    # Significance lines
    for sigma_val in [3, 5]:
        threshold = sigma_val**2
        ax.axhline(threshold, color='red', ls='--', lw=1.0, alpha=0.7, zorder=4)
        ax.text(-0.97, threshold + 1.0, f'{sigma_val}σ',
                ha='left', va='bottom', fontsize=9, color='red')

    # Formatting
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 80)
    ax.set_xlabel(r'$\delta_{\rm CP}$', fontsize=13)
    ax.set_ylabel(r'$\Delta\chi^2 = \chi^2_{\rm IO} - \chi^2_{\rm NO}$', fontsize=12)
    ax.set_title(title, fontsize=11, fontweight='bold')

    # Ticks
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.tick_params(which='both', direction='in', top=True, right=True)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        plt.Line2D([0], [0], color='k', lw=1.8, label='GLoBES Estimation'),
        Patch(facecolor='#4CAF50', alpha=0.4, label='68%'),
        Patch(facecolor='#D4AA00', alpha=0.3, label='95%'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=7, 
              framealpha=0.9, edgecolor='gray')

def main():
    print("Loading data...")
    data_5050 = load_data('mo_fig6_5050.dat')
    data_100fhc = load_data('mo_fig6_100fhc.dat')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, top=0.90, bottom=0.13)

    plot_panel(ax1, data_5050,
               r'NO, $\sin^2\theta_{23}=0.58$, 21.6 kt MW year')
    plot_panel(ax2, data_100fhc,
               r'NO, $\sin^2\theta_{23}=0.58$, 21.6 kt MW year')

    # Panel labels
    ax1.text(0.02, 0.95, '(a) 50/50 FHC–RHC split', transform=ax1.transAxes,
             fontsize=9, va='top', fontweight='bold')
    ax2.text(0.02, 0.95, '(b) 100% FHC', transform=ax2.transAxes,
             fontsize=9, va='top', fontweight='bold')

    plt.savefig('figure6_reproduction.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figure6_reproduction.png', dpi=200, bbox_inches='tight')
    print("Figure saved to: figure6_reproduction.pdf and figure6_reproduction.png")

    # Summary stats
    print("\n" + "=" * 60)
    print("Summary Statistics")
    print("=" * 60)
    for name, data in [("50/50 FHC-RHC", data_5050), ("100% FHC", data_100fhc)]:
        for label, key in [("True NO", "trueNO"), ("True IO", "trueIO")]:
            chi2 = data[key]
            peak = np.max(chi2)
            peak_dcp = data['deltacp'][np.argmax(chi2)]
            at_m180 = chi2[np.argmin(np.abs(data['deltacp'] + 180))]
            print(f"\n{name} ({label}):")
            print(f"  Peak Δχ² = {peak:.1f} (√Δχ² = {np.sqrt(peak):.1f}σ) at δ_CP = {peak_dcp:.0f}°")
            print(f"  Δχ² at δ_CP = -180° : {at_m180:.1f}")

if __name__ == "__main__":
    main()
