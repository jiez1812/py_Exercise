r = 0
def sec(*,d=0,h=0,m=0,s=0):
    r = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)
    print ('{0}s'.format(r))

def min(*,d=0,h=0,m=0,s=0):
    if s>=60:
        r = int(s/60) + m + (h * 60) + (d * 24 * 60)
        s = s - (60 * int(s/60))
        print ('{0}m {1}s'.format(r, s))
    else:
        r = m + (h * 60) + (d * 24 * 60)
        print ('{0}m {1}s'.format(r, s))
    