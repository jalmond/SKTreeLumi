import os, sys

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
                "HLT_IsoMu20_v",
                "HLT_IsoTkMu20_v",
                "HLT_IsoMu22_v",
                "HLT_IsoTkMu22_v",
                "HLT_Mu17_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v",
                "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v",
                "HLT_TripleMu_12_10_5_v",
                "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v"]                


el_trigger_list = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
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
                   "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v"]


#### configure
lumifile = open("triggers_catversion2016_801.txt","w")
normtag="/afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json"

goldenjson="/afs/cern.ch/user/j/jalmond/POSTDOC/Analysis/General/Lumi/Bril/jsonfiles/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt"


lumifile.write("### Config \n")
os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + " > golden_BE.txt")              
print "brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson


lumifile.write("### Period B--E ")
lumifile.write("### brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + "\n")


read_json_lumi_split = open("golden_BE.txt","r")
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

lumifile.write("Lumi = " + str(lumi_total) + "\n")





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
       lumifile.write(trig + " " + str(trig_lumi) + "\n")
    


for trig in el_trigger_list:
       print "brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson
       os.system("brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson)
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
       lumifile.write(trig + " " + str(trig_lumi) + "\n")
       


lumifile.write("END")
lumifile.close()
