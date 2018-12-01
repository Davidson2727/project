if(self._wave2 != Nums.NONE.value):
    self.wave2Out()
    self.assignWave2Filt1(self._wave2)
    if(self._wave2Filt1 != Nums.NONE.value):
        self.w2Filt1Out()
        self.assignWave2Filt2(self._wave2Filt1)
        if(self._wave2Filt2 != Nums.NONE.value):
            self.w2Filt2Out()
            self.assignWave2Filt3(self._wave2Filt2)
            if(self._wave2Filt3 != Nums.NONE.value):
                self.w2Filt3Out()
                self.assignWave2Filt4(self._wave2Filt3)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                #Occurs if filter 4 is not assigned
                else:
                    self.w2Filt3Out()
                    self.assignWave2Filt5(self._wave2Filt3)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
            #Occurs if filter 3 in not assigned.
            else:
                self.w2Filt2Out()
                self.assignWave2Filt4(self._wave2Filt2)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.w2Filt2Out()
                    self.assignWave2Filt5(self._wave2Filt2)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
        else:
            self.w2Filt1Out()
            self.assignWave2Filt3(self._wave2Filt1)
            if(self._wave2Filt3 != Nums.NONE.value):
                self.w2Filt3Out()
                self.assignWave2Filt4(self._wave2Filt3)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.w2Filt3Out()
                    self.assignWave2Filt5(self._wave2Filt3)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
            else:
                self.w2Filt1Out()
                self.assignWave2Filt4(self._wave2Filt1)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.w2Filt1Out()
                    self.assignWave2Filt5(self._wave2Filt1)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
    else:
        self.wave2Out()
        self.assignWave2Filt2(self._wave2)
        if(self._wave2Filt2 != Nums.NONE.value):
            self.w2Filt2Out()
            self.assignWave2Filt3(self._wave2Filt2)
            if(self._wave2Filt3 != Nums.NONE.value):
                self.w2Filt3Out()
                self.assignWave2Filt4(self._wave2Filt3)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.w2Filt3Out()
                    self.assignWave2Filt5(self._wave2Filt3)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
            else:
                self.w2Filt2Out()
                self.assignWave2Filt4(self._wave2Filt2)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.w2Filt2Out()
                    self.assignWave2Filt5(self._wave2Filt2)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
        else:
            self.wave2Out()
            self.assignWave2Filt3(self._wave2)
            if(self._wave2Filt3 != Nums.NONE.value):
                self.w2Filt3Out()
                self.assignWave2Filt4(self._wave2Filt3)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.assignWave2Filt5(self._wave2Filt3)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        self.w2Filt3Out()
            else:
                self.wave2Out()
                self.assignWave2Filt4(self._wave2)
                if(self._wave2Filt4 != Nums.NONE.value):
                    self.w2Filt4Out()
                    self.assignWave2Filt5(self._wave2Filt4)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
                else:
                    self.wave2Out()
                    self.assignWave2Filt5(self._wave2)
                    if(self._wave2Filt5 != Nums.NONE.value):
                        self.w2Filt5Out()
                    else:
                        pass
else:
    pass
