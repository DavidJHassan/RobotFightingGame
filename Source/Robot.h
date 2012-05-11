#ifndef ROBOT_H
#define ROBOT_H



// Basic Robot class that can be inherited to create different kinds of robots
class Robot
{
private:
    static int n;//Number of robots currently alive in game
    
    
protected:
    
    //Position on game board in x, y, z directions
    float posX; //Left, right
    float posY; // Forward, Backward
    float posZ; // Up , Down
    
    //Movement speed in x, y, z directions
    float dx;
    float dy;
    float dz;
    
    float health;
    float shield;
    
    float attack; //Damage capable of producing given equipment
    float defense; //Damage capable of blocking before hitting the shield
    
    //Possible positions to add equipment that may increase attack or defense capabilities
    float head;
    float neck;
    float shoulder;
    float arm;
    float wrist;
    float hand;
    float torso;
    float hips;
    float thighs;
    float shins;
    float calfs;
    float ankles;
    float feet;
    
public:
    
    Robot()
    {
        n++;
        //Settings to be determined
    };
    
    ~Robot()
    {
        if(n != 0)
        {
            n--;
        }
    };
};

 

#endif
