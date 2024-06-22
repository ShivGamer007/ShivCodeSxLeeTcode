/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function(nums, k) {
    let i = 0, j = 0, cnt = 0, ans = 0;
    while (j<nums.length){
        if(nums[j] % 2){
            cnt = 0;
            k--;
        }
        while (k == 0){
            if (nums[i]%2){
                k++;
            }
            i++;
            cnt++;
        }
        ans += cnt;
        j++;
    }
    return ans;
    
};