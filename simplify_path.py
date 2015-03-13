# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# click to show corner cases.
# Corner Cases:
#
#     Did you consider the case where path = "/../"?
#     In this case, you should return "/".
#     Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#     In this case, you should ignore redundant slashes and return "/home/foo".

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if not path:
            return "/"

        # Reduce consecutive redudant slashes
        i = 0
        while i < len(path) - 1:
            if path[i] == '/' and path[i+1] == '/':
                path = path[:i+1] + path[i+2:]
                continue
            i += 1

        # Reduce trailing slash
        if path[-1] == '/':
            path = path[:len(path)-1]

        # Build level list
        levels = path.split('/')[1:]
        to_build = []
        for level in levels:
            if level == ".":
                continue
            elif level == "..":
                if to_build:
                    to_build.pop()
            else:
                to_build.append(level)

        return '/' + '/'.join(to_build)


print Solution().simplifyPath(path)
