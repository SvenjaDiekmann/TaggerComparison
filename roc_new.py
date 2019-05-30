
import numpy as np
import ROOT
from sklearn import metrics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import rc


#Hbb
chain = ROOT.TChain("btaganaFatJets/ttree")
#1000
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1000_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1000_narr_Apr03-19/190403_125037/0000/"+i)
print("Hbb 1000 done!")

#1200
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1200_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1200_narr_Apr03-19/190403_125104/0000/"+i)
#failed
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1200_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1200_narr_Apr03-19/190403_125104/0000/failed/"+i)
print("Hbb 1200 done!")

#1250
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1250_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1250_narr_Apr03-19/190403_125130/0000/"+i)
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1250_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1250_narr_Apr03-19/190403_125130/0000/failed/JetTree_mc_FatJets_1.root")
print("Hbb 1250 done!")

#1400
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1400_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1400_narr_Apr03-19/190403_125153/0000/JetTree_mc_FatJets_3.root")
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1400_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1400_narr_Apr03-19/190403_125153/0000/failed/"+i)
print("Hbb 1400 done!")

#1500
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1500_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1500_narr_Apr03-19/190403_125214/0000/JetTree_mc_FatJets_2.root")
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1500_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1500_narr_Apr03-19/190403_125214/0000/failed/JetTree_mc_FatJets_1.root")
print("Hbb 1500 done!")

#1600
list="JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1600_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1600_narr_Apr03-19/190403_125245/0000/"+i)
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1600_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1600_narr_Apr03-19/190403_125245/0000/failed/JetTree_mc_FatJets_2.root")
print("Hbb 1600 done!")

#1750
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1750_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1750_narr_Apr03-19/190403_125312/0000/"+i)
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1750_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1750_narr_Apr03-19/190403_125312/0000/failed/JetTree_mc_FatJets_4.root")
print("Hbb 1750 done!")

#1800
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1800_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1800_narr_Apr03-19/190403_125332/0000/"+i)
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-1800_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-1800_narr_Apr03-19/190403_125332/0000/failed/JetTree_mc_FatJets_4.root")
print("Hbb 1800 done!")

#2000
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-2000_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-2000_narrow_13TeV-madgraph_correctedcfg_RunIIFall/190322_141937/0000/failed/JetTree_mc_FatJets_1.root")
print("Hbb 2000 done!")

#2500
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-2500_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-2500_narrow_13TeV-madgraph_correctedcfg_RunIIFall/190322_142027/0000/")
print("Hbb 2500 done!")

#250
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-250_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-250_narro_Apr03-19/190403_125442/0000/"+i)
print("Hbb 250 done!")

#260
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-260_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-260_narro_Apr03-19/190403_125509/0000/failed/"+i)
print("Hbb 260 done!")

#270
list="JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-270_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-270_narro_Apr03-19/190403_125529/0000/"+i)
print("Hbb 270 done!")

#280
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-280_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-280_narro_Apr03-19/190403_125548/0000/"+i)
print("Hbb 280 done!")

#290
list="JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-290_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-290_narro_Apr03-19/190403_125625/0000/"+i)
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-290_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-290_narro_Apr03-19/190403_125625/0000/failed/"+i)
print("Hbb 290 done!")

#3000
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-3000_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-3000_narr_Apr03-19/190403_125645/0000/JetTree_mc_FatJets_1.root")
print("Hbb 3000 done!")

#300
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-300_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-300_narro_Apr03-19/190403_125706/0000/failed/"+i)
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-300_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-300_narro_Apr03-19/190403_125706/0000/JetTree_mc_FatJets_4.root")
print("Hbb 3000 done!")

#320
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-320_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-320_narro_Apr03-19/190403_125730/0000/JetTree_mc_FatJets_3.root")
print("Hbb 320 done!")

#3500
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-3500_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-3500_narr_Apr03-19/190403_125749/0000/"+i)
print("Hbb 3500 done!")

