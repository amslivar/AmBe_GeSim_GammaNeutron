#ifndef gesimPrimaryGeneratorAction_h
#define gesimPrimaryGeneratorAction_h 1

#include "G4VUserPrimaryGeneratorAction.hh"
#include <vector>
#include <string>
class G4ParticleGun;
//class G4GeneralParticleSource;
class G4Event;
class gesimDetectorConstruction; //added with the previous version

class gesimPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
public:
  gesimPrimaryGeneratorAction(gesimDetectorConstruction*);
  virtual ~gesimPrimaryGeneratorAction();


    // Declare the missing member functions
  G4double EnergySampler(const G4double* ptr_NeutronCDF, const G4double* ptr_NeutronEnergy, unsigned int size);
  //G4double GetNeutronEnergy(G4int state);
  G4double GetGammaAngle();
  G4double AngleSampler(const G4double* ptr_GammaCDF, const G4double* ptr_GammaAngle, unsigned int size);
  G4double loadArrayFromFile(const std::string& filename);

  virtual void GeneratePrimaries(G4Event* anEvent);

private:
  //G4GeneralParticleSource* fParticleGun;
  G4ParticleGun* fParticleGun;
  gesimDetectorConstruction*    gesimDetector;
  
};

#endif



