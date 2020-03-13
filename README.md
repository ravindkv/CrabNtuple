# MultiCrab

 ### First setup the MiniTree package
 * https://github.com/ravindkv/MiniTree/blob/Ether2016Tree/README.md

 #### Download and set MultiCrab ####
 * git clone -b Ether2016Crab git@github.com:ravindkv/MultiCrab.git
 * cd MultiCrab/crab
 * source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
 * voms-proxy-init -voms cms

 #### Run CRAB over single sample ####
 * crab submit oneMiniTreeCrab_cfg.py

 #### Run CRAB over multiple samples ####
 * python multiMiniTreeCrab_cfg.py

#### Push the changes to github ####
 * git branch
 * git status
 * git add -A
 * git commit -m "new changes"
 * git push origin Ether2016Crab

 #### Take a look at CRAB tutorial ####
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task
