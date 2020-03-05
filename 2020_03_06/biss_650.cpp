class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n+1, 1e10);
        dp[1] = 0;
        for(int i=2;i<=n;i++){
            for(int j=1;j<i;j++){
                if(i % j == 0){
                    dp[i] = min(i / j  + dp[j], dp[i]);
                }
            }
        }
        return dp[n];
    }
};