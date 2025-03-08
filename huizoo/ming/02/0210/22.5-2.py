n = int(input())
date_course = []
# def dfs(number, path) :
#     if len(path) == number :
#         print(''.join(path))
#         return
#     for ox in ['x', 'o'] :
#         path.append(ox)
#         dfs(number, path)
#         path.pop()
#
# dfs(n, date_course)


def dfs(level, max_level) :
    if level == max_level :
        print(''.join(date_course))
        return
    for ox in ['x','o'] :
        date_course.append(ox)
        dfs(level+1, max_level)
        date_course.pop()

dfs(0, n)