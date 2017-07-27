import FWCore.ParameterSet.Config as cms

process = cms.Process("LOCALUSER")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/120000/0EA60289-18C4-E611-8A8F-008CFA110AB4.root')
)
process.BaseElectronsSet = cms.PSet(
    dedxSource = cms.InputTag("dedxHarmonic2"),
    id = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose'),
    maxEta = cms.double(2.5),
    maxRelCombPFIsoEA = cms.double(0.0994),
    minEt = cms.double(10),
    mvacut = cms.double(0.3),
    rhoIso = cms.InputTag("fixedGridRhoFastjetAll"),
    sources = cms.InputTag("slimmedElectrons"),
    triggerEvent = cms.InputTag("patTrigger"),
    triggerMatch = cms.string('TrigMatch')
)

process.BaseJetsSet = cms.PSet(
    CaloJetId = cms.PSet(
        quality = cms.string('LOOSE'),
        version = cms.string('PURE09')
    ),
    PFJetId = cms.PSet(
        quality = cms.string('LOOSE'),
        version = cms.string('FIRSTDATA')
    ),
    dedxSource = cms.InputTag("dedxHarmonic2"),
    jet_rho = cms.InputTag("fixedGridRhoAll"),
    maxEta = cms.double(2.5),
    minDeltaRtoLepton = cms.double(0.4),
    minPt = cms.double(17),
    puMVADiscriminant = cms.InputTag("puJetMva","fullDiscriminant"),
    puMVADiscriminantResCor = cms.InputTag("puJetMvaResCor","fullDiscriminant"),
    puMVAID = cms.InputTag("puJetMva","fullId"),
    puMVAIDResCor = cms.InputTag("puJetMvaResCor","fullId"),
    resolutionsFile = cms.string('Spring16_25nsV6_MC_PtResolution_AK4PF.txt'),
    scaleFactorsFile = cms.string('Spring16_25nsV6_MC_SF_AK4PF.txt'),
    sources = cms.InputTag("slimmedJets"),
    triggerEvent = cms.InputTag("hltTriggerSummaryAOD"),
    triggerMatch = cms.string('TrigMatch'),
    useRawJets = cms.bool(False)
)

process.BaseKFPSet = cms.PSet(
    chi2OfFit = cms.InputTag("kinFitTtSemiLepEvent","Chi2"),
    chi2OfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown","Chi2"),
    chi2OfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","Chi2"),
    chi2OfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","Chi2"),
    chi2OfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp","Chi2"),
    njetsUsed = cms.InputTag("kinFitTtSemiLepEvent","NumberOfConsideredJets"),
    njetsUsedDown = cms.InputTag("kinFitTtSemiLepEventJESDown","NumberOfConsideredJets"),
    njetsUsedJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","NumberOfConsideredJets"),
    njetsUsedJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","NumberOfConsideredJets"),
    njetsUsedUp = cms.InputTag("kinFitTtSemiLepEventJESUp","NumberOfConsideredJets"),
    probOfFit = cms.InputTag("kinFitTtSemiLepEvent","Prob"),
    probOfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown","Prob"),
    probOfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","Prob"),
    probOfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","Prob"),
    probOfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp","Prob"),
    runKineFitter = cms.bool(True),
    sources = cms.VInputTag("kinFitTtSemiLepEvent:Leptons", "kinFitTtSemiLepEvent:Neutrinos", "kinFitTtSemiLepEvent:PartonsHadB", "kinFitTtSemiLepEvent:PartonsHadP", "kinFitTtSemiLepEvent:PartonsHadQ", 
        "kinFitTtSemiLepEvent:PartonsLepB", "kinFitTtSemiLepEventJESUp:Leptons", "kinFitTtSemiLepEventJESUp:Neutrinos", "kinFitTtSemiLepEventJESUp:PartonsHadB", "kinFitTtSemiLepEventJESUp:PartonsHadP", 
        "kinFitTtSemiLepEventJESUp:PartonsHadQ", "kinFitTtSemiLepEventJESUp:PartonsLepB", "kinFitTtSemiLepEventJESDown:Leptons", "kinFitTtSemiLepEventJESDown:Neutrinos", "kinFitTtSemiLepEventJESDown:PartonsHadB", 
        "kinFitTtSemiLepEventJESDown:PartonsHadP", "kinFitTtSemiLepEventJESDown:PartonsHadQ", "kinFitTtSemiLepEventJESDown:PartonsLepB", "kinFitTtSemiLepEventJERUp:Leptons", "kinFitTtSemiLepEventJERUp:Neutrinos", 
        "kinFitTtSemiLepEventJERUp:PartonsHadB", "kinFitTtSemiLepEventJERUp:PartonsHadP", "kinFitTtSemiLepEventJERUp:PartonsHadQ", "kinFitTtSemiLepEventJERUp:PartonsLepB", "kinFitTtSemiLepEventJERDown:Leptons", 
        "kinFitTtSemiLepEventJERDown:Neutrinos", "kinFitTtSemiLepEventJERDown:PartonsHadB", "kinFitTtSemiLepEventJERDown:PartonsHadP", "kinFitTtSemiLepEventJERDown:PartonsHadQ", "kinFitTtSemiLepEventJERDown:PartonsLepB"),
    statusOfFit = cms.InputTag("kinFitTtSemiLepEvent","Status"),
    statusOfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown","Status"),
    statusOfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","Status"),
    statusOfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","Status"),
    statusOfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp","Status")
)

process.BaseMCTruthSet = cms.PSet(
    isData = cms.bool(False),
    jpMatchSources = cms.VInputTag("selectedPatJetsByRef", "selectedPatJetsAK5JPTByRef", "selectedPatJetsAK5PFByRef", "selectedPatJetsPFlowByRef"),
    producePDFweights = cms.bool(False),
    sampleChannel = cms.string('muon'),
    sampleCode = cms.string('W4JetsToLNu')
)

process.BaseMetsSet = cms.PSet(
    minMET = cms.double(10),
    sources = cms.InputTag("slimmedMETs")
)

process.BaseMuonsSet = cms.PSet(
    maxEta = cms.double(2.4),
    maxRelIso = cms.double(0.25),
    minMatchStations = cms.int32(1),
    minMuonHits = cms.int32(0),
    minPixelHits = cms.int32(0),
    minPt = cms.double(10),
    minTrackerLayers = cms.int32(5),
    sources = cms.InputTag("slimmedMuons"),
    triggerEvent = cms.InputTag("patTrigger"),
    triggerMatch = cms.string('TrigMatch')
)

process.BaseTrackSet = cms.PSet(
    dedxSource = cms.InputTag("dedxHarmonic2"),
    maxD0 = cms.double(400),
    maxEta = cms.double(2.5),
    maxPtSumInTrackIsoCone = cms.double(10),
    maxTrackChi2 = cms.double(10),
    minDeltaRtoLepton = cms.double(0.1),
    minPixelHits = cms.int32(1),
    minPrimaryVertexWeight = cms.double(0),
    minPt = cms.double(1),
    minQuality = cms.int32(2),
    minTrackValidHits = cms.int32(5),
    source = cms.InputTag("generalTracks"),
    trackIsoCone = cms.double(0.3)
)

process.BaseTriggerSet = cms.PSet(
    bits = cms.vstring('HLT_IsoMu27_v3', 
        'HLT_IsoMu27_v4', 
        'HLT_IsoMu27_v5', 
        'HLT_IsoMu27_v7', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v2', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v3', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v4', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v5', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v6', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v7', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v8', 
        'HLT_JetE30_NoBPTX_v2', 
        'HLT_JetE30_NoBPTX_v3', 
        'HLT_JetE30_NoBPTX_v4'),
    source = cms.InputTag("TriggerResults","","HLT")
)

process.BaseVertexSet = cms.PSet(
    beamSpotSource = cms.InputTag("offlineBeamSpot"),
    maxRho = cms.double(2.0),
    maxZ = cms.double(24),
    minNDOF = cms.int32(4),
    rho = cms.InputTag("fixedGridRhoAll"),
    useBeamSpot = cms.bool(True),
    vertexSource = cms.InputTag("offlineSlimmedPrimaryVertices")
)

process.METSignificanceParams = cms.PSet(
    dRMatch = cms.double(0.4),
    jetThreshold = cms.double(15),
    jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
    jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
    pjpar = cms.vdouble(-0.04, 0.6504)
)

process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('top dileptons analysis'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/UserCode/anayak/MiniTree/Selection/python/LocalRunSkeleton_cff.py,v $'),
    version = cms.untracked.string('$Revision: 1.3 $')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

process.ElectronsTrigMatch = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('path("HLT_Ele27_eta2p1_WPLoose_Gsf_v2") | path("HLT_Ele27_eta2p1_WPLoose_Gsf_v3") | path("HLT_Ele27_eta2p1_WPLoose_Gsf_v4") | path("HLT_Ele27_eta2p1_WPLoose_Gsf_v5") | path("HLT_Ele27_eta2p1_WPLoose_Gsf_v6") | path("HLT_Ele27_eta2p1_WPLoose_Gsf_v7") | path("HLT_Ele27_eta2p1_WPLoose_Gsf_v8")'),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("selectedPatElectrons")
)


process.JetsTrigMatch = cms.EDProducer("PATTriggerMatcherDRLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('path("HLT_JetE30_NoBPTX_v2") | path("HLT_JetE30_NoBPTX_v3") | path("HLT_JetE30_NoBPTX_v4")'),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("selectedPatJets")
)


process.MuonsTrigMatch = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('path("HLT_IsoMu27_v3") | path("HLT_IsoMu27_v4") | path("HLT_IsoMu27_v5") | path("HLT_IsoMu27_v7")'),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("selectedPatMuons")
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4JPTL1FastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4JPTL1FastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.caloMetT1 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"))
)


process.caloMetT1T2 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"), cms.InputTag("corrCaloMetType2"))
)


process.cleanPatElectrons = cms.EDProducer("PATElectronCleaner",
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatElectrons")
)


process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>20 && abs(eta)<2.5'),
    src = cms.InputTag("selectedPatJets")
)


process.cleanPatJetsJESDown = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>24 && abs(eta)<2.5'),
    src = cms.InputTag("scaledJetEnergyDown","slimmedJets")
)


process.cleanPatJetsJESUp = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>24 && abs(eta)<2.5'),
    src = cms.InputTag("scaledJetEnergyUp","slimmedJets")
)


process.cleanPatJetsResCor = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>24 && abs(eta)<2.5'),
    src = cms.InputTag("selectedPatJets")
)


process.cleanPatJetsResnDown = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>24 && abs(eta)<2.5'),
    src = cms.InputTag("scaledJetEnergyResnDown","slimmedJets")
)


process.cleanPatJetsResnUp = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>24 && abs(eta)<2.5'),
    src = cms.InputTag("scaledJetEnergyResnUp","slimmedJets")
)


process.cleanPatMuons = cms.EDProducer("PATMuonCleaner",
    checkOverlaps = cms.PSet(

    ),
    finalCut = cms.string(''),
    preselection = cms.string('pt>25 && abs(eta)<2.1 && isGlobalMuon && isPFMuon && isTrackerMuon && globalTrack.isNonnull  && globalTrack.normalizedChi2<10 && globalTrack.hitPattern.numberOfValidMuonHits>0 && numberOfMatchedStations>1 && innerTrack.hitPattern.numberOfValidPixelHits>0 && track.hitPattern.trackerLayersWithMeasurement > 5 && dB() < 0.2 && (pfIsolationR04.sumChargedHadronPt+ max(0.,pfIsolationR04.sumNeutralHadronEt+pfIsolationR04.sumPhotonEt-0.5*pfIsolationR04.sumPUPt))/pt < 0.30'),
    src = cms.InputTag("selectedPatMuons")
)


process.cleanPatPhotons = cms.EDProducer("PATPhotonCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('bySuperClusterSeed'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatPhotons")
)


process.cleanPatTaus = cms.EDProducer("PATTauCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string('pt > 18. & abs(eta) < 2.3'),
    preselection = cms.string('tauID("decayModeFinding") > 0.5 & tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5 & tauID("againstMuonTight3") > 0.5 & tauID("againstElectronVLooseMVA6") > 0.5'),
    src = cms.InputTag("selectedPatTaus")
)


process.corrCaloMetType1 = cms.EDProducer("CaloJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4CaloL2L3Corrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    src = cms.InputTag("ak4CaloJets"),
    srcMET = cms.InputTag("caloMetM"),
    type1JetPtThreshold = cms.double(20.0)
)


process.corrCaloMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrCaloMetType1","type2"), cms.InputTag("muCaloMetCorr")),
    type2CorrFormula = cms.string('A + B*TMath::Exp(-C*x)'),
    type2CorrParameter = cms.PSet(
        A = cms.double(2.0),
        B = cms.double(1.3),
        C = cms.double(0.1)
    )
)


process.corrPfMetType1 = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsCHS"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1","type2"), cms.InputTag("corrPfMetType1","offset"), cms.InputTag("pfCandMETcorr")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.elPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedAllPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoValueCharged03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.electronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons")
)


process.hpsPFTauChargedIsoPtSum = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByLoosePileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByMediumPileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(1.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(True),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByRawPileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByTightPileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(0.8),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauFootprintCorrection = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawFootprintCorrection = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauNeutralIsoPtSum = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauNeutralIsoPtSumWeight = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauPUcorrPtSum = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(True),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauPhotonPtSumOutsideSignalCone = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.isoDeposits = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag(""),
    trackType = cms.string('candidate')
)


