class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize an empty list to store all valid combinations of parentheses.
        # This list will be populated by the recursive 'backtrack' function.
        result = []

        # Define the recursive helper function 'backtrack'.
        # It takes three arguments:
        # - openCount: The current number of opening parentheses '(' added to currentString.
        # - closeCount: The current number of closing parentheses ')' added to currentString.
        # - currentString: The string of parentheses being built in the current recursive path.
        def backtrack(openCount, closeCount, currentString):
        
            # Base Case: This is where we stop the recursion for a given path.
            # If both openCount and closeCount equal 'n', it means we have successfully
            # added 'n' pairs of well-formed parentheses.
            if openCount == n and closeCount == n:
                # Add the complete, valid string to our 'result' list.
                result.append(currentString)
                # Terminate this recursive call, as we've found a solution for this path.
                return

            # Recursive Step 1: Try adding an opening parenthesis '('
            # Condition: We can only add an opening parenthesis if we haven't
            # used all 'n' allowed opening parentheses yet.
            if openCount < n:
                # Make a recursive call:
                # - Increment openCount.
                # - Keep closeCount the same.
                # - Append '(' to the currentString.
                backtrack(openCount + 1, closeCount, currentString + "(")

            # Recursive Step 2: Try adding a closing parenthesis ')'
            # Pruning Condition: This is crucial for ensuring well-formedness.
            # We can only add a closing parenthesis if the number of closing parentheses
            # is less than the number of opening parentheses already in the currentString.
            # This prevents invalid combinations like ")(" or "())("
            if closeCount < openCount:
                # Make a recursive call:
                # - Keep openCount the same.
                # - Increment closeCount.
                # - Append ')' to the currentString.
                backtrack(openCount, closeCount + 1, currentString + ")")

        # Initial Call: Start the backtracking process.
        # We begin with:
        # - 0 open parentheses used.
        # - 0 close parentheses used.
        # - An empty string to start building from.
        backtrack(0, 0, "")
            
        # After the initial call completes and all recursive paths have been explored,
        # 'result' will contain all valid combinations. Return this list.
        return result
