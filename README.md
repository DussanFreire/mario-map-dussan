# Help Mario 👨⚠‼ Save the princess 👸

# Project Description
_Is a basic web application where you can build your own board which includes pipelines 🏁, walls 🟥 and of course Mario 👨! The main objective of this application is to find the distance from each free
space on the board to all pipelines and to find the path from Mario's position to the closest pipeline in the board._

This web application has two basic interfaces:
1. Menú:
  <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/menu.jpg" /></div>

2. Board:
* You can load our default board and have a fast view of the application:<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/default_board.jpg" /></div>
* You can create your own board with the dimensions that you want and play with the application options 😉: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/created_map.jpg" /></div>
* Don't trap Mario 😂:<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/mario_trapped.jpg" /></div>
## Problem solver agent:
* **Formulation of the objective:** Find the closest pipeline in an optimal way.
* **Problem formulation:** 
    * **Initial state:** The initial state is a pipeline position.
      * **Description of the actions:**
        * UP = Move up from the current position ⬆ 
        * DOWN = Move down from the current position ⬇
        * LEFT = Move left from the current position ⬅
        * RIGHT = Move right from the current position ➡
    * **Transitional model:** 
      * pass
    * **Target test:**
      * Si el espacio en que se encuentra el agente es de tipo tubería
    * **Route cost:**
      * The route cost for echa action is 1
    * **State space:**
* **Buscar, solucionar, ejecutar:**
      
### 2. Para la parte de buscar, solucionar y ejecutar vimos tres algoritmos de búsqueda no informada: BFS, DFS, e Iterative Deepening. Escoge el algoritmo más apropiado para poder ayudar a Mario y justifica tu decisión.
En este caso lo más eficiente seria usar BFS debido a que pueden existir caminos muy largos que no nos lleven a una tubería.
### 3. Explica de manera escrita y sin demasiados formalismos, cómo tu algoritmo va a funcionar y resolver el problema (me interesa saber cual es tu idea).
_pass_
## Parte Práctica 💻:
_pass_
