# recursive function for Tower of Hanoi
def hanoi(disks,source,helper,destination):
    # Base case
    if(disks==1):
        print('Disk {} moves from tower {} to tower {}'.format(disks,source,destination))
        return

# Recursive call in which function call itself

    hanoi(disks-1,source,destination,helper)
    print('Disk {} moves from tower {} to tower {}'.format(disks,source,destination))
    hanoi(disks-1,helper,source,destination)

# Drive code: Initializing & Calling the function
disks=int(input('No of disks to be placed: '))

'''
Tower names passed as arguments:
Source:A
Helper:B
Destination:C
'''

# Actual Function call
hanoi(disks,'A','B','C')