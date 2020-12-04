class Television:
    def __init__(self,Name=None,Balance=None,Channel=None,Type=None,Location=None):
        self.Name = Name
        self.Balance = Balance
        self.Channel = Channel
        self.Type = Type
        self.Location=Location
    def Requirement(self):
        print("Do you want to subscribe or upgrade")
        ms = str(input())
        if(ms=="subscribe" or ms=="Subscribe" or ms=="SUBSCRIBE"):
            self.Subscribe()
        elif(ms=="upgrade" or ms=="Upgrade" or ms=="UPGRADE"):
            pass
        else:
            print("Please Choose correct option")
            self.Requirement()
    def Channels_sub(self,mc):
        cha = {"ABC":{"Base":120,"SD":130,"HD":150,"4K":200,"Canada":1,"USA":1},"PQR":{"Base":120,"SD":120,"All":1}}
        if(mc=="PQR"):
            self.Location="All"
        m1 = 0
        try:
            m1 = cha[mc][self.Location]
        except:
            print("This channel not availabe in your region")
            print("Choose other channels")
            self.Requirement()
        print("Please choose subscription type:(Base,SD,HD,4K)")
        mt = str(input())
        if mc in cha and m1==1:
            bb = cha[mc][mt]
            bal = int(self.Balance)-bb
            if(bal<0):
                print("your account balance is not enough! Recharge")
            else:
                print("Channel "+mc+" ("+mt+")"+" Subsribed sucessfully")
                print("Available account balance:"+str(bal))
                exit()
        else:
            print("Your subscription type is not available in your region choose other")
            self.Channels_sub(mc)
    def Subscribe(self):
        print("Enter Channel name:(ABC,PQR)")
        mc = str(input())
        if(mc==Channel):
            print("You are already subcribed to this channel")
            print("Choose other channels")
            self.Subscribe()
        else:
            self.Channels_sub(mc)
Name = "John Doe"
Balance = "1000"
Channel = "PQR"
Type = "Base"
Location = "USA"
m = Television(Name,Balance,Channel,Type,Location)
m.Requirement()
