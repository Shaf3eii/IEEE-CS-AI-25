// https://leetcode.com/problems/statistics-from-a-large-sample/


class Solution {
    public:
        vector<double> sampleStats(vector<int>& count) {
            int n = (int)count.size();
            int mode = 0;
            int Min = INT_MAX, Max = INT_MIN;
            long double mean = 0;
            int sz = 0;
            for (int i = 0; i < n; ++i) {
                if (count[i]) {
                    if (count[i] > count[mode]) { // if the current count[i] > mode, mode = i 
                        mode = i;
                    }
                    Min = min(Min, i); // Min Value soFar
                    Max = max(Max, i); // Max Value soFar
                    sz += count[i];    // the number of values
                    mean += i * (long long)(count[i]); // the sum of values
                }
            }
            mean /= double(sz); // divide the sum by size to calculate the mean
            double median = 0;
            int target = (sz / 2) + 1; // The target position for finding the median
            int last = -1; // Stores the previous value when needed for even-sized
            int curCount = 0;  // Counter to track how many values we have traversed
            cout << target << '\n'; // Debugging output
            for (int i = 0; i < n; ++i) {
                if (!count[i]) continue;
    
                curCount += count[i];
    
                if (sz & 1) {  // Case: Odd total number of elements
                    if (curCount >= target){
                        median = i;
                        goto done;
                    }
                } else { // Case: Even total number of elements
                    if (curCount == sz / 2) {
                        last = i;
                    } else if (curCount > sz / 2) {
                        median = (last == -1 ? i : (last + i) / 2.0);
                        goto done;
                    }
                }
            }
            done: // Label to exit the loop and return the results
            return {double(Min), double(Max), double(mean), double(median), double(mode)};
        }
    };