# CrabNtuple

 #### Set the CMSSSW release ####
 
 * cmsrel CMSSW_8_0_25
 * cd CMSSW_8_0_25/src/
 * cmsenv
 
 #### Download and compile MiniTree ####
 
 * git clone https://github.com/ravindkv/MiniTree.git
 * cd MiniTree
 * scram b -j20
 * cd ..
 
 #### Download and set CrabNtuple ####
 
 * https://github.com/ravindkv/CrabNtuple.git
 * cd CrabNtuple/test
 * source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
 * voms-proxy-init -voms cms

 #### Run CRAB over single samples ####
 
 * crab submit -c CrabOneSample_cfg.py 
 
 #### Run CRAB over multiple samples ####
 
 * python CrabAllSamples_cfg.py
 

