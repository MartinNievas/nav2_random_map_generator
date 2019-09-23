#ifndef rmg_hpp
#define rmg_hpp
#include <opencv2/opencv.hpp>
#include "map.hpp"
#include "obstacle.hpp"

using namespace cv;

class RMG {
    private:
        // member variables
        int circle_number;
        int square_number;
        int robot_size;
        int pixel_value;
        int thickness;
        int shift;
        LineTypes lineType;
        bool show_map;
        int max_obstacle_radius;
        int min_obstacle_radius;

    public:
        //member functions
        RMG();
        bool checkArea(Map orig, Map temp, Obstacle obs);
        int randomNumberGenerator(int min, int max);
        void generateMap();
};

#endif // map_hpp
