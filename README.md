# globes_dune
DUNE sensitivity study using GLoBES (https://www.mpi-hd.mpg.de/personalhomes/globes/index.html).

Originally written by Xuyang Ning (xning@bnl.gov).

Requires GLoBES v3.2.18 to run.

dune.c	  for delta CP
dune_hie.c  for mass order
dune_stage.c for DUNE staged sensitivity
dune_res.c  for resolution (This result is not consistency with DUNE TDR)

To compile:

make dune
make dune_hie
make dune_stage
make dune_res

A script all.sh that can change the smear matrix and run everything. 
Tag “ori” is the original result in DUNE. Others are the number of different method.

0-2 are for Q1 to Q3; 
3 is for Q4 which we didn’t shown in the paper.
4 is for L1.

In process.sh you can choose whatever you want to run.

For delta CP, the output result would be dune_dcp_{tag}.dat and the result can be drawn in plot.cc

Some other information:
- The smear matrix is defined in folder smr/
- DUNE flux is in the folder flux/
- Channels and rules are defined in DUNE_GLoBES.glb
- Systematic uncertainties are defined in definitions.inc