#350
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-350_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-350_narro_Apr03-19/190403_125809/0000/JetTree_mc_FatJets_3.root")
print("Hbb 350 done!")

#4000
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-4000_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-4000_narr_Apr03-19/190403_125834/0000/"+i)
print("Hbb 4000 done!")

#400
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-400_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-400_narro_Apr03-19/190403_125855/0000/JetTree_mc_FatJets_1.root")
print("Hbb 400 done!")

#4500
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-4500_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-4500_narr_Apr03-19/190403_125914/0000/"+i)
print("Hbb 4500 done!")

#450
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_5.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-450_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-450_narro_Apr03-19/190403_125938/0000/"+i)
print("Hbb 450 done!")

#500
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_3.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-500_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-500_narro_Apr03-19/190403_125959/0000/"+i)
print("Hbb 500 done!")

#550
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-550_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-550_narro_Apr03-19/190403_130018/0000/JetTree_mc_FatJets_3.root")
print("Hbb 550 done!")

#600
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-600_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-600_narro_Apr03-19/190403_130045/0000/JetTree_mc_FatJets_3.root")
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-600_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-600_narro_Apr03-19/190403_130045/0000/failed/"+i)
print("Hbb 600 done!")

#650
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-650_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-650_narrow_13TeV-madgraph_correctedcfg_RunIIFall1/190322_143132/0000/failed/JetTree_mc_FatJets_1.root")
print("Hbb 650 done!")

#700
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-700_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-700_narro_Apr03-19/190403_130131/0000/"+i)
print("Hbb 700 done!")

#750
list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-750_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-750_narro_Apr03-19/190403_130156/0000/"+i)
print("Hbb 750 done!")

#800
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-800_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-800_narro_Apr03-19/190403_130217/0000/JetTree_mc_FatJets_3.root")
chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-800_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-800_narro_Apr03-19/190403_130217/0000/failed/JetTree_mc_FatJets_1.root")
print("Hbb 800 done!")

#850
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-850_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-850_narro_Apr03-19/190403_130235/0000/"+i)
print("Hbb 850 done!")

#900
list="JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_4.root".split(',')
for i in list:
    chain.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/GluGluToBulkGravitonToHHTo4B_M-900_narrow_13TeV-madgraph_correctedcfg/GluGlu_oBulkGravitonToHHTo4B_M-900_narro_Apr03-19/190403_130258/0000/"+i)
print("Hbb 900 done!")

#QCD
chain1 = ROOT.TChain("btaganaFatJets/ttree")
#300-470
chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/QCD_Pt_300to470_TuneCP5_13TeV_pythia8_Apr03-19/190403_130319/0000/failed/JetTree_mc_FatJets_179.root")
print("QCD 300-470 done!")

#470-600
for i in range(1,70):
    if i in [2,5,7,9,14,15,17,26,27,29,30,31,34,37,38,40,41,47,52,54,57,60,61,66,67,70,71,72,78,80,87,90]:
        continue
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/QCD_Pt_470to600_TuneCP5_13TeV_pythia8_Apr03-19/190403_130338/0000/failed/JetTree_mc_FatJets_"+str(i)+".root")
print("QCD 470-600 done!")

