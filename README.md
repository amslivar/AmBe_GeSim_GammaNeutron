# AmBe_GeSim_efficiency

AmBe simulations of gammas and neutrons in UA's GeIII detector based on GeSim code by Raymond Tsang. Read https://github.com/rhmtsang/GeSim/blob/master/README.md for more information about GeSim. 

Prerequisite: Geant 4.10.04.p02 and ROOT 5.34/07 (later versions are ok)

Current author: Ana Maria Slivar, anamaria.sslivar@gmail.com 
Original author of AmBe_GeSim_efficiency: Mariia Fedkevych, mariia.fedkevych@gmail.com 


1. Source setup scripts for Geant4, e.g.

```
source /usr/local/geant4.10.04.p02/bin/geant4.sh
source /usr/local/geant4.10.04.p02/share/Geant4-10.4.2/geant4make/geant4make.sh
```

2. Go to the GeSim_AmBe_efficiency folder and run `cmake .`:
3. Compile with `make -f Makefile`
4. Before starting the simulations, run `export AllowForHeavyElements=1`
5. The simulations can be executed by running `./GeSim AmBe.mac`
    - depending on the geometry you want to use, you will need to replace the content of src/gesimPrimaryGeneratorAction.cc with the content of
        - gesimPrimaryGeneratorAction.cc_no_outer_W_remote for simulations of AmBe source without the outer tungsten capsule in remote position at GeIII,
        - gesimPrimaryGeneratorAction.cc_with_outer_W_remote for simulations of AmBe source in the outer tungsten capsule in remote position at GeIII,
        - gesimPrimaryGeneratorAction.cc_with_outer_W_on_endcap for simulations of AmBe source in the outer tungsten capsule centered on the endcap face of GeIII
        - gesimPrimaryGeneratorAction.cc_oneE for only one energy peak 
        - gesimPrimaryGeneratorAction.cc for a spectrum of energies, created from step 6 in AmBe_emergent_gammas 
        - gesimPrimaryGeneratorAction.cc_neutronsandgammas considers the different neutron spectras, the 4.4 MeV gamma, and the Am-241 gammas
          -  If using this version, you need to first create the events usingPrepare an HEPEvt format generator file for AmBe gamma spectrum (from the  `particle.spectrum` under the data folder) which will be read by gesimPrimaryGeneratorAction: 
            - make an executable of energyspectrum.cc, e.g. run
            ```bash
            g++ energyspectrum.cc -o energyspectrum.exe
            ```
            - run the executable with the number of events to be generated and the output file name "generator.data", e.g.
            ```bash
            ./energyspectrum.exe 10000000 > generator.data
            ```   
      
      and indicate the correct geometry name in the "AmBe.mac" file in "/gesim/source/setSourcePosition": 
        - LZAmBe2Remote for simulations of AmBe source without the outer tungsten capsule in remote position at GeIII,
        - LZAmBe2inOuterWCapsuleRemote for simulations of AmBe source in the outer tungsten capsule in remote position at GeIII,
        - LZAmBe2inOuterWCapsuleEndcap for simulations of AmBe source in the outer tungsten capsule centered on the endcap face of GeIII.
    - energy of primary gammas can be changed in src/gesimPrimaryGeneratorAction.cc
    - when you need to switch between geometries, or change generated gamma energy in gesimPrimaryGeneratorAction.cc etc, you will need to re-make by running `make clean` and then `make`
    - if you log out, make sure that steps 2 and 5 are execured before rtrying to run simulations again
6. The output root file containing energy distributions of primary and detected gammas will be generated within the same folder (the name is set in AmBe.mac). 
7. If you didn't comment out the visualization options in AmBe.mac, it will generate .wrl file in the same folder. 
8. To visualize origins of the primary gammas, copy the content of Particle_position_VRML.txt produced during the simulation at the end of the .wrl file. Example .wrl files which visualize all 3 geometries are contained within "geometry_vis_example" subfolder


For more info on the neutron and gamma energies, refer to https://gitlab.com/luxzeplin/sim/baccarat/-/blob/master/generator/src/BaccGeneratorAmBeSOURCES4A.cc , quoted below: 

*/
////////////////////////////////////////////////////////////////////////////////

//
//   General notes on this generator
//
/*

DISCLAIMER:
This altenative AmBe generator is
based on neutron energy spectra obtained by SOURCES4A software.

The standard AmBe generator has cutoffs in neutron energy for
each neutron group, namely n0, n1 and n2. (Note that the indices
indicate how many gammas are produced during neutron emission.)
In reality, one does not expect that to occur. Using the binned neutron energy
spectra obtained by SOURCES4A and the Python 1D interpolator, smooth and
continuous neutron energy spectra were derived.

The neutron spectra of standard AmBe generator and those of SOURCES4A
were compared at https://gitlab.com/luxzeplin/sim/BACCARAT/issues/270
Please follow the link for a slightly longer discussion.

SOURCES4A calculates the relative probabilities to be 27%, 62.7% and 10.3% for n0, n1 and n2 groups, respectively.
Note that the contribution from the break-up neutrons as a result
of inelastic alpha scatterings on Be nucleus (E_n < 0.5 MeV) is negligible.
These probabilities agree with the ones referred by the paper, https://www.sciencedirect.com/science/article/pii/0029554X73901997
Nuclear Instruments and Methods, Volume 111, Issue 3, 1 September 1973, Pages 435-440
Besides, n1(with 4.4 MeV)/(n0+n1+n2) was measured to be ~60% in literature (i.e, Applied Radiation and Isotopes 65 (2007) 1318–1321
and Applied Radiation and Isotopes 60 (2004) 959–962). So, it all sounds reasonable.
In the standard generator, n2 probability is overestimated (about 16%).

For the tagging purposes, n1 state is the main interest, though n2 state is particularly interesting as
the most neutrons have energies lower than 2.45 MeV (DD neutrons) and n0
state might interest the high energy NR people (6 MeV < E_n < 11 MeV).

The gamma energies were taken from the NuDat data base at
http://www.nndc.bnl.gov/nudat2/getdataset.jsp?nucleus=12C&unc=nds
In state 1, the C12 nucleus de-excites by emitting single 4439 keV gamma
In state 2, the C12 nucleus is at 7654 keV excitation level and it de-excites
via alpha emision 99.96% of the time. Rarely (~0.04% of the time), it decays
with a double-gamma emission.
Due to the selection rules, the two gammas are angularly correlated. 
The probability of angle theta between the two gammas is described by
a function, which basically is the superposition of even Legendre polynomials.
The coefficients for this function is given in Evans, The Atomic Nucleus (McGraw-Hill, New York, 1955) (Table 8.1).
////////W(theta) = 1-3\*cos^2(theta)+4\*cos^4(theta)\\\\\\\\\
A cumulative PDF was constructed based on this function to help sample a theta angle. 

However, since the double-gamma emission probability is extremely low (10^{-5} per neutron),
the angular correlation function will not be employed. I believe that it is completely fine
to leave the sampling function here for future reference. 
  
*/

