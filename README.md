# Find-The-Treasure

## About the Game
Game represents the squared map where every field is one of the several types. There are 6 types of field, with the given price in the brackets, road (2), grass (3), mud(5), sand(7), water (500) and stone (1000). When you are crossing the field, your path cost is incremented with the appropriate price. Agents need to find the treasure, marked as X on map, using one of the following searching algorithms.

## Agents
There are 4 agents, Aki, Jocke, Draza and Bole, and according to this, there are 4 different strategies. 
#### Aki
Aki uses the Depth First Search (DFS) algorithm, with the direction prioriting as north-east-south-west order. 
#### Jocke
Jocke uses the Breadth First Search (BFS) algorithm, with the direction prioriting as the field whom neighbours, excluding the current field, has the lowest average price. 
#### Draza
Draza uses the Branch and Bound algorithm, that guarantee the best path from the start to the goal field, using the lowest acumulated price as the criteria of the expanding. 
#### Bole
Bole uses the A* algorithm with the same logic as Draza's approach as far as the accumulated price is considered, while he uses the Manhattan Metric as the heuristics.

## Solutions
Some of the agents' paths are shown in the following images:
