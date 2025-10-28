import os,sys
from ROOT import *
from math import *

def formatHist(hist):
    hist.SetTitle("")
    hist.SetStats(0)
    hist.GetXaxis().SetLabelSize(0)    
    hist.GetXaxis().SetTitleSize(0)    
    hist.SetAxisRange(1200,5500,"x")   

def gPadSetup(logy):
    if logy == 1:
        gPad.SetLogy(1)
    if logy == 2:
        gPad.SetLogx(1)
    if logy == 3:
        gPad.SetLogy(1)
        gPad.SetLogx(1)
    gPad.SetTopMargin(0.05)
    gPad.SetBottomMargin(0.0)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.09)

inf = TFile("fit_cl.root")
outf = TFile("fitPlots_cl.root", "RECREATE")

bkgHist = inf.Get("h_mjj_12_yStarCut_is_cl").Clone()
fitHist = inf.Get("hist").Clone()
sigHist = inf.Get("sig").Clone()
formatHist(bkgHist)
formatHist(fitHist)
formatHist(sigHist)

outf.cd()

canvas = TCanvas("mc23d_cc","mc23d_cc",10,10,600,600)
canvas.SetFillStyle(0)
canvas.Divide(1,2)
canvas.cd(1)
gPadSetup(1)
gPad.SetPad(0,0.3,1,1)
gPad.SetMargin(0.15,0.0,0.01,0.07)
gPad.SetFillStyle(0)
gPad.Update()
gPad.Draw()
canvas.cd(2)
gPad.SetPad(0,0.05,1,0.3)
gPad.SetMargin(0.15,0.1,0,0.00)
gPad.SetFillStyle(0)
gPad.SetGridy(1)
gPad.Update()
gPad.Draw()

canvas.cd(1)
gPadSetup(1)
    
legend = TLegend(0.6, 0.7, 0.9, 0.93)
legend.SetBorderSize(0)
legend.SetTextFont(42)
legend.SetFillColor(0)
legend.SetTextSize(0.03)
legend.SetFillStyle(0)
 
canvas.cd(1)
bkgHist.SetLineColor(13)
bkgHist.SetLineWidth(4)
bkgHist.SetLineStyle(9)
bkgHist.GetYaxis().SetTitle("Events")
bkgHist.GetYaxis().SetTitleSize(0.04)
bkgHist.Draw("p")
fitHist.SetLineColor(46)
fitHist.SetLineWidth(4)
fitHist.SetLineStyle(9)
fitHist.Draw("histo same")
bkgHist.GetYaxis().Draw("same")

legend.AddEntry(bkgHist,"multijet cl-tagged","l")
legend.AddEntry(fitHist,"5-par fit","l")

legend.Draw("same")

canvas.cd(2)
gPadSetup(0)
gPad.SetBottomMargin(0.25)
gPad.SetTopMargin(0.00)
 
sigHist.SetLineColor(9)
sigHist.SetLineWidth(4)
sigHist.SetLineStyle(1)
sigHist.SetFillColor(9)
sigHist.GetYaxis().SetTitleSize(0.12)
sigHist.GetYaxis().SetTitleOffset(0.35)
sigHist.GetYaxis().SetLabelSize(0.1)
sigHist.GetYaxis().SetTitle("Significance")
sigHist.GetXaxis().SetTitle("m_{jj} [GeV]")
sigHist.GetXaxis().SetTitleSize(0.12)
sigHist.GetXaxis().SetLabelSize(0.1)
sigHist.Draw("histo")

canvas.cd(1)
bkgHist.GetYaxis().Draw("same")
canvas.cd(2)
sigHist.GetYaxis().Draw("same")
sigHist.GetXaxis().Draw("same")

gPad.Update()
gPad.Modified()
gPad.RedrawAxis()
outf.cd()
canvas.Write()
