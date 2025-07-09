class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # This list will store all valid combinations of parentheses.
        result = []

        # 'backtrack' is a recursive helper function to build the parenthesis strings.
        # openCount: current number of '('
        # closeCount: current number of ')'
        # currentString: the string built so far in the current recursive path
        def backtrack(openCount, closeCount, currentString):
            # Base case: If we have used 'n' opening and 'n' closing parentheses,
            # we've found a valid combination.
            if openCount == n and closeCount == n:
                result.append(currentString)
                return

            # Recursive Step 1: Add an opening parenthesis.
            # We can add an opening parenthesis if we haven't reached the limit 'n'.
            if openCount < n:
                backtrack(openCount + 1, closeCount, currentString + "(")

            # Recursive Step 2: Add a closing parenthesis.
            # We can add a closing parenthesis only if it won't violate the well-formedness
            # (i.e., closeCount must be less than openCount).
            if closeCount < openCount:
                backtrack(openCount, closeCount + 1, currentString + ")")

        # Start the backtracking process with 0 open, 0 close, and an empty string.
        backtrack(0, 0, "")
        return result
