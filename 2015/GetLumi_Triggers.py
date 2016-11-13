import os
trigger_list = ["HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_" ,
                "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v",
                "HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele23_WPLoose_Gsf_v",
                "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v",
                "HLT_Mu17_Mu8_DZ_v",
                "HLT_Mu17_Mu8_SameSign_DZ_v",
                "HLT_Mu20_Mu10_SameSign_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v",
                "HLT_Mu8_v",
                "HLT_Mu17_v",
                "HLT_Mu20_v",
                "HLT_IsoMu20_v",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v",
                "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v",
                "HLT_TripleMu_12_10_5",
                "HLT_DiMu9_Ele9_CaloIdL_TrackIdL"]                


normtag="/afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json"

goldenjson="/afs/cern.ch/user/j/jalmond/POSTDOC/Analysis/General/Lumi/Bril/jsonfiles/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt"



os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + " > golden.txt")              
print "brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson 

read_json_lumi_split = open("golden.txt","r")
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


read_json_lumi2_split = open("golden.txt","r")
CheckLumi2=False
for line in read_json_lumi2_split:
    
    if "run:fill" in line:
        CheckLumi2=True
    if "#Summary" in line:
        CheckLumi2=True
    if CheckLumi2:
            splitlumi = line.split()
            if not "run:fill":
                if len(splitlumi) == 13:
                    lumi_subtotal+=float(splitlumi[12])
                    print splitlumi[12]  +  " : " + str(lumi_subtotal)
                    
                    

for trig in trigger_list:
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
                
    Check=False            

                
    if "trig" == "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v":
        print "  /// Electron triggers "
        print "  // Double Electron   "
    if "trig" == "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v":
        print " "
        print "    // Single Electon "
    if "trig" == "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v":
        print " "
        print "   // TriLepton Electron "
        
    if "trig" == "HLT_Mu17_Mu8_DZ_v":
        print " "
        print "   /// Muon Triggers"
        print "    // Double Muon"
    if "trig" == "HLT_Mu8_v":
        print "    // single muon "
    if "trig" == "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v":
        print " "
        print "   /// multilepton"

    print 'else if(triggername.Contains("'+ trig + '")) return (('+ str(trig_lumi) +')/tlumi);'
