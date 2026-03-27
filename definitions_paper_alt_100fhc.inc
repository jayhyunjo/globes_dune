// Systematic uncertainties based on paper's ALTERNATIVE scheme (lines 446-460)
// "Alternative treatment inspired by NuMI flux prediction framework"
// For Figure 6(b): 100% FHC
//
// Paper describes:
// - 5.5% fully correlated across all channels
// - 4% for FHC running mode
// - (no RHC component for 100% FHC)
// - Scale factors 1.6 for FHC wrong-sign
//
// GLoBES approximation: Use quadrature sum
// All channels: sqrt(5.5^2 + 4^2) = 6.8%

NUTIME = 1.5
NUBARTIME = 0
LAMASS = 12

// All systematics same for 100% FHC mode
ERR_NUE_SIG = 0.068
ERR_NUE_SIGBAR = 0.068
ERR_NUMU_SIG = 0.068
ERR_NUMU_SIGBAR = 0.068

ERR_NUMU_BG = 0.068
ERR_NUE_BG = 0.068
ERR_NUTAU_BG = 0.2
ERR_NUE_BGBAR = 0.068
ERR_NC_BGDIS = 0.1
