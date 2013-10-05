# vroom

Vroom is an open-source car circulation simulator


## Vision

 * Test different driving strategies in road scenarios
 * Load openstreetmaps sections and calculates road flow possibilities


## Installation

Install dependencies:

    pip install -r requirements.txt


## Run

Run it. It's easy.

    python main.py

Beautiful, isn't it?


## Coding

 * The default distance unit is the meter
 * The default time unit is the ms


## TODO

 * Cars' desired distance should depend on it's speed
 * Cars' deceleration should depend on front vehicle distance and speed delta
 * Cars' should decelerate according to turning angle
 * Cars' should never accelerate enough to cause accident
 * Every car should have a specific acceleration / decelaration limit
 * Every drive should apply differente accelerations
 * Drivers' variations should be coherent (someone driving very fast is likely
   to let less distance before front vehicles)