#600-800
list="JetTree_mc_FatJets_103.root,JetTree_mc_FatJets_106.root,JetTree_mc_FatJets_109.root,JetTree_mc_FatJets_116.root,JetTree_mc_FatJets_122.root,JetTree_mc_FatJets_123.root,JetTree_mc_FatJets_126.root,JetTree_mc_FatJets_131.root,JetTree_mc_FatJets_133.root,JetTree_mc_FatJets_134.root,JetTree_mc_FatJets_135.root,JetTree_mc_FatJets_141.root,JetTree_mc_FatJets_145.root,JetTree_mc_FatJets_149.root,JetTree_mc_FatJets_151.root,JetTree_mc_FatJets_163.root,JetTree_mc_FatJets_165.root,JetTree_mc_FatJets_168.root,JetTree_mc_FatJets_172.root,JetTree_mc_FatJets_176.root,JetTree_mc_FatJets_179.root,JetTree_mc_FatJets_184.root,JetTree_mc_FatJets_188.root,JetTree_mc_FatJets_189.root,JetTree_mc_FatJets_18.root,JetTree_mc_FatJets_190.root,JetTree_mc_FatJets_192.root,JetTree_mc_FatJets_193.root,JetTree_mc_FatJets_194.root,JetTree_mc_FatJets_195.root,JetTree_mc_FatJets_196.root,JetTree_mc_FatJets_197.root,JetTree_mc_FatJets_198.root,JetTree_mc_FatJets_199.root,JetTree_mc_FatJets_19.root,JetTree_mc_FatJets_200.root,JetTree_mc_FatJets_207.root,JetTree_mc_FatJets_20.root,JetTree_mc_FatJets_213.root,JetTree_mc_FatJets_214.root".split(",")
for i in list:
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/QCD_Pt_600to800_TuneCP5_13TeV_pythia8_Apr03-19/190403_130401/0000/failed/"+i)
print("QCD 600-800 done!")

#800-1000
list="JetTree_mc_FatJets_100.root,JetTree_mc_FatJets_108.root,JetTree_mc_FatJets_114.root,JetTree_mc_FatJets_117.root,JetTree_mc_FatJets_123.root,JetTree_mc_FatJets_14.root,JetTree_mc_FatJets_28.root,JetTree_mc_FatJets_37.root,JetTree_mc_FatJets_39.root,JetTree_mc_FatJets_42.root,JetTree_mc_FatJets_43.root,JetTree_mc_FatJets_44.root,JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_62.root,JetTree_mc_FatJets_68.root,JetTree_mc_FatJets_77.root,JetTree_mc_FatJets_83.root,JetTree_mc_FatJets_8.root,JetTree_mc_FatJets_91.root,JetTree_mc_FatJets_97.root,JetTree_mc_FatJets_98.root".split(",")
for i in list:
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8_Apr03-19/190403_130421/0000/failed/"+i)
print("QCD 800-1000 done!")

#1000-1400
chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8_Apr03-19/190403_130441/0000/failed/JetTree_mc_FatJets_43.root")
print("QCD 1000-1400 done!")

#1400-1800
list="JetTree_mc_FatJets_12.root,JetTree_mc_FatJets_13.root,JetTree_mc_FatJets_15.root,JetTree_mc_FatJets_16.root,JetTree_mc_FatJets_17.root,JetTree_mc_FatJets_18.root,JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_20.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root".split(",")
for i in list:
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8_Apr03-19/190403_130508/0000/failed/"+i)
chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8_Apr03-19/190403_130508/0000/JetTree_mc_FatJets_21.root")
print("QCD 1400-1800 done!")

#1800-2400
list="JetTree_mc_FatJets_10.root,JetTree_mc_FatJets_2.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root,JetTree_mc_FatJets_5.root,JetTree_mc_FatJets_8.root,JetTree_mc_FatJets_9.root".split(",")
for i in list:
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/190322_143916/0000/failed"+i)
print("QCD 1800-2400 done!")

#2400-3200
'''list="JetTree_mc_FatJets_6.root,JetTree_mc_FatJets_8.root".split(",")
for i in list:
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/190322_143938/0000/failed"+i)
print("QCD 2400-3200 done!")'''

#3200-inf
'''list="JetTree_mc_FatJets_1.root,JetTree_mc_FatJets_3.root,JetTree_mc_FatJets_4.root".split(",")
for i in list:
    chain1.AddFile("root://cmsxrootd.fnal.gov///store/user/sdiekman/btag/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/190322_144004/0000/failed"+i)
print("QCD 3200-inf done!")
'''


