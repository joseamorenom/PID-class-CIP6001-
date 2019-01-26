class pid:

    def __init__(self):
        self.p=0
        self.i=0
        self.d=0
        self.senal=0
        self.error=0
        self.error_ant=0
        self.sp=0
        self.integral=0
        self.derivative=0

    def calibrarPID(self,ku,tu):
        self.p=0.6*ku
        self.i=1.2*ku/tu
        self.d=3*ku*tu/40

    def setPID(self,p,i,d):
        self.p=p
        self.i=i
        self.d=d

    def setSetPoint(self,sp):
        self.sp=sp

    def actualizarSenal(self,sensor):
        self.error=self.sp-sensor
        self.integral = self.integral + (self.error*0.01)
        self.derivative = (self.error - self.error_ant) / 0.01
        self.senal = self.p*self.error + self.i*self.integral + self.d*self.derivative
        self.error_ant=self.error

