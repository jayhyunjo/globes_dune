#!/bin/sh


sed -i '21s/.*/include \".\/smr\/app_nue_sig.txt"/' smr/Smear_nominal.inc
sed -i '29s/.*/include \".\/smr\/app_nuebar_sig.txt"/' smr/Smear_nominal.inc
./process.sh ori

#sed -i '21s/.*/include \".\/smr\/nue_sig_0.txt"/' smr/Smear_nominal.inc
#sed -i '29s/.*/include \".\/smr\/nuebar_sig_0.txt"/' smr/Smear_nominal.inc
#./process.sh 0
#
#sed -i '21s/.*/include \".\/smr\/nue_sig_1.txt"/' smr/Smear_nominal.inc
#sed -i '29s/.*/include \".\/smr\/nuebar_sig_1.txt"/' smr/Smear_nominal.inc
#./process.sh 1
#
#sed -i '21s/.*/include \".\/smr\/nue_sig_2.txt"/' smr/Smear_nominal.inc
#sed -i '29s/.*/include \".\/smr\/nuebar_sig_2.txt"/' smr/Smear_nominal.inc
#./process.sh 2
#
#sed -i '21s/.*/include \".\/smr\/nue_sig_3.txt"/' smr/Smear_nominal.inc
#sed -i '29s/.*/include \".\/smr\/nuebar_sig_3.txt"/' smr/Smear_nominal.inc
#./process.sh 3
#
#sed -i '21s/.*/include \".\/smr\/nue_sig_4.txt"/' smr/Smear_nominal.inc
#sed -i '29s/.*/include \".\/smr\/nuebar_sig_4.txt"/' smr/Smear_nominal.inc
#./process.sh 4
#
#sed -i '21s/.*/include \".\/smr\/mcb_nue_sig_0.txt"/' smr/Smear_nominal.inc
#sed -i '29s/.*/include \".\/smr\/app_nuebar_sig.txt"/' smr/Smear_nominal.inc
#./process.sh 5
