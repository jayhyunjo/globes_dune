/* GLoBES -- General LOng Baseline Experiment Simulator
 * Mass ordering sensitivity calculation for DUNE
 * Figure 6(b): 100% FHC
 * Outputs both True NO and True IO curves
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#include <globes/globes.h>
#include "myio.h"

int main(int argc, char *argv[])
{
  glbInit(argv[0]);
  char *MYFILE=argv[1];

  glbInitExperiment("DUNE_GLoBES_fig6_100fhc.glb",&glb_experiment_list[0],&glb_num_of_exps);
  InitOutput(MYFILE,"#Format: deltacp   delta_chi2_trueNO  delta_chi2_trueIO \n");

  double theta12 = 0.5903;
  double theta13 = 0.15;
  double theta23 = 0.86734;
  double deltacp = 0;
  double sdm = 7.39e-5;
  double ldm = 2.451e-3;

  glb_params true_values = glbAllocParams();
  glb_params fit_values = glbAllocParams();
  glb_params input_errors = glbAllocParams();
  glb_params central_values = glbAllocParams();

  glbDefineParams(true_values,theta12,theta13,theta23,deltacp,sdm,ldm);
  glbSetDensityParams(true_values,1.0,GLB_ALL);
  glbDefineParams(input_errors,theta12*0.023,theta13*0.015,theta23*0.041,0,sdm*0.028,ldm*0.013);
  glbSetDensityParams(input_errors,0.02,GLB_ALL);
  glbSetInputErrors(input_errors);

  double y;
  for(y=-180;y<180.0+0.01;y=y+180.0/50)
  {
    /* === TRUE NORMAL ORDERING === */
    glbDefineParams(true_values,theta12,theta13,theta23,y*M_PI/180.0,sdm,ldm);
    glbSetDensityParams(true_values,1.0,GLB_ALL);
    glbSetOscillationParameters(true_values);
    glbSetRates();

    /* Fit IO hypothesis to NO data */
    glbDefineParams(central_values,theta12,theta13,theta23,y*M_PI/180.0,sdm,-ldm);
    glbSetDensityParams(central_values,1.0,GLB_ALL);
    glbSetCentralValues(central_values);
    double chi2_IO_trueNO = glbChiAll(central_values,fit_values,GLB_ALL);

    /* Fit NO hypothesis to NO data */
    glbDefineParams(central_values,theta12,theta13,theta23,y*M_PI/180.0,sdm,ldm);
    glbSetDensityParams(central_values,1.0,GLB_ALL);
    glbSetCentralValues(central_values);
    double chi2_NO_trueNO = glbChiAll(central_values,fit_values,GLB_ALL);

    double res_trueNO = chi2_IO_trueNO - chi2_NO_trueNO;

    /* === TRUE INVERTED ORDERING === */
    glbDefineParams(true_values,theta12,theta13,theta23,y*M_PI/180.0,sdm,-ldm);
    glbSetDensityParams(true_values,1.0,GLB_ALL);
    glbSetOscillationParameters(true_values);
    glbSetRates();

    /* Fit IO hypothesis to IO data */
    glbDefineParams(central_values,theta12,theta13,theta23,y*M_PI/180.0,sdm,-ldm);
    glbSetDensityParams(central_values,1.0,GLB_ALL);
    glbSetCentralValues(central_values);
    double chi2_IO_trueIO = glbChiAll(central_values,fit_values,GLB_ALL);

    /* Fit NO hypothesis to IO data */
    glbDefineParams(central_values,theta12,theta13,theta23,y*M_PI/180.0,sdm,ldm);
    glbSetDensityParams(central_values,1.0,GLB_ALL);
    glbSetCentralValues(central_values);
    double chi2_NO_trueIO = glbChiAll(central_values,fit_values,GLB_ALL);

    double res_trueIO = chi2_NO_trueIO - chi2_IO_trueIO;

    AddToOutput(y, res_trueNO, res_trueIO);
  }

  glbFreeParams(true_values);
  glbFreeParams(central_values);
  glbFreeParams(fit_values);
  glbFreeParams(input_errors);
  exit(0);
}
