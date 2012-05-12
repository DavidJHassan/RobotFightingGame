class Equipment
{
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


	Equipment()
	{
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


	bool isHealth()
	{
		return isHealth;
	}

	bool isShield()
	{
		return isShield;
	}

	bool isStamina()
	{
		return isStamina;
	}

	bool isSpeed()
	{
		return isSpeed;
	}

	bool isOffense()
	{
		return isOffense;
	}

	bool isDefense()
	{
		return isDefense;
	}

	float getHeath()
	{
		return health;
	}

	float getShield()
	{
		return shield;
	}

	float getSpeed()
	{
		return speed;
	}

	float getStamina()
	{
		return stamina;
	}

	float getOffense()
	{
		return offense;
	}

	float getDefense()
	{
		return defense;
	}
}