import os,sys,re
from array import array
from ROOT import *
from ctypes import *
import math

outf = TFile("fit_cl.root","RECREATE")

def Global(x,par):
  z = x[0]/13600.0
  value = par[0]*math.pow(1-z, par[1])*math.pow(z, par[2] + par[3]*math.log(z) + par[4]*math.pow(math.log(z) ,2))
  return value

def Global_6par(x,par):
  z = x[0]/13600.0
  value = par[0]*math.pow(1-z, par[1])*math.pow(z, par[2] + par[3]*math.log(z) + par[4]*math.pow(math.log(z) ,2) + par[5]*math.pow(math.log(z) ,3))
  return value

Fitting = TF1("Global",Global_6par,1200,5500,6)
Fitting.SetParName(0, "norm")
Fitting.SetParName(1, "p1")
Fitting.SetParName(2, "p2")
Fitting.SetParName(3, "p3")
Fitting.SetParName(4, "p4")
Fitting.SetParName(5, "p5")
#Fitting.SetParameter(0, 91283)
#Fitting.SetParameter(0, 10057)
#Fitting.SetParameter(0, 42865)
#Fitting.SetParameter(0, 313506)
Fitting.SetParameter(0, 1354374)
Fitting.SetParameter(1, 5)
Fitting.SetParameter(2, 10)
Fitting.SetParameter(3, 0.5)
Fitting.SetParameter(4, -0.05)
Fitting.SetParameter(5, -0.005)
#Fitting.SetParLimits(0, 90000, 91283)
#Fitting.SetParLimits(0, 10000, 10057)
#Fitting.SetParLimits(0, 55000, 42865)
#Fitting.SetParLimits(0, 300000, 313506)
Fitting.SetParLimits(0, 1300000, 1354374)

thisFitter = ROOT.Fit.Fitter()
thisFitter.Config().MinimizerOptions().SetMinimizerType("Minuit2")
thisFitter.Config().MinimizerOptions().SetMinimizerAlgorithm("Minimize")
thisFitter.Config().MinimizerOptions().SetMaxIterations(100000000)
thisFitter.Config().MinimizerOptions().SetMaxFunctionCalls(10000000)
thisFitter.Config().MinimizerOptions().SetDefaultMaxFunctionCalls(10000000)
thisFitter.Config().MinimizerOptions().SetPrintLevel(0)
thisFitter.Config().MinimizerOptions().SetTolerance(1) #minimize tolerance to reach EDM, 1 = 1e-3

inf = TFile("pseudoData.root")
hist = inf.Get("h_mjj_12_yStarCut_is_cl").Clone()
bkgHist = hist.Clone()
bkgHist.SetName("hist")
sigHist = hist.Clone()
sigHist.SetName("sig")
sigHist.GetXaxis().SetTitle("m_{jj} [GeV]")
sigHist.GetYaxis().SetTitle("Significance")

status = hist.Fit("Global", "IMSL", "",1200,5500)
for binNum in range(bkgHist.GetXaxis().FindBin(1200), bkgHist.GetXaxis().FindBin(5500)):
  count = Fitting.Integral(bkgHist.GetBinLowEdge(binNum), bkgHist.GetBinLowEdge(binNum) + bkgHist.GetBinWidth(binNum))/bkgHist.GetBinWidth(binNum)
  bkgHist.SetBinContent(binNum, count)
  if hist.GetBinContent(binNum):
    sigHist.SetBinContent(binNum, (hist.GetBinContent(binNum) - count)/math.sqrt(hist.GetBinContent(binNum)))
  else:
    sigHist.SetBinContent(binNum, 0)
  sigHist.SetBinError(binNum, 0)

outf.cd()
hist.Write()
bkgHist.Write()
sigHist.Write()
