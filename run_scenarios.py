#!/usr/bin/env python3
"""
Run GLoBES simulations for Figure 6 scenarios
Generates central values and uncertainty bands using Gaussian approximation
"""

import subprocess
import numpy as np
import sys

def run_globes(executable, output_file):
    """Run GLoBES executable and save to output file"""
    print(f"Running {executable} -> {output_file}")
    try:
        result = subprocess.run([f"./{executable}", output_file],
                                check=True, capture_output=True, text=True)
        print(f"  Success: {output_file} created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error running {executable}:")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        return False

def compute_uncertainty_bands(data_file, output_base):
    """
    Compute 68% and 95% uncertainty bands using Gaussian approximation
    According to paper: Δχ² distribution approximated as Gaussian with
    mean = Δχ² and sigma = 2*sqrt(Δχ²)
    """
    print(f"\nComputing uncertainty bands for {data_file}")

    # Load data
    data = np.loadtxt(data_file, comments='#')
    deltacp = data[:, 0]
    delta_chi2 = data[:, 1]

    # Gaussian approximation: mean = delta_chi2, sigma = 2*sqrt(delta_chi2)
    # For small delta_chi2, set a minimum sigma to avoid issues
    sigma = 2 * np.sqrt(np.maximum(delta_chi2, 0.1))

    # Calculate bands
    # 68% = 1 sigma, 95% = 2 sigma (approximately 1.96 sigma)
    lower_68 = np.maximum(delta_chi2 - sigma, 0)
    upper_68 = delta_chi2 + sigma
    lower_95 = np.maximum(delta_chi2 - 2*sigma, 0)
    upper_95 = delta_chi2 + 2*sigma

    # Save bands
    bands_file = output_base + "_bands.dat"
    header = "# deltacp  delta_chi2  lower_68  upper_68  lower_95  upper_95"
    output_data = np.column_stack([deltacp, delta_chi2, lower_68, upper_68, lower_95, upper_95])
    np.savetxt(bands_file, output_data, header=header, fmt='%.6f')
    print(f"  Saved bands to: {bands_file}")

    return bands_file

def main():
    """Main execution"""
    print("=" * 60)
    print("Reproducing Figure 6 from arXiv paper")
    print("Mass Ordering Sensitivity vs δ_CP")
    print("=" * 60)

    scenarios = [
        {
            'name': '50/50 FHC-RHC split',
            'executable': 'dune_mo_5050',
            'output': 'mo_fig6_5050.dat',
            'bands_base': 'mo_fig6_5050'
        },
        {
            'name': '100% FHC',
            'executable': 'dune_mo_100fhc',
            'output': 'mo_fig6_100fhc.dat',
            'bands_base': 'mo_fig6_100fhc'
        }
    ]

    success = True

    for scenario in scenarios:
        print(f"\n--- Running scenario: {scenario['name']} ---")

        # Run GLoBES simulation
        if run_globes(scenario['executable'], scenario['output']):
            # Compute uncertainty bands
            compute_uncertainty_bands(scenario['output'], scenario['bands_base'])
        else:
            print(f"  Failed to run {scenario['executable']}")
            success = False

    if success:
        print("\n" + "=" * 60)
        print("All scenarios completed successfully!")
        print("Ready to plot with: python3 plot_fig6.py")
        print("=" * 60)
        return 0
    else:
        print("\nSome scenarios failed. Please check errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