process.kinFitTtSemiLepEvent = cms.EDProducer("TtSemiLepKinFitProducerMuon",
    bResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0686^2 + (1.03/sqrt(et))^2 + (1.68/et)^2))'),
        eta = cms.string('sqrt(0.00605^2 + (1.63/et)^2)'),
        phi = cms.string('sqrt(0.00787^2 + (1.74/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0737^2 + (1.01/sqrt(et))^2 + (1.74/et)^2))'),
            eta = cms.string('sqrt(0.00592^2 + (1.64/et)^2)'),
            phi = cms.string('sqrt(0.00766^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0657^2 + (1.07/sqrt(et))^2 + (5.16e-06/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00755^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.062^2 + (1.07/sqrt(et))^2 + (0.000134/et)^2))'),
            eta = cms.string('sqrt(0.00593^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.0605^2 + (1.07/sqrt(et))^2 + (1.84e-07/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.059^2 + (1.08/sqrt(et))^2 + (9.06e-09/et)^2))'),
            eta = cms.string('sqrt(0.00646^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00767^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0577^2 + (1.08/sqrt(et))^2 + (5.46e-06/et)^2))'),
            eta = cms.string('sqrt(0.00661^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00742^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.0525^2 + (1.09/sqrt(et))^2 + (4.05e-05/et)^2))'),
            eta = cms.string('sqrt(0.00724^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00771^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.0582^2 + (1.09/sqrt(et))^2 + (1.17e-05/et)^2))'),
            eta = cms.string('sqrt(0.00763^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00758^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0649^2 + (1.08/sqrt(et))^2 + (7.85e-06/et)^2))'),
            eta = cms.string('sqrt(0.00746^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00789^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0654^2 + (1.1/sqrt(et))^2 + (1.09e-07/et)^2))'),
            eta = cms.string('sqrt(0.00807^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00802^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0669^2 + (1.11/sqrt(et))^2 + (1.87e-06/et)^2))'),
            eta = cms.string('sqrt(0.00843^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.0078^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0643^2 + (1.15/sqrt(et))^2 + (2.76e-05/et)^2))'),
            eta = cms.string('sqrt(0.00886^2 + (1.74/et)^2)'),
            phi = cms.string('sqrt(0.00806^2 + (1.82/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0645^2 + (1.16/sqrt(et))^2 + (1.04e-06/et)^2))'),
            eta = cms.string('sqrt(0.0101^2 + (1.76/et)^2)'),
            phi = cms.string('sqrt(0.00784^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0637^2 + (1.19/sqrt(et))^2 + (1.08e-07/et)^2))'),
            eta = cms.string('sqrt(0.0127^2 + (1.78/et)^2)'),
            phi = cms.string('sqrt(0.00885^2 + (1.9/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0695^2 + (1.21/sqrt(et))^2 + (5.75e-06/et)^2))'),
            eta = cms.string('sqrt(0.0161^2 + (1.73/et)^2)'),
            phi = cms.string('sqrt(0.0108^2 + (1.93/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0748^2 + (1.2/sqrt(et))^2 + (5.15e-08/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.77/et)^2)'),
            phi = cms.string('sqrt(0.0112^2 + (2/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0624^2 + (1.23/sqrt(et))^2 + (2.28e-05/et)^2))'),
            eta = cms.string('sqrt(0.0123^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (2.02/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(0.0283^2 + (1.25/sqrt(et))^2 + (4.79e-07/et)^2))'),
            eta = cms.string('sqrt(0.0111^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.00857^2 + (2.01/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(0.0316^2 + (1.21/sqrt(et))^2 + (5e-05/et)^2))'),
            eta = cms.string('sqrt(0.0106^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00856^2 + (1.97/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.29e-07^2 + (1.2/sqrt(et))^2 + (1.71e-05/et)^2))'),
            eta = cms.string('sqrt(0.0115^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00761^2 + (1.95/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(5.18e-09^2 + (1.14/sqrt(et))^2 + (1.7/et)^2))'),
            eta = cms.string('sqrt(0.012^2 + (1.88/et)^2)'),
            phi = cms.string('sqrt(0.00721^2 + (1.92/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(2.17e-07^2 + (1.09/sqrt(et))^2 + (2.08/et)^2))'),
            eta = cms.string('sqrt(0.0131^2 + (1.91/et)^2)'),
            phi = cms.string('sqrt(0.00722^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(3.65e-07^2 + (1.09/sqrt(et))^2 + (1.63/et)^2))'),
            eta = cms.string('sqrt(0.0134^2 + (1.92/et)^2)'),
            phi = cms.string('sqrt(0.00703^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(2.02e-07^2 + (1.09/sqrt(et))^2 + (1.68/et)^2))'),
            eta = cms.string('sqrt(0.0132^2 + (1.89/et)^2)'),
            phi = cms.string('sqrt(0.00845^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(5.27e-07^2 + (1.12/sqrt(et))^2 + (1.78/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (2.28/et)^2)'),
            phi = cms.string('sqrt(0.00975^2 + (2/et)^2)')
        )),
    bTagAlgo = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    constraints = cms.vuint32(3, 4),
    jetEnergyResolutionEtaBinning = cms.vdouble(0.0, -1.0),
    jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
    jetParametrisation = cms.uint32(1),
    jets = cms.InputTag("cleanPatJetsResCor"),
    lepParametrisation = cms.uint32(1),
    lepResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.100'),
        et = cms.string('et * (0.00517 + 0.000143 * et)'),
        eta = cms.string('sqrt(0.000433^2 + (0.000161/sqrt(et))^2 + (0.00334/et)^2)'),
        phi = cms.string('sqrt(7.21e-05^2 + (7e-05/sqrt(et))^2 + (0.00296/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.100<=abs(eta) && abs(eta)<0.200'),
            et = cms.string('et * (0.00524 + 0.000143 * et)'),
            eta = cms.string('sqrt(0.000381^2 + (0.000473/sqrt(et))^2 + (0.00259/et)^2)'),
            phi = cms.string('sqrt(6.79e-05^2 + (0.000245/sqrt(et))^2 + (0.00274/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.200<=abs(eta) && abs(eta)<0.300'),
            et = cms.string('et * (0.00585 + 0.000138 * et)'),
            eta = cms.string('sqrt(0.000337^2 + (0.000381/sqrt(et))^2 + (0.0023/et)^2)'),
            phi = cms.string('sqrt(7.08e-05^2 + (6.75e-05/sqrt(et))^2 + (0.00307/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.300<=abs(eta) && abs(eta)<0.400'),
            et = cms.string('et * (0.0065 + 0.000133 * et)'),
            eta = cms.string('sqrt(0.000308^2 + (0.000166/sqrt(et))^2 + (0.00249/et)^2)'),
            phi = cms.string('sqrt(6.59e-05^2 + (0.000301/sqrt(et))^2 + (0.00281/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.400<=abs(eta) && abs(eta)<0.500'),
            et = cms.string('et * (0.0071 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000289^2 + (5.37e-09/sqrt(et))^2 + (0.00243/et)^2)'),
            phi = cms.string('sqrt(6.27e-05^2 + (0.000359/sqrt(et))^2 + (0.00278/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.500<=abs(eta) && abs(eta)<0.600'),
            et = cms.string('et * (0.00721 + 0.00013 * et)'),
            eta = cms.string('sqrt(0.000279^2 + (0.000272/sqrt(et))^2 + (0.0026/et)^2)'),
            phi = cms.string('sqrt(6.46e-05^2 + (0.00036/sqrt(et))^2 + (0.00285/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.600<=abs(eta) && abs(eta)<0.700'),
            et = cms.string('et * (0.00757 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000282^2 + (3.63e-10/sqrt(et))^2 + (0.00288/et)^2)'),
            phi = cms.string('sqrt(6.54e-05^2 + (0.000348/sqrt(et))^2 + (0.00301/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.700<=abs(eta) && abs(eta)<0.800'),
            et = cms.string('et * (0.0081 + 0.000127 * et)'),
            eta = cms.string('sqrt(0.000265^2 + (0.000609/sqrt(et))^2 + (0.00212/et)^2)'),
            phi = cms.string('sqrt(6.2e-05^2 + (0.000402/sqrt(et))^2 + (0.00304/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.800<=abs(eta) && abs(eta)<0.900'),
            et = cms.string('et * (0.00916 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000241^2 + (0.000678/sqrt(et))^2 + (0.00221/et)^2)'),
            phi = cms.string('sqrt(6.26e-05^2 + (0.000458/sqrt(et))^2 + (0.0031/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.900<=abs(eta) && abs(eta)<1.000'),
            et = cms.string('et * (0.0108 + 0.000151 * et)'),
            eta = cms.string('sqrt(0.000228^2 + (0.000612/sqrt(et))^2 + (0.00245/et)^2)'),
            phi = cms.string('sqrt(7.18e-05^2 + (0.000469/sqrt(et))^2 + (0.00331/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.000<=abs(eta) && abs(eta)<1.100'),
            et = cms.string('et * (0.0115 + 0.000153 * et)'),
            eta = cms.string('sqrt(0.000217^2 + (0.000583/sqrt(et))^2 + (0.00307/et)^2)'),
            phi = cms.string('sqrt(6.98e-05^2 + (0.000507/sqrt(et))^2 + (0.00338/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.100<=abs(eta) && abs(eta)<1.200'),
            et = cms.string('et * (0.013 + 0.000136 * et)'),
            eta = cms.string('sqrt(0.000195^2 + (0.000751/sqrt(et))^2 + (0.00282/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000584/sqrt(et))^2 + (0.00345/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.200<=abs(eta) && abs(eta)<1.300'),
            et = cms.string('et * (0.0144 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000183^2 + (0.000838/sqrt(et))^2 + (0.00227/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000667/sqrt(et))^2 + (0.00352/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.300<=abs(eta) && abs(eta)<1.400'),
            et = cms.string('et * (0.0149 + 0.000141 * et)'),
            eta = cms.string('sqrt(0.000196^2 + (0.000783/sqrt(et))^2 + (0.00274/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000711/sqrt(et))^2 + (0.00358/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.400<=abs(eta) && abs(eta)<1.500'),
            et = cms.string('et * (0.014 + 0.000155 * et)'),
            eta = cms.string('sqrt(0.0002^2 + (0.000832/sqrt(et))^2 + (0.00254/et)^2)'),
            phi = cms.string('sqrt(5.98e-05^2 + (0.000713/sqrt(et))^2 + (0.00362/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.500<=abs(eta) && abs(eta)<1.600'),
            et = cms.string('et * (0.0132 + 0.000169 * et)'),
            eta = cms.string('sqrt(0.000205^2 + (0.0007/sqrt(et))^2 + (0.00304/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000781/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.600<=abs(eta) && abs(eta)<1.700'),
            et = cms.string('et * (0.0129 + 0.0002 * et)'),
            eta = cms.string('sqrt(0.000214^2 + (0.000747/sqrt(et))^2 + (0.00319/et)^2)'),
            phi = cms.string('sqrt(6.92e-05^2 + (0.000865/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.700<=abs(eta) && abs(eta)<1.800'),
            et = cms.string('et * (0.0135 + 0.000264 * et)'),
            eta = cms.string('sqrt(0.000238^2 + (0.000582/sqrt(et))^2 + (0.00343/et)^2)'),
            phi = cms.string('sqrt(9.13e-05^2 + (0.000896/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.800<=abs(eta) && abs(eta)<1.900'),
            et = cms.string('et * (0.0144 + 0.00034 * et)'),
            eta = cms.string('sqrt(0.000263^2 + (0.000721/sqrt(et))^2 + (0.00322/et)^2)'),
            phi = cms.string('sqrt(0.000102^2 + (0.000994/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.900<=abs(eta) && abs(eta)<2.000'),
            et = cms.string('et * (0.0147 + 0.000441 * et)'),
            eta = cms.string('sqrt(0.000284^2 + (0.000779/sqrt(et))^2 + (0.0031/et)^2)'),
            phi = cms.string('sqrt(0.000123^2 + (0.00108/sqrt(et))^2 + (0.00315/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.000<=abs(eta) && abs(eta)<2.100'),
            et = cms.string('et * (0.0154 + 0.000604 * et)'),
            eta = cms.string('sqrt(0.000316^2 + (0.000566/sqrt(et))^2 + (0.00384/et)^2)'),
            phi = cms.string('sqrt(0.000169^2 + (0.000947/sqrt(et))^2 + (0.00422/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.100<=abs(eta) && abs(eta)<2.200'),
            et = cms.string('et * (0.0163 + 0.000764 * et)'),
            eta = cms.string('sqrt(0.000353^2 + (0.000749/sqrt(et))^2 + (0.0038/et)^2)'),
            phi = cms.string('sqrt(0.000176^2 + (0.00116/sqrt(et))^2 + (0.00423/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.200<=abs(eta) && abs(eta)<2.300'),
            et = cms.string('et * (0.0173 + 0.000951 * et)'),
            eta = cms.string('sqrt(0.000412^2 + (0.00102/sqrt(et))^2 + (0.00351/et)^2)'),
            phi = cms.string('sqrt(0.000207^2 + (0.00115/sqrt(et))^2 + (0.00469/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.300<=abs(eta) && abs(eta)<2.400'),
            et = cms.string('et * (0.0175 + 0.00126 * et)'),
            eta = cms.string('sqrt(0.000506^2 + (0.000791/sqrt(et))^2 + (0.0045/et)^2)'),
            phi = cms.string('sqrt(0.00027^2 + (0.00113/sqrt(et))^2 + (0.00528/et)^2)')
        )),
    leps = cms.InputTag("slimmedMuons"),
    mTop = cms.double(172.5),
    mW = cms.double(80.4),
    match = cms.InputTag("findTtSemiLepJetCombMVA"),
    maxBDiscLightJets = cms.double(3.0),
    maxDeltaS = cms.double(5e-05),
    maxF = cms.double(0.0001),
    maxNComb = cms.int32(1),
    maxNJets = cms.int32(-1),
    maxNrIter = cms.uint32(500),
    metParametrisation = cms.uint32(1),
    metResolutions = cms.VPSet(cms.PSet(
        et = cms.string('et * (sqrt(0.0337^2 + (0.888/sqrt(et))^2 + (19.6/et)^2))'),
        eta = cms.string('9999'),
        phi = cms.string('sqrt(1.28e-08^2 + (1.45/sqrt(et))^2 + (1.03/et)^2)')
    )),
    mets = cms.InputTag("slimmedMETs"),
    minBDiscBJets = cms.double(0.5426),
    udscResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0591^2 + (1/sqrt(et))^2 + (0.891/et)^2))'),
        eta = cms.string('sqrt(0.00915^2 + (1.51/et)^2)'),
        phi = cms.string('sqrt(0.01^2 + (1.6/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0619^2 + (0.975/sqrt(et))^2 + (1.54/et)^2))'),
            eta = cms.string('sqrt(0.00887^2 + (1.53/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0574^2 + (1/sqrt(et))^2 + (1.49e-05/et)^2))'),
            eta = cms.string('sqrt(0.00865^2 + (1.54/et)^2)'),
            phi = cms.string('sqrt(0.0101^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.0569^2 + (1.01/sqrt(et))^2 + (1.22e-07/et)^2))'),
            eta = cms.string('sqrt(0.00867^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.00988^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.057^2 + (1/sqrt(et))^2 + (2.17e-08/et)^2))'),
            eta = cms.string('sqrt(0.00907^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.0522^2 + (1.02/sqrt(et))^2 + (2.64e-05/et)^2))'),
            eta = cms.string('sqrt(0.00844^2 + (1.59/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0502^2 + (1.02/sqrt(et))^2 + (2.6e-06/et)^2))'),
            eta = cms.string('sqrt(0.00915^2 + (1.57/et)^2)'),
            phi = cms.string('sqrt(0.00979^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.053^2 + (1.03/sqrt(et))^2 + (4.87e-07/et)^2))'),
            eta = cms.string('sqrt(0.00856^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00925^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.051^2 + (1.03/sqrt(et))^2 + (7.53e-06/et)^2))'),
            eta = cms.string('sqrt(0.00897^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00973^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0549^2 + (1.04/sqrt(et))^2 + (5.62e-08/et)^2))'),
            eta = cms.string('sqrt(0.0095^2 + (1.6/et)^2)'),
            phi = cms.string('sqrt(0.00971^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0544^2 + (1.06/sqrt(et))^2 + (1.07e-05/et)^2))'),
            eta = cms.string('sqrt(0.00836^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00916^2 + (1.64/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0519^2 + (1.09/sqrt(et))^2 + (8.43e-06/et)^2))'),
            eta = cms.string('sqrt(0.00782^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00959^2 + (1.66/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0539^2 + (1.12/sqrt(et))^2 + (1.97e-07/et)^2))'),
            eta = cms.string('sqrt(0.0093^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00964^2 + (1.67/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0492^2 + (1.16/sqrt(et))^2 + (1.37e-08/et)^2))'),
            eta = cms.string('sqrt(0.00986^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00969^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0489^2 + (1.18/sqrt(et))^2 + (3.44e-07/et)^2))'),
            eta = cms.string('sqrt(0.0124^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.00992^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0414^2 + (1.25/sqrt(et))^2 + (1.98e-07/et)^2))'),
            eta = cms.string('sqrt(0.0181^2 + (1.63/et)^2)'),
            phi = cms.string('sqrt(0.0124^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0373^2 + (1.26/sqrt(et))^2 + (5.4e-07/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0135^2 + (1.8/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0125^2 + (1.24/sqrt(et))^2 + (1e-06/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0107^2 + (1.85/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(1.37e-07^2 + (1.08/sqrt(et))^2 + (3.06/et)^2))'),
            eta = cms.string('sqrt(0.00975^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00895^2 + (1.84/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(2.37e-07^2 + (1.04/sqrt(et))^2 + (3.01/et)^2))'),
            eta = cms.string('sqrt(0.00881^2 + (1.71/et)^2)'),
            phi = cms.string('sqrt(0.00902^2 + (1.81/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.3e-07^2 + (1/sqrt(et))^2 + (3.1/et)^2))'),
            eta = cms.string('sqrt(0.00938^2 + (1.75/et)^2)'),
            phi = cms.string('sqrt(0.00861^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(1.25e-07^2 + (0.965/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00894^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00877^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(5.78e-08^2 + (0.924/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00893^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00791^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(4.25e-08^2 + (0.923/sqrt(et))^2 + (2.85/et)^2))'),
            eta = cms.string('sqrt(0.0099^2 + (1.82/et)^2)'),
            phi = cms.string('sqrt(0.00775^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(0.00601^2 + (0.881/sqrt(et))^2 + (3.23/et)^2))'),
            eta = cms.string('sqrt(0.00944^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00807^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(4.94e-08^2 + (0.86/sqrt(et))^2 + (3.56/et)^2))'),
            eta = cms.string('sqrt(0.0103^2 + (2.15/et)^2)'),
            phi = cms.string('sqrt(0.0103^2 + (1.81/et)^2)')
        )),
    useBTagging = cms.bool(True),
    useOnlyMatch = cms.bool(False)
)


