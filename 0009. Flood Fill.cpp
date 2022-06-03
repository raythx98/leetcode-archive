// time = O(n)
// space = O(1)

class Solution {
public:
    void fill (vector<vector<int>>& image, int r, int c, int startingColor, int newColor) {
        if (r < 0 || c < 0 || r >= image.size() || c >= image[0].size() || image[r][c] != startingColor) return;
        image[r][c] = newColor;
        for (auto &[x, y]: vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
            fill (image, r + x, c + y, startingColor, newColor);
        }
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor) return image;
        fill(image, sr, sc, image[sr][sc], newColor);
        return image;
    }
};