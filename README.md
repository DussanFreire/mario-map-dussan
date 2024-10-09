# 🏃‍♂️ Help Mario Save the Princess 👸

## Project Overview
Help Mario navigate through a custom-built board filled with obstacles like walls 🟥 and pipelines 🏁. The goal is to find the shortest path from Mario's position to the nearest pipeline using search algorithms. This project demonstrates how Breadth-First Search (BFS) and Depth-First Search (DFS) can be applied to pathfinding challenges.

## Prerequisites

- **Conda 4.9.2** (Recommended)
- **JetBrains IDE** (Optional, but preferred)
- If Conda is not available, you might need to install Flask separately using `pip install flask`.

## Installation and Setup

1. Open a terminal in the project folder, named `mario-pathfinder`.
2. Run the following command to start the Flask application:
   ```bash
   python app.py
   ```
3.	Once the server is running, access the web app by clicking the URL provided in the terminal or by visiting localhost in your browser

<p align="center">
  <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/instruccions.jpg" alt="Instructions Screenshot"/>
</p>

## Project Description

This web application lets you build custom boards containing Mario 👨, pipelines 🏁, and walls 🟥. The main goal is to calculate the shortest path between Mario’s position and the nearest pipeline while also computing the distances from every free space on the board to all pipelines.

### User Interfaces

1.	Menu: Select or create a new board.
<p align="center">
  <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/menu.jpg" alt="Menu Interface"/>
</p>

2.	Board: Load a default board or create your own and start playing.
*	Default Board: Get a quick overview of the app.

<p align="center">
  <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/default_board.jpg" alt="Default Board"/>
</p>

* Custom Board: Build a board with the dimensions you prefer and explore its features.
  
<p align="center">
  <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/created_map.jpg" alt="Custom Board"/>
</p>

### Gameplay Tip:

* Don't trap Mario 😂:
<p align="center">
  <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/mario_trapped.jpg" alt="Mario Trapped"/>
</p>

## Agent’s Role

The agent’s task is to mark the shortest distance from all free spaces to the nearest pipeline and find the best path for Mario to reach one of the pipelines.

### Problem Formulation

* Initial State: The initial state is a board without any distances marked 
  * Actions:
    * UP = Move up from the current position ⬆ 
    * DOWN = Move down from the current position ⬇
    * LEFT = Move left from the current position ⬅
    * RIGHT = Move right from the current position ➡
* Transitional model:
    * UP: move("up", state.row, state.col) -> state: (row, col + 1)
    * DOWN: move("down", state.row, state.col) -> state: (row, col - 1)
    * LEFT: move("left", state.row, state.col) -> state: (row - 1, col)
    * RIGHT: move("right", state.row, state.col) -> state: (row - 1, col)
* Goal Test: Mark all free spaces with the shortest distance to the nearest pipeline.
* Cost: Each movement has a cost of 1.
* State space:
    
<p align="center">
   <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states_bfs.jpg" />
</p>

## Search

The search algorithm BFS was used in this project, even though it uses more memory, its quantity of states is much
lower than the quantity of states used in DFS. For example in the following image we can see how the dfs algorithm 
would mark all the free spaces on the board: 
<p align="center">
  <img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states using dfs.jpg" />
</p>
This quantity doesn't seam to high when we compare it with the same example using BFS:
<p align="center">
<img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states_bfs.jpg" />
</p>
But when the algorithm dfs is used on a 11x11 board with a pipeline at the 
position (6, 6), the program goes through 1043 states. 
 <p align="center">
<img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/dfs in a 11x11 board.jpg" />
</p>
In the other hand, when a bfs algorithm is used for the same problem the program only goes through 121 states.
   <p align="center">
<img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/bfs in a 11x11 board.jpg" />
</p>
That's the main reason why we rather use bfs for this program.
  
## Algorithms:

* Algorithm used to mark all the distances:
  * Steps used:
    * All the pipelines positions were selected and saved in the queue from the bfs algorithm
    * An empty list was declared to save all the states or successors 
    * The loop begun       
        * One position from the queue was taken, and the agent created 4 possible successors for that position(each 
          successor comes from the chosen actions) 
        * The possible successors that weren't able to complete the following conditions were removed from the list of 
          possible successors 🚫: 
            * The position must be inside the board
            * The position must be a free space
            * The successor can't be the parent from the current state
            * A free space that has already been marked can't be a successor
        * The distance was marked, on the successors, in the following way:
            * if the state is the root, then the successor distance marked in the free space is 1
            * if the state is also a free space, then the successor distance is the state distance + 1
        * The current state was added to the "states list"
        * All the successors were added to the queue
    * At the end, of the process, the length from the states list was returned
* **Algorithm used to mark and select the best path from Mario's Position ✅:**
  * Steps used:
    * The process begun finding the initial step from Mario's position 
        * The agent created 4 possible successors(each successor comes from the chosen actions) from Mario's position
        * If one of the posible positions was a pipeline, the position was marked, and the process ended
        * If there wasn't a pipeline around Mario, then the initial state would be one of the possible options which follows 
          the next conditions:
            * Must be a free space
            * Its distance must be higher than 0
            * It's distance must be the lower from the posible successors
            * If there is only free spaces with a distance 0 marked, then we can't select the initial state because Mario is trapped
    * The position of the initial step will be the current position from the first cicle of the next step
    * if the pipeline wasn't around Mario, then a similar process was used and repeated until the pipeline was found 