process.kinFitTtSemiLepEventJERDown = cms.EDProducer("TtSemiLepKinFitProducerMuon",
    bResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0686^2 + (1.03/sqrt(et))^2 + (1.68/et)^2))'),
        eta = cms.string('sqrt(0.00605^2 + (1.63/et)^2)'),
        phi = cms.string('sqrt(0.00787^2 + (1.74/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0737^2 + (1.01/sqrt(et))^2 + (1.74/et)^2))'),
            eta = cms.string('sqrt(0.00592^2 + (1.64/et)^2)'),
            phi = cms.string('sqrt(0.00766^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0657^2 + (1.07/sqrt(et))^2 + (5.16e-06/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00755^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.062^2 + (1.07/sqrt(et))^2 + (0.000134/et)^2))'),
            eta = cms.string('sqrt(0.00593^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.0605^2 + (1.07/sqrt(et))^2 + (1.84e-07/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.059^2 + (1.08/sqrt(et))^2 + (9.06e-09/et)^2))'),
            eta = cms.string('sqrt(0.00646^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00767^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0577^2 + (1.08/sqrt(et))^2 + (5.46e-06/et)^2))'),
            eta = cms.string('sqrt(0.00661^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00742^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.0525^2 + (1.09/sqrt(et))^2 + (4.05e-05/et)^2))'),
            eta = cms.string('sqrt(0.00724^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00771^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.0582^2 + (1.09/sqrt(et))^2 + (1.17e-05/et)^2))'),
            eta = cms.string('sqrt(0.00763^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00758^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0649^2 + (1.08/sqrt(et))^2 + (7.85e-06/et)^2))'),
            eta = cms.string('sqrt(0.00746^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00789^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0654^2 + (1.1/sqrt(et))^2 + (1.09e-07/et)^2))'),
            eta = cms.string('sqrt(0.00807^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00802^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0669^2 + (1.11/sqrt(et))^2 + (1.87e-06/et)^2))'),
            eta = cms.string('sqrt(0.00843^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.0078^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0643^2 + (1.15/sqrt(et))^2 + (2.76e-05/et)^2))'),
            eta = cms.string('sqrt(0.00886^2 + (1.74/et)^2)'),
            phi = cms.string('sqrt(0.00806^2 + (1.82/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0645^2 + (1.16/sqrt(et))^2 + (1.04e-06/et)^2))'),
            eta = cms.string('sqrt(0.0101^2 + (1.76/et)^2)'),
            phi = cms.string('sqrt(0.00784^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0637^2 + (1.19/sqrt(et))^2 + (1.08e-07/et)^2))'),
            eta = cms.string('sqrt(0.0127^2 + (1.78/et)^2)'),
            phi = cms.string('sqrt(0.00885^2 + (1.9/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0695^2 + (1.21/sqrt(et))^2 + (5.75e-06/et)^2))'),
            eta = cms.string('sqrt(0.0161^2 + (1.73/et)^2)'),
            phi = cms.string('sqrt(0.0108^2 + (1.93/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0748^2 + (1.2/sqrt(et))^2 + (5.15e-08/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.77/et)^2)'),
            phi = cms.string('sqrt(0.0112^2 + (2/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0624^2 + (1.23/sqrt(et))^2 + (2.28e-05/et)^2))'),
            eta = cms.string('sqrt(0.0123^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (2.02/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(0.0283^2 + (1.25/sqrt(et))^2 + (4.79e-07/et)^2))'),
            eta = cms.string('sqrt(0.0111^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.00857^2 + (2.01/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(0.0316^2 + (1.21/sqrt(et))^2 + (5e-05/et)^2))'),
            eta = cms.string('sqrt(0.0106^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00856^2 + (1.97/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.29e-07^2 + (1.2/sqrt(et))^2 + (1.71e-05/et)^2))'),
            eta = cms.string('sqrt(0.0115^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00761^2 + (1.95/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(5.18e-09^2 + (1.14/sqrt(et))^2 + (1.7/et)^2))'),
            eta = cms.string('sqrt(0.012^2 + (1.88/et)^2)'),
            phi = cms.string('sqrt(0.00721^2 + (1.92/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(2.17e-07^2 + (1.09/sqrt(et))^2 + (2.08/et)^2))'),
            eta = cms.string('sqrt(0.0131^2 + (1.91/et)^2)'),
            phi = cms.string('sqrt(0.00722^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(3.65e-07^2 + (1.09/sqrt(et))^2 + (1.63/et)^2))'),
            eta = cms.string('sqrt(0.0134^2 + (1.92/et)^2)'),
            phi = cms.string('sqrt(0.00703^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(2.02e-07^2 + (1.09/sqrt(et))^2 + (1.68/et)^2))'),
            eta = cms.string('sqrt(0.0132^2 + (1.89/et)^2)'),
            phi = cms.string('sqrt(0.00845^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(5.27e-07^2 + (1.12/sqrt(et))^2 + (1.78/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (2.28/et)^2)'),
            phi = cms.string('sqrt(0.00975^2 + (2/et)^2)')
        )),
    bTagAlgo = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    constraints = cms.vuint32(3, 4),
    jetEnergyResolutionEtaBinning = cms.vdouble(0.0, -1.0),
    jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
    jetParametrisation = cms.uint32(1),
    jets = cms.InputTag("cleanPatJetsResnDown"),
    lepParametrisation = cms.uint32(1),
    lepResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.100'),
        et = cms.string('et * (0.00517 + 0.000143 * et)'),
        eta = cms.string('sqrt(0.000433^2 + (0.000161/sqrt(et))^2 + (0.00334/et)^2)'),
        phi = cms.string('sqrt(7.21e-05^2 + (7e-05/sqrt(et))^2 + (0.00296/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.100<=abs(eta) && abs(eta)<0.200'),
            et = cms.string('et * (0.00524 + 0.000143 * et)'),
            eta = cms.string('sqrt(0.000381^2 + (0.000473/sqrt(et))^2 + (0.00259/et)^2)'),
            phi = cms.string('sqrt(6.79e-05^2 + (0.000245/sqrt(et))^2 + (0.00274/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.200<=abs(eta) && abs(eta)<0.300'),
            et = cms.string('et * (0.00585 + 0.000138 * et)'),
            eta = cms.string('sqrt(0.000337^2 + (0.000381/sqrt(et))^2 + (0.0023/et)^2)'),
            phi = cms.string('sqrt(7.08e-05^2 + (6.75e-05/sqrt(et))^2 + (0.00307/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.300<=abs(eta) && abs(eta)<0.400'),
            et = cms.string('et * (0.0065 + 0.000133 * et)'),
            eta = cms.string('sqrt(0.000308^2 + (0.000166/sqrt(et))^2 + (0.00249/et)^2)'),
            phi = cms.string('sqrt(6.59e-05^2 + (0.000301/sqrt(et))^2 + (0.00281/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.400<=abs(eta) && abs(eta)<0.500'),
            et = cms.string('et * (0.0071 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000289^2 + (5.37e-09/sqrt(et))^2 + (0.00243/et)^2)'),
            phi = cms.string('sqrt(6.27e-05^2 + (0.000359/sqrt(et))^2 + (0.00278/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.500<=abs(eta) && abs(eta)<0.600'),
            et = cms.string('et * (0.00721 + 0.00013 * et)'),
            eta = cms.string('sqrt(0.000279^2 + (0.000272/sqrt(et))^2 + (0.0026/et)^2)'),
            phi = cms.string('sqrt(6.46e-05^2 + (0.00036/sqrt(et))^2 + (0.00285/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.600<=abs(eta) && abs(eta)<0.700'),
            et = cms.string('et * (0.00757 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000282^2 + (3.63e-10/sqrt(et))^2 + (0.00288/et)^2)'),
            phi = cms.string('sqrt(6.54e-05^2 + (0.000348/sqrt(et))^2 + (0.00301/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.700<=abs(eta) && abs(eta)<0.800'),
            et = cms.string('et * (0.0081 + 0.000127 * et)'),
            eta = cms.string('sqrt(0.000265^2 + (0.000609/sqrt(et))^2 + (0.00212/et)^2)'),
            phi = cms.string('sqrt(6.2e-05^2 + (0.000402/sqrt(et))^2 + (0.00304/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.800<=abs(eta) && abs(eta)<0.900'),
            et = cms.string('et * (0.00916 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000241^2 + (0.000678/sqrt(et))^2 + (0.00221/et)^2)'),
            phi = cms.string('sqrt(6.26e-05^2 + (0.000458/sqrt(et))^2 + (0.0031/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.900<=abs(eta) && abs(eta)<1.000'),
            et = cms.string('et * (0.0108 + 0.000151 * et)'),
            eta = cms.string('sqrt(0.000228^2 + (0.000612/sqrt(et))^2 + (0.00245/et)^2)'),
            phi = cms.string('sqrt(7.18e-05^2 + (0.000469/sqrt(et))^2 + (0.00331/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.000<=abs(eta) && abs(eta)<1.100'),
            et = cms.string('et * (0.0115 + 0.000153 * et)'),
            eta = cms.string('sqrt(0.000217^2 + (0.000583/sqrt(et))^2 + (0.00307/et)^2)'),
            phi = cms.string('sqrt(6.98e-05^2 + (0.000507/sqrt(et))^2 + (0.00338/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.100<=abs(eta) && abs(eta)<1.200'),
            et = cms.string('et * (0.013 + 0.000136 * et)'),
            eta = cms.string('sqrt(0.000195^2 + (0.000751/sqrt(et))^2 + (0.00282/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000584/sqrt(et))^2 + (0.00345/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.200<=abs(eta) && abs(eta)<1.300'),
            et = cms.string('et * (0.0144 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000183^2 + (0.000838/sqrt(et))^2 + (0.00227/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000667/sqrt(et))^2 + (0.00352/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.300<=abs(eta) && abs(eta)<1.400'),
            et = cms.string('et * (0.0149 + 0.000141 * et)'),
            eta = cms.string('sqrt(0.000196^2 + (0.000783/sqrt(et))^2 + (0.00274/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000711/sqrt(et))^2 + (0.00358/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.400<=abs(eta) && abs(eta)<1.500'),
            et = cms.string('et * (0.014 + 0.000155 * et)'),
            eta = cms.string('sqrt(0.0002^2 + (0.000832/sqrt(et))^2 + (0.00254/et)^2)'),
            phi = cms.string('sqrt(5.98e-05^2 + (0.000713/sqrt(et))^2 + (0.00362/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.500<=abs(eta) && abs(eta)<1.600'),
            et = cms.string('et * (0.0132 + 0.000169 * et)'),
            eta = cms.string('sqrt(0.000205^2 + (0.0007/sqrt(et))^2 + (0.00304/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000781/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.600<=abs(eta) && abs(eta)<1.700'),
            et = cms.string('et * (0.0129 + 0.0002 * et)'),
            eta = cms.string('sqrt(0.000214^2 + (0.000747/sqrt(et))^2 + (0.00319/et)^2)'),
            phi = cms.string('sqrt(6.92e-05^2 + (0.000865/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.700<=abs(eta) && abs(eta)<1.800'),
            et = cms.string('et * (0.0135 + 0.000264 * et)'),
            eta = cms.string('sqrt(0.000238^2 + (0.000582/sqrt(et))^2 + (0.00343/et)^2)'),
            phi = cms.string('sqrt(9.13e-05^2 + (0.000896/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.800<=abs(eta) && abs(eta)<1.900'),
            et = cms.string('et * (0.0144 + 0.00034 * et)'),
            eta = cms.string('sqrt(0.000263^2 + (0.000721/sqrt(et))^2 + (0.00322/et)^2)'),
            phi = cms.string('sqrt(0.000102^2 + (0.000994/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.900<=abs(eta) && abs(eta)<2.000'),
            et = cms.string('et * (0.0147 + 0.000441 * et)'),
            eta = cms.string('sqrt(0.000284^2 + (0.000779/sqrt(et))^2 + (0.0031/et)^2)'),
            phi = cms.string('sqrt(0.000123^2 + (0.00108/sqrt(et))^2 + (0.00315/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.000<=abs(eta) && abs(eta)<2.100'),
            et = cms.string('et * (0.0154 + 0.000604 * et)'),
            eta = cms.string('sqrt(0.000316^2 + (0.000566/sqrt(et))^2 + (0.00384/et)^2)'),
            phi = cms.string('sqrt(0.000169^2 + (0.000947/sqrt(et))^2 + (0.00422/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.100<=abs(eta) && abs(eta)<2.200'),
            et = cms.string('et * (0.0163 + 0.000764 * et)'),
            eta = cms.string('sqrt(0.000353^2 + (0.000749/sqrt(et))^2 + (0.0038/et)^2)'),
            phi = cms.string('sqrt(0.000176^2 + (0.00116/sqrt(et))^2 + (0.00423/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.200<=abs(eta) && abs(eta)<2.300'),
            et = cms.string('et * (0.0173 + 0.000951 * et)'),
            eta = cms.string('sqrt(0.000412^2 + (0.00102/sqrt(et))^2 + (0.00351/et)^2)'),
            phi = cms.string('sqrt(0.000207^2 + (0.00115/sqrt(et))^2 + (0.00469/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.300<=abs(eta) && abs(eta)<2.400'),
            et = cms.string('et * (0.0175 + 0.00126 * et)'),
            eta = cms.string('sqrt(0.000506^2 + (0.000791/sqrt(et))^2 + (0.0045/et)^2)'),
            phi = cms.string('sqrt(0.00027^2 + (0.00113/sqrt(et))^2 + (0.00528/et)^2)')
        )),
    leps = cms.InputTag("slimmedMuons"),
    mTop = cms.double(172.5),
    mW = cms.double(80.4),
    match = cms.InputTag("findTtSemiLepJetCombMVA"),
    maxBDiscLightJets = cms.double(3.0),
    maxDeltaS = cms.double(5e-05),
    maxF = cms.double(0.0001),
    maxNComb = cms.int32(1),
    maxNJets = cms.int32(-1),
    maxNrIter = cms.uint32(500),
    metParametrisation = cms.uint32(1),
    metResolutions = cms.VPSet(cms.PSet(
        et = cms.string('et * (sqrt(0.0337^2 + (0.888/sqrt(et))^2 + (19.6/et)^2))'),
        eta = cms.string('9999'),
        phi = cms.string('sqrt(1.28e-08^2 + (1.45/sqrt(et))^2 + (1.03/et)^2)')
    )),
    mets = cms.InputTag("scaledJetEnergyResnDown","slimmedMETs"),
    minBDiscBJets = cms.double(0.5426),
    udscResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0591^2 + (1/sqrt(et))^2 + (0.891/et)^2))'),
        eta = cms.string('sqrt(0.00915^2 + (1.51/et)^2)'),
        phi = cms.string('sqrt(0.01^2 + (1.6/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0619^2 + (0.975/sqrt(et))^2 + (1.54/et)^2))'),
            eta = cms.string('sqrt(0.00887^2 + (1.53/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0574^2 + (1/sqrt(et))^2 + (1.49e-05/et)^2))'),
            eta = cms.string('sqrt(0.00865^2 + (1.54/et)^2)'),
            phi = cms.string('sqrt(0.0101^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.0569^2 + (1.01/sqrt(et))^2 + (1.22e-07/et)^2))'),
            eta = cms.string('sqrt(0.00867^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.00988^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.057^2 + (1/sqrt(et))^2 + (2.17e-08/et)^2))'),
            eta = cms.string('sqrt(0.00907^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.0522^2 + (1.02/sqrt(et))^2 + (2.64e-05/et)^2))'),
            eta = cms.string('sqrt(0.00844^2 + (1.59/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0502^2 + (1.02/sqrt(et))^2 + (2.6e-06/et)^2))'),
            eta = cms.string('sqrt(0.00915^2 + (1.57/et)^2)'),
            phi = cms.string('sqrt(0.00979^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.053^2 + (1.03/sqrt(et))^2 + (4.87e-07/et)^2))'),
            eta = cms.string('sqrt(0.00856^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00925^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.051^2 + (1.03/sqrt(et))^2 + (7.53e-06/et)^2))'),
            eta = cms.string('sqrt(0.00897^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00973^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0549^2 + (1.04/sqrt(et))^2 + (5.62e-08/et)^2))'),
            eta = cms.string('sqrt(0.0095^2 + (1.6/et)^2)'),
            phi = cms.string('sqrt(0.00971^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0544^2 + (1.06/sqrt(et))^2 + (1.07e-05/et)^2))'),
            eta = cms.string('sqrt(0.00836^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00916^2 + (1.64/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0519^2 + (1.09/sqrt(et))^2 + (8.43e-06/et)^2))'),
            eta = cms.string('sqrt(0.00782^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00959^2 + (1.66/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0539^2 + (1.12/sqrt(et))^2 + (1.97e-07/et)^2))'),
            eta = cms.string('sqrt(0.0093^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00964^2 + (1.67/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0492^2 + (1.16/sqrt(et))^2 + (1.37e-08/et)^2))'),
            eta = cms.string('sqrt(0.00986^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00969^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0489^2 + (1.18/sqrt(et))^2 + (3.44e-07/et)^2))'),
            eta = cms.string('sqrt(0.0124^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.00992^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0414^2 + (1.25/sqrt(et))^2 + (1.98e-07/et)^2))'),
            eta = cms.string('sqrt(0.0181^2 + (1.63/et)^2)'),
            phi = cms.string('sqrt(0.0124^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0373^2 + (1.26/sqrt(et))^2 + (5.4e-07/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0135^2 + (1.8/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0125^2 + (1.24/sqrt(et))^2 + (1e-06/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0107^2 + (1.85/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(1.37e-07^2 + (1.08/sqrt(et))^2 + (3.06/et)^2))'),
            eta = cms.string('sqrt(0.00975^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00895^2 + (1.84/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(2.37e-07^2 + (1.04/sqrt(et))^2 + (3.01/et)^2))'),
            eta = cms.string('sqrt(0.00881^2 + (1.71/et)^2)'),
            phi = cms.string('sqrt(0.00902^2 + (1.81/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.3e-07^2 + (1/sqrt(et))^2 + (3.1/et)^2))'),
            eta = cms.string('sqrt(0.00938^2 + (1.75/et)^2)'),
            phi = cms.string('sqrt(0.00861^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(1.25e-07^2 + (0.965/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00894^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00877^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(5.78e-08^2 + (0.924/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00893^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00791^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(4.25e-08^2 + (0.923/sqrt(et))^2 + (2.85/et)^2))'),
            eta = cms.string('sqrt(0.0099^2 + (1.82/et)^2)'),
            phi = cms.string('sqrt(0.00775^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(0.00601^2 + (0.881/sqrt(et))^2 + (3.23/et)^2))'),
            eta = cms.string('sqrt(0.00944^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00807^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(4.94e-08^2 + (0.86/sqrt(et))^2 + (3.56/et)^2))'),
            eta = cms.string('sqrt(0.0103^2 + (2.15/et)^2)'),
            phi = cms.string('sqrt(0.0103^2 + (1.81/et)^2)')
        )),
    useBTagging = cms.bool(True),
    useOnlyMatch = cms.bool(False)
)


