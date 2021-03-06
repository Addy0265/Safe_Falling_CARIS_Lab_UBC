## USER SPECIFIC - OLIVER
ardPort = '/dev/ttyACM0'   
motorPort = '/dev/ttyACM1' 

dataFolder = '/media/adarsh/DA6E6C0B6E6BDEAF/Summer-2016 UBC/Work/Safe_Falling_CARIS_Lab_UBC'
matlabPath = dataFolder + 'Matlab Codes/'
torqueListPath = dataFolder + '/Python Codes/myCode/stateVariables20ms.csv'

# USER SPECIFIC - RASPBERRY PI
#comPorts = ['/dev/ttyACM0']
#dataFolder = '/home/pi/GitStuff/459_Project_Code/Results/'
#matlabPath = dataFolder + 'MATLAB_Results/' + '04-10-16_14-46-19/'
#torqueListPath = matlabPath + 'dataForPi.csv'


# LIST OF EXPERIMENT DATA SETS
# 	CONSTANT TORQUE 1: '04-10-16_14-46-19/'


######################### Interfacing Parameters #########################

# MOTOR PARAMS
#address = 0x80
baudRate = 38400
pulsePerRotation = 768 	#12*64

# ADC PARAMS
#potentiometer_adc = 0
#SPICLK  = 0x12 #18
#SPIMOSI = 0x18 #24
#SPIMISO = 0x17 #23
#SPICS   = 0x19 #25
#maxADC  = 1024 #2^10




######################### Metadata Parameters #########################

metadataNames = ['matlabPath', 'torqueListPath', 'shankLength', 'thighLength',
	'trunkLength', 'shankMass', 'thighMass', 'trunkMass', 'initialAngle_Knee',
	'initialAngle_Hip', 'calibratedValues']	




######################### Motor Parameters #########################

torque_motorConstant = 13.4e-3 												#torque constant
angVel_motorConstant = (1.4*60)/pulsePerRotation							#angVel constant, 1.4e-3 * 2*pi/60
armRes_motorConstant = 1.9 													#armature resistance


motorPos = [0]*2
potVal = 0
startByte = 222


######################### Physical System Parameters #########################

# PHYSICAL LENGTHS
shankLength = 1
thighLength = 1
trunkLength = 1

# PHYSICAL MASSES
shankMass = 1
thighMass = 1
trunkMass = 1

# INITIAL ANGLES
initialAngle_Knee = -40  ## -40
initialAngle_Hip = 40  ## +40




######################### Modified by Program #########################

calibratedValues = [] # knee, hip, heel, saves as encoder value
calibrated = False
torqueManager = []
torqueListGenerated = False

