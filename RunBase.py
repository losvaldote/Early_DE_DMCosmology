#Add paths, we want to be able to run in either root or Run/
import sys,os
#print sys.path
sys.path=["py","../py","models"]+sys.path


#Cosmologies
from LCDMCosmology import *
from oLCDMCosmology import *
from wLCDMCosmology import *
from PolyCDMCosmology import *
from owa0CDMCosmology import *
from JordiCDMCosmology import *
from WeirdCDMCosmology import *
from TiredLightDecorator import *
from SplineLCDMCosmology import *
from DecayLCDMCosmology import *
from StepCDMCosmology import *
from EarlyDECosmology import *
from SlowRDECosmology import *
#from QuintCosmology_try import *
from wDMCosmology import *
from OzcosCosmology import *
from owa0CDMCosmology_modified import *  #Aqui se agrega el modelo modificado.
from EKCDMCosmology import *             #Nuevo modelo.
from Early_DE_DMCosmology import *       #Nuevo modelo.

#Like modules
from BAOLikelihoods import *
from SimpleCMB import *
from CompressedSNLikelihood import *
from HubbleParameterLikelihood import *

#Composite Likelihood
from CompositeLikelihood import *

#Likelihood Multiplier
from LikelihoodMultiplier import *

#Analyzers
from MaxLikeAnalyzer import *
from MCMCAnalyzer import *


## String parser Aux routines
model_list="LCDOM, LCDMasslessnu, nuLCDM, NeffLCDM, noradLCDM, nuoLCDM, nuwLCDM, oLCDM, wCDM, waCDM, owCDM,"\
           "owaCDM, JordiCDM, WeirdCDM, TLight, StepCDM, Spline, PolyCDM, fPolyCDM, Decay, Decay01, Decay05,"\
           "EarlyDE, EarlyDE_rd_DE, SlowRDE, owaCDM_modified" #Se agrega el modelo modificado

def ParseModel(model):
    if model=="LCDM":
        T=LCDMCosmology()
    elif model=="LCDMmasslessnu":
        T=LCDMCosmology(mnu=0)
    elif model=="nuLCDM":
        T=LCDMCosmology()
        T.setVaryMnu()
    elif model=="NeffLCDM":
        LCDMCosmology.rd_approx="CuestaNeff"
        T=LCDMCosmology()
        T.setVaryNnu()
    elif model=="noradLCDM":
        T=LCDMCosmology(disable_radiation=True)
    elif model=="oLCDM":
        T=oLCDMCosmology()
    elif model=="nuoLCDM":
        T=oLCDMCosmology()
        T.setVaryMnu()
    elif model=="wCDM":
        T=wLCDMCosmology()
    elif model=="nuwCDM":
        T=wLCDMCosmology()
        T.setVaryMnu()
    elif model=="waCDM":
        T=owa0CDMCosmology(varyOk=False)
    elif model=="owCDM":
        T=owa0CDMCosmology(varywa=False)
    elif model=="owaCDM":
        T=owa0CDMCosmology()
    elif model=='FCDM':
        T=OzcosCosmology()
    elif model=="JordiCDM":
        T=JordiCDMCosmology()
    elif model=="WeirdCDM":
        T=WeirdCDMCosmology()
    elif model=="TLight":
        T=TiredLightDecorator(PolyCDMCosmology())
    elif model=="StepCDM":
        T=StepCDMCosmology()
    elif model=="Spline":
        T=SplineLCDMCosmology()
    elif model=="DecayFrac":
        T=DecayLCDMCosmology() 
    elif model=="Decay":
        T=DecayLCDMCosmology(varyxfrac=False) 
    elif model=="Decay01":
        T=DecayLCDMCosmology(varyxfrac=False,xfrac=0.1) 
    elif model=="Decay05":
        T=DecayLCDMCosmology(varyxfrac=False,xfrac=0.5) 
    elif model=="PolyCDM":
        T=PolyCDMCosmology()
    elif model=="fPolyCDM":
        T=PolyCDMCosmology(varyOk=False)
    elif model=="EarlyDE":
        T=EarlyDECosmology(varyw=False,userd_DE=False)
    elif model=="EarlyDE_rd_DE":
        T=EarlyDECosmology(varyw=False)
    elif model=="SlowRDE":
        T=SlowRDECosmology(varyOk=False)
    elif model=="Quint":
        T=QuintCosmology()
    elif model=='wDM':
        T=wDMCosmology()
    elif model=='owaCDM_modified': #Se agrego el modificado
	T=owa0CDMCosmology_modified()
    elif model=='EKCDM1':
	T=EKCDMCosmology(varywa=False)
    elif model=='EKCDM2':
	T=EKCDMCosmology()
    elif model=='Early_DE_DM1':
	T=Early_DE_DMCosmology(userd_DE=False)
    else:
        print "Cannot recognize model", model
        sys.exit(1)

    return T

