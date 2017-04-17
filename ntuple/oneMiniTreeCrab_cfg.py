
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
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 10
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

config.JobType.maxMemoryMB = 4000
config.General.requestName = 'TTJets_8April17'
config.General.workArea = 'TTJets_8April17'
config.JobType.psetName = '../../MiniTree/Selection/test/muonNtuple_cfg.py'
config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
config.Data.outLFNDirBase = '/store/user/%s/TTJets_8April17' % (getUsernameFromSiteDB())

