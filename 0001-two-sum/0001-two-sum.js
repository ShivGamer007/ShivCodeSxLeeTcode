/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const mp = {};
    for (let i=0;i<nums.length; i++){
        const complement = target-nums[i];
        if(mp.hasOwnProperty(complement)){
            return [mp[complement],i];
        }
        mp[nums[i]] = i;
    }
    return [];
};