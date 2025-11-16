"""
LeetCode Problem [Problem Number]: [Problem Title]
Difficulty: [Easy/Medium/Hard]
Category: Graphs & Search & [Secondary Category]
URL: https://leetcode.com/problems/[problem-slug]/

[Complete problem description from LeetCode]

[Additional constraints or requirements]
"""

from collections import deque, defaultdict
from typing import List, Optional, Dict, Set, Tuple

class Solution:
    def graph_method(self, graph: List[List[int]], start_node: int) -> List[int]:
        """
        Approach: [Brief description of graph approach - BFS/DFS/Union-Find/Topological Sort]

        [Detailed explanation of the graph algorithm]
        [Step-by-step description of the approach]

        Graph Representation:
        - [ ] Adjacency List
        - [ ] Adjacency Matrix
        - [ ] Edge List

        Time Complexity: O(V + E) - [Explanation for BFS/DFS]
        Space Complexity: O(V) - [Explanation for visited set]

        Key Graph Patterns:
        - [ ] Number of Islands (Connected Components)
        - [ ] Course Schedule (Topological Sort)
        - [ ] Word Ladder (BFS Shortest Path)
        - [ ] Clone Graph (Graph Traversal)
        - [ ] Network Delay Time (Dijkstra)

        Key Insights:
        - [Important insight 1]
        - [Important insight 2]
        - [Important insight 3]

        Alternative Approaches Considered:
        - [Alternative approach 1] - [Why it wasn't chosen]
        - [Alternative approach 2] - [Why it wasn't chosen]
        """

        # Approach 1: BFS
        def bfs_approach():
            """Breadth-First Search approach"""
            # Initialize queue, visited set, distance tracking
            queue = deque([start_node])
            visited = set([start_node])
            result = []

            while queue:
                node = queue.popleft()
                result.append(node)  # Process node
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return result

        # Approach 2: DFS
        def dfs_approach():
            """Depth-First Search approach"""
            visited = set()
            result = []

            def dfs(node):
                if node in visited:
                    return
                visited.add(node)
                result.append(node)  # Process node
                for neighbor in graph[node]:
                    dfs(neighbor)

            dfs(start_node)
            return result

        return bfs_approach()  # or dfs_approach()


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        # Example 1: Basic functionality
        {
            "input": ([[1, 2], [0, 3], [0, 3], [1, 2]], 0),
            "expected": [0, 1, 2, 3],
            "description": "Basic BFS traversal test"
        },
        # Example 2: Disconnected graph
        {
            "input": ([[1], [0], [3], [2]], 0),
            "expected": [0, 1],
            "description": "Disconnected graph test"
        },
        # Example 3: Single node
        {
            "input": ([[]], 0),
            "expected": [0],
            "description": "Single node graph test"
        }
    ]

    # Run test cases
    print("=== Running Graph Test Cases ===")
    for i, test in enumerate(test_cases, 1):
        result = solution.graph_method(*test["input"])
        status = "✅ PASS" if result == test["expected"] else "❌ FAIL"
        print(f"Test {i}: {status} - {test['description']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got: {result}")
        print()

    # Compare approaches if multiple methods exist
    if hasattr(solution, 'alternative_approach'):
        print("\n=== Graph Approach Comparison ===")
        for test in test_cases[:2]:  # Compare first 2 test cases
            result1 = solution.graph_method(*test["input"])
            result2 = solution.alternative_approach(*test["input"])
            print(f"Test: {test['description']}")
            print(f"  Primary approach: {result1}")
            print(f"  Alternative approach: {result2}")
            print(f"  Results match: {result1 == result2}")
            print()