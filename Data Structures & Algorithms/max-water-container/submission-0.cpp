class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left=0;
        int right=heights.size()-1;
        int water=0;
        while(left<right){
            int height_left=heights[left];
            int height_right=heights[right];
            int area = min(height_left, height_right) * (right - left);
            if (area > water) {
                water = area;
            }
            if(height_left<height_right){
                left++;
            }else{
                right--;
            }
            }
                return water;
        }
};
