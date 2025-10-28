import ROOT as r
from math import *

f_in = r.TFile("basicSel_pythia_dijet_mc23d_histograms.root","r+w")
f_out = r.TFile("pseudoData.root","RECREATE")

hist_cc = f_in.Get("h_mjj_12_yStarCut_is_cc").Clone()
for i in range(1,hist_cc.GetNbinsX()+1):
  hist_cc.SetBinContent(i, int(hist_cc.GetBinContent(i)))
  hist_cc.SetBinError(i, sqrt(int(hist_cc.GetBinContent(i))))

print(hist_cc.Integral(hist_cc.GetXaxis().FindBin(1200), hist_cc.GetXaxis().FindBin(4500)))

hist_bb = f_in.Get("h_mjj_12_yStarCut_is_bb").Clone()
for i in range(1,hist_bb.GetNbinsX()+1):
  hist_bb.SetBinContent(i, int(hist_bb.GetBinContent(i)))
  hist_bb.SetBinError(i, sqrt(int(hist_bb.GetBinContent(i))))

print(hist_bb.Integral(hist_bb.GetXaxis().FindBin(1200), hist_bb.GetXaxis().FindBin(3500)))

hist_bc = f_in.Get("h_mjj_12_yStarCut_is_bc").Clone()
for i in range(1,hist_bc.GetNbinsX()+1):
  hist_bc.SetBinContent(i, int(hist_bc.GetBinContent(i)))
  hist_bc.SetBinError(i, sqrt(int(hist_bc.GetBinContent(i))))

print(hist_bc.Integral(hist_bc.GetXaxis().FindBin(1200), hist_bc.GetXaxis().FindBin(4000)))

hist_bl = f_in.Get("h_mjj_12_yStarCut_is_bl").Clone()
for i in range(1,hist_bl.GetNbinsX()+1):
  hist_bl.SetBinContent(i, int(hist_bl.GetBinContent(i)))
  hist_bl.SetBinError(i, sqrt(int(hist_bl.GetBinContent(i))))

print(hist_bl.Integral(hist_bl.GetXaxis().FindBin(1200), hist_bl.GetXaxis().FindBin(5000)))

hist_cl = f_in.Get("h_mjj_12_yStarCut_is_cl").Clone()
for i in range(1,hist_cl.GetNbinsX()+1):
  hist_cl.SetBinContent(i, int(hist_cl.GetBinContent(i)))
  hist_cl.SetBinError(i, sqrt(int(hist_cl.GetBinContent(i))))

print(hist_cl.Integral(hist_cl.GetXaxis().FindBin(1200), hist_cl.GetXaxis().FindBin(5500)))

f_out.cd()
hist_cc.Write()
hist_bb.Write()
hist_bc.Write()
hist_bl.Write()
hist_cl.Write()
f_out.Close()
f_in.Close()