process.kinFitTtSemiLepEventJERUp = cms.EDProducer("TtSemiLepKinFitProducerMuon",
    bResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0686^2 + (1.03/sqrt(et))^2 + (1.68/et)^2))'),
        eta = cms.string('sqrt(0.00605^2 + (1.63/et)^2)'),
        phi = cms.string('sqrt(0.00787^2 + (1.74/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0737^2 + (1.01/sqrt(et))^2 + (1.74/et)^2))'),
            eta = cms.string('sqrt(0.00592^2 + (1.64/et)^2)'),
            phi = cms.string('sqrt(0.00766^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0657^2 + (1.07/sqrt(et))^2 + (5.16e-06/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00755^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.062^2 + (1.07/sqrt(et))^2 + (0.000134/et)^2))'),
            eta = cms.string('sqrt(0.00593^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.0605^2 + (1.07/sqrt(et))^2 + (1.84e-07/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.059^2 + (1.08/sqrt(et))^2 + (9.06e-09/et)^2))'),
            eta = cms.string('sqrt(0.00646^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00767^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0577^2 + (1.08/sqrt(et))^2 + (5.46e-06/et)^2))'),
            eta = cms.string('sqrt(0.00661^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00742^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.0525^2 + (1.09/sqrt(et))^2 + (4.05e-05/et)^2))'),
            eta = cms.string('sqrt(0.00724^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00771^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.0582^2 + (1.09/sqrt(et))^2 + (1.17e-05/et)^2))'),
            eta = cms.string('sqrt(0.00763^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00758^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0649^2 + (1.08/sqrt(et))^2 + (7.85e-06/et)^2))'),
            eta = cms.string('sqrt(0.00746^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00789^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0654^2 + (1.1/sqrt(et))^2 + (1.09e-07/et)^2))'),
            eta = cms.string('sqrt(0.00807^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00802^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0669^2 + (1.11/sqrt(et))^2 + (1.87e-06/et)^2))'),
            eta = cms.string('sqrt(0.00843^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.0078^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0643^2 + (1.15/sqrt(et))^2 + (2.76e-05/et)^2))'),
            eta = cms.string('sqrt(0.00886^2 + (1.74/et)^2)'),
            phi = cms.string('sqrt(0.00806^2 + (1.82/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0645^2 + (1.16/sqrt(et))^2 + (1.04e-06/et)^2))'),
            eta = cms.string('sqrt(0.0101^2 + (1.76/et)^2)'),
            phi = cms.string('sqrt(0.00784^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0637^2 + (1.19/sqrt(et))^2 + (1.08e-07/et)^2))'),
            eta = cms.string('sqrt(0.0127^2 + (1.78/et)^2)'),
            phi = cms.string('sqrt(0.00885^2 + (1.9/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0695^2 + (1.21/sqrt(et))^2 + (5.75e-06/et)^2))'),
            eta = cms.string('sqrt(0.0161^2 + (1.73/et)^2)'),
            phi = cms.string('sqrt(0.0108^2 + (1.93/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0748^2 + (1.2/sqrt(et))^2 + (5.15e-08/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.77/et)^2)'),
            phi = cms.string('sqrt(0.0112^2 + (2/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0624^2 + (1.23/sqrt(et))^2 + (2.28e-05/et)^2))'),
            eta = cms.string('sqrt(0.0123^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (2.02/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(0.0283^2 + (1.25/sqrt(et))^2 + (4.79e-07/et)^2))'),
            eta = cms.string('sqrt(0.0111^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.00857^2 + (2.01/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(0.0316^2 + (1.21/sqrt(et))^2 + (5e-05/et)^2))'),
            eta = cms.string('sqrt(0.0106^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00856^2 + (1.97/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.29e-07^2 + (1.2/sqrt(et))^2 + (1.71e-05/et)^2))'),
            eta = cms.string('sqrt(0.0115^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00761^2 + (1.95/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(5.18e-09^2 + (1.14/sqrt(et))^2 + (1.7/et)^2))'),
            eta = cms.string('sqrt(0.012^2 + (1.88/et)^2)'),
            phi = cms.string('sqrt(0.00721^2 + (1.92/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(2.17e-07^2 + (1.09/sqrt(et))^2 + (2.08/et)^2))'),
            eta = cms.string('sqrt(0.0131^2 + (1.91/et)^2)'),
            phi = cms.string('sqrt(0.00722^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(3.65e-07^2 + (1.09/sqrt(et))^2 + (1.63/et)^2))'),
            eta = cms.string('sqrt(0.0134^2 + (1.92/et)^2)'),
            phi = cms.string('sqrt(0.00703^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(2.02e-07^2 + (1.09/sqrt(et))^2 + (1.68/et)^2))'),
            eta = cms.string('sqrt(0.0132^2 + (1.89/et)^2)'),
            phi = cms.string('sqrt(0.00845^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(5.27e-07^2 + (1.12/sqrt(et))^2 + (1.78/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (2.28/et)^2)'),
            phi = cms.string('sqrt(0.00975^2 + (2/et)^2)')
        )),
    bTagAlgo = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    constraints = cms.vuint32(3, 4),
    jetEnergyResolutionEtaBinning = cms.vdouble(0.0, -1.0),
    jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
    jetParametrisation = cms.uint32(1),
    jets = cms.InputTag("cleanPatJetsResnUp"),
    lepParametrisation = cms.uint32(1),
    lepResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.100'),
        et = cms.string('et * (0.00517 + 0.000143 * et)'),
        eta = cms.string('sqrt(0.000433^2 + (0.000161/sqrt(et))^2 + (0.00334/et)^2)'),
        phi = cms.string('sqrt(7.21e-05^2 + (7e-05/sqrt(et))^2 + (0.00296/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.100<=abs(eta) && abs(eta)<0.200'),
            et = cms.string('et * (0.00524 + 0.000143 * et)'),
            eta = cms.string('sqrt(0.000381^2 + (0.000473/sqrt(et))^2 + (0.00259/et)^2)'),
            phi = cms.string('sqrt(6.79e-05^2 + (0.000245/sqrt(et))^2 + (0.00274/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.200<=abs(eta) && abs(eta)<0.300'),
            et = cms.string('et * (0.00585 + 0.000138 * et)'),
            eta = cms.string('sqrt(0.000337^2 + (0.000381/sqrt(et))^2 + (0.0023/et)^2)'),
            phi = cms.string('sqrt(7.08e-05^2 + (6.75e-05/sqrt(et))^2 + (0.00307/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.300<=abs(eta) && abs(eta)<0.400'),
            et = cms.string('et * (0.0065 + 0.000133 * et)'),
            eta = cms.string('sqrt(0.000308^2 + (0.000166/sqrt(et))^2 + (0.00249/et)^2)'),
            phi = cms.string('sqrt(6.59e-05^2 + (0.000301/sqrt(et))^2 + (0.00281/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.400<=abs(eta) && abs(eta)<0.500'),
            et = cms.string('et * (0.0071 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000289^2 + (5.37e-09/sqrt(et))^2 + (0.00243/et)^2)'),
            phi = cms.string('sqrt(6.27e-05^2 + (0.000359/sqrt(et))^2 + (0.00278/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.500<=abs(eta) && abs(eta)<0.600'),
            et = cms.string('et * (0.00721 + 0.00013 * et)'),
            eta = cms.string('sqrt(0.000279^2 + (0.000272/sqrt(et))^2 + (0.0026/et)^2)'),
            phi = cms.string('sqrt(6.46e-05^2 + (0.00036/sqrt(et))^2 + (0.00285/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.600<=abs(eta) && abs(eta)<0.700'),
            et = cms.string('et * (0.00757 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000282^2 + (3.63e-10/sqrt(et))^2 + (0.00288/et)^2)'),
            phi = cms.string('sqrt(6.54e-05^2 + (0.000348/sqrt(et))^2 + (0.00301/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.700<=abs(eta) && abs(eta)<0.800'),
            et = cms.string('et * (0.0081 + 0.000127 * et)'),
            eta = cms.string('sqrt(0.000265^2 + (0.000609/sqrt(et))^2 + (0.00212/et)^2)'),
            phi = cms.string('sqrt(6.2e-05^2 + (0.000402/sqrt(et))^2 + (0.00304/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.800<=abs(eta) && abs(eta)<0.900'),
            et = cms.string('et * (0.00916 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000241^2 + (0.000678/sqrt(et))^2 + (0.00221/et)^2)'),
            phi = cms.string('sqrt(6.26e-05^2 + (0.000458/sqrt(et))^2 + (0.0031/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.900<=abs(eta) && abs(eta)<1.000'),
            et = cms.string('et * (0.0108 + 0.000151 * et)'),
            eta = cms.string('sqrt(0.000228^2 + (0.000612/sqrt(et))^2 + (0.00245/et)^2)'),
            phi = cms.string('sqrt(7.18e-05^2 + (0.000469/sqrt(et))^2 + (0.00331/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.000<=abs(eta) && abs(eta)<1.100'),
            et = cms.string('et * (0.0115 + 0.000153 * et)'),
            eta = cms.string('sqrt(0.000217^2 + (0.000583/sqrt(et))^2 + (0.00307/et)^2)'),
            phi = cms.string('sqrt(6.98e-05^2 + (0.000507/sqrt(et))^2 + (0.00338/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.100<=abs(eta) && abs(eta)<1.200'),
            et = cms.string('et * (0.013 + 0.000136 * et)'),
            eta = cms.string('sqrt(0.000195^2 + (0.000751/sqrt(et))^2 + (0.00282/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000584/sqrt(et))^2 + (0.00345/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.200<=abs(eta) && abs(eta)<1.300'),
            et = cms.string('et * (0.0144 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000183^2 + (0.000838/sqrt(et))^2 + (0.00227/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000667/sqrt(et))^2 + (0.00352/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.300<=abs(eta) && abs(eta)<1.400'),
            et = cms.string('et * (0.0149 + 0.000141 * et)'),
            eta = cms.string('sqrt(0.000196^2 + (0.000783/sqrt(et))^2 + (0.00274/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000711/sqrt(et))^2 + (0.00358/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.400<=abs(eta) && abs(eta)<1.500'),
            et = cms.string('et * (0.014 + 0.000155 * et)'),
            eta = cms.string('sqrt(0.0002^2 + (0.000832/sqrt(et))^2 + (0.00254/et)^2)'),
            phi = cms.string('sqrt(5.98e-05^2 + (0.000713/sqrt(et))^2 + (0.00362/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.500<=abs(eta) && abs(eta)<1.600'),
            et = cms.string('et * (0.0132 + 0.000169 * et)'),
            eta = cms.string('sqrt(0.000205^2 + (0.0007/sqrt(et))^2 + (0.00304/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000781/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.600<=abs(eta) && abs(eta)<1.700'),
            et = cms.string('et * (0.0129 + 0.0002 * et)'),
            eta = cms.string('sqrt(0.000214^2 + (0.000747/sqrt(et))^2 + (0.00319/et)^2)'),
            phi = cms.string('sqrt(6.92e-05^2 + (0.000865/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.700<=abs(eta) && abs(eta)<1.800'),
            et = cms.string('et * (0.0135 + 0.000264 * et)'),
            eta = cms.string('sqrt(0.000238^2 + (0.000582/sqrt(et))^2 + (0.00343/et)^2)'),
            phi = cms.string('sqrt(9.13e-05^2 + (0.000896/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.800<=abs(eta) && abs(eta)<1.900'),
            et = cms.string('et * (0.0144 + 0.00034 * et)'),
            eta = cms.string('sqrt(0.000263^2 + (0.000721/sqrt(et))^2 + (0.00322/et)^2)'),
            phi = cms.string('sqrt(0.000102^2 + (0.000994/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.900<=abs(eta) && abs(eta)<2.000'),
            et = cms.string('et * (0.0147 + 0.000441 * et)'),
            eta = cms.string('sqrt(0.000284^2 + (0.000779/sqrt(et))^2 + (0.0031/et)^2)'),
            phi = cms.string('sqrt(0.000123^2 + (0.00108/sqrt(et))^2 + (0.00315/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.000<=abs(eta) && abs(eta)<2.100'),
            et = cms.string('et * (0.0154 + 0.000604 * et)'),
            eta = cms.string('sqrt(0.000316^2 + (0.000566/sqrt(et))^2 + (0.00384/et)^2)'),
            phi = cms.string('sqrt(0.000169^2 + (0.000947/sqrt(et))^2 + (0.00422/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.100<=abs(eta) && abs(eta)<2.200'),
            et = cms.string('et * (0.0163 + 0.000764 * et)'),
            eta = cms.string('sqrt(0.000353^2 + (0.000749/sqrt(et))^2 + (0.0038/et)^2)'),
            phi = cms.string('sqrt(0.000176^2 + (0.00116/sqrt(et))^2 + (0.00423/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.200<=abs(eta) && abs(eta)<2.300'),
            et = cms.string('et * (0.0173 + 0.000951 * et)'),
            eta = cms.string('sqrt(0.000412^2 + (0.00102/sqrt(et))^2 + (0.00351/et)^2)'),
            phi = cms.string('sqrt(0.000207^2 + (0.00115/sqrt(et))^2 + (0.00469/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.300<=abs(eta) && abs(eta)<2.400'),
            et = cms.string('et * (0.0175 + 0.00126 * et)'),
            eta = cms.string('sqrt(0.000506^2 + (0.000791/sqrt(et))^2 + (0.0045/et)^2)'),
            phi = cms.string('sqrt(0.00027^2 + (0.00113/sqrt(et))^2 + (0.00528/et)^2)')
        )),
    leps = cms.InputTag("slimmedMuons"),
    mTop = cms.double(172.5),
    mW = cms.double(80.4),
    match = cms.InputTag("findTtSemiLepJetCombMVA"),
    maxBDiscLightJets = cms.double(3.0),
    maxDeltaS = cms.double(5e-05),
    maxF = cms.double(0.0001),
    maxNComb = cms.int32(1),
    maxNJets = cms.int32(-1),
    maxNrIter = cms.uint32(500),
    metParametrisation = cms.uint32(1),
    metResolutions = cms.VPSet(cms.PSet(
        et = cms.string('et * (sqrt(0.0337^2 + (0.888/sqrt(et))^2 + (19.6/et)^2))'),
        eta = cms.string('9999'),
        phi = cms.string('sqrt(1.28e-08^2 + (1.45/sqrt(et))^2 + (1.03/et)^2)')
    )),
    mets = cms.InputTag("scaledJetEnergyResnUp","slimmedMETs"),
    minBDiscBJets = cms.double(0.5426),
    udscResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0591^2 + (1/sqrt(et))^2 + (0.891/et)^2))'),
        eta = cms.string('sqrt(0.00915^2 + (1.51/et)^2)'),
        phi = cms.string('sqrt(0.01^2 + (1.6/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0619^2 + (0.975/sqrt(et))^2 + (1.54/et)^2))'),
            eta = cms.string('sqrt(0.00887^2 + (1.53/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0574^2 + (1/sqrt(et))^2 + (1.49e-05/et)^2))'),
            eta = cms.string('sqrt(0.00865^2 + (1.54/et)^2)'),
            phi = cms.string('sqrt(0.0101^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.0569^2 + (1.01/sqrt(et))^2 + (1.22e-07/et)^2))'),
            eta = cms.string('sqrt(0.00867^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.00988^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.057^2 + (1/sqrt(et))^2 + (2.17e-08/et)^2))'),
            eta = cms.string('sqrt(0.00907^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.0522^2 + (1.02/sqrt(et))^2 + (2.64e-05/et)^2))'),
            eta = cms.string('sqrt(0.00844^2 + (1.59/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0502^2 + (1.02/sqrt(et))^2 + (2.6e-06/et)^2))'),
            eta = cms.string('sqrt(0.00915^2 + (1.57/et)^2)'),
            phi = cms.string('sqrt(0.00979^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.053^2 + (1.03/sqrt(et))^2 + (4.87e-07/et)^2))'),
            eta = cms.string('sqrt(0.00856^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00925^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.051^2 + (1.03/sqrt(et))^2 + (7.53e-06/et)^2))'),
            eta = cms.string('sqrt(0.00897^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00973^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0549^2 + (1.04/sqrt(et))^2 + (5.62e-08/et)^2))'),
            eta = cms.string('sqrt(0.0095^2 + (1.6/et)^2)'),
            phi = cms.string('sqrt(0.00971^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0544^2 + (1.06/sqrt(et))^2 + (1.07e-05/et)^2))'),
            eta = cms.string('sqrt(0.00836^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00916^2 + (1.64/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0519^2 + (1.09/sqrt(et))^2 + (8.43e-06/et)^2))'),
            eta = cms.string('sqrt(0.00782^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00959^2 + (1.66/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0539^2 + (1.12/sqrt(et))^2 + (1.97e-07/et)^2))'),
            eta = cms.string('sqrt(0.0093^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00964^2 + (1.67/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0492^2 + (1.16/sqrt(et))^2 + (1.37e-08/et)^2))'),
            eta = cms.string('sqrt(0.00986^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00969^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0489^2 + (1.18/sqrt(et))^2 + (3.44e-07/et)^2))'),
            eta = cms.string('sqrt(0.0124^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.00992^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0414^2 + (1.25/sqrt(et))^2 + (1.98e-07/et)^2))'),
            eta = cms.string('sqrt(0.0181^2 + (1.63/et)^2)'),
            phi = cms.string('sqrt(0.0124^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0373^2 + (1.26/sqrt(et))^2 + (5.4e-07/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0135^2 + (1.8/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0125^2 + (1.24/sqrt(et))^2 + (1e-06/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0107^2 + (1.85/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(1.37e-07^2 + (1.08/sqrt(et))^2 + (3.06/et)^2))'),
            eta = cms.string('sqrt(0.00975^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00895^2 + (1.84/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(2.37e-07^2 + (1.04/sqrt(et))^2 + (3.01/et)^2))'),
            eta = cms.string('sqrt(0.00881^2 + (1.71/et)^2)'),
            phi = cms.string('sqrt(0.00902^2 + (1.81/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.3e-07^2 + (1/sqrt(et))^2 + (3.1/et)^2))'),
            eta = cms.string('sqrt(0.00938^2 + (1.75/et)^2)'),
            phi = cms.string('sqrt(0.00861^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(1.25e-07^2 + (0.965/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00894^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00877^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(5.78e-08^2 + (0.924/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00893^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00791^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(4.25e-08^2 + (0.923/sqrt(et))^2 + (2.85/et)^2))'),
            eta = cms.string('sqrt(0.0099^2 + (1.82/et)^2)'),
            phi = cms.string('sqrt(0.00775^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(0.00601^2 + (0.881/sqrt(et))^2 + (3.23/et)^2))'),
            eta = cms.string('sqrt(0.00944^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00807^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(4.94e-08^2 + (0.86/sqrt(et))^2 + (3.56/et)^2))'),
            eta = cms.string('sqrt(0.0103^2 + (2.15/et)^2)'),
            phi = cms.string('sqrt(0.0103^2 + (1.81/et)^2)')
        )),
    useBTagging = cms.bool(True),
    useOnlyMatch = cms.bool(False)
)


