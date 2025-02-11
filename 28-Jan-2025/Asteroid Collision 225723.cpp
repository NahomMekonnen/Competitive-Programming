# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> roids;
        for(int i : asteroids)
        {
            if(roids.empty()|| i > 0){
                roids.push_back(i);
            }else{
                if(roids.back()>0 && i<0){
                    if(roids.back() + i == 0)
                    {
                        roids.pop_back();
                        continue;
                    }else{
                        while(!roids.empty() && roids.back()>0 && (roids.back() < abs(i)))
                            roids.pop_back();
                        
                        if(roids.empty()|| (roids.back() < 0))
                        {
                            roids.push_back(i);
                        }else if(roids.back() == abs(i)){
                            roids.pop_back();
                        }
                    }
                }else{
                    roids.push_back(i);
                }

            }
        }
        return roids;
    }
};
