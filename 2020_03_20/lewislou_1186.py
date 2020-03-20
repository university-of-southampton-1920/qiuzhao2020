class Solution:
	def maximumSum(self, arr: List[int]) -> int:
		if max(arr) < 0:
			return max(arr)
		if min(arr) > 0:
			return sum(arr)

		fwd = [arr[0]]
		bwd = [arr[-1]]
		fwd_curr = arr[0]
		bwd_curr = arr[-1]
		best_val = max(arr[0], arr[-1])
		for i in range(1, len(arr)):
			fwd.append(max([fwd_curr+arr[i], arr[i]]))
			bwd.insert(0, max([bwd_curr+arr[-i-1], arr[-i-1]]))
			fwd_curr = fwd[-1]
			bwd_curr = bwd[0]
			best_val = max(best_val, fwd_curr, bwd_curr)

		max_val = min(arr)
		for i in range(1, len(arr)-1):
			max_val = max([max_val, fwd[i-1] + bwd[i+1]])

		return max(best_val, max_val)