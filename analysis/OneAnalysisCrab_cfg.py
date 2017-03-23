
#/////////////////////////////////////////////
#                                            #
# CRAB configuration to run over ONE sample  #
#                                            #
#/////////////////////////////////////////////

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#Do read the below link, for CRAB parameters:
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.disableAutomaticOutputCollection = True
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 50
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

config.JobType.pyCfgParams = ["sampleCode=TTJetsName"]
config.General.requestName = 'TTJets_22March17'
config.General.workArea = 'crab_projects'
config.JobType.psetName = '../../MiniTree/Selection/test/muons_miniAOD_to_ntuple_13TeV_cfg.py'
config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM'
config.JobType.outputFiles = ["TTJets_22March17_Ntuple.root" ]
config.Data.outLFNDirBase = '/store/user/%s/test2/TTJets_20170322' % (getUsernameFromSiteDB())

