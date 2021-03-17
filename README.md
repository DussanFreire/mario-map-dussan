# Help Mario 👨⚠‼ Save the princess 👸
# Prerequisites:
* Conda 4.9.2
* JetBrains IDE
# Installation
* Open a terminal in the folder named "mario-map-dussan"
* Write the following command: "python app.py"
* Click on the URL or open your localhost <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/instruccions.jpg" /></div>
# Project Description
_Is a basic web application where you can build your own board which includes pipelines 🏁, walls 🟥 and of course Mario 👨! The main objective of this application is to find the distance from each free
space on the board to all pipelines, and the path from Mario's position to the closest pipeline in the board._

This web application has two basic interfaces:
1. Menú:  <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/menu.jpg" /></div>
2. Board:
* You can load a default board and have a fast view of the application:<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/default_board.jpg" /></div>
* You can create your own board with the dimensions that you want and play with the application options 😉: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/created_map.jpg" /></div>
* Don't trap Mario 😂:<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/mario_trapped.jpg" /></div>
## Agent:
* **Formulation of the objective:** The objective is to mark the shortest distance from a pipeline in all the free spaces of the board, and find the shortest path from Mario's position
* **Problem formulation:** 
    * **Initial state:** The initial state is a board without any distances marked 
      * **Description of the actions:**
        * UP = Move up from the current position ⬆ 
        * DOWN = Move down from the current position ⬇
        * LEFT = Move left from the current position ⬅
        * RIGHT = Move right from the current position ➡
    * **Transitional model:**
        * UP: move("up", state.row, state.col) -> state: (row, col + 1)
        * DOWN: move("down", state.row, state.col) -> state: (row, col - 1)
        * LEFT: move("left", state.row, state.col) -> state: (row - 1, col)
        * RIGHT: move("right", state.row, state.col) -> state: (row - 1, col)
    * **Target test:**
      * In this case we don't have a target because this prophecy is working with a normal agent. We could
      say that the target test would be to mark all the free spaces with the correct distance to the closest pipeline
    * **Route cost:**
      * The route cost for each action is 1
    * **State space:** :<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states_bfs.jpg" /></div>     
* **Search:**
    The search algorithm BFS was used in this project, even though it uses more memory, its quantity of states is much
  lower than the quantity of states used in DFS. For example: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states using dfs.jpg" /></div>
  This quantity doesn't seam to high when we compare it with the same example using BFS: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states_bfs.jpg" /></div>
  But testing both with bigger boards the difference are bigger.<br> 
  When the algorithm dfs is used on a 11x11 board with a pipeline at the 
  position (6, 6), the program goes through 1043 states. <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/dfs in a 11x11 board.jpg" /></div>
  In the other hand, when a bfs algorithm is used for the same problem the program only goes through 121 states. <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/bfs in a 11x11 board.jpg" /></div>
  That's the main reason why we rather use bfs for this program.
  
## Algorithms:
* **Algorithm used to mark all the distances:** 
    * All the pipelines positions are selected and saved in the queue from the bfs algorithm
    * An empty list was declared to save all the states or successors 
    * The loop begins       
        * The agent creates 4 possible successors(each successor comes from the chosen actions) from each pipeline position in the list
        * The possible successors that doesn't complete the following conditions are remove from the list 🚫: 
            * The position must be inside the board
            * The position must be a free space
            * The successor can't be the parent from the current state
            * A free space that has already been marked can't be a successor
        * The distance is marked, on the successors, in the following way:
            * if the state is the root, then the successor distance marked in the free space is 1
            * if the state is also a free space, then the successor distance is the state distance + 1
        * The current state is added to the "states list"
        * All the successors are added to the queue
    * The length from the states list was returned
* **Algorithm used to mark and select the best path from Mario's Position ✅:**
    * First we need to find the initial step from Mario's position 
        * The agent creates 4 possible successors(each successor comes from the chosen actions) from Mario's position
        * If one of the posible positions is a pipeline, the position is marked, and the process ends
        * If the is not a pipeline around Mario, then the initial state will be one of the possible options which follows 
          the next conditions:
            * Must be a free space
            * Its distance must be higher than 0
            * It's distance must ve the lower from the posible successors
            * If there is only free spaces with a distance 0 marked, then we can't select the initial state because Mario is trapped
    * The position of the initial step will be the current position from the first cicle of the next step
    * It's time to choose the next step, this process will be repeated until we find a pipeline. 
        * The next free space, which has a distance equals to the current position distance - 1, will be  the next step 
          and the current position for the next step. 