process.kinFitTtSemiLepEventJESDown = cms.EDProducer("TtSemiLepKinFitProducerMuon",
    bResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0686^2 + (1.03/sqrt(et))^2 + (1.68/et)^2))'),
        eta = cms.string('sqrt(0.00605^2 + (1.63/et)^2)'),
        phi = cms.string('sqrt(0.00787^2 + (1.74/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0737^2 + (1.01/sqrt(et))^2 + (1.74/et)^2))'),
            eta = cms.string('sqrt(0.00592^2 + (1.64/et)^2)'),
            phi = cms.string('sqrt(0.00766^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0657^2 + (1.07/sqrt(et))^2 + (5.16e-06/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00755^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.062^2 + (1.07/sqrt(et))^2 + (0.000134/et)^2))'),
            eta = cms.string('sqrt(0.00593^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.0605^2 + (1.07/sqrt(et))^2 + (1.84e-07/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.059^2 + (1.08/sqrt(et))^2 + (9.06e-09/et)^2))'),
            eta = cms.string('sqrt(0.00646^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00767^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0577^2 + (1.08/sqrt(et))^2 + (5.46e-06/et)^2))'),
            eta = cms.string('sqrt(0.00661^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00742^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.0525^2 + (1.09/sqrt(et))^2 + (4.05e-05/et)^2))'),
            eta = cms.string('sqrt(0.00724^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00771^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.0582^2 + (1.09/sqrt(et))^2 + (1.17e-05/et)^2))'),
            eta = cms.string('sqrt(0.00763^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00758^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0649^2 + (1.08/sqrt(et))^2 + (7.85e-06/et)^2))'),
            eta = cms.string('sqrt(0.00746^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00789^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0654^2 + (1.1/sqrt(et))^2 + (1.09e-07/et)^2))'),
            eta = cms.string('sqrt(0.00807^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00802^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0669^2 + (1.11/sqrt(et))^2 + (1.87e-06/et)^2))'),
            eta = cms.string('sqrt(0.00843^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.0078^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0643^2 + (1.15/sqrt(et))^2 + (2.76e-05/et)^2))'),
            eta = cms.string('sqrt(0.00886^2 + (1.74/et)^2)'),
            phi = cms.string('sqrt(0.00806^2 + (1.82/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0645^2 + (1.16/sqrt(et))^2 + (1.04e-06/et)^2))'),
            eta = cms.string('sqrt(0.0101^2 + (1.76/et)^2)'),
            phi = cms.string('sqrt(0.00784^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0637^2 + (1.19/sqrt(et))^2 + (1.08e-07/et)^2))'),
            eta = cms.string('sqrt(0.0127^2 + (1.78/et)^2)'),
            phi = cms.string('sqrt(0.00885^2 + (1.9/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0695^2 + (1.21/sqrt(et))^2 + (5.75e-06/et)^2))'),
            eta = cms.string('sqrt(0.0161^2 + (1.73/et)^2)'),
            phi = cms.string('sqrt(0.0108^2 + (1.93/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0748^2 + (1.2/sqrt(et))^2 + (5.15e-08/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.77/et)^2)'),
            phi = cms.string('sqrt(0.0112^2 + (2/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0624^2 + (1.23/sqrt(et))^2 + (2.28e-05/et)^2))'),
            eta = cms.string('sqrt(0.0123^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (2.02/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(0.0283^2 + (1.25/sqrt(et))^2 + (4.79e-07/et)^2))'),
            eta = cms.string('sqrt(0.0111^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.00857^2 + (2.01/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(0.0316^2 + (1.21/sqrt(et))^2 + (5e-05/et)^2))'),
            eta = cms.string('sqrt(0.0106^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00856^2 + (1.97/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.29e-07^2 + (1.2/sqrt(et))^2 + (1.71e-05/et)^2))'),
            eta = cms.string('sqrt(0.0115^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00761^2 + (1.95/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(5.18e-09^2 + (1.14/sqrt(et))^2 + (1.7/et)^2))'),
            eta = cms.string('sqrt(0.012^2 + (1.88/et)^2)'),
            phi = cms.string('sqrt(0.00721^2 + (1.92/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(2.17e-07^2 + (1.09/sqrt(et))^2 + (2.08/et)^2))'),
            eta = cms.string('sqrt(0.0131^2 + (1.91/et)^2)'),
            phi = cms.string('sqrt(0.00722^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(3.65e-07^2 + (1.09/sqrt(et))^2 + (1.63/et)^2))'),
            eta = cms.string('sqrt(0.0134^2 + (1.92/et)^2)'),
            phi = cms.string('sqrt(0.00703^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(2.02e-07^2 + (1.09/sqrt(et))^2 + (1.68/et)^2))'),
            eta = cms.string('sqrt(0.0132^2 + (1.89/et)^2)'),
            phi = cms.string('sqrt(0.00845^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(5.27e-07^2 + (1.12/sqrt(et))^2 + (1.78/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (2.28/et)^2)'),
            phi = cms.string('sqrt(0.00975^2 + (2/et)^2)')
        )),
    bTagAlgo = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    constraints = cms.vuint32(3, 4),
    jetEnergyResolutionEtaBinning = cms.vdouble(0.0, -1.0),
    jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
    jetParametrisation = cms.uint32(1),
    jets = cms.InputTag("cleanPatJetsJESDown"),
    lepParametrisation = cms.uint32(1),
    lepResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.100'),
        et = cms.string('et * (0.00517 + 0.000143 * et)'),
        eta = cms.string('sqrt(0.000433^2 + (0.000161/sqrt(et))^2 + (0.00334/et)^2)'),
        phi = cms.string('sqrt(7.21e-05^2 + (7e-05/sqrt(et))^2 + (0.00296/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.100<=abs(eta) && abs(eta)<0.200'),
            et = cms.string('et * (0.00524 + 0.000143 * et)'),
            eta = cms.string('sqrt(0.000381^2 + (0.000473/sqrt(et))^2 + (0.00259/et)^2)'),
            phi = cms.string('sqrt(6.79e-05^2 + (0.000245/sqrt(et))^2 + (0.00274/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.200<=abs(eta) && abs(eta)<0.300'),
            et = cms.string('et * (0.00585 + 0.000138 * et)'),
            eta = cms.string('sqrt(0.000337^2 + (0.000381/sqrt(et))^2 + (0.0023/et)^2)'),
            phi = cms.string('sqrt(7.08e-05^2 + (6.75e-05/sqrt(et))^2 + (0.00307/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.300<=abs(eta) && abs(eta)<0.400'),
            et = cms.string('et * (0.0065 + 0.000133 * et)'),
            eta = cms.string('sqrt(0.000308^2 + (0.000166/sqrt(et))^2 + (0.00249/et)^2)'),
            phi = cms.string('sqrt(6.59e-05^2 + (0.000301/sqrt(et))^2 + (0.00281/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.400<=abs(eta) && abs(eta)<0.500'),
            et = cms.string('et * (0.0071 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000289^2 + (5.37e-09/sqrt(et))^2 + (0.00243/et)^2)'),
            phi = cms.string('sqrt(6.27e-05^2 + (0.000359/sqrt(et))^2 + (0.00278/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.500<=abs(eta) && abs(eta)<0.600'),
            et = cms.string('et * (0.00721 + 0.00013 * et)'),
            eta = cms.string('sqrt(0.000279^2 + (0.000272/sqrt(et))^2 + (0.0026/et)^2)'),
            phi = cms.string('sqrt(6.46e-05^2 + (0.00036/sqrt(et))^2 + (0.00285/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.600<=abs(eta) && abs(eta)<0.700'),
            et = cms.string('et * (0.00757 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000282^2 + (3.63e-10/sqrt(et))^2 + (0.00288/et)^2)'),
            phi = cms.string('sqrt(6.54e-05^2 + (0.000348/sqrt(et))^2 + (0.00301/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.700<=abs(eta) && abs(eta)<0.800'),
            et = cms.string('et * (0.0081 + 0.000127 * et)'),
            eta = cms.string('sqrt(0.000265^2 + (0.000609/sqrt(et))^2 + (0.00212/et)^2)'),
            phi = cms.string('sqrt(6.2e-05^2 + (0.000402/sqrt(et))^2 + (0.00304/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.800<=abs(eta) && abs(eta)<0.900'),
            et = cms.string('et * (0.00916 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000241^2 + (0.000678/sqrt(et))^2 + (0.00221/et)^2)'),
            phi = cms.string('sqrt(6.26e-05^2 + (0.000458/sqrt(et))^2 + (0.0031/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.900<=abs(eta) && abs(eta)<1.000'),
            et = cms.string('et * (0.0108 + 0.000151 * et)'),
            eta = cms.string('sqrt(0.000228^2 + (0.000612/sqrt(et))^2 + (0.00245/et)^2)'),
            phi = cms.string('sqrt(7.18e-05^2 + (0.000469/sqrt(et))^2 + (0.00331/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.000<=abs(eta) && abs(eta)<1.100'),
            et = cms.string('et * (0.0115 + 0.000153 * et)'),
            eta = cms.string('sqrt(0.000217^2 + (0.000583/sqrt(et))^2 + (0.00307/et)^2)'),
            phi = cms.string('sqrt(6.98e-05^2 + (0.000507/sqrt(et))^2 + (0.00338/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.100<=abs(eta) && abs(eta)<1.200'),
            et = cms.string('et * (0.013 + 0.000136 * et)'),
            eta = cms.string('sqrt(0.000195^2 + (0.000751/sqrt(et))^2 + (0.00282/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000584/sqrt(et))^2 + (0.00345/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.200<=abs(eta) && abs(eta)<1.300'),
            et = cms.string('et * (0.0144 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000183^2 + (0.000838/sqrt(et))^2 + (0.00227/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000667/sqrt(et))^2 + (0.00352/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.300<=abs(eta) && abs(eta)<1.400'),
            et = cms.string('et * (0.0149 + 0.000141 * et)'),
            eta = cms.string('sqrt(0.000196^2 + (0.000783/sqrt(et))^2 + (0.00274/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000711/sqrt(et))^2 + (0.00358/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.400<=abs(eta) && abs(eta)<1.500'),
            et = cms.string('et * (0.014 + 0.000155 * et)'),
            eta = cms.string('sqrt(0.0002^2 + (0.000832/sqrt(et))^2 + (0.00254/et)^2)'),
            phi = cms.string('sqrt(5.98e-05^2 + (0.000713/sqrt(et))^2 + (0.00362/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.500<=abs(eta) && abs(eta)<1.600'),
            et = cms.string('et * (0.0132 + 0.000169 * et)'),
            eta = cms.string('sqrt(0.000205^2 + (0.0007/sqrt(et))^2 + (0.00304/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000781/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.600<=abs(eta) && abs(eta)<1.700'),
            et = cms.string('et * (0.0129 + 0.0002 * et)'),
            eta = cms.string('sqrt(0.000214^2 + (0.000747/sqrt(et))^2 + (0.00319/et)^2)'),
            phi = cms.string('sqrt(6.92e-05^2 + (0.000865/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.700<=abs(eta) && abs(eta)<1.800'),
            et = cms.string('et * (0.0135 + 0.000264 * et)'),
            eta = cms.string('sqrt(0.000238^2 + (0.000582/sqrt(et))^2 + (0.00343/et)^2)'),
            phi = cms.string('sqrt(9.13e-05^2 + (0.000896/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.800<=abs(eta) && abs(eta)<1.900'),
            et = cms.string('et * (0.0144 + 0.00034 * et)'),
            eta = cms.string('sqrt(0.000263^2 + (0.000721/sqrt(et))^2 + (0.00322/et)^2)'),
            phi = cms.string('sqrt(0.000102^2 + (0.000994/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.900<=abs(eta) && abs(eta)<2.000'),
            et = cms.string('et * (0.0147 + 0.000441 * et)'),
            eta = cms.string('sqrt(0.000284^2 + (0.000779/sqrt(et))^2 + (0.0031/et)^2)'),
            phi = cms.string('sqrt(0.000123^2 + (0.00108/sqrt(et))^2 + (0.00315/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.000<=abs(eta) && abs(eta)<2.100'),
            et = cms.string('et * (0.0154 + 0.000604 * et)'),
            eta = cms.string('sqrt(0.000316^2 + (0.000566/sqrt(et))^2 + (0.00384/et)^2)'),
            phi = cms.string('sqrt(0.000169^2 + (0.000947/sqrt(et))^2 + (0.00422/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.100<=abs(eta) && abs(eta)<2.200'),
            et = cms.string('et * (0.0163 + 0.000764 * et)'),
            eta = cms.string('sqrt(0.000353^2 + (0.000749/sqrt(et))^2 + (0.0038/et)^2)'),
            phi = cms.string('sqrt(0.000176^2 + (0.00116/sqrt(et))^2 + (0.00423/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.200<=abs(eta) && abs(eta)<2.300'),
            et = cms.string('et * (0.0173 + 0.000951 * et)'),
            eta = cms.string('sqrt(0.000412^2 + (0.00102/sqrt(et))^2 + (0.00351/et)^2)'),
            phi = cms.string('sqrt(0.000207^2 + (0.00115/sqrt(et))^2 + (0.00469/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.300<=abs(eta) && abs(eta)<2.400'),
            et = cms.string('et * (0.0175 + 0.00126 * et)'),
            eta = cms.string('sqrt(0.000506^2 + (0.000791/sqrt(et))^2 + (0.0045/et)^2)'),
            phi = cms.string('sqrt(0.00027^2 + (0.00113/sqrt(et))^2 + (0.00528/et)^2)')
        )),
    leps = cms.InputTag("slimmedMuons"),
    mTop = cms.double(172.5),
    mW = cms.double(80.4),
    match = cms.InputTag("findTtSemiLepJetCombMVA"),
    maxBDiscLightJets = cms.double(3.0),
    maxDeltaS = cms.double(5e-05),
    maxF = cms.double(0.0001),
    maxNComb = cms.int32(1),
    maxNJets = cms.int32(-1),
    maxNrIter = cms.uint32(500),
    metParametrisation = cms.uint32(1),
    metResolutions = cms.VPSet(cms.PSet(
        et = cms.string('et * (sqrt(0.0337^2 + (0.888/sqrt(et))^2 + (19.6/et)^2))'),
        eta = cms.string('9999'),
        phi = cms.string('sqrt(1.28e-08^2 + (1.45/sqrt(et))^2 + (1.03/et)^2)')
    )),
    mets = cms.InputTag("scaledJetEnergyDown","slimmedMETs"),
    minBDiscBJets = cms.double(0.5426),
    udscResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0591^2 + (1/sqrt(et))^2 + (0.891/et)^2))'),
        eta = cms.string('sqrt(0.00915^2 + (1.51/et)^2)'),
        phi = cms.string('sqrt(0.01^2 + (1.6/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0619^2 + (0.975/sqrt(et))^2 + (1.54/et)^2))'),
            eta = cms.string('sqrt(0.00887^2 + (1.53/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0574^2 + (1/sqrt(et))^2 + (1.49e-05/et)^2))'),
            eta = cms.string('sqrt(0.00865^2 + (1.54/et)^2)'),
            phi = cms.string('sqrt(0.0101^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.0569^2 + (1.01/sqrt(et))^2 + (1.22e-07/et)^2))'),
            eta = cms.string('sqrt(0.00867^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.00988^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.057^2 + (1/sqrt(et))^2 + (2.17e-08/et)^2))'),
            eta = cms.string('sqrt(0.00907^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.0522^2 + (1.02/sqrt(et))^2 + (2.64e-05/et)^2))'),
            eta = cms.string('sqrt(0.00844^2 + (1.59/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0502^2 + (1.02/sqrt(et))^2 + (2.6e-06/et)^2))'),
            eta = cms.string('sqrt(0.00915^2 + (1.57/et)^2)'),
            phi = cms.string('sqrt(0.00979^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.053^2 + (1.03/sqrt(et))^2 + (4.87e-07/et)^2))'),
            eta = cms.string('sqrt(0.00856^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00925^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.051^2 + (1.03/sqrt(et))^2 + (7.53e-06/et)^2))'),
            eta = cms.string('sqrt(0.00897^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00973^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0549^2 + (1.04/sqrt(et))^2 + (5.62e-08/et)^2))'),
            eta = cms.string('sqrt(0.0095^2 + (1.6/et)^2)'),
            phi = cms.string('sqrt(0.00971^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0544^2 + (1.06/sqrt(et))^2 + (1.07e-05/et)^2))'),
            eta = cms.string('sqrt(0.00836^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00916^2 + (1.64/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0519^2 + (1.09/sqrt(et))^2 + (8.43e-06/et)^2))'),
            eta = cms.string('sqrt(0.00782^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00959^2 + (1.66/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0539^2 + (1.12/sqrt(et))^2 + (1.97e-07/et)^2))'),
            eta = cms.string('sqrt(0.0093^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00964^2 + (1.67/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0492^2 + (1.16/sqrt(et))^2 + (1.37e-08/et)^2))'),
            eta = cms.string('sqrt(0.00986^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00969^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0489^2 + (1.18/sqrt(et))^2 + (3.44e-07/et)^2))'),
            eta = cms.string('sqrt(0.0124^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.00992^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0414^2 + (1.25/sqrt(et))^2 + (1.98e-07/et)^2))'),
            eta = cms.string('sqrt(0.0181^2 + (1.63/et)^2)'),
            phi = cms.string('sqrt(0.0124^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0373^2 + (1.26/sqrt(et))^2 + (5.4e-07/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0135^2 + (1.8/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0125^2 + (1.24/sqrt(et))^2 + (1e-06/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0107^2 + (1.85/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(1.37e-07^2 + (1.08/sqrt(et))^2 + (3.06/et)^2))'),
            eta = cms.string('sqrt(0.00975^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00895^2 + (1.84/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(2.37e-07^2 + (1.04/sqrt(et))^2 + (3.01/et)^2))'),
            eta = cms.string('sqrt(0.00881^2 + (1.71/et)^2)'),
            phi = cms.string('sqrt(0.00902^2 + (1.81/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.3e-07^2 + (1/sqrt(et))^2 + (3.1/et)^2))'),
            eta = cms.string('sqrt(0.00938^2 + (1.75/et)^2)'),
            phi = cms.string('sqrt(0.00861^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(1.25e-07^2 + (0.965/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00894^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00877^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(5.78e-08^2 + (0.924/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00893^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00791^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(4.25e-08^2 + (0.923/sqrt(et))^2 + (2.85/et)^2))'),
            eta = cms.string('sqrt(0.0099^2 + (1.82/et)^2)'),
            phi = cms.string('sqrt(0.00775^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(0.00601^2 + (0.881/sqrt(et))^2 + (3.23/et)^2))'),
            eta = cms.string('sqrt(0.00944^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00807^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(4.94e-08^2 + (0.86/sqrt(et))^2 + (3.56/et)^2))'),
            eta = cms.string('sqrt(0.0103^2 + (2.15/et)^2)'),
            phi = cms.string('sqrt(0.0103^2 + (1.81/et)^2)')
        )),
    useBTagging = cms.bool(True),
    useOnlyMatch = cms.bool(False)
)


