# Semana 9: Pilas y Colas en Python

**Práctica guiada y retos en equipo** · Programación Estructurada · Unidad III: Estructuras de Datos

| | |
|---|---|
| **Lenguaje** | Python 3.13.2 |
| **Entorno** | Visual Studio Code |
| **Sesiones** | 25, 26 y 27 (12, 14 y 16 de octubre de 2026) |
| **Evaluación** | Formativa, sin puntaje |

## Integrantes

1. Roberto Rafael Sobalvarro Gutiérrez
2. Carlos Raúl Cerda Elizondo
3. Santiago José Centeno Meléndez
4. Jorge Luis Acevedo Pulido

Cada integrante aportó mediante commits propios, que pueden verificarse en el historial de este repositorio.

## Objetivo

Implementar estructuras de datos lineales de tipo **pila** y **cola** en Python, mediante operaciones de inserción, eliminación y consulta, para resolver problemas sencillos de gestión de información (indicador IL3.3).

## Estructura del repositorio

```
Semana9_Pilas_Colas_EquipoN/
├── pila_guiada.py
├── reto1_bodega.py
├── pila_acciones.py
├── reto2_navegador.py
├── cola_guiada.py
├── reto3_atencion.py
├── README.md
└── evidencias/
    ├── simulacion_pila.png
    ├── simulacion_cola.png
    └── pruebas/
```

## Descripción de los programas

### Sesión 25: Pilas

**`pila_guiada.py`: Mi primera pila (libros de una biblioteca).**
Menú para apilar un libro (el nombre se pide con `input()`), desapilar, mostrar la pila con su tope y salir. Si se intenta desapilar con la pila vacía, avisa y no genera error.

**`reto1_bodega.py`: Reto 1, control de cajas en una bodega.**
Sistema de consola que respeta LIFO, con menú para apilar cajas, desapilar, consultar el tope, mostrar la pila y salir.
- Cada caja tiene un código único: rechaza códigos vacíos y duplicados.
- La bodega tiene una capacidad máxima de 5 cajas y avisa cuando la pila está llena.
- No retira cajas cuando la pila está vacía.
- Al mostrar la pila dibuja las cajas de arriba hacia abajo (la primera es el tope) e indica la cantidad de cajas.
- Las operaciones están separadas en funciones (`push`, `pop_stack`, `peek`, `isEmpty`, `isFull`, `showStack`).

### Sesión 26: Pilas (aplicaciones)

**`pila_acciones.py`: Deshacer acciones (editor de texto).**
Cada acción se guarda en una pila para poder deshacer la última. Menú para registrar una acción, deshacer la última, mostrar las acciones pendientes (numeradas) y salir. Valida que la descripción no esté vacía, que la opción sea un número entero y controla el caso de no tener acciones que deshacer.

**`reto2_navegador.py`: Reto 2, historial de navegación.**
Simulador de navegación que usa una pila para regresar a páginas anteriores. Menú para visitar una página nueva, regresar, consultar la página actual, mostrar el historial de retroceso y salir. No permite regresar si no hay páginas anteriores ni registrar una dirección vacía.

Prueba obligatoria: visitar `uam.edu.ni`, `python.org` y `github.com`, y regresar tres veces.

```
Regresaste a: python.org
Regresaste a: uam.edu.ni
No existen páginas anteriores.
```

### Sesión 27: Colas

**`cola_guiada.py`: Mi primera cola (pacientes de una clínica).**
Cola con `collections.deque` y atención en orden de llegada. Menú para registrar un paciente, atender al siguiente, mostrar los pacientes en espera (numerados) y salir.

**`reto3_atencion.py`: Reto 3, sistema de atención al cliente.**
Cola FIFO con `collections.deque` en la que cada cliente recibe un número de turno automático. Menú para:
- registrar cliente (rechaza nombres vacíos);
- atender al siguiente cliente;
- consultar al próximo cliente sin retirarlo;
- mostrar los clientes en espera;
- mostrar la cantidad de pendientes;
- salir.

Maneja la cola vacía sin errores y repite el menú hasta que se elige salir.

## Cómo ejecutar

1. Instalar Python 3.13.2 y abrir la carpeta del repositorio en Visual Studio Code.
2. Abrir una terminal en esa carpeta.
3. Ejecutar el programa que se quiera probar:

```bash
python pila_guiada.py
python reto1_bodega.py
python pila_acciones.py
python reto2_navegador.py
python cola_guiada.py
python reto3_atencion.py
```

4. Seguir el menú que aparece en pantalla e ingresar el número de la opción.

> **Nota:** `pila_guiada.py` y `reto1_bodega.py` limpian la pantalla con el comando `cls`, por lo que están pensados para ejecutarse en **Windows**. En Linux o macOS el comando no existe, aunque el programa sigue funcionando sin limpiar la pantalla.

## LIFO y FIFO

### Pila (LIFO: *Last In, First Out*)

El **último** elemento en entrar es el **primero** en salir. Se trabaja siempre por un solo extremo, llamado **tope**. Como una pila de libros: el último que se coloca encima es el primero que se retira.

| Operación | En Python | Programa |
|---|---|---|
| Apilar (insertar) | `lista.append(x)` | todos los de pila |
| Desapilar (eliminar) | `lista.pop()` | todos los de pila |
| Consultar el tope | `lista[-1]` | `reto1_bodega.py`, `pila_guiada.py` |

Se usa en: deshacer acciones de un editor, el botón «atrás» de un navegador, apilar cajas.

### Cola (FIFO: *First In, First Out*)

El **primer** elemento en entrar es el **primero** en salir. Se inserta por el final y se retira por el frente. Como la fila de una clínica: se atiende en orden de llegada.

| Operación | En Python | Programa |
|---|---|---|
| Encolar (insertar) | `cola.append(x)` | `cola_guiada.py`, `reto3_atencion.py` |
| Desencolar (eliminar) | `cola.popleft()` | `cola_guiada.py`, `reto3_atencion.py` |
| Consultar el frente | `cola[0]` | `reto3_atencion.py` |

Se usa en: turnos de atención al cliente, pacientes en espera, tareas pendientes.

### ¿Por qué `deque` para la cola?

Con una lista normal, `pop(0)` obliga a mover todos los elementos restantes. `collections.deque` está diseñado para insertar y retirar por ambos extremos de forma eficiente con `append()` y `popleft()`.

### Diferencia entre `pop()` y `popleft()`

- `pop()` retira el **último** elemento (comportamiento de pila).
- `popleft()` retira el **primero** (comportamiento de cola).

Si la clínica usara una pila, se atendería primero al último paciente en llegar y los primeros pacientes esperarían indefinidamente.

### ¿Cuándo conviene cada una?

- **Pila:** cuando importa deshacer o volver al paso más reciente.
- **Cola:** cuando importa respetar el orden de llegada.

## Evidencias

La carpeta `evidencias/` contiene:

- `simulacion_pila.png`: simulación gráfica de al menos cinco cajas.
- `simulacion_cola.png`: simulación gráfica de cinco clientes.
- `pruebas/`: capturas de las pruebas ejecutadas, incluida la prueba obligatoria del Reto 2.

## Referencias

- Joyanes, L. (2008). *Fundamentos de Programación* (4.ª ed.), cap. 12, pp. 429–477. McGraw-Hill.
- Runestone Academy: https://runestone.academy/ns/books/published/pythoned/index.html
- VisuAlgo: https://visualgo.net/en
- Documentación oficial de `collections.deque`: https://docs.python.org/3/library/collections.html#collections.deque