nb_Had=[]
DoubleSV=[]
DeepDouble=[]
DeepBoosted=[]
jet_pt_H=[]
jet_pt_QCD=[]
#print(tree.GetEntries())
#Hbb
for i in range (0,chain.GetEntries()):
    chain.GetEntry(i)
    n=getattr(chain,"FatJetInfo.nJet")
    if n > 0:
        
        for j in range(n):
            if np.isnan(getattr(chain,"FatJetInfo.Jet_MassIndDeepDoubleBvLHbb")[j])==True:
                print(j,i)
                continue
            jet_pt=getattr(chain,"FatJetInfo.Jet_pt")[j]
            jet_mass=getattr(chain,"FatJetInfo.Jet_mass")[j]
            if jet_pt<300 or jet_pt>2000:
                 continue
            if jet_mass<40 or jet_mass>200:
                 continue
            jet_pt_H.append(jet_pt)
            DoubleSV.append(getattr(chain,"FatJetInfo.Jet_DoubleSV")[j])
            DeepDouble.append(getattr(chain,"FatJetInfo.Jet_MassIndDeepDoubleBvLHbb")[j])
            DeepBoosted.append(getattr(chain,"FatJetInfo.Jet_DeepBoostedJetbbvsLight")[j])
            if getattr(chain,"FatJetInfo.Jet_nbHadrons")[j] >= 2:
                nb_Had.append(1)
            else :
                nb_Had.append(0)
#QCD 
for i in range (0,chain1.GetEntries()):
    chain1.GetEntry(i)
    n=getattr(chain1,"FatJetInfo.nJet")
    if n > 0:
        
        for j in range(n):
            if np.isnan(getattr(chain1,"FatJetInfo.Jet_MassIndDeepDoubleBvLHbb")[j])==True:
                print(j,i)
                continue
            jet_pt=getattr(chain1,"FatJetInfo.Jet_pt")[j]
            jet_mass=getattr(chain1,"FatJetInfo.Jet_mass")[j]
            if jet_pt<300 or jet_pt>2000:
                 continue
            if jet_mass<40 or jet_mass>200:
                 continue
            jet_pt_QCD.append(jet_pt)
            DoubleSV.append(getattr(chain1,"FatJetInfo.Jet_DoubleSV")[j])
            DeepDouble.append(getattr(chain1,"FatJetInfo.Jet_MassIndDeepDoubleBvLHbb")[j])
            DeepBoosted.append(getattr(chain1,"FatJetInfo.Jet_DeepBoostedJetbbvsLight")[j])
            nb_Had.append(0)

nb_Had=np.array(nb_Had)
DoubleSV=np.array(DoubleSV)
DeepDouble=np.array(DeepDouble)
DeepBoosted=np.array(DeepBoosted)
    
fpr, tpr, thresholds = metrics.roc_curve(nb_Had,DoubleSV)
fpr1, tpr1, thresholds1 = metrics.roc_curve(nb_Had,DeepDouble)
fpr2, tpr2, thresholds2 = metrics.roc_curve(nb_Had,DeepBoosted)

plt.figure()
plt.plot(tpr,fpr,label='DoubleB')
plt.plot(tpr1,fpr1,label='DDBvL')
plt.plot(tpr2,fpr2,label='DeepAK8')
plt.xlabel('Efficiency Hbb')
plt.ylabel('misid. probability')
plt.ylim(0.001,1)
plt.legend(loc=0)
plt.yscale("log")
plt.grid()
#plt.savefig('DoubleSV.png')

plt.figure()
plt.hist(jet_pt_H,bins=30,label='Entries='+str(len(jet_pt_H)))
plt.legend(loc=0)
plt.xlabel('Jet_pt')
plt.yscale("log")
plt.savefig('Jet_pt_Hbb_log.png')

