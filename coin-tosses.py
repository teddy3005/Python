import random
      
def coinToss(num_of_flips):
    heads_count=0
    tails_count=0
    for i in range(num_of_flips):
        rand=random.randint(1,2)
        if rand==1:
            tails_count +=1
            print tails_count, 'tails'
        elif rand==2:
            heads_count +=1
            print heads_count,'heads'
print "Attempt #",
coinToss(10)


