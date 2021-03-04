import sys
sys.setrecursionlimit(10**6)

pre_oreder, post_order = [], []

def make_tree(arrange):
    if not len(arrange): return
    pre_oreder.append(arrange[0][0])

    left, right = [], []
    for node, x, y in arrange:
        if arrange[0][2] <= y:
            continue
        if x < arrange[0][1]:
            left.append((node, x, y))
        else:
            right.append((node, x, y))
    make_tree(left)
    make_tree(right)

    post_order.append(arrange[0][0])

def solution(nodeinfo):
    for idx, v in enumerate(nodeinfo):
        nodeinfo[idx] = [idx+1] + v
    nodeinfo = sorted(nodeinfo, key=lambda x: [-x[2], x[1]])
    make_tree(nodeinfo)
    return [pre_oreder, post_order]

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])