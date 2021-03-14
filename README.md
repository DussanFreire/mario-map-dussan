# Help Mario 👨⚠‼ Save the princess 👸

# Project Description
_Is a basic web application where we can build our on Mario board which includes
pipelines 🏁, walls 🟥 and of course Mario 👨! The main objective of this application is to find the distance from each free 
space on the board to all pipelines and to find the path from Mario's position to the closest pipeline in the board._

This web application has two basic interfaces:
1. "Menu":
     ![alt text](https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/menu.jpg)

2. "Board"
   * You can load our default board and have a fast view of the application
     ![alt text](https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/default_board.jpg)
   * You can crearte your own board with the dimensions that you want and play with the application options 😉
     ![alt text](https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/mario_trapped.jpg)
   * Don't trap Mario 😂
     ![alt text](https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/created_map.jpg)
## Parte Teórica 📖:
### 1. Diseña un Problem-Solver agent. Para esto tendrás que hacer una breve descripción de la formulación del objetivo, la formulacióon del problema (estado inicial, estado objetivo, test del objetivo, acciones, función de transición, costo) y finalmente, buscar, solucionar y ejecutar.

* **Formulación del objetivo:** Encontrar la tubería más cercana de manera optima. 
* **Formulación del problema:** 
    * **Estado inicial:** El estado inicial es "Búsqueda de Tubería", el cual
      empieza en la esquina superior izquierda del tablero.
    * **Descripción de las acciones:** 
      * El agente busca una tubería dentro del tablero
      * El agente solo se acuerda de la distancia más corta hacia una tubería
      desde el espacio donde este
    * **Modelo de transición:** 
      * pass
    * **Test del objetivo:**
      * Si el espacio en que se encuentra el agente es de tipo tubería
    * **Costo de ruta:**
      * pass
    * **Espacio de estados:**
* **Buscar, solucionar, ejecutar:**
      
### 2. Para la parte de buscar, solucionar y ejecutar vimos tres algoritmos de búsqueda no informada: BFS, DFS, e Iterative Deepening. Escoge el algoritmo más apropiado para poder ayudar a Mario y justifica tu decisión.
En este caso lo más eficiente seria usar BFS debido a que pueden existir caminos muy largos que no nos lleven a una tubería.
### 3. Explica de manera escrita y sin demasiados formalismos, cómo tu algoritmo va a funcionar y resolver el problema (me interesa saber cual es tu idea).
_pass_
## Parte Práctica 💻:
_pass_
