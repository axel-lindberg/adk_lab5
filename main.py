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
    
def heuristic(n, s, k, roles, scenes):
    #Lista över vilka roller som är med i samma scen
    neighbors = [set() for _ in range(n + 1)]
    for scene in scenes:
        for a in scene:
            for b in scene:
                if a != b:
                    neighbors[a].add(b)
                    
    assigned = []
    actor_roles = {}
    
def can_play(a, r):
    if a not in roles[r]:
        return False
    
    
def main():
    n, s, k, roles, scenes = readInput()
    optimize(n, s, k, roles, scenes)
    
if __name__ == "__main__":
    main()
    