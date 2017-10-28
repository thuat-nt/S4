import S4

period = [2,2]
S = S4.New(Lattice=((period[0],0),(0,period[1])),NumBasis=100)
S.SetMaterial(Name = 'PMMA',Epsilon = (1.5 + 0.0j)**2)
S.SetMaterial(Name = 'Gold',Epsilon = (12.85 + 71.77j)**2)
S.SetMaterial(Name = 'Vacuum',Epsilon = (1 + 0j)**2)

S.AddLayer(Name = 'AirAbove',Thickness = 0, S4_Material = 'Vacuum')
S.AddLayer(Name = 'PMMA_Layer',Thickness = 0.3,S4_Material = 'PMMA')
S.SetRegionCircle(
	S4_Layer = 'PMMA_Layer',
	S4_Material = 'Vacuum',
	Center = (0,0),
	Radius = 0.5
)
S.AddLayer(Name = 'GoldLayer',Thickness = 1,S4_Material = 'Gold')
S.AddLayerCopy(Name = 'AirBelow',Thickness = 0, S4_Layer = 'AirAbove')
#S.AddLayer(Name = 'AirBelow',Thickness = 0,S4_Material = 'Vacuum')

S.SetExcitationPlanewave(
	IncidenceAngles=(
		0,# polar angle in [0,180)
		0 # azimuthal angle in [0,360)
	),
	sAmplitude = 1,
	pAmplitude = 0,
	Order = 0
)

S.SetOptions(
	PolarizationDecomposition = True
)

wavelengthRange = [8.0,14.0]
minFreq = 1/wavelengthRange[1]
maxFreq = 1/wavelengthRange[0]
print('Min: '+str(minFreq)+'    Max: '+str(maxFreq))
print('Wavelength\tForward\tBackward')
ptsNum = 20
freqDelta = (maxFreq - minFreq)/(ptsNum - 1)
for count in range(ptsNum):
	freq = minFreq + count*freqDelta
	S.SetFrequency(freq)
	forward,backward = S.GetPowerFlux(S4_Layer = 'AirAbove', zOffset = 0)
	forward = S.GetPowerFlux(S4_Layer = 'AirBelow',zOffset = 0)
	print(str(1/freq)+'\t'+str(forward[0].real)+'\t'+str(backward.real))

print('If you can read this, the configuration work is finished!')
