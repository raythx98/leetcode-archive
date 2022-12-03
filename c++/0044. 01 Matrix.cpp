// time = O(n)
// space = O(1)

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size(), inf = m + n;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!mat[i][j]) continue;
                int left = inf, top = inf;
                if (i > 0) top = mat[i-1][j];
                if (j > 0) left = mat[i][j-1];
                mat[i][j] = min(top, left) + 1;
            }
        }
        
        m--; n--;
        for (int i = m; i >= 0; i--) {
            for (int j = n; j >= 0; j--) {
                if (!mat[i][j]) continue;
                int right = inf, bottom = inf;
                if (i < m) bottom = mat[i+1][j];
                if (j < n) right = mat[i][j+1];
                mat[i][j] = min(mat[i][j], min(bottom, right) + 1);
            }
        }
        return mat;
    }
};