process.kinFitTtSemiLepEventJESUp = cms.EDProducer("TtSemiLepKinFitProducerMuon",
    bResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0686^2 + (1.03/sqrt(et))^2 + (1.68/et)^2))'),
        eta = cms.string('sqrt(0.00605^2 + (1.63/et)^2)'),
        phi = cms.string('sqrt(0.00787^2 + (1.74/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0737^2 + (1.01/sqrt(et))^2 + (1.74/et)^2))'),
            eta = cms.string('sqrt(0.00592^2 + (1.64/et)^2)'),
            phi = cms.string('sqrt(0.00766^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0657^2 + (1.07/sqrt(et))^2 + (5.16e-06/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00755^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.062^2 + (1.07/sqrt(et))^2 + (0.000134/et)^2))'),
            eta = cms.string('sqrt(0.00593^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.0605^2 + (1.07/sqrt(et))^2 + (1.84e-07/et)^2))'),
            eta = cms.string('sqrt(0.00584^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00734^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.059^2 + (1.08/sqrt(et))^2 + (9.06e-09/et)^2))'),
            eta = cms.string('sqrt(0.00646^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00767^2 + (1.74/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0577^2 + (1.08/sqrt(et))^2 + (5.46e-06/et)^2))'),
            eta = cms.string('sqrt(0.00661^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00742^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.0525^2 + (1.09/sqrt(et))^2 + (4.05e-05/et)^2))'),
            eta = cms.string('sqrt(0.00724^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00771^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.0582^2 + (1.09/sqrt(et))^2 + (1.17e-05/et)^2))'),
            eta = cms.string('sqrt(0.00763^2 + (1.67/et)^2)'),
            phi = cms.string('sqrt(0.00758^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0649^2 + (1.08/sqrt(et))^2 + (7.85e-06/et)^2))'),
            eta = cms.string('sqrt(0.00746^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00789^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0654^2 + (1.1/sqrt(et))^2 + (1.09e-07/et)^2))'),
            eta = cms.string('sqrt(0.00807^2 + (1.7/et)^2)'),
            phi = cms.string('sqrt(0.00802^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0669^2 + (1.11/sqrt(et))^2 + (1.87e-06/et)^2))'),
            eta = cms.string('sqrt(0.00843^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.0078^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0643^2 + (1.15/sqrt(et))^2 + (2.76e-05/et)^2))'),
            eta = cms.string('sqrt(0.00886^2 + (1.74/et)^2)'),
            phi = cms.string('sqrt(0.00806^2 + (1.82/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0645^2 + (1.16/sqrt(et))^2 + (1.04e-06/et)^2))'),
            eta = cms.string('sqrt(0.0101^2 + (1.76/et)^2)'),
            phi = cms.string('sqrt(0.00784^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0637^2 + (1.19/sqrt(et))^2 + (1.08e-07/et)^2))'),
            eta = cms.string('sqrt(0.0127^2 + (1.78/et)^2)'),
            phi = cms.string('sqrt(0.00885^2 + (1.9/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0695^2 + (1.21/sqrt(et))^2 + (5.75e-06/et)^2))'),
            eta = cms.string('sqrt(0.0161^2 + (1.73/et)^2)'),
            phi = cms.string('sqrt(0.0108^2 + (1.93/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0748^2 + (1.2/sqrt(et))^2 + (5.15e-08/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.77/et)^2)'),
            phi = cms.string('sqrt(0.0112^2 + (2/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0624^2 + (1.23/sqrt(et))^2 + (2.28e-05/et)^2))'),
            eta = cms.string('sqrt(0.0123^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (2.02/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(0.0283^2 + (1.25/sqrt(et))^2 + (4.79e-07/et)^2))'),
            eta = cms.string('sqrt(0.0111^2 + (1.79/et)^2)'),
            phi = cms.string('sqrt(0.00857^2 + (2.01/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(0.0316^2 + (1.21/sqrt(et))^2 + (5e-05/et)^2))'),
            eta = cms.string('sqrt(0.0106^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00856^2 + (1.97/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.29e-07^2 + (1.2/sqrt(et))^2 + (1.71e-05/et)^2))'),
            eta = cms.string('sqrt(0.0115^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00761^2 + (1.95/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(5.18e-09^2 + (1.14/sqrt(et))^2 + (1.7/et)^2))'),
            eta = cms.string('sqrt(0.012^2 + (1.88/et)^2)'),
            phi = cms.string('sqrt(0.00721^2 + (1.92/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(2.17e-07^2 + (1.09/sqrt(et))^2 + (2.08/et)^2))'),
            eta = cms.string('sqrt(0.0131^2 + (1.91/et)^2)'),
            phi = cms.string('sqrt(0.00722^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(3.65e-07^2 + (1.09/sqrt(et))^2 + (1.63/et)^2))'),
            eta = cms.string('sqrt(0.0134^2 + (1.92/et)^2)'),
            phi = cms.string('sqrt(0.00703^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(2.02e-07^2 + (1.09/sqrt(et))^2 + (1.68/et)^2))'),
            eta = cms.string('sqrt(0.0132^2 + (1.89/et)^2)'),
            phi = cms.string('sqrt(0.00845^2 + (1.86/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(5.27e-07^2 + (1.12/sqrt(et))^2 + (1.78/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (2.28/et)^2)'),
            phi = cms.string('sqrt(0.00975^2 + (2/et)^2)')
        )),
    bTagAlgo = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    constraints = cms.vuint32(3, 4),
    jetEnergyResolutionEtaBinning = cms.vdouble(0.0, -1.0),
    jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
    jetParametrisation = cms.uint32(1),
    jets = cms.InputTag("cleanPatJetsJESUp"),
    lepParametrisation = cms.uint32(1),
    lepResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.100'),
        et = cms.string('et * (0.00517 + 0.000143 * et)'),
        eta = cms.string('sqrt(0.000433^2 + (0.000161/sqrt(et))^2 + (0.00334/et)^2)'),
        phi = cms.string('sqrt(7.21e-05^2 + (7e-05/sqrt(et))^2 + (0.00296/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.100<=abs(eta) && abs(eta)<0.200'),
            et = cms.string('et * (0.00524 + 0.000143 * et)'),
            eta = cms.string('sqrt(0.000381^2 + (0.000473/sqrt(et))^2 + (0.00259/et)^2)'),
            phi = cms.string('sqrt(6.79e-05^2 + (0.000245/sqrt(et))^2 + (0.00274/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.200<=abs(eta) && abs(eta)<0.300'),
            et = cms.string('et * (0.00585 + 0.000138 * et)'),
            eta = cms.string('sqrt(0.000337^2 + (0.000381/sqrt(et))^2 + (0.0023/et)^2)'),
            phi = cms.string('sqrt(7.08e-05^2 + (6.75e-05/sqrt(et))^2 + (0.00307/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.300<=abs(eta) && abs(eta)<0.400'),
            et = cms.string('et * (0.0065 + 0.000133 * et)'),
            eta = cms.string('sqrt(0.000308^2 + (0.000166/sqrt(et))^2 + (0.00249/et)^2)'),
            phi = cms.string('sqrt(6.59e-05^2 + (0.000301/sqrt(et))^2 + (0.00281/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.400<=abs(eta) && abs(eta)<0.500'),
            et = cms.string('et * (0.0071 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000289^2 + (5.37e-09/sqrt(et))^2 + (0.00243/et)^2)'),
            phi = cms.string('sqrt(6.27e-05^2 + (0.000359/sqrt(et))^2 + (0.00278/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.500<=abs(eta) && abs(eta)<0.600'),
            et = cms.string('et * (0.00721 + 0.00013 * et)'),
            eta = cms.string('sqrt(0.000279^2 + (0.000272/sqrt(et))^2 + (0.0026/et)^2)'),
            phi = cms.string('sqrt(6.46e-05^2 + (0.00036/sqrt(et))^2 + (0.00285/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.600<=abs(eta) && abs(eta)<0.700'),
            et = cms.string('et * (0.00757 + 0.000129 * et)'),
            eta = cms.string('sqrt(0.000282^2 + (3.63e-10/sqrt(et))^2 + (0.00288/et)^2)'),
            phi = cms.string('sqrt(6.54e-05^2 + (0.000348/sqrt(et))^2 + (0.00301/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.700<=abs(eta) && abs(eta)<0.800'),
            et = cms.string('et * (0.0081 + 0.000127 * et)'),
            eta = cms.string('sqrt(0.000265^2 + (0.000609/sqrt(et))^2 + (0.00212/et)^2)'),
            phi = cms.string('sqrt(6.2e-05^2 + (0.000402/sqrt(et))^2 + (0.00304/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.800<=abs(eta) && abs(eta)<0.900'),
            et = cms.string('et * (0.00916 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000241^2 + (0.000678/sqrt(et))^2 + (0.00221/et)^2)'),
            phi = cms.string('sqrt(6.26e-05^2 + (0.000458/sqrt(et))^2 + (0.0031/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.900<=abs(eta) && abs(eta)<1.000'),
            et = cms.string('et * (0.0108 + 0.000151 * et)'),
            eta = cms.string('sqrt(0.000228^2 + (0.000612/sqrt(et))^2 + (0.00245/et)^2)'),
            phi = cms.string('sqrt(7.18e-05^2 + (0.000469/sqrt(et))^2 + (0.00331/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.000<=abs(eta) && abs(eta)<1.100'),
            et = cms.string('et * (0.0115 + 0.000153 * et)'),
            eta = cms.string('sqrt(0.000217^2 + (0.000583/sqrt(et))^2 + (0.00307/et)^2)'),
            phi = cms.string('sqrt(6.98e-05^2 + (0.000507/sqrt(et))^2 + (0.00338/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.100<=abs(eta) && abs(eta)<1.200'),
            et = cms.string('et * (0.013 + 0.000136 * et)'),
            eta = cms.string('sqrt(0.000195^2 + (0.000751/sqrt(et))^2 + (0.00282/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000584/sqrt(et))^2 + (0.00345/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.200<=abs(eta) && abs(eta)<1.300'),
            et = cms.string('et * (0.0144 + 0.000131 * et)'),
            eta = cms.string('sqrt(0.000183^2 + (0.000838/sqrt(et))^2 + (0.00227/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000667/sqrt(et))^2 + (0.00352/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.300<=abs(eta) && abs(eta)<1.400'),
            et = cms.string('et * (0.0149 + 0.000141 * et)'),
            eta = cms.string('sqrt(0.000196^2 + (0.000783/sqrt(et))^2 + (0.00274/et)^2)'),
            phi = cms.string('sqrt(5.37e-05^2 + (0.000711/sqrt(et))^2 + (0.00358/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.400<=abs(eta) && abs(eta)<1.500'),
            et = cms.string('et * (0.014 + 0.000155 * et)'),
            eta = cms.string('sqrt(0.0002^2 + (0.000832/sqrt(et))^2 + (0.00254/et)^2)'),
            phi = cms.string('sqrt(5.98e-05^2 + (0.000713/sqrt(et))^2 + (0.00362/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.500<=abs(eta) && abs(eta)<1.600'),
            et = cms.string('et * (0.0132 + 0.000169 * et)'),
            eta = cms.string('sqrt(0.000205^2 + (0.0007/sqrt(et))^2 + (0.00304/et)^2)'),
            phi = cms.string('sqrt(6.21e-05^2 + (0.000781/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.600<=abs(eta) && abs(eta)<1.700'),
            et = cms.string('et * (0.0129 + 0.0002 * et)'),
            eta = cms.string('sqrt(0.000214^2 + (0.000747/sqrt(et))^2 + (0.00319/et)^2)'),
            phi = cms.string('sqrt(6.92e-05^2 + (0.000865/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.700<=abs(eta) && abs(eta)<1.800'),
            et = cms.string('et * (0.0135 + 0.000264 * et)'),
            eta = cms.string('sqrt(0.000238^2 + (0.000582/sqrt(et))^2 + (0.00343/et)^2)'),
            phi = cms.string('sqrt(9.13e-05^2 + (0.000896/sqrt(et))^2 + (0.00348/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.800<=abs(eta) && abs(eta)<1.900'),
            et = cms.string('et * (0.0144 + 0.00034 * et)'),
            eta = cms.string('sqrt(0.000263^2 + (0.000721/sqrt(et))^2 + (0.00322/et)^2)'),
            phi = cms.string('sqrt(0.000102^2 + (0.000994/sqrt(et))^2 + (0.00337/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.900<=abs(eta) && abs(eta)<2.000'),
            et = cms.string('et * (0.0147 + 0.000441 * et)'),
            eta = cms.string('sqrt(0.000284^2 + (0.000779/sqrt(et))^2 + (0.0031/et)^2)'),
            phi = cms.string('sqrt(0.000123^2 + (0.00108/sqrt(et))^2 + (0.00315/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.000<=abs(eta) && abs(eta)<2.100'),
            et = cms.string('et * (0.0154 + 0.000604 * et)'),
            eta = cms.string('sqrt(0.000316^2 + (0.000566/sqrt(et))^2 + (0.00384/et)^2)'),
            phi = cms.string('sqrt(0.000169^2 + (0.000947/sqrt(et))^2 + (0.00422/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.100<=abs(eta) && abs(eta)<2.200'),
            et = cms.string('et * (0.0163 + 0.000764 * et)'),
            eta = cms.string('sqrt(0.000353^2 + (0.000749/sqrt(et))^2 + (0.0038/et)^2)'),
            phi = cms.string('sqrt(0.000176^2 + (0.00116/sqrt(et))^2 + (0.00423/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.200<=abs(eta) && abs(eta)<2.300'),
            et = cms.string('et * (0.0173 + 0.000951 * et)'),
            eta = cms.string('sqrt(0.000412^2 + (0.00102/sqrt(et))^2 + (0.00351/et)^2)'),
            phi = cms.string('sqrt(0.000207^2 + (0.00115/sqrt(et))^2 + (0.00469/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.300<=abs(eta) && abs(eta)<2.400'),
            et = cms.string('et * (0.0175 + 0.00126 * et)'),
            eta = cms.string('sqrt(0.000506^2 + (0.000791/sqrt(et))^2 + (0.0045/et)^2)'),
            phi = cms.string('sqrt(0.00027^2 + (0.00113/sqrt(et))^2 + (0.00528/et)^2)')
        )),
    leps = cms.InputTag("slimmedMuons"),
    mTop = cms.double(172.5),
    mW = cms.double(80.4),
    match = cms.InputTag("findTtSemiLepJetCombMVA"),
    maxBDiscLightJets = cms.double(3.0),
    maxDeltaS = cms.double(5e-05),
    maxF = cms.double(0.0001),
    maxNComb = cms.int32(1),
    maxNJets = cms.int32(-1),
    maxNrIter = cms.uint32(500),
    metParametrisation = cms.uint32(1),
    metResolutions = cms.VPSet(cms.PSet(
        et = cms.string('et * (sqrt(0.0337^2 + (0.888/sqrt(et))^2 + (19.6/et)^2))'),
        eta = cms.string('9999'),
        phi = cms.string('sqrt(1.28e-08^2 + (1.45/sqrt(et))^2 + (1.03/et)^2)')
    )),
    mets = cms.InputTag("scaledJetEnergyUp","slimmedMETs"),
    minBDiscBJets = cms.double(0.5426),
    udscResolutions = cms.VPSet(cms.PSet(
        bin = cms.string('0.000<=abs(eta) && abs(eta)<0.087'),
        et = cms.string('et * (sqrt(0.0591^2 + (1/sqrt(et))^2 + (0.891/et)^2))'),
        eta = cms.string('sqrt(0.00915^2 + (1.51/et)^2)'),
        phi = cms.string('sqrt(0.01^2 + (1.6/et)^2)')
    ), 
        cms.PSet(
            bin = cms.string('0.087<=abs(eta) && abs(eta)<0.174'),
            et = cms.string('et * (sqrt(0.0619^2 + (0.975/sqrt(et))^2 + (1.54/et)^2))'),
            eta = cms.string('sqrt(0.00887^2 + (1.53/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.174<=abs(eta) && abs(eta)<0.261'),
            et = cms.string('et * (sqrt(0.0574^2 + (1/sqrt(et))^2 + (1.49e-05/et)^2))'),
            eta = cms.string('sqrt(0.00865^2 + (1.54/et)^2)'),
            phi = cms.string('sqrt(0.0101^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.261<=abs(eta) && abs(eta)<0.348'),
            et = cms.string('et * (sqrt(0.0569^2 + (1.01/sqrt(et))^2 + (1.22e-07/et)^2))'),
            eta = cms.string('sqrt(0.00867^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.00988^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.348<=abs(eta) && abs(eta)<0.435'),
            et = cms.string('et * (sqrt(0.057^2 + (1/sqrt(et))^2 + (2.17e-08/et)^2))'),
            eta = cms.string('sqrt(0.00907^2 + (1.55/et)^2)'),
            phi = cms.string('sqrt(0.0102^2 + (1.59/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.435<=abs(eta) && abs(eta)<0.522'),
            et = cms.string('et * (sqrt(0.0522^2 + (1.02/sqrt(et))^2 + (2.64e-05/et)^2))'),
            eta = cms.string('sqrt(0.00844^2 + (1.59/et)^2)'),
            phi = cms.string('sqrt(0.00982^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.522<=abs(eta) && abs(eta)<0.609'),
            et = cms.string('et * (sqrt(0.0502^2 + (1.02/sqrt(et))^2 + (2.6e-06/et)^2))'),
            eta = cms.string('sqrt(0.00915^2 + (1.57/et)^2)'),
            phi = cms.string('sqrt(0.00979^2 + (1.6/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.609<=abs(eta) && abs(eta)<0.696'),
            et = cms.string('et * (sqrt(0.053^2 + (1.03/sqrt(et))^2 + (4.87e-07/et)^2))'),
            eta = cms.string('sqrt(0.00856^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00925^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.696<=abs(eta) && abs(eta)<0.783'),
            et = cms.string('et * (sqrt(0.051^2 + (1.03/sqrt(et))^2 + (7.53e-06/et)^2))'),
            eta = cms.string('sqrt(0.00897^2 + (1.58/et)^2)'),
            phi = cms.string('sqrt(0.00973^2 + (1.61/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.783<=abs(eta) && abs(eta)<0.870'),
            et = cms.string('et * (sqrt(0.0549^2 + (1.04/sqrt(et))^2 + (5.62e-08/et)^2))'),
            eta = cms.string('sqrt(0.0095^2 + (1.6/et)^2)'),
            phi = cms.string('sqrt(0.00971^2 + (1.62/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.870<=abs(eta) && abs(eta)<0.957'),
            et = cms.string('et * (sqrt(0.0544^2 + (1.06/sqrt(et))^2 + (1.07e-05/et)^2))'),
            eta = cms.string('sqrt(0.00836^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00916^2 + (1.64/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('0.957<=abs(eta) && abs(eta)<1.044'),
            et = cms.string('et * (sqrt(0.0519^2 + (1.09/sqrt(et))^2 + (8.43e-06/et)^2))'),
            eta = cms.string('sqrt(0.00782^2 + (1.68/et)^2)'),
            phi = cms.string('sqrt(0.00959^2 + (1.66/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.044<=abs(eta) && abs(eta)<1.131'),
            et = cms.string('et * (sqrt(0.0539^2 + (1.12/sqrt(et))^2 + (1.97e-07/et)^2))'),
            eta = cms.string('sqrt(0.0093^2 + (1.65/et)^2)'),
            phi = cms.string('sqrt(0.00964^2 + (1.67/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.131<=abs(eta) && abs(eta)<1.218'),
            et = cms.string('et * (sqrt(0.0492^2 + (1.16/sqrt(et))^2 + (1.37e-08/et)^2))'),
            eta = cms.string('sqrt(0.00986^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00969^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.218<=abs(eta) && abs(eta)<1.305'),
            et = cms.string('et * (sqrt(0.0489^2 + (1.18/sqrt(et))^2 + (3.44e-07/et)^2))'),
            eta = cms.string('sqrt(0.0124^2 + (1.72/et)^2)'),
            phi = cms.string('sqrt(0.00992^2 + (1.76/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.305<=abs(eta) && abs(eta)<1.392'),
            et = cms.string('et * (sqrt(0.0414^2 + (1.25/sqrt(et))^2 + (1.98e-07/et)^2))'),
            eta = cms.string('sqrt(0.0181^2 + (1.63/et)^2)'),
            phi = cms.string('sqrt(0.0124^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.392<=abs(eta) && abs(eta)<1.479'),
            et = cms.string('et * (sqrt(0.0373^2 + (1.26/sqrt(et))^2 + (5.4e-07/et)^2))'),
            eta = cms.string('sqrt(0.0121^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0135^2 + (1.8/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.479<=abs(eta) && abs(eta)<1.566'),
            et = cms.string('et * (sqrt(0.0125^2 + (1.24/sqrt(et))^2 + (1e-06/et)^2))'),
            eta = cms.string('sqrt(0.0122^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.0107^2 + (1.85/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.566<=abs(eta) && abs(eta)<1.653'),
            et = cms.string('et * (sqrt(1.37e-07^2 + (1.08/sqrt(et))^2 + (3.06/et)^2))'),
            eta = cms.string('sqrt(0.00975^2 + (1.69/et)^2)'),
            phi = cms.string('sqrt(0.00895^2 + (1.84/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.653<=abs(eta) && abs(eta)<1.740'),
            et = cms.string('et * (sqrt(2.37e-07^2 + (1.04/sqrt(et))^2 + (3.01/et)^2))'),
            eta = cms.string('sqrt(0.00881^2 + (1.71/et)^2)'),
            phi = cms.string('sqrt(0.00902^2 + (1.81/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.740<=abs(eta) && abs(eta)<1.830'),
            et = cms.string('et * (sqrt(2.3e-07^2 + (1/sqrt(et))^2 + (3.1/et)^2))'),
            eta = cms.string('sqrt(0.00938^2 + (1.75/et)^2)'),
            phi = cms.string('sqrt(0.00861^2 + (1.79/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.830<=abs(eta) && abs(eta)<1.930'),
            et = cms.string('et * (sqrt(1.25e-07^2 + (0.965/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00894^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00877^2 + (1.75/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('1.930<=abs(eta) && abs(eta)<2.043'),
            et = cms.string('et * (sqrt(5.78e-08^2 + (0.924/sqrt(et))^2 + (3.14/et)^2))'),
            eta = cms.string('sqrt(0.00893^2 + (1.83/et)^2)'),
            phi = cms.string('sqrt(0.00791^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.043<=abs(eta) && abs(eta)<2.172'),
            et = cms.string('et * (sqrt(4.25e-08^2 + (0.923/sqrt(et))^2 + (2.85/et)^2))'),
            eta = cms.string('sqrt(0.0099^2 + (1.82/et)^2)'),
            phi = cms.string('sqrt(0.00775^2 + (1.73/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.172<=abs(eta) && abs(eta)<2.322'),
            et = cms.string('et * (sqrt(0.00601^2 + (0.881/sqrt(et))^2 + (3.23/et)^2))'),
            eta = cms.string('sqrt(0.00944^2 + (1.8/et)^2)'),
            phi = cms.string('sqrt(0.00807^2 + (1.71/et)^2)')
        ), 
        cms.PSet(
            bin = cms.string('2.322<=abs(eta) && abs(eta)<2.500'),
            et = cms.string('et * (sqrt(4.94e-08^2 + (0.86/sqrt(et))^2 + (3.56/et)^2))'),
            eta = cms.string('sqrt(0.0103^2 + (2.15/et)^2)'),
            phi = cms.string('sqrt(0.0103^2 + (1.81/et)^2)')
        )),
    useBTagging = cms.bool(True),
    useOnlyMatch = cms.bool(False)
)


process.muCaloMetCorr = cms.EDProducer("MuonMETcorrInputProducer",
    src = cms.InputTag("muons"),
    srcMuonCorrections = cms.InputTag("muonMETValueMapProducer","muCorrData")
)


process.muPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedAllPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositGammaPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositNeutralPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositPUPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("muons")
)


process.particleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(True),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        eidLoose = cms.InputTag("eidLoose"),
        eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
        eidRobustLoose = cms.InputTag("eidRobustLoose"),
        eidRobustTight = cms.InputTag("eidRobustTight"),
        eidTight = cms.InputTag("eidTight")
    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("electronMatch"),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("elPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04PFIdPAT")
    ),
    isolationValuesNoPFId = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04NoPFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04NoPFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04NoPFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04NoPFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04NoPFIdPAT")
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patHemispheres = cms.EDProducer("PATHemisphereProducer",
    combinationMethod = cms.int32(3),
    maxElectronEta = cms.double(5),
    maxJetEta = cms.double(5),
    maxMuonEta = cms.double(5),
    maxPhotonEta = cms.double(5),
    maxTauEta = cms.double(-1),
    minElectronEt = cms.double(7),
    minJetEt = cms.double(30),
    minMuonEt = cms.double(7),
    minPhotonEt = cms.double(200000),
    minTauEt = cms.double(1000000),
    patElectrons = cms.InputTag("cleanLayer1Electrons"),
    patJets = cms.InputTag("cleanLayer1Jets"),
    patMets = cms.InputTag("layer1METs"),
    patMuons = cms.InputTag("cleanLayer1Muons"),
    patPhotons = cms.InputTag("cleanLayer1Photons"),
    patTaus = cms.InputTag("cleanLayer1Taus"),
    seedMethod = cms.int32(3)
)


process.patJetCharge = cms.EDProducer("JetChargeProducer",
    exp = cms.double(1.0),
    src = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    var = cms.string('Pt')
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4)
)


process.patJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacy")
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4PFJetsCHS"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleInclusiveSecondaryVertexHighEffBJetTags"), 
        cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("softPFMuonBJetTags"), cms.InputTag("softPFElectronBJetTags"), cms.InputTag("pfCombinedMVAV2BJetTags"), 
        cms.InputTag("pfCombinedCvsLJetTags"), cms.InputTag("pfCombinedCvsBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactors")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsCHS"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMETs = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetT1"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
        pjpar = cms.vdouble(-0.04, 0.6504)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("selectedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPfEcalEnergy = cms.bool(True),
    embedPickyMuon = cms.bool(True),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(True),
    embedTrack = cms.bool(False),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("muPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoValueChargedAll04PAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU04PAT"),
        pfPhotons = cms.InputTag("muPFIsoValueGamma04PAT")
    ),
    muonSource = cms.InputTag("muons"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    resolutions = cms.PSet(

    ),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(True),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("phPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("phPFIsoValueGamma04PFIdPAT")
    ),
    photonIDSources = cms.PSet(
        PhotonCutBasedIDLoose = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDLoose"),
        PhotonCutBasedIDTight = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDTight")
    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTaus = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatch"),
    genParticleMatch = cms.InputTag("tauMatch"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6LooseElectronRejection"),
        againstElectronMVA6Raw = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejection"),
        againstElectronMVA6category = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejection","category"),
        againstElectronMediumMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6MediumElectronRejection"),
        againstElectronTightMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6TightElectronRejection"),
        againstElectronVLooseMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6VLooseElectronRejection"),
        againstElectronVTightMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6VTightElectronRejection"),
        againstMuonLoose3 = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection3"),
        againstMuonTight3 = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection3"),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.InputTag("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits"),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw"),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw"),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw"),
        byIsolationMVArun2v1PWdR03oldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw"),
        byIsolationMVArun2v1PWnewDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw"),
        byIsolationMVArun2v1PWoldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw"),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits"),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT"),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT"),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT"),
        byLooseIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT"),
        byLooseIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT"),
        byLooseIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT"),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits"),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT"),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT"),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT"),
        byMediumIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT"),
        byMediumIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT"),
        byMediumIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT"),
        byPhotonPtSumOutsideSignalCone = cms.InputTag("hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone"),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits"),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT"),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT"),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT"),
        byTightIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT"),
        byTightIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT"),
        byTightIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT"),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT"),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT"),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT"),
        byVLooseIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT"),
        byVLooseIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT"),
        byVLooseIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT"),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT"),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT"),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT"),
        byVTightIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT"),
        byVTightIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT"),
        byVTightIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT"),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT"),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT"),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT"),
        byVVTightIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT"),
        byVVTightIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT"),
        byVVTightIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT"),
        chargedIsoPtSum = cms.InputTag("hpsPFTauChargedIsoPtSum"),
        chargedIsoPtSumdR03 = cms.InputTag("hpsPFTauChargedIsoPtSumdR03"),
        decayModeFinding = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
        decayModeFindingNewDMs = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
        footprintCorrection = cms.InputTag("hpsPFTauFootprintCorrection"),
        footprintCorrectiondR03 = cms.InputTag("hpsPFTauFootprintCorrectiondR03"),
        neutralIsoPtSum = cms.InputTag("hpsPFTauNeutralIsoPtSum"),
        neutralIsoPtSumWeight = cms.InputTag("hpsPFTauNeutralIsoPtSumWeight"),
        neutralIsoPtSumWeightdR03 = cms.InputTag("hpsPFTauNeutralIsoPtSumWeightdR03"),
        neutralIsoPtSumdR03 = cms.InputTag("hpsPFTauNeutralIsoPtSumdR03"),
        photonPtSumOutsideSignalCone = cms.InputTag("hpsPFTauPhotonPtSumOutsideSignalCone"),
        photonPtSumOutsideSignalConedR03 = cms.InputTag("hpsPFTauPhotonPtSumOutsideSignalConedR03"),
        puCorrPtSum = cms.InputTag("hpsPFTauPUcorrPtSum")
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducer"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("PATTriggerProducer",
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis"),
    l1GtRecordInputTag = cms.InputTag("gtDigis"),
    l1GtTriggerMenuLiteInputTag = cms.InputTag("gtDigis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
    onlyStandAlone = cms.bool(False),
    processName = cms.string('HLT')
)


process.patTriggerEvent = cms.EDProducer("PATTriggerEventProducer",
    patTriggerMatches = cms.VInputTag(cms.InputTag("MuonsTrigMatch"), cms.InputTag("ElectronsTrigMatch"), cms.InputTag("JetsTrigMatch")),
    patTriggerProducer = cms.InputTag("patTrigger"),
    processName = cms.string('HLT')
)


process.pdfWeights = cms.EDProducer("PdfWeightProducer",
    PdfInfoTag = cms.untracked.InputTag("generator"),
    PdfSetNames = cms.untracked.vstring('cteq66.LHgrid')
)


process.pfCandMETcorr = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorr")
)


process.pfCandsNotInJetsForMetCorr = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsPtrForMetCorr = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorr"),
    verbose = cms.untracked.bool(False)
)


process.pfJetsPtrForMetCorr = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfMetT0pc = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"))
)


process.pfMetT0pcT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT0pcT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0pcT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0pcTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rt = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"))
)


process.pfMetT0rtT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT0rtT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT0rtT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rtT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rtT2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT0rtTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetXYMult"))
)


process.pfNoJet = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("pfNoElectronJME"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrs"),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpIsoPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECO"),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpPFBRECO"),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpIsoPFBRECO = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpPFBRECO = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.phPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedAllPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(False),
        SCMatch_Veto = cms.bool(True),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositGammaPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(False),
        SCMatch_Veto = cms.bool(True),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositNeutralPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositPUPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoValueCharged03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositCharged"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositCharged"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAll"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAll"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPU"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPU"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.photonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedPhotons")
)


process.scaledJetEnergyDown = cms.EDProducer("JetEnergyScale",
    JECUncSrcFile = cms.FileInPath('MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_miniAODv2_v1_Uncertainty_AK4PF.txt'),
    inputJets = cms.InputTag("slimmedJets"),
    inputMETs = cms.InputTag("slimmedMETs"),
    jetEMLimitForMET = cms.double(0.9),
    jetPTThresholdForMET = cms.double(10.0),
    payload = cms.string('AK4PF'),
    resolutionEtaRanges = cms.vdouble(0.0, 0.5, 0.5, 1.1, 1.1, 
        1.7, 1.7, 2.3, 2.3, -1.0),
    resolutionFactors = cms.vdouble(1.052, 1.057, 1.096, 1.134, 1.288),
    scaleFactor = cms.double(1.0),
    scaleFactorB = cms.double(1.0),
    scaleType = cms.string('jes:down')
)


process.scaledJetEnergyNominal = cms.EDProducer("JetEnergyScale",
    JECUncSrcFile = cms.FileInPath('MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_miniAODv2_v1_Uncertainty_AK4PF.txt'),
    inputJets = cms.InputTag("slimmedJets"),
    inputMETs = cms.InputTag("slimmedMETs"),
    jetEMLimitForMET = cms.double(0.9),
    jetPTThresholdForMET = cms.double(10.0),
    payload = cms.string('AK4PF'),
    resolutionEtaRanges = cms.vdouble(0.0, 0.5, 0.5, 1.1, 1.1, 
        1.7, 1.7, 2.3, 2.3, -1.0),
    resolutionFactors = cms.vdouble(1.052, 1.057, 1.096, 1.134, 1.288),
    scaleFactor = cms.double(1.0),
    scaleFactorB = cms.double(1.0),
    scaleType = cms.string('jer')
)


process.scaledJetEnergyResnDown = cms.EDProducer("JetEnergyScale",
    JECUncSrcFile = cms.FileInPath('MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_miniAODv2_v1_Uncertainty_AK4PF.txt'),
    inputJets = cms.InputTag("slimmedJets"),
    inputMETs = cms.InputTag("slimmedMETs"),
    jetEMLimitForMET = cms.double(0.9),
    jetPTThresholdForMET = cms.double(10.0),
    payload = cms.string('AK4PF'),
    resolutionEtaRanges = cms.vdouble(0.0, 0.5, 0.5, 1.1, 1.1, 
        1.7, 1.7, 2.3, 2.3, -1.0),
    resolutionFactors = cms.vdouble(0.99, 1.001, 1.032, 1.042, 1.089),
    scaleFactor = cms.double(1.0),
    scaleFactorB = cms.double(1.0),
    scaleType = cms.string('jer')
)


process.scaledJetEnergyResnUp = cms.EDProducer("JetEnergyScale",
    JECUncSrcFile = cms.FileInPath('MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_miniAODv2_v1_Uncertainty_AK4PF.txt'),
    inputJets = cms.InputTag("slimmedJets"),
    inputMETs = cms.InputTag("slimmedMETs"),
    jetEMLimitForMET = cms.double(0.9),
    jetPTThresholdForMET = cms.double(10.0),
    payload = cms.string('AK4PF'),
    resolutionEtaRanges = cms.vdouble(0.0, 0.5, 0.5, 1.1, 1.1, 
        1.7, 1.7, 2.3, 2.3, -1.0),
    resolutionFactors = cms.vdouble(1.115, 1.114, 1.161, 1.228, 1.488),
    scaleFactor = cms.double(1.0),
    scaleFactorB = cms.double(1.0),
    scaleType = cms.string('jer')
)


process.scaledJetEnergyUp = cms.EDProducer("JetEnergyScale",
    JECUncSrcFile = cms.FileInPath('MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_miniAODv2_v1_Uncertainty_AK4PF.txt'),
    inputJets = cms.InputTag("slimmedJets"),
    inputMETs = cms.InputTag("slimmedMETs"),
    jetEMLimitForMET = cms.double(0.9),
    jetPTThresholdForMET = cms.double(10.0),
    payload = cms.string('AK4PF'),
    resolutionEtaRanges = cms.vdouble(0.0, 0.5, 0.5, 1.1, 1.1, 
        1.7, 1.7, 2.3, 2.3, -1.0),
    resolutionFactors = cms.vdouble(1.052, 1.057, 1.096, 1.134, 1.288),
    scaleFactor = cms.double(1.0),
    scaleFactorB = cms.double(1.0),
    scaleType = cms.string('jes:up')
)


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("genParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.allEventsFilter = cms.EDFilter("AllEventsFilter")


process.countPatElectrons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatElectrons")
)


process.countPatJets = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatJets")
)


process.countPatLeptons = cms.EDFilter("PATLeptonCountFilter",
    countElectrons = cms.bool(True),
    countMuons = cms.bool(True),
    countTaus = cms.bool(False),
    electronSource = cms.InputTag("cleanPatElectrons"),
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    muonSource = cms.InputTag("cleanPatMuons"),
    tauSource = cms.InputTag("cleanPatTaus")
)


process.countPatMuons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatMuons")
)


process.countPatPhotons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatPhotons")
)


process.countPatTaus = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatTaus")
)


process.eg_selector = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Ele10_LW_L1R'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.egmu_selector = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Ele10_LW_L1R', 
        'HLT_Mu9'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.hltPhysicsDeclared = cms.EDFilter("HLTPhysicsDeclared",
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    invert = cms.bool(False)
)


process.jet_selector = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Jet15U'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.mu_selector = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Mu9'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.pfAllChargedHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfPileUpAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
    maxAbsZ = cms.double(24),
    maxd0 = cms.double(2),
    minimumNDOF = cms.uint32(3),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
    cut = cms.string(''),
    src = cms.InputTag("slimmedElectrons")
)


process.selectedPatJets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    src = cms.InputTag("slimmedJets")
)


process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
    cut = cms.string(''),
    src = cms.InputTag("slimmedMuons")
)


process.selectedPatPhotons = cms.EDFilter("PATPhotonSelector",
    cut = cms.string(''),
    src = cms.InputTag("slimmedPhotons")
)


process.selectedPatTaus = cms.EDFilter("PATTauSelector",
    cut = cms.string(''),
    src = cms.InputTag("slimmedTaus")
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring('oneProng0Pi0', 
        'oneProng1Pi0', 
        'oneProng2Pi0', 
        'oneProngOther', 
        'threeProng0Pi0', 
        'threeProng1Pi0', 
        'threeProngOther', 
        'rare'),
    src = cms.InputTag("tauGenJets")
)


process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("cleanPatElectrons"), cms.InputTag("cleanPatMuons"), cms.InputTag("cleanPatTaus"), cms.InputTag("cleanPatPhotons"), cms.InputTag("cleanPatJets")),
    logName = cms.untracked.string('cleanPatCandidates|PATSummaryTables')
)


process.myMiniTreeProducer = cms.EDAnalyzer("MiniTreeProducer",
    Electrons = cms.PSet(
        dedxSource = cms.InputTag("dedxHarmonic2"),
        id = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose'),
        maxEta = cms.double(2.5),
        maxRelCombPFIsoEA = cms.double(0.0994),
        minEt = cms.double(10),
        mvacut = cms.double(0.3),
        rhoIso = cms.InputTag("fixedGridRhoFastjetAll"),
        sources = cms.InputTag("slimmedElectrons"),
        triggerEvent = cms.InputTag("patTrigger"),
        triggerMatch = cms.string('TrigMatch')
    ),
    Jets = cms.PSet(
        CaloJetId = cms.PSet(
            quality = cms.string('LOOSE'),
            version = cms.string('PURE09')
        ),
        PFJetId = cms.PSet(
            quality = cms.string('LOOSE'),
            version = cms.string('FIRSTDATA')
        ),
        dedxSource = cms.InputTag("dedxHarmonic2"),
        jet_rho = cms.InputTag("fixedGridRhoAll"),
        maxEta = cms.double(2.5),
        minDeltaRtoLepton = cms.double(0.4),
        minPt = cms.double(17),
        puMVADiscriminant = cms.InputTag("puJetMva","fullDiscriminant"),
        puMVADiscriminantResCor = cms.InputTag("puJetMvaResCor","fullDiscriminant"),
        puMVAID = cms.InputTag("puJetMva","fullId"),
        puMVAIDResCor = cms.InputTag("puJetMvaResCor","fullId"),
        resolutionsFile = cms.string('Spring16_25nsV6_MC_PtResolution_AK4PF.txt'),
        scaleFactorsFile = cms.string('Spring16_25nsV6_MC_SF_AK4PF.txt'),
        sources = cms.InputTag("slimmedJets"),
        triggerEvent = cms.InputTag("hltTriggerSummaryAOD"),
        triggerMatch = cms.string('TrigMatch'),
        useRawJets = cms.bool(False)
    ),
    KineFit = cms.PSet(
        chi2OfFit = cms.InputTag("kinFitTtSemiLepEvent","Chi2"),
        chi2OfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown","Chi2"),
        chi2OfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","Chi2"),
        chi2OfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","Chi2"),
        chi2OfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp","Chi2"),
        njetsUsed = cms.InputTag("kinFitTtSemiLepEvent","NumberOfConsideredJets"),
        njetsUsedDown = cms.InputTag("kinFitTtSemiLepEventJESDown","NumberOfConsideredJets"),
        njetsUsedJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","NumberOfConsideredJets"),
        njetsUsedJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","NumberOfConsideredJets"),
        njetsUsedUp = cms.InputTag("kinFitTtSemiLepEventJESUp","NumberOfConsideredJets"),
        probOfFit = cms.InputTag("kinFitTtSemiLepEvent","Prob"),
        probOfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown","Prob"),
        probOfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","Prob"),
        probOfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","Prob"),
        probOfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp","Prob"),
        runKineFitter = cms.bool(True),
        sources = cms.VInputTag("kinFitTtSemiLepEvent:Leptons", "kinFitTtSemiLepEvent:Neutrinos", "kinFitTtSemiLepEvent:PartonsHadB", "kinFitTtSemiLepEvent:PartonsHadP", "kinFitTtSemiLepEvent:PartonsHadQ", 
            "kinFitTtSemiLepEvent:PartonsLepB", "kinFitTtSemiLepEventJESUp:Leptons", "kinFitTtSemiLepEventJESUp:Neutrinos", "kinFitTtSemiLepEventJESUp:PartonsHadB", "kinFitTtSemiLepEventJESUp:PartonsHadP", 
            "kinFitTtSemiLepEventJESUp:PartonsHadQ", "kinFitTtSemiLepEventJESUp:PartonsLepB", "kinFitTtSemiLepEventJESDown:Leptons", "kinFitTtSemiLepEventJESDown:Neutrinos", "kinFitTtSemiLepEventJESDown:PartonsHadB", 
            "kinFitTtSemiLepEventJESDown:PartonsHadP", "kinFitTtSemiLepEventJESDown:PartonsHadQ", "kinFitTtSemiLepEventJESDown:PartonsLepB", "kinFitTtSemiLepEventJERUp:Leptons", "kinFitTtSemiLepEventJERUp:Neutrinos", 
            "kinFitTtSemiLepEventJERUp:PartonsHadB", "kinFitTtSemiLepEventJERUp:PartonsHadP", "kinFitTtSemiLepEventJERUp:PartonsHadQ", "kinFitTtSemiLepEventJERUp:PartonsLepB", "kinFitTtSemiLepEventJERDown:Leptons", 
            "kinFitTtSemiLepEventJERDown:Neutrinos", "kinFitTtSemiLepEventJERDown:PartonsHadB", "kinFitTtSemiLepEventJERDown:PartonsHadP", "kinFitTtSemiLepEventJERDown:PartonsHadQ", "kinFitTtSemiLepEventJERDown:PartonsLepB"),
        statusOfFit = cms.InputTag("kinFitTtSemiLepEvent","Status"),
        statusOfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown","Status"),
        statusOfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown","Status"),
        statusOfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp","Status"),
        statusOfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp","Status")
    ),
    MCTruth = cms.PSet(
        isData = cms.bool(False),
        jpMatchSources = cms.VInputTag("selectedPatJetsByRef", "selectedPatJetsAK5JPTByRef", "selectedPatJetsAK5PFByRef", "selectedPatJetsPFlowByRef"),
        producePDFweights = cms.bool(False),
        sampleChannel = cms.string('muon'),
        sampleCode = cms.string('W4JetsToLNu')
    ),
    Mets = cms.PSet(
        minMET = cms.double(10),
        sources = cms.InputTag("slimmedMETs")
    ),
    Muons = cms.PSet(
        maxEta = cms.double(2.4),
        maxRelIso = cms.double(0.25),
        minMatchStations = cms.int32(1),
        minMuonHits = cms.int32(0),
        minPixelHits = cms.int32(0),
        minPt = cms.double(10),
        minTrackerLayers = cms.int32(5),
        sources = cms.InputTag("slimmedMuons"),
        triggerEvent = cms.InputTag("patTrigger"),
        triggerMatch = cms.string('TrigMatch')
    ),
    Tracks = cms.PSet(
        dedxSource = cms.InputTag("dedxHarmonic2"),
        maxD0 = cms.double(400),
        maxEta = cms.double(2.5),
        maxPtSumInTrackIsoCone = cms.double(10),
        maxTrackChi2 = cms.double(10),
        minDeltaRtoLepton = cms.double(0.1),
        minPixelHits = cms.int32(1),
        minPrimaryVertexWeight = cms.double(0),
        minPt = cms.double(1),
        minQuality = cms.int32(2),
        minTrackValidHits = cms.int32(5),
        source = cms.InputTag("generalTracks"),
        trackIsoCone = cms.double(0.3)
    ),
    Trigger = cms.PSet(
        bits = cms.vstring('HLT_IsoMu27_v3', 
            'HLT_IsoMu27_v4', 
            'HLT_IsoMu27_v5', 
            'HLT_IsoMu27_v7', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v2', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v3', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v4', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v5', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v6', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v7', 
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v8', 
            'HLT_JetE30_NoBPTX_v2', 
            'HLT_JetE30_NoBPTX_v3', 
            'HLT_JetE30_NoBPTX_v4'),
        source = cms.InputTag("TriggerResults","","HLT")
    ),
    Vertex = cms.PSet(
        beamSpotSource = cms.InputTag("offlineBeamSpot"),
        maxRho = cms.double(2.0),
        maxZ = cms.double(24),
        minNDOF = cms.int32(4),
        rho = cms.InputTag("fixedGridRhoAll"),
        useBeamSpot = cms.bool(True),
        vertexSource = cms.InputTag("offlineSlimmedPrimaryVertices")
    ),
    minEventQualityToStore = cms.int32(0),
    rhoCorSrc = cms.InputTag("kt6PFJetsForIso","rho")
)


process.patCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("patElectrons"), cms.InputTag("patMuons"), cms.InputTag("patTaus"), cms.InputTag("patPhotons"), cms.InputTag("patJets"), 
        cms.InputTag("patMETs")),
    logName = cms.untracked.string('patCandidates|PATSummaryTables')
)


