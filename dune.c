/* GLoBES -- General LOng Baseline Experiment Simulator
 * (C) 2002 - 2007,  The GLoBES Team
 *
 * GLoBES is mainly intended for academic purposes. Proper
 * credit must be given if you use GLoBES or parts of it. Please
 * read the section 'Credit' in the README file.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */
 
 /* 
 * Example: Correlation between s22th13 and deltacp
 * Compile with ``make example1''
 */ 

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#include <globes/globes.h>   /* GLoBES library */
#include "myio.h"             /* my input-output routines */


int main(int argc, char *argv[])
{ 
  /* Initialize libglobes */
  glbInit(argv[0]);

/* If filename given, write to file; for empty filename write to screen */
char *MYFILE=argv[1];

  /* Initialize experiment NFstandard.glb */
  glbInitExperiment("DUNE_GLoBES.glb",&glb_experiment_list[0],&glb_num_of_exps); 
 
  /* Intitialize output */
  InitOutput(MYFILE,"#Format:deltacp   chi^2 \n"); 
  
  /* Define standard oscillation parameters */
 // double theta12 = asin(sqrt(0.8))/2;
 // double theta13 = asin(sqrt(0.001))/2;
  double theta12 = 0.59;
  double theta13 = 0.15;
  double theta23 = 0.866;
  double deltacp = 0;
  double sdm = 7.39e-5;
  double ldm = 2.451e-3;
  
  /* Initialize parameter vector(s) */
  glb_params true_values = glbAllocParams();
  glb_params test_values = glbAllocParams();
  glb_params fit_values = glbAllocParams();
  glb_params input_errors = glbAllocParams();

  glbDefineParams(true_values,theta12,theta13,theta23,deltacp,sdm,ldm);
  glbSetDensityParams(true_values,1,GLB_ALL);
  glbDefineParams(test_values,theta12,theta13,theta23,deltacp,sdm,ldm);  
  glbSetDensityParams(test_values,1,GLB_ALL);
  glbDefineParams(input_errors,theta12*0.023,theta13*0.015,theta23*0.041,0,sdm*0.028,ldm*0.013);
  glbSetDensityParams(input_errors,0.02,GLB_ALL);
  glbSetInputErrors(input_errors);

  /* Iteration over all values to be computed */
  double thetheta13,x,y,res;    
    
  for(y=-180;y<180.0+0.01;y=y+180.0/50)
  {

  glbSetOscParams(true_values,y*M_PI/180.0,GLB_DELTA_CP);
  glbSetCentralValues(true_values);
  /* The simulated data are computed */
  glbSetOscillationParameters(true_values);
  glbSetRates();

      /* Set vector of test values */
      glbSetOscParams(test_values,0,GLB_DELTA_CP);
  
      /* Compute Chi^2 for all loaded experiments and all rules */
      //double res1=glbChiSys(test_values,GLB_ALL,GLB_ALL);
      double res1=glbChiDelta(test_values,fit_values,GLB_ALL);

	  glbSetOscParams(test_values,M_PI,GLB_DELTA_CP);

	  //double res2 = glbChiSys(test_values,GLB_ALL,GLB_ALL);
	  double res2 = glbChiDelta(test_values,fit_values,GLB_ALL);
	  if(res1<=res2) res = res1;
	  else res = res2;

      AddToOutput2(y,sqrt(fabs(res)));
      //AddToOutput2(y,res);
  }
   
  /* Destroy parameter vector(s) */
  glbFreeParams(true_values);
  glbFreeParams(test_values); 
  
  exit(0);
}