plt.figure()
plt.hist(jet_pt_QCD,bins=30,label='Entries='+str(len(jet_pt_QCD)))
plt.legend(loc=0)
plt.xlabel('Jet_pt')
plt.yscale("log")
plt.savefig('Jet_pt_QCD_log.png')

# Native matplitlib font can be done like this: 
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

# Needs to install tex-live to have helvetica and use tex to render labels
rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]  
rc('text', usetex=True)

font_size = 22
rcParams['font.size'] = font_size  # Legend title for example
rcParams['axes.labelsize'] = font_size 
rcParams['xtick.labelsize'] = font_size - 2 
rcParams['ytick.labelsize'] = font_size - 2
rcParams['legend.fontsize'] = font_size - 2
rc('axes', linewidth=2)

# Use seaborn color palette
#import seaborn as sns
#p = sns.color_palette("Paired")
#p = sns.color_palette("muted")
#sns.set_palette(p)
C = ['darkorange', 'steelblue', 'firebrick', 'purple', 'seagreen']

f, ax = plt.subplots(figsize=(10,10))

#ax.plot(x, y1, lw=4, label="Q - tail strikethrough ", c=C[0])
#ax.plot(x, y2, lw=4, label="\& - amepersand has two full loops", c=C[1])
ax.plot(tpr,fpr,lw=4,label='DoubleB', c=C[4])
ax.plot(tpr1,fpr1,lw=4,label='DDBvL', c=C[2])
ax.plot(tpr2,fpr2,lw=4,label='DeepAK8', c=C[1])

ax.set_xlim(0,1)
ax.set_ylim(0.001,1)
ax.set_xlabel(r'Efficiency ($\mathrm{H \rightarrow\ b\bar{b}}$)', ha='right', x=1.0)
ax.set_ylabel('Misidentification Probability (QCD)', ha='right', y=1.0)

# Legend
leg = ax.legend(borderpad=0.5, frameon=False, loc=2,
    title=""+"300"+" $\mathrm{<\ jet\ p_T\ <}$ "+"2000"+" GeV" \
             +"\n "   + "40"+" $\mathrm{<\ jet\ m_{SD}\ <}$ "+"200"+" GeV" \
    )
leg._legend_box.align = "left" # Align legend title

####################### ROOT-like CMS ticks and labels ##############################
# Sets 10 major ticks and 5 minor between each major, calling ax.semilogy() overwrites this.
import matplotlib.ticker as plticker
xl = ax.get_xlim()
ax.xaxis.set_major_locator(plticker.MultipleLocator(base=(xl[-1]-xl[0])/10))
ax.xaxis.set_minor_locator(plticker.MultipleLocator(base=(xl[-1]-xl[0])/50))
yl = ax.get_ylim()
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=(yl[-1]-yl[0])/10))
ax.yaxis.set_minor_locator(plticker.MultipleLocator(base=(yl[-1]-yl[0])/50))
ax.tick_params(direction='in', axis='both', which='major', length=12 )
ax.tick_params(direction='in', axis='both', which='minor', length=6)
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')    
ax.grid(which='minor', alpha=0.4, axis='y', linestyle='dotted')
ax.grid(which='major', alpha=0.8, linestyle='dotted')
ax.annotate(r'{} (13 TeV)'.format("2017"), xy=(1, 1.015), xycoords='axes fraction', fontsize=font_size,  fontname='Helvetica', 
            ha='right', annotation_clip=False)
ax.annotate('$\mathbf{CMS}$', xy=(0.001, 1.015), xycoords='axes fraction', fontname='Helvetica', fontsize=font_size+6,
            ha='left', annotation_clip=False)
ax.annotate('$Simulation\ Preliminary$', xy=(0.12, 1.015), xycoords='axes fraction', fontsize=font_size, fontname='Helvetica',
            fontstyle='italic', ha='left', annotation_clip=False)
##########################################################################



ax.semilogy()
f.savefig('roc_1.png')

    
