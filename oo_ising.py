from ising_class import *
Temp=2.3              #Temperature
n=20                       # Sites per edge for n x n system
ntrials=500000     # Number Trials
nequil=100000     #Equilibration steps

ising1=ising(Temp,n)
ising1.randomize()

ising1.trials(nequil)
ising1.resetprops()

for i in range (ntrials):
    ising1.trial()
    ising1.addprops()

ising1.calcprops()
ising1.printsys()
