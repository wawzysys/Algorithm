public class Main {
    public static int maxSubArray(int[] nums){
        int m = nums[0], c = nums[0];
        for(int i=1;i<nums.length;i++){
            c = Math.max(nums[i], c + nums[i]);
            m = Math.max(m, c);
        }
        return m;
    }
    public static void main(String[] args){
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArray(nums));
    }
}