data_list="BBAO, GBAO, GBAO_no6dF, CMASS, LBAO, LaBAO, LxBAO, MGS, Planck, WMAP, PlRd, WRd, PlDa, PlRdx10,"\
          "CMBW, SN, SNx10, UnionSN, RiessH0, 6dFGS"


def ParseDataset(datasets):
    dlist=datasets.split('+')
    L=CompositeLikelihood([])
    for name in dlist:
        if name=='BBAO':
            L.addLikelihoods([
            DR11LOWZ(),
            DR11CMASS(),
            DR11LyaAuto(),
            DR11LyaCross(),
            SixdFGS(),
            SDSSMGS()
            ])
        elif name=='GBAO':
            L.addLikelihoods([
            DR11LOWZ(),
            DR11CMASS(),
            SixdFGS(),
            SDSSMGS()    
            ])
        elif name=='GBAOx10':
            L.addLikelihoods([
            LikelihoodMultiplier(DR11LOWZ(),100.0),
            LikelihoodMultiplier(DR11CMASS(),100.0),
            LikelihoodMultiplier(SixdFGS(),100.0)
            ])
        elif name=='GBAO_no6dF':
            L.addLikelihoods([
            DR11LOWZ(),
            DR11CMASS()
            ])
        elif name=='CMASS':
            L.addLikelihoods([
            DR11CMASS()
            ])
        elif name=='LBAO':
            L.addLikelihoods([
            DR11LyaAuto(),
            DR11LyaCross()
            ])
        elif name=='LaBAO':
            L.addLikelihoods([
            DR11LyaAuto(),
            ])
        elif name=='LxBAO':
            L.addLikelihoods([
            DR11LyaCross(),
            ])
        elif name=="MGS":
            L.addLikelihood(SDSSMGS())
        elif name=='Planck':
            L.addLikelihood(PlanckLikelihood())
        elif name=='Planck_15':
            L.addLikelihood(PlanckLikelihood_15())
        elif name=='WMAP':
            L.addLikelihood(WMAP9Likelihood())
        elif name=='PlRd':
            L.addLikelihood(PlanckLikelihood(kill_Da=True))
        elif name=='WRd':
            L.addLikelihood(WMAP9Likelihood(kill_Da=True))
        elif name=='PlDa':
            L.addLikelihood(PlanckLikelihood(kill_rd=True))
        elif name=='PlRdx10':
            L.addLikelihood(LikelihoodMultiplier(PlanckLikelihood(kill_Da=True),100.0))
        elif name=='CMBW':
            L.addLikelihood(WMAP9Likelihood())
        elif name=='SN':
            L.addLikelihood(BetouleSN())
        elif name=='SNx10':
            L.addLikelihood(LikelihoodMultiplier(BetouleSN(),100.0))
        elif name=='UnionSN':
            L.addLikelihood(UnionSN())
        elif name=='RiessH0':
            L.addLikelihood(RiessH0())
        elif name=='6dFGS':
            L.addLikelihood(SixdFGS())
        elif name=='ACPNS_1':       #DR12 -test
            L.addLikelihood(ACPNS_1())
        elif name=='ACPNS_3':
            L.addLikelihood(ACPNS_3())
        elif name=='ACPNS':
            L.addLikelihoods([
            ACPNS_1(), ACPNS_3()
            ])
        elif name=='CombBAOzb1':    #Combine BAO DR12
            L.addLikelihood(CombBAOzb1())
        elif name=='CombBAOzb2':
            L.addLikelihood(CombBAOzb2())
        elif name=='CombBAOzb3':
            L.addLikelihood(CombBAOzb3())
        elif name=='CombBAOzball':
            L.addLikelihoods([
            CombBAOzb1(), CombBAOzb2(), CombBAOzb3()
            ])
        else:
            print "Cannot parse data, unrecognizable part:", name
            sys.exit(1)

    return L

