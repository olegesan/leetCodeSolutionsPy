def canFinish(numCourses, prerequisites) -> bool:
        pointingNodes = {}
        hasPrereqs = {}
        for prereq in prerequisites:
            if prereq[1] not in pointingNodes:
                pointingNodes[prereq[1]] = []
            pointingNodes[prereq[1]].append(prereq[0])
            if prereq[0] not in hasPrereqs:
                hasPrereqs[prereq[0]] = 1
        S = set()
        output = []

        for course in range(numCourses):
            if course not in hasPrereqs:
                S.add(course)
        
        while len(S)>0:
            n = S.pop()
            output.append(n)
            edges = pointingNodes.get(n,[]).copy()
            for m in edges:
                pointingNodes.get(n).remove(m)
                hasEdge = False
                for key in pointingNodes.keys():
                    if m in pointingNodes[key]:
                        hasEdge = True
                if not hasEdge:
                    S.add(m)
        
        return len(output) == numCourses

##worked

##solution by zenitator from Leetcode for myself to study
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites: return True
        # build the graph
        graph = {}
        for pair in prerequisites:
            _from, _to = pair
            graph.setdefault(_from, []).append(_to)
        # we need to find a topological sort if we detect a cycle we are done
        visiting, visited = set(), set()
        def dfs(node):
            # cycle detected
            if node in visiting: return False
            visiting.add(node)
            # explore children
            res = True
            for child in graph.get(node, []):
                if child not in visited:
                    res &= dfs(child)
                    if not res: return False
            # done with this node and its children
            visiting.discard(node)
            visited.add(node)
            return res
        # explore all nodes
        for i in range(numCourses):
            if not dfs(i): return False
        return True
