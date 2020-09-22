def findOrder(numCourses, prerequisites):
    openCourseDic = {}
    hasPrereqs = {}
    S = set()
    output = []
    for prereq in prerequisites:
        # making a dictionary for courses and their prereqs
        if not prereq[0] in hasPrereqs:
            hasPrereqs[prereq[0]] = ''
        #making a dict for courses and where they are prereqs
        if not prereq[1] in openCourseDic:
            openCourseDic[prereq[1]] = []
        openCourseDic.get(prereq[1]).append(prereq[0])
        

    #adding all the courses that don't need prereqs
    for course in range(0, numCourses):
        if not course  in hasPrereqs:
            S.add(course)

    while len(S) > 0:
        n = S.pop()
        output.append(n)
        edges = openCourseDic.get(n, []).copy()
        for m in edges:
            openCourseDic[n].remove(m)
            present = False
            for course in openCourseDic.keys():
                if m in openCourseDic[course]:
                    present = True
            if not present:
                S.add(m)
    

    return output if len(output) == numCourses else []

course4 = findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
course3 = findOrder(3, [])
course2 = findOrder(3, [[0,1],[0,2],[1,2]])
course1 = findOrder(3, [[1,0],[1,2],[0,1]])
print(course4)
print(course3)
print(course2)
print(course1)