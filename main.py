import sys

def readInput():
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data) #antal roller
    s = next(data) #antal scener
    k = next(data) #antal skådespelare
    
    roles = [[]]
    
    for _ in range(n):
        num = next(data)
        roles.append([next(data) for _ in range(num)])
        
    scenes = []
    
    for _ in range(s):
        num = next(data)
        scenes.append([next(data) for _ in range(num)])
        
    return n, s, k, roles, scenes

def optimize(n, s, k, roles, scenes):
    
    
    print(opt_k)
    
    
def main():
    n, s, k, roles, scenes = readInput()
    optimize(n, s, k, roles, scenes)
    
if __name__ == "__main__":
    main()
    