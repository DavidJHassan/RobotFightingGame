#include <iostream>
using namespace std;
class Head : public BodyPart
{
private:
	Equipment e; // for some equipment e that is being equipped 
	
	Head()
	{
		//Nothing happens takes defaults that BodyPart constructs
	}

	Head(Equipment e)
	{
		this.e = e;
		isEquipped = true;

		if(e.isHealth())
		{
			health = e.getHealth();
			isHealth = true;
		}


		if(e.isShield())
		{
			shield = e.getShield();
			isShield = true;
		}

		if(e.isSpeed())
		{
			speed = e.getSpeed();
			isSpeed = true;
		}

		if(e.isStamina())
		{
			stamina = e.getStamina();
			isStamina = true;
		}


		if(e.isOffense())
		{
			offense = e.getOffense();
			isOffense = true;
		}

		if(e.isDefense())
		{

			defense = e.getDefense();
			isDefense = true;
		}
	}
}