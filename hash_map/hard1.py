### AUG 7, 2025 -- P2508: ADD EDGES TO MAKE DEGREES OF ALL NODES EVEN ###

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Build degree frequency and edge set
        degree = [0] * (n+1)
        edge_set = set()
        for u, v in edges:
            degree[u] += 1; degree[v] += 1
            edge_set.add((min(u,v), max(u,v)))
            # always add edges as u <= v to avoid having both (1, 2) and (2, 1)

        # 2. Identify nodes with odd degree
        # You can only fix a graph if the number of odd-degree nodes is in {0, 2, 4}:
        odd = 0
        odd_nodes = []
        for i, d in enumerate(degree):
            if d % 2 == 1: 
                odd += 1
                odd_nodes.append(i)
        if odd not in {0, 2, 4}: # UNFIXABLE
            return False
        elif odd == 0: # ODD == 0; ALR VALID
            return True
        elif odd == 2: # 1 DIRECT EDGE OR A->INTER+INTER->B (2 EDGES)
            # Try connecting the two nodes directly, or through a third node.
            n1, n2 = odd_nodes
            # Connect directly --> done
            if (min(n1,n2), max(n1,n2)) not in edge_set: return True
            # Intermediary
            # we can do that bc its degree will inc by 2 so still even
            for n3 in range(1, n+1):
                if n3 != n1 and n3 != n2:
                    if (min(n1, n3), max(n1,n3)) not in edge_set and (min(n2, n3), max(n2,n3)) not in edge_set:
                        return True
            return False
        else: # ODD == 4: 2 DIRECT EDGES
            # can only add up to 2 new edges
            # so we can't look for an intermediary like we did for odd == 2

            # Try pairing the 4 nodes in 3 different pair combinations 
            # and check if both edges in the pair are not already present.
            n1, n2, n3, n4 = odd_nodes
            cands = [
                ((n1, n2), (n3, n4)),
                ((n1, n3), (n2, n4)),
                ((n1, n4), (n2, n3))
            ]
            for (u1, v1), (u2, v2) in cands:
                if (min(u1, v1), max(u1, v1)) not in edge_set and (min(u2, v2), max(u2, v2)) not in edge_set:
                    return True
            return False
