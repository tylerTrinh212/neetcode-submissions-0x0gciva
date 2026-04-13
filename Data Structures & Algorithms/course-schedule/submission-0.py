class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = {i:[] for i in range(numCourses)} # Empty list for each course

        # Populate prerequisiteMap
        for course, pre in prerequisites:
            prerequisiteMap[course].append(pre)

        # All courses along the current DFS path
        visitSet = set()

        def dfs(course):
            # Loop case
            if course in visitSet:
                return False

            # No prerequisites
            if prerequisiteMap[course] == []:
                return True
            
            visitSet.add(course)

            # Run dfs on all prerequisites per course
            for pre in prerequisiteMap[course]:
                if not dfs(pre):
                    return False

            visitSet.remove(course)
            prerequisiteMap[course] = []

            return True

        # Run dfs on all courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True