process.selectedPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("selectedPatElectrons"), cms.InputTag("selectedPatMuons"), cms.InputTag("selectedPatTaus"), cms.InputTag("selectedPatPhotons"), cms.InputTag("selectedPatJets")),
    logName = cms.untracked.string('selectedPatCanddiates|PATSummaryTables')
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('data.root'),
    outputCommands = cms.untracked.vstring('keep *', 
        'keep patTriggerObjects_patTrigger_*_LOCALUSER', 
        'keep patTriggerFilters_patTrigger_*_LOCALUSER', 
        'keep patTriggerPaths_patTrigger_*_LOCALUSER', 
        'keep patTriggerEvent_patTriggerEvent_*_LOCALUSER', 
        'keep patTriggerObjectsedmAssociation_patTriggerEvent_MuonsTrigMatch_LOCALUSER', 
        'keep *_selectedPatMuons_*_*', 
        'keep patTriggerObjectsedmAssociation_patTriggerEvent_ElectronsTrigMatch_LOCALUSER', 
        'keep *_selectedPatElectrons_*_*', 
        'keep patTriggerObjectsedmAssociation_patTriggerEvent_JetsTrigMatch_LOCALUSER', 
        'keep *_selectedPatJets_*_*'),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(99)
)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4L1JPTOffsetCorrector)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1OffsetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL1L2L3Corrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastjetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL1FastL2L3ResidualCorrector)


process.patShrinkingConePFTauDiscrimination = cms.Sequence()


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastjetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL1FastL2L3Corrector)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL1L2L3Corrector)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL1FastL2L3Corrector)


process.cleanPatCandidates = cms.Sequence(process.cleanPatMuons+process.cleanPatElectrons+process.cleanPatPhotons+process.cleanPatTaus+process.cleanPatJets+process.cleanPatCandidateSummary)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1OffsetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL1L2L3ResidualCorrector)


process.electronPFIsolationDepositsPFBRECOSequence = cms.Sequence(process.elPFIsoDepositChargedPFBRECO+process.elPFIsoDepositChargedAllPFBRECO+process.elPFIsoDepositGammaPFBRECO+process.elPFIsoDepositNeutralPFBRECO+process.elPFIsoDepositPUPFBRECO)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL1FastL2L3ResidualCorrector)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL1L2L3Corrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastjetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL1FastL2L3ResidualCorrector)


process.patJetFlavourIdLegacy = cms.Sequence(process.patJetPartonsLegacy+process.patJetPartonAssociationLegacy+process.patJetFlavourAssociationLegacy)


process.pfNoPileUpIsoPFBRECOSequence = cms.Sequence(process.pfPileUpIsoPFBRECO+process.pfNoPileUpIsoPFBRECO)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL2L3ResidualCorrector)


process.pfSortByTypePFBRECOSequence = cms.Sequence(process.pfAllNeutralHadronsPFBRECO+process.pfAllChargedHadronsPFBRECO+process.pfAllPhotonsPFBRECO+process.pfAllChargedParticlesPFBRECO+process.pfPileUpAllChargedParticlesPFBRECO+process.pfAllNeutralHadronsAndPhotonsPFBRECO)


process.updateHPSPFTaus = cms.Sequence()


process.basePreSel = cms.Sequence(process.primaryVertexFilter)


process.selectedPatCandidates = cms.Sequence(process.selectedPatElectrons+process.selectedPatMuons+process.selectedPatTaus+process.selectedPatPhotons+process.selectedPatJets+process.selectedPatCandidateSummary)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastjetCorrector+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL1FastL2L3Corrector)


process.countPatCandidates = cms.Sequence(process.countPatElectrons+process.countPatMuons+process.countPatTaus+process.countPatLeptons+process.countPatPhotons+process.countPatJets)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL2L3Corrector)


process.patCaloTauDiscrimination = cms.Sequence()


process.photonPFIsolationDepositsPFBRECOSequence = cms.Sequence(process.phPFIsoDepositChargedPFBRECO+process.phPFIsoDepositChargedAllPFBRECO+process.phPFIsoDepositGammaPFBRECO+process.phPFIsoDepositNeutralPFBRECO+process.phPFIsoDepositPUPFBRECO)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL1FastL2L3Corrector)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL6SLBCorrector+process.ak4CaloL1FastL2L3L6Corrector)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1OffsetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL1L2L3ResidualCorrector)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL2L3ResidualCorrector)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL6SLBCorrector+process.ak4PFL1FastL2L3L6Corrector)


process.photonPFIsolationDepositsPATSequence = cms.Sequence(process.phPFIsoDepositChargedPAT+process.phPFIsoDepositChargedAllPAT+process.phPFIsoDepositGammaPAT+process.phPFIsoDepositNeutralPAT+process.phPFIsoDepositPUPAT)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2RelativeCorrector+process.ak4TrackL3AbsoluteCorrector+process.ak4TrackL2L3Corrector)


process.patJetFlavourId = cms.Sequence(process.patJetPartons+process.patJetFlavourAssociation)


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL2L3ResidualCorrector)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastjetCorrector+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL1FastL2L3ResidualCorrector)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL6SLBCorrector+process.ak4PFL2L3L6Corrector)


process.patPFTauIsolation = cms.Sequence(process.tauIsoDepositPFCandidates+process.tauIsoDepositPFChargedHadrons+process.tauIsoDepositPFNeutralHadrons+process.tauIsoDepositPFGammas)


process.pfNoPileUpPFBRECOSequence = cms.Sequence(process.pfPileUpPFBRECO+process.pfNoPileUpPFBRECO)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL1FastL2L3ResidualCorrector)


process.electronPFIsolationDepositsPATSequence = cms.Sequence(process.elPFIsoDepositChargedPAT+process.elPFIsoDepositChargedAllPAT+process.elPFIsoDepositGammaPAT+process.elPFIsoDepositNeutralPAT+process.elPFIsoDepositPUPAT)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL6SLBCorrector+process.ak4CaloL2L3L6Corrector)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastjetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL1FastL2L3Corrector)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL2L3Corrector)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL2L3Corrector)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL1L2L3ResidualCorrector)


process.pfPhotonIsolationPATSequence = cms.Sequence(process.photonPFIsolationDepositsPATSequence+process.phPFIsoValueCharged03PFIdPAT+process.phPFIsoValueChargedAll03PFIdPAT+process.phPFIsoValueGamma03PFIdPAT+process.phPFIsoValueNeutral03PFIdPAT+process.phPFIsoValuePU03PFIdPAT+process.phPFIsoValueCharged04PFIdPAT+process.phPFIsoValueChargedAll04PFIdPAT+process.phPFIsoValueGamma04PFIdPAT+process.phPFIsoValueNeutral04PFIdPAT+process.phPFIsoValuePU04PFIdPAT)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1OffsetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL1L2L3Corrector)


process.patJetCorrections = cms.Sequence(process.patJetCorrFactors)


process.muonPFIsolationDepositsPATSequence = cms.Sequence(process.muPFIsoDepositChargedPAT+process.muPFIsoDepositChargedAllPAT+process.muPFIsoDepositGammaPAT+process.muPFIsoDepositNeutralPAT+process.muPFIsoDepositPUPAT)


process.patFixedConePFTauDiscrimination = cms.Sequence()


process.muonPFIsolationPATSequence = cms.Sequence(process.muonPFIsolationDepositsPATSequence+process.muPFIsoValueCharged03PAT+process.muPFMeanDRIsoValueCharged03PAT+process.muPFSumDRIsoValueCharged03PAT+process.muPFIsoValueChargedAll03PAT+process.muPFMeanDRIsoValueChargedAll03PAT+process.muPFSumDRIsoValueChargedAll03PAT+process.muPFIsoValueGamma03PAT+process.muPFMeanDRIsoValueGamma03PAT+process.muPFSumDRIsoValueGamma03PAT+process.muPFIsoValueNeutral03PAT+process.muPFMeanDRIsoValueNeutral03PAT+process.muPFSumDRIsoValueNeutral03PAT+process.muPFIsoValueGammaHighThreshold03PAT+process.muPFMeanDRIsoValueGammaHighThreshold03PAT+process.muPFSumDRIsoValueGammaHighThreshold03PAT+process.muPFIsoValueNeutralHighThreshold03PAT+process.muPFMeanDRIsoValueNeutralHighThreshold03PAT+process.muPFSumDRIsoValueNeutralHighThreshold03PAT+process.muPFIsoValuePU03PAT+process.muPFMeanDRIsoValuePU03PAT+process.muPFSumDRIsoValuePU03PAT+process.muPFIsoValueCharged04PAT+process.muPFMeanDRIsoValueCharged04PAT+process.muPFSumDRIsoValueCharged04PAT+process.muPFIsoValueChargedAll04PAT+process.muPFMeanDRIsoValueChargedAll04PAT+process.muPFSumDRIsoValueChargedAll04PAT+process.muPFIsoValueGamma04PAT+process.muPFMeanDRIsoValueGamma04PAT+process.muPFSumDRIsoValueGamma04PAT+process.muPFIsoValueNeutral04PAT+process.muPFMeanDRIsoValueNeutral04PAT+process.muPFSumDRIsoValueNeutral04PAT+process.muPFIsoValueGammaHighThreshold04PAT+process.muPFMeanDRIsoValueGammaHighThreshold04PAT+process.muPFSumDRIsoValueGammaHighThreshold04PAT+process.muPFIsoValueNeutralHighThreshold04PAT+process.muPFMeanDRIsoValueNeutralHighThreshold04PAT+process.muPFSumDRIsoValueNeutralHighThreshold04PAT+process.muPFIsoValuePU04PAT+process.muPFMeanDRIsoValuePU04PAT+process.muPFSumDRIsoValuePU04PAT)


process.pfElectronIsolationPATSequence = cms.Sequence(process.electronPFIsolationDepositsPATSequence+process.elPFIsoValueCharged03PFIdPAT+process.elPFIsoValueChargedAll03PFIdPAT+process.elPFIsoValueGamma03PFIdPAT+process.elPFIsoValueNeutral03PFIdPAT+process.elPFIsoValuePU03PFIdPAT+process.elPFIsoValueCharged04PFIdPAT+process.elPFIsoValueChargedAll04PFIdPAT+process.elPFIsoValueGamma04PFIdPAT+process.elPFIsoValueNeutral04PFIdPAT+process.elPFIsoValuePU04PFIdPAT+process.elPFIsoValueCharged03NoPFIdPAT+process.elPFIsoValueChargedAll03NoPFIdPAT+process.elPFIsoValueGamma03NoPFIdPAT+process.elPFIsoValueNeutral03NoPFIdPAT+process.elPFIsoValuePU03NoPFIdPAT+process.elPFIsoValueCharged04NoPFIdPAT+process.elPFIsoValueChargedAll04NoPFIdPAT+process.elPFIsoValueGamma04NoPFIdPAT+process.elPFIsoValueNeutral04NoPFIdPAT+process.elPFIsoValuePU04NoPFIdPAT)


process.muonPFIsolationDepositsPFBRECOSequence = cms.Sequence(process.muPFIsoDepositChargedPFBRECO+process.muPFIsoDepositChargedAllPFBRECO+process.muPFIsoDepositGammaPFBRECO+process.muPFIsoDepositNeutralPFBRECO+process.muPFIsoDepositPUPFBRECO)


process.kinFitSequence = cms.Sequence(process.scaledJetEnergyNominal+process.selectedPatMuons+process.selectedPatElectrons+process.selectedPatPhotons+process.selectedPatTaus+process.selectedPatJets+process.cleanPatMuons+process.cleanPatElectrons+process.cleanPatPhotons+process.cleanPatTaus+process.cleanPatJets+process.cleanPatJetsResCor+process.kinFitTtSemiLepEvent)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL2L3ResidualCorrector)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL2L3Corrector)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL2L3ResidualCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1OffsetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL1L2L3ResidualCorrector)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL2L3Corrector)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL1L2L3ResidualCorrector)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1OffsetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL1L2L3Corrector)


process.patHPSPFTauDiscrimination = cms.Sequence(process.updateHPSPFTaus)


process.pfParticleSelectionPFBRECOSequence = cms.Sequence(process.pfNoPileUpIsoPFBRECOSequence+process.pfNoPileUpPFBRECOSequence+process.pfSortByTypePFBRECOSequence)


process.correctionTermsPfMetType1Type2 = cms.Sequence(process.pfJetsPtrForMetCorr+process.particleFlowPtrs+process.pfCandsNotInJetsPtrForMetCorr+process.pfCandsNotInJetsForMetCorr+process.pfCandMETcorr+process.ak4PFCHSL1FastL2L3ResidualCorrectorChain+process.ak4PFCHSL1FastL2L3Corrector+process.corrPfMetType1+process.corrPfMetType2)


process.correctionTermsCaloMet = cms.Sequence(process.ak4CaloL2L3CorrectorChain+process.corrCaloMetType1+process.muCaloMetCorr+process.corrCaloMetType2)


process.pfParticleSelectionForIsoSequence = cms.Sequence(process.particleFlowPtrs+process.pfParticleSelectionPFBRECOSequence)


process.patMETCorrections = cms.Sequence(process.correctionTermsCaloMet+process.caloMetT1+process.caloMetT1T2+process.correctionTermsPfMetType1Type2+process.pfMetT1+process.pfMetT1T2)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.pfNoPileUpIsoPFBRECOSequence+process.pfSortByTypePFBRECOSequence)


process.makePatTaus = cms.Sequence(process.patHPSPFTauDiscrimination+process.patPFCandidateIsoDepositSelection+process.patPFTauIsolation+process.tauMatch+process.tauGenJets+process.tauGenJetsSelectorAllHadrons+process.tauGenJetMatch+process.patTaus)


process.makePatJets = cms.Sequence(process.patJetCorrections+process.patJetCharge+process.patJetPartonMatch+process.patJetGenJetMatch+process.patJetFlavourIdLegacy+process.patJetFlavourId+process.patJets)


process.makePatMuons = cms.Sequence(process.pfParticleSelectionForIsoSequence+process.muonPFIsolationPATSequence+process.muonMatch+process.patMuons)


process.makePatElectrons = cms.Sequence(process.pfParticleSelectionForIsoSequence+process.pfElectronIsolationPATSequence+process.electronMatch+process.patElectrons)


process.makePatMETs = cms.Sequence(process.patMETCorrections+process.patMETs)


process.makePatPhotons = cms.Sequence(process.pfParticleSelectionForIsoSequence+process.pfPhotonIsolationPATSequence+process.photonMatch+process.patPhotons)


process.patCandidates = cms.Sequence(process.makePatElectrons+process.makePatMuons+process.makePatTaus+process.makePatPhotons+process.makePatJets+process.makePatMETs+process.patCandidateSummary)


process.patDefaultSequence = cms.Sequence(process.patCandidates+process.selectedPatCandidates+process.cleanPatCandidates+process.countPatCandidates)


process.genUtilsSequence = cms.Path(process.pdfWeights)


process.p = cms.Path(process.kinFitSequence+process.allEventsFilter+process.basePreSel+process.myMiniTreeProducer)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(100)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(False),
    fileName = cms.string('W4JetsToLNu_MuMC_20170717_Ntuple.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ak10PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL1Fastjet', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual')
)


process.ak10PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL1Offset', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual')
)


process.ak10PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute')
)


process.ak10PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual')
)


process.ak10PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL1Fastjet', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual')
)


process.ak10PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL1Offset', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual')
)


process.ak10PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL2Relative', 
        'ak10PFL3Absolute')
)


process.ak10PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual')
)


process.ak10PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL1Fastjet', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual')
)


process.ak1PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL1Offset', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual')
)


process.ak1PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute')
)


process.ak1PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual')
)


process.ak1PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL1Fastjet', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual')
)


process.ak1PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL1Offset', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual')
)


process.ak1PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL2Relative', 
        'ak1PFL3Absolute')
)


process.ak1PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual')
)


process.ak1PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL1Fastjet', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual')
)


process.ak2PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL1Offset', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual')
)


process.ak2PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute')
)


process.ak2PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual')
)


process.ak2PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL1Fastjet', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual')
)


process.ak2PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL1Offset', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual')
)


process.ak2PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL2Relative', 
        'ak2PFL3Absolute')
)


process.ak2PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual')
)


process.ak2PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL1Fastjet', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual')
)


process.ak3PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL1Offset', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual')
)


process.ak3PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute')
)


process.ak3PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual')
)


process.ak3PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL1Fastjet', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual')
)


process.ak3PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL1Offset', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual')
)


process.ak3PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL2Relative', 
        'ak3PFL3Absolute')
)


process.ak3PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual')
)


process.ak3PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2L3Residual')
)


process.ak4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute')
)


process.ak4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB')
)


process.ak4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual')
)


process.ak4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute')
)


process.ak4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual')
)


process.ak4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL2Relative', 
        'ak4CaloL3Absolute')
)


process.ak4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB')
)


process.ak4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual')
)


process.ak4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4JPTL1Fastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute')
)


process.ak4JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4JPTL1Fastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual')
)


process.ak4JPTL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute')
)


process.ak4JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual')
)


process.ak4JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute')
)


process.ak4JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual')
)


process.ak4JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)


process.ak4PFCHSL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual')
)


process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)


process.ak4PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual')
)


process.ak4PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)


process.ak4PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual')
)


process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute')
)


process.ak4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB')
)


process.ak4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual')
)


process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute')
)


process.ak4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual')
)


process.ak4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL2Relative', 
        'ak4PFL3Absolute')
)


process.ak4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB')
)


process.ak4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual')
)


process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4TrackL2Relative', 
        'ak4TrackL3Absolute')
)


process.ak4TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4TrackL2Relative', 
        'ak4TrackL3Absolute')
)


process.ak4TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL1Fastjet', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual')
)


process.ak5PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL1Offset', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual')
)


process.ak5PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute')
)


process.ak5PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual')
)


process.ak5PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL1Fastjet', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual')
)


process.ak6PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL1Offset', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual')
)


process.ak6PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute')
)


process.ak6PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual')
)


process.ak6PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL1Fastjet', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual')
)


process.ak6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL1Offset', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual')
)


process.ak6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL2Relative', 
        'ak6PFL3Absolute')
)


process.ak6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual')
)


process.ak6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2L3Residual')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Fastjet', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak7PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute')
)


process.ak7PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual')
)


process.ak7PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL1Offset', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual')
)


process.ak7PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute')
)


process.ak7PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual')
)


process.ak7PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL1Fastjet', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual')
)


process.ak8PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL1Offset', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual')
)


process.ak8PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute')
)


process.ak8PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual')
)


process.ak8PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL1Fastjet', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual')
)


process.ak8PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL1Offset', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual')
)


process.ak8PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL2Relative', 
        'ak8PFL3Absolute')
)


process.ak8PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual')
)


process.ak8PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL1Fastjet', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual')
)


process.ak9PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL1Offset', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual')
)


process.ak9PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute')
)


process.ak9PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual')
)


process.ak9PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL1Fastjet', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual')
)


process.ak9PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL1Offset', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual')
)


process.ak9PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL2Relative', 
        'ak9PFL3Absolute')
)


process.ak9PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual')
)


process.ak9PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2L3Residual')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2L3Residual')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v6'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.prefer("es_hardcode")

process.schedule = cms.Schedule(*[ process.p ])
