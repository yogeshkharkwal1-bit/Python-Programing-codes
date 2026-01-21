class player:
    player_count=0

    def __init__(self,name,leval):
        self.name=name
        self.leval=leval
        player.player_count += 1

p1=player("sruresh",56)        
p2=player("ramesh",36)        
p3=player("yogesh",46)        
p4=player("mukesh",26)        
p5=player("yash",76)      

print(p1.name,p1.leval)
print(player.player_count)
