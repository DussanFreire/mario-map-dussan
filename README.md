# mario-map-dussan

_En este proyecto se hizo la resolución del la práctica número 2 de la asignatura "Sistemas Inteligentes" dirigida por el docente Gerard Salinas Joan Sebastian en la UCB Cochabamba._

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
