class Interview:
    def __init__(self,A,R,I):
        self.A = A
        self.R = R
        self.I = I
    def Room(self,RR):
        RR = RR+1
        return RR
    def HR(self,II):
        II = II+1
        return II
    def AS(self,AA):
        AA = AA+1
        return AA
    def meeting(self,RR,II,AA,DD):
        print("Day - "+str(DD))
        for i in range(9,16+1,2):
            print("time:"+str(i)+"-"+str(i+2) +" Room:"+str(RR)+ " Interviwer:"+str(II)+" Attendee:"+str(AA))
            if(i==11):
                i=i+2
            if(RR==self.R):
                RR=0
            if(II==self.I):
                II=0
            if(AA==self.A):
                print("All attendees finished Interview")
                exit()
            RR = self.Room(RR)
            II = self.HR(II)
            AA = self.AS(AA)
        if(AA<self.A+1):
            DD+=1
            self.meeting(RR,II,AA,DD)

attendees = 5
rooms = 2
interviewer = 3
ans = []
m = Interview(attendees,rooms,interviewer)
RR = 1
II = 1
AA = 1
DD = 1
m.meeting(RR,II,AA,DD)

