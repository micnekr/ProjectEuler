def checkPath(dims, x=0, y=0, table = {}):
    if x==dims or y==dims:
        return 1
    if x in table:
        if y in table[x]:
            return table[x][y]
    paths = 0
    paths+=checkPath(dims, x+1, y, table=table)
    paths+=checkPath(dims, x, y+1, table=table)
    if x not in table:
        table[x]={}
    table[x][y]=paths
    return paths

if __name__ == '__main__':
    dims = 20
    table = {}
    print(checkPath(dims, table=table))



# def checkPath(dims, x=0, y=0, table = {}):
#     if x==dims or y==dims:
#         return 1
#     if x==y and x in table:
#         return table[x]
#     paths = 0
#     paths+=checkPath(dims, x+1, y)
#     paths+=checkPath(dims, x, y+1)
#     if x==y:
#         table[x]=paths
#     return paths
