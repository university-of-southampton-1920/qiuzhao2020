class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int N = (1<<target.length());
        vector<long> dp(N, INT_MAX);
        dp[0] = 0;
        for(int i=1;i<N;i++){
            for(string s:stickers){
                int j = su(i, s, target);
                dp[i] = min(dp[i], dp[j]+1);
            }
        }
        if(dp[N-1] == INT_MAX)
            return -1;
        return dp[N-1];
    }
    int su(int status, string& s, string& target){
        int K = target.length();
        for(char c: s){
            for(int k=0;k<K;k++){
                int pos = K - k - 1;
                if( ((status >> k)&1) && target[k] == c ){
                    status -= (1<<k);
                    break;
                }
            }
        }
        return status;
    }
};