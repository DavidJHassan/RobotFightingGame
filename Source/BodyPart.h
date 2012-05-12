class BodyPart
{

protected:

	bool isEquipped;

	bool isOffense;
	bool isDefense;
	bool isHealth;
	bool isShield;
	bool isStamina;
	bool isSpeed;

	float health;
	float shield;
	float speed;
	float stamina;
	float offense;
	float defense;


	BodyPart()
	{
		isEquipped = false;
		isOffense = false;
		isDefense = false;
		isHealth = false;
		isShield = false;
		isStamina = false;
		isSpeed = false;

		health = 0.0;
		shield = 0.0;
		speed = 0.0;
		stamina = 0.0;
		offense = 0.0;
		defense = 0.0;
	}


/*Children of BodyPart
head;
eyes;
neck;
shoulder;
arm;
wrist;
hand;
torso;
hips;
thighs;
shins;
calfs;
ankles;
feet;
*/
}