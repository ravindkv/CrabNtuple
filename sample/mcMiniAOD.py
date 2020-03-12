import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Excited Lepton & Bkg at 13 TeV
RUN = "RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
M = "MINIAODSIM"
'''
mcSampDict_ = {"DYJetsToLL_M50":"/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext2-v1/"+M}
mcSampDict_["DYJetsToLL_Pt50To100"]="/DYJetsToLL_Pt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v3/"+M
mcSampDict_["DYJetsToLL_Pt100To250"]="/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v2/"+M
mcSampDict_["DYJetsToLL_Pt250To400"]="/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["DYJetsToLL_Pt400To650"]="/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["DYJetsToLL_Pt650ToInf"]="/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["TT"]="/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WJetsToLNu"]="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WW"]="/WW_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WZ"]="/WZ_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ZZ"]="/ZZ_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ST_tW_top"]="/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/"+RUN+"-v1/"+M
mcSampDict_["ST_tW_antitop"]="/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/"+RUN+"-v1/"+M
mcSampDict_["ST_t_top"]="/ST_t-channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV-powhegV2-madspin/"+RUN+"-v1/"+M
mcSampDict_["ST_t_antitop"]="/ST_t-channel_antitop_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV-powhegV2-madspin/"+RUN+"-v1/"+M
mcSampDict_["ST_s"]="/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/"+RUN+"-v1/"+M
'''
# Sort dictionaly w.r.t the keys
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))

