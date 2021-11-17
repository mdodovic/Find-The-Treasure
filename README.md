# Find-The-Treasure

## About the Game
Game represents the squared map where every field is one of the several types. There are 6 types of field, with the given price in the brackets, road (2), grass (3), mud(5), sand(7), water (500) and stone (1000). When you are crossing the field, your path cost is incremented with the appropriate price. Agents need to find the treasure, marked as X on map, using one of the following searching algorithms.

## Agents
There are 4 agents, Aki, Jocke, Draza and Bole, and according to this, there are 4 different strategies. 
#### Aki
Aki uses the Depth First Search (DFS) algorithm, with the direction prioriting as the cheapest neighbours field. If the neighbours has the same cost, the direction is priorited in north-east-south-west order. Toy example of DFS algorithm is in the following image:

![map0Aki](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/aki/map3_solution.png?raw=true)

#### Jocke
Jocke uses the Breadth First Search (BFS) algorithm, with the direction prioriting as the field whom neighbours, excluding the current field, has the lowest average price. 

![map0Jocke](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/jocke/map3_solution.png?raw=true)

#### Draza
Draza uses the Branch and Bound algorithm, that guarantee the best path from the start to the goal field, using the lowest acumulated price as the criteria of the expanding. 

![map0Draza](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/draza/map3_solution.png?raw=true)

#### Bole
Bole uses the A* algorithm with the same logic as Draza's approach as far as the accumulated price is considered, while he uses the Manhattan Metric as the heuristics.

![map0Bole](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/bole/map3_solution.png?raw=true)

## Solutions
Some of the agents' paths are shown in the following images:

![map0Jocke](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/jocke/map3_solution.png?raw=true)


![map0Jocke](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/jocke/map3_solution.png?raw=true)


![map0Jocke](https://github.com/mdodovic/Find-The-Treasure/blob/main/solutions/jocke/map3_solution.png?raw=true)

