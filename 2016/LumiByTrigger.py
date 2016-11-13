import os, sys

from Setup import *

#### how many lumi period blocks to make
ndiv=10
#### 
trigger_list = ["HLT_Mu17_Mu8_DZ_v",
                "HLT_Mu17_Mu8_SameSign_DZ_v",
                "HLT_Mu20_Mu10_SameSign_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v",
                "HLT_Mu8_v",
                "HLT_Mu17_v",
                "HLT_Mu20_v",
                "HLT_Mu50_v",
                "HLT_IsoMu20_v",
                "HLT_IsoTkMu20_v",
                "HLT_IsoMu22_v",
                "HLT_IsoTkMu22_v",
                "HLT_Mu17_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v",
                "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v",
                "HLT_TripleMu_12_10_5_v",
                "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v",
                "HLT_IsoTkMu24_v",
                "HLT_IsoMu24_v"]              



el_trigger_list = ["HLT_Ele105_CaloIdVT_GsfTrkIdT_v"
                   ,"HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13_v"
                   ,"HLT_Ele115_CaloIdVT_GsfTrkIdT_v"
                   ,"HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v"
                   ,"HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v"
                   ,"HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v"
                   ,"HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400_v"
                   ,"HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v"
                   ,"HLT_Ele15_IsoVVVL_PFHT350_v"
                   ,"HLT_Ele15_IsoVVVL_PFHT400_PFMET50_v"
                   ,"HLT_Ele15_IsoVVVL_PFHT400_v"
                   ,"HLT_Ele15_IsoVVVL_PFHT600_v"
                   ,"HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v"
                   ,"HLT_Ele17_CaloIdL_GsfTrkIdVL_v"
                   ,"HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30_v"
                   ,"HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v"
                   ,"HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v"
                   ,"HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"
                   ,"HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v"
                   ,"HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v"
                   ,"HLT_Ele22_eta2p1_WPLoose_Gsf_v"
                   ,"HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v"
                   ,"HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v"
                   ,"HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v"
                   ,"HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded_v"
                   ,"HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"
                   ,"HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v"
                   ,"HLT_Ele23_WPLoose_Gsf_WHbbBoost_v"
                   ,"HLT_Ele23_WPLoose_Gsf_v"
                   ,"HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v"
                   ,"HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v"
                   ,"HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v"
                   ,"HLT_Ele24_eta2p1_WPLoose_Gsf_v"
                   ,"HLT_Ele250_CaloIdVT_GsfTrkIdT_v"
                   ,"HLT_Ele25_WPTight_Gsf_v"
                   ,"HLT_Ele25_eta2p1_WPLoose_Gsf_v"
                   ,"HLT_Ele25_eta2p1_WPTight_Gsf_v"
                   ,"HLT_Ele27_HighEta_Ele20_Mass55_v"
                   ,"HLT_Ele27_WPLoose_Gsf_WHbbBoost_v"
                   ,"HLT_Ele27_WPLoose_Gsf_v"
                   ,"HLT_Ele27_WPTight_Gsf_L1JetTauSeeded_v"
                   ,"HLT_Ele27_WPTight_Gsf_v"
                   ,"HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v"
                   ,"HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v"
                   ,"HLT_Ele27_eta2p1_WPLoose_Gsf_v"
                   ,"HLT_Ele27_eta2p1_WPTight_Gsf_v"
                   ,"HLT_Ele300_CaloIdVT_GsfTrkIdT_v"
                   ,"HLT_Ele30WP60_Ele8_Mass55_v"
                   ,"HLT_Ele30WP60_SC4_Mass55_v"
                   ,"HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v"
                   ,"HLT_Ele32_eta2p1_WPTight_Gsf_v"
                   ,"HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50_v"
                   ,"HLT_Ele35_WPLoose_Gsf_v"
                   ,"HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v"
                   ,"HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded_v"
                   ,"HLT_Ele45_WPLoose_Gsf_v"
                   ,"HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v"
                   ,"HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v"
                   ,"HLT_Ele50_IsoVVVL_PFHT400_v"
                   ,"HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v"
                   ,"HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v"]

#### configure
triggerfile = open(triggerfilepath,"w")
#normtag="/afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json"
#goldenjson="/afs/cern.ch/user/j/jalmond/POSTDOC/Analysis/General/Lumi/Bril/jsonfiles/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt"


triggerfile.write("### Config \n")
os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + " > golden_BG.txt")              
print "brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson


triggerfile.write("### Period B--G ")
triggerfile.write("### brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + "\n")


read_json_lumi_split = open("golden_BG.txt","r")
CheckLumi=False
lumi_total=0.
for line in read_json_lumi_split:
       if "#Summary" in line:
           CheckLumi=True
       if CheckLumi:
           splitlumi = line.split()
           if not "nls" in line:
               if len(splitlumi) == 13:
                   lumi_total+=float(splitlumi[11])
             
print "Lumi  = " + str(lumi_total)

triggerfile.write("Lumi = " + str(lumi_total) + "\n")

os.system("rm golden_BG.txt")


for trig in trigger_list:
       print "brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson 
       os.system("brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson + " > goldentrig.log" )
       
       read_golden_trig = open("goldentrig.log","r")
       
       Check=False
       trig_lumi=0.
       
       for line in read_golden_trig:
              if "#Summary" in line:
                  Check=True
              if Check:
                     if trig in line:
                            splittrig = line.split()
                            trig_lumi+=float(splittrig[11])
                            
                            
       print trig + " " + str(trig_lumi)
       triggerfile.write(trig + " " + str(trig_lumi) + "\n")
    

os.system("rm goldentrig.log")

for trig in el_trigger_list:
       print "brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson
       #os.system("brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson)
       os.system("brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson + " > elgoldentrig.log" )

       read_golden_trig = open("elgoldentrig.log","r")

       Check=False
       trig_lumi=0.

       for line in read_golden_trig:
              if "#Summary" in line:
                  Check=True
              if Check:
                     if trig in line:
                            splittrig = line.split()
                            trig_lumi+=float(splittrig[11])

       print trig   + " " + str(trig_lumi)
       triggerfile.write(trig + " " + str(trig_lumi) + "\n")
       


triggerfile.write("END")
triggerfile.close()

os.system("rm elgoldentrig.log")
