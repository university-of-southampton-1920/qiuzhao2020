class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int K) {
        int row = matrix.size();
        int col = matrix[0].size();
        
        // 转置
        if(col < row){
            vector<vector<int>>t_matrix(col, vector<int>(row, 0));
            for(int i=0;i<row;i++){
                for(int j=0;j<col;j++){
                    t_matrix[j][i] = matrix[i][j];
                }
            }
            matrix = t_matrix;
            int t = row;
            row = col;
            col = t;
        }
            
        
        int res = INT_MIN;
        for (int i=0;i<row;i++){
            vector<int> tmp(col, 0);
            for(int j=i;j<row;j++){
                // cumsum
                for (int z=0;z<col;z++)
                    tmp[z] += matrix[j][z];
                res = max(res, helper(tmp, K));
            }
        }
        return res;
    }
    
    int helper(vector<int>& tmp, int K){
        multiset<int>Set({0});
        int N = tmp.size();
        int presum = 0;
        int res = INT_MIN;
        for(int j=0;j<N;j++){
            presum+=tmp[j];
            auto iter = Set.lower_bound(presum - K);
        if (iter != Set.end())
                res = max(res, presum-*iter);
            Set.insert(presum);
        }
        return res;
    }
};