# Curso de Videojuegos – Introducción

## Índice

1. ¿Qué es un videojuego?
2. ¿Cómo funciona un videojuego?
3. Ejemplos de Código
4. Taxonomía MDA
5. Mecánicas
6. Dinámicas
7. Resumen de Conceptos

---

# ¿Qué es un videojuego?

Un videojuego es un sistema interactivo compuesto por **mecánicas** (reglas, componentes y acciones posibles) y **dinámicas** (comportamientos emergentes del sistema) que se ejecutan de forma continua dentro de un **bucle principal**.  
Su fin es generar una **experiencia estética** que involucre al jugador mediante interacción en tiempo real.

---

# ¿Cómo funciona un videojuego?

Un videojuego opera mediante un ciclo continuo conocido como **Game Loop**, que ejecuta tres pasos fundamentales:

1. **Procesar Entrada**: Detectar interacciones del jugador.
2. **Actualizar Estado del Juego**: Posiciones, físicas, reglas, colisiones, IA.
3. **Renderizar**: Mostrar el estado actualizado en pantalla.

Este ciclo ocurre decenas o cientos de veces por segundo.

---

# Ejemplos de Código

## Ejemplo 1 – Bucle básico

Código en C# que representa un bucle de juego mínimo:

```csharp
using System;

class Program
{
    static void Main()
    {
        // Ejemplo simple de bucle de juego
        while (true)
        {
            // 1. Procesar entrada
            // 2. Actualizar estado del juego
            // 3. Renderizar en pantalla

            // Este es el ciclo fundamental de todo videojuego
            System.Threading.Thread.Sleep(16); // Aproximadamente 60 FPS
        }
    }
}
```

## Ejemplo 2

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;

        while (true)
        {
            Console.Clear();
            Console.WriteLine("Usa ← (a) o → (d) para mover al jugador:\n");

            // Dibuja jugador estático
            Console.WriteLine("👾");

            System.Threading.Thread.Sleep(100);
        }
    }
}
```

# Taxonomía MDA

La **taxonomía MDA** es un marco formal que analiza un videojuego desde tres perspectivas principales.

## 1. Mecánicas (Mechanics)

Reglas, datos y algoritmos que definen el funcionamiento del juego.

Ejemplos:

- Movimiento
- Saltos
- Física
- Puntos de vida
- Inteligencia Artificial (IA)
- Colisiones

## Ejemplo 3 – Mvimiento en Consola

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        int posicion = 5;

        while (true)
        {
            Console.Clear();
            Console.WriteLine("Usa ← (a) o → (d) para mover al jugador:\n");

            // Dibuja posición actual
            for (int i = 0; i < posicion; i++)
                Console.Write(" ");
            Console.WriteLine("👾");

            // Lectura de teclado sin bloquear
            if (Console.KeyAvailable)
            {
                var tecla = Console.ReadKey(true).Key;

                // Mecánicas de movimiento
                if (tecla == ConsoleKey.A) posicion--;
                if (tecla == ConsoleKey.D) posicion++;
            }

            // Mecánica de límites
            posicion = Math.Clamp(posicion, 0, 20);

            System.Threading.Thread.Sleep(50);
        }
    }
}
```

## 2. Dinámicas (Dynamics)

Comportamientos que emergen cuando las mecánicas interactúan entre sí y con el jugador.

Ejemplos:

- Esquivar
- Explorar
- Competir
- Optimizar

## 3. Estéticas (Aesthetics)

Emociones y experiencias que se busca generar en el jugador.

Ejemplos:

- Tensión
- Sorpresa
- Fantasía
- Desafío
- Expresión

##Ejemplo 4 - Obstaculos

```csharp
using System;
using System.Threading;

internal class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.CursorVisible = false;

        // Configuración del área de juego
        int ancho = 30;
        int alto = 15;

        // Posiciones iniciales
        int jugadorX = 5;
        int jugadorY = 5;

        int obstX = ancho - 3;
        int obstY = 5;

        Console.Clear();

        // ==========================
        // DIBUJA EL CONTORNO UNA VEZ
        // ==========================
        for (int y = 0; y < alto; y++)
        {
            for (int x = 0; x < ancho; x++)
            {
                if (y == 0 || y == alto - 1 || x == 0 || x == ancho - 1)
                    Console.Write("█");
                else
                    Console.Write(" ");
            }
            Console.WriteLine();
        }

        while (true)
        {
            // ============================
            // BORRAR POSICIÓN ANTERIOR
            // ============================
            Console.SetCursorPosition(jugadorX, jugadorY);
            Console.Write(" ");

            Console.SetCursorPosition(obstX, obstY);
            Console.Write(" ");

            // ============================
            // INPUT DEL JUGADOR
            // ============================
            if (Console.KeyAvailable)
            {
                var key = Console.ReadKey(true).Key;

                // Mecánicas de control
                if (key == ConsoleKey.A) jugadorX--;
                if (key == ConsoleKey.D) jugadorX++;
                if (key == ConsoleKey.W) jugadorY--;
                if (key == ConsoleKey.S) jugadorY++;

                // Mecánica de límites
                jugadorX = Math.Clamp(jugadorX, 1, ancho - 2);
                jugadorY = Math.Clamp(jugadorY, 1, alto - 2);
            }

            // ============================
            // MOVER OBSTÁCULO (Dinámica)
            // ============================
            obstX--;

            // Dinámica de respawn del obstáculo
            if (obstX <= 1)
            {
                obstX = ancho - 3;
                obstY = new Random().Next(1, alto - 2);
            }

            // ============================
            // DIBUJAR NUEVAS POSICIONES
            // ============================
            Console.SetCursorPosition(jugadorX, jugadorY);
            Console.Write("@");

            Console.SetCursorPosition(obstX, obstY);
            Console.Write("#");

            // ============================
            // COLISIÓN (Dinámica emergente)
            // ============================
            if (jugadorX == obstX && jugadorY == obstY)
            {
                Console.SetCursorPosition(0, alto);
                Console.WriteLine("Has sido golpeado");
                Console.WriteLine("Juego Terminado");
                break;
            }

            Thread.Sleep(60);
        }

        Console.CursorVisible = true;
        Console.WriteLine("\nPresiona cualquier tecla para salir...");
        Console.ReadKey();
    }
}

```
