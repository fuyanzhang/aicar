class RespberryController:
    def forword(self):
        print("forword")
    def stop(self):
        print("stop")
    def back(self):
        print("back")
    def trunRight(self):
        print ("trun right")
    def trunLeft(self):
        print("trun left")
    def control(self,direction):
        if direction == 'forword':
            self.forword()
        elif direction == 'stop':
            self.stop()
        elif direction == 'back':
            self.back()
        elif direction == 'right':
            self.trunRight()
        elif direction == 'left':
            self.trunLeft ()
        else:
            print("error")           
