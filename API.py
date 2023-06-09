################API for operatin the ThorLabs PM100D over PyVisa serial communication ##########################################
class OpticalPower:
    #function will initailize communication to device with given address
    #an error will be raised if communication is not established
    def __init__(self,address):
        rm = visa.ResourceManager()
        try:
            self.OpticBoi = rm.open_resource(address)
            #check we are connected to the correct device
            name = self.OpticBoi.query("*IDN?")
            #responce should be "Thorlabs,PM100D,P0012289,2.4.0"
            if ((str(name[0]) == 'T') & (name[1] == 'h')):
                print('Connected to OpticBoi')
            else:
                print('Device did not respond with correct name')
                logging.error('Device did not respond with correct name')
        except:
            print("Error connecting to device")
            logging.error("Error connecting to device")
            
   ##funcion writes the wavelength value given to optical power meter##
    def writeWav(self,wavelength):
        try:
            #writes voltage to power supply
            self.OpticBoi.write('sense:corr:wav ' + str(wavelength))
            #wait one second as to not send commands to quickly
            time.sleep(1)
            #querry for wavelenth set of power meter
            actualWav = self.OpticBoi.query('sense:corr:wav?')
            #if the wavelength read is equal to the wavelength sent no error raised
            if (float(wavelength) == float(actualWav)) :
                print('')
            else:
                print('actual wavelength does not match wavelegth writen')
                logging.error('actual wavelength does not match wavelegth writen')
        except Exception as e:
            print('wavelength write failed')
            logging.error('wavelength write failed')
            print(e)
            
    #function reads the power 
    def readPower(self):
        try:
            power = self.OpticBoi.query('measure:power?')
            return power
            
        except Exception as e:
            print('power read failed')
            logging.error('power read failed')
            print(e)
            
    #function will close device
    def close(self):
        try:
            self.OpticBoi.close()
        except Exception as e:
            print('faild to close ThorLabs PM100D')
            logging.error('faild to close ThorLabs PM100D')
            print(e)
            
    #function writes to device
    def write(self,com):
        try:
            self.OpticBoi.write(com)
        except Exception as e:
            print('failed to send command to ThorLabs PM100D')
            logging.error('failed to send command to ThorLabs PM100D')
            print(e)
