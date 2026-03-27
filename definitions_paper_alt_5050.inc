// Systematic uncertainties based on paper's ALTERNATIVE scheme (lines 446-460)
// "Alternative treatment inspired by NuMI flux prediction framework"
// For Figure 6(a): 50/50 FHC-RHC split
//
// Paper describes:
// - 5.5% fully correlated across all channels
// - 4% for FHC running mode
// - 3% for RHC running mode
// - Scale factors 1.6 (FHC) and 1.8 (RHC) for wrong-sign
//
// GLoBES approximation: Use quadrature sum since cannot implement correlations
// FHC channels: sqrt(5.5^2 + 4^2) = 6.8%
// RHC channels: sqrt(5.5^2 + 3^2) = 6.3%

NUTIME = 0.75
NUBARTIME = 0.75
LAMASS = 12

// FHC mode systematics
ERR_NUE_SIG = 0.068          // FHC appearance signal
ERR_NUMU_SIG = 0.068         // FHC disappearance signal
ERR_NUMU_BG = 0.068          // FHC backgrounds
ERR_NUE_BG = 0.068

// RHC mode systematics
ERR_NUE_SIGBAR = 0.063       // RHC appearance signal
ERR_NUMU_SIGBAR = 0.063      // RHC disappearance signal
ERR_NUE_BGBAR = 0.063

// Other backgrounds
ERR_NUTAU_BG = 0.2
ERR_NC_BGDIS = 0.1
