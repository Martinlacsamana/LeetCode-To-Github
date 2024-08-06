class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        if startColor == color:
            print("here")
            return image

        m, n = len(image), len(image[0])

        def dfs(r, c):
            # Base Case 1: If the current pixel is not in bounds, return
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            # Base Case 2: If the current pixel is not the startColor, return
            if image[r][c] != startColor:
                return
            
            image[r][c] = color
            
            # DFS through each 4-directional adjacent pixel
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # DFS on the starting pixel
        dfs(sr, sc)

        return image    # return modified image
