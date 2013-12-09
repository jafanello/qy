import numpy as np
import os, json, sys
import qy
import qy.settings
from nidaqmx import System
from nidaqmx import AnalogOutputTask
import socket

'''the card which we want to use'''
CARD_NAME='NI 9264'

class dac:
    def connect_nidaqmx(self):
        '''look at nidaqmx'''
        system=System()

        '''search for the card that we want to use'''
        card=None
        for dev in system.devices:
            if dev.get_product_type() == CARD_NAME: card=dev
        assert(card!=None)

        '''create the 8-channel task'''
        self.task = AnalogOutputTask()
        channels=card.get_analog_output_channels()[:8]
        for channel in channels:
            self.task.create_voltage_channel(channel, min_val=0, max_val=7)

        '''zero everything'''
        self.zero()
        
    def write_voltages(self, voltages):    
        av=np.array(voltages)
        if max(av)>7.0:
            print 'CANNOT WRITE VOLTAGES GREATER THAN 7.0V'
            voltages=[0,0,0,0,0,0,0,0]
        self.task.write(voltages)
        print 'wrote', av.round(2)
        
    def zero(self):
        self.write_voltages([0,0,0,0,0,0,0,0])
        
    def listen(self):
        while True:
            '''wait for a connection from the client'''
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('localhost', 50007))
            print 'waiting for connection from client...'
            s.listen(1)
            conn, addr = s.accept()
            print 'connected by', addr
            
            '''wait for new data'''
            connected=True
            while connected:
                try:
                    data = conn.recv(4096)
                    if data==0 or data=='':
                        print 'connection closed'
                        self.zero()
                        connected=False
                    else:
                        voltages=[float(x) for x in data.split('\t')]
                        if len(voltages)==8:
                            self.write_voltages(voltages)
                            conn.send('done')
                        
                except socket.error:
                    print 'connection lost prematurely'
                    self.zero()
                    connected=False
                            
    def __init__(self):
        print 'CNOT-MZ heater server\n'
        self.connect_nidaqmx()
    
    
class table:
    def __init__(self, filename=None):
        ''' A heater calibration table, stored on disk, with lookup functions '''
        if filename==None: filename=os.path.join(qy.settings.get_config_path(), 'heater_calibration.json')
        self.filename=filename
        self.heater_count=0
        self.curve_parameters={}
        if os.path.exists(self.filename): self.load()

    def load(self, filename=None):
        ''' Load the table from a JSON file on disk '''
        f=open(self.filename, 'r')
        data=json.loads(f.read())
        f.close()
        self.curve_parameters=data['curve_parameters']
        self.heater_count=len(self.curve_parameters)

    def save(self, filename=None):
        ''' Save to a JSON file on disk '''
        if filename!=None: self.filename=filename
        self.curve_parameters={key: tuple(value) for key, value in self.curve_parameters.items()}
        print self.curve_parameters
        d={'heater_count':len(self.curve_parameters), 'curve_parameters':self.curve_parameters}
        f=open(self.filename, 'w')
        f.write(json.dumps(d))
        f.close()
        print 'saved %s' % self.filename

    def set_table(self, new_table):
        ''' Set the entire phase-voltage table '''
        self.curve_parameters=new_table

    def set_curve(self, heater_index, fit_parameters):
        ''' Set a single curve '''
        self.curve_parameters[heater_index]=fit_parameters

    def get_parameters(self, heater_index):
        ''' Get the full set of parameters for a particular heater '''
        try:
            p=self.curve_parameters[heater_index]
        except KeyError:
            p=self.curve_parameters[unicode(heater_index)]
        return p

    def get_voltage(self, heater_index, phase):
        ''' Get the appropriate voltage to set to the chip, given a phase '''
        p=self.get_parameters(heater_index)
        phase=phase % (2*np.pi)
        phase=phase-2*np.pi
        while p[0]>phase: phase=phase+2*np.pi
        v=np.sqrt((phase-float(p[0]))/float(p[1]))
        if v>7:
            phase=phase-2*np.pi
            v=self.get_voltage(heater_index,phase)
        return v if v>=0 else -v
        
    def get_voltages(self, phases):
        '''Turn a list of (8) phases in to a list of voltages'''
        if len(phases)!=8:
            print 'Please provide 8 phases'
            '''Is this the best way?'''
            exit()
        v=[self.get_voltage(heater_index,phase) for heater_index, phase in enumerate(phases)]
        return v
    
    def __str__(self):
        ''' Print the calibration table out as a string '''
        s='Heater calibration table [%s]\n%s heaters\n' % (self.filename,str(self.heater_count))
        #print self.curve_parameters
        for index, params in self.curve_parameters.iteritems():
            s+='Heater %s: %s\n' % (index, str(params))
        return s
    
class heaters:
    def __init__():
        self.dac=dac()
        self.table=table()
        self.dac.zero()
        self.ontime=2
        self.offtime=15
        self.integration_time=1
        
    def pulse(phases,fpga,callback=None):
        counts=zeros(22)
        voltages=self.table.get_voltages(phases)
        self.dac.write_voltages(voltages)
        for i in range(self.integration_time):
            print 'integrating [%.3f %% done]...' % (100*i/float(integration_time))
            for _ in range(self.ontime): self.fpga.read()
            c=fpga.read()
            counts+=c
            self.dac.zero()
            for i in range(self.offtime):
                callback('cooling, step %d' % i)
        return counts
        
    def set_ontime(ontime):
        if int(ontime)!=ontime: 
            print 'Please provide an integer ontime'
            self.ontime=1
        if ontime>3:
            print 'Cannot heat for longer than 3 seconds'
            self.ontime=1
        self.ontime=ontime
        
    def set_offtime(offtime):
        if int(offtime)!=offtime: 
            print 'Please provide an integer offtime'
            self.offtime=15
        if offtime<15:
            print 'Cannot cool for less than 15 seconds'
            self.offtime=15
        self.offtime=offtime
        
    def set_integration_time(integration_time):
        if int(integration_time)!=integration_time:
            print 'please provide an integer integration time'
            self.integration_time=1
        self.integration_time=integration_time
        
        
if __name__=='__main__':
    t=table()
    phases=np.zeros(8)
    v = t.get_voltages(phases)
    print v