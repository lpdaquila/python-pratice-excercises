
x = 1
def escopo():
    x = 10
    print('x dentro da funcao:', x)
    def escopo_interno():
        # global x
        x = 100
        print('x dentro da funcao interna:', x)
    escopo_interno()
escopo()
print('x fora da funcao:', x)
exit()

def soma(x, y, z=None):
    if z is not None:
        print('x=%d + y=%d + z=%d' % (x, y, z), '|', 'x+y+z=', x + y + z)
    else:
        print('x=%d + y=%d' % (x, y), '|', 'x+y=', x + y)
        
        

soma(1, 2)
soma(y=2, x=1, z=3)
soma(100, 200)
# soma(y=1, 2) # Error