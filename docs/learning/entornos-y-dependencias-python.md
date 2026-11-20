# Entornos virtuales y gestión de dependencias en Python

> **Estado:** Draft — pendiente de revisión y validación por el propietario del proyecto.
> **Tipo:** concepto general. Su aplicación en CompAI se documenta en los ADR enlazados al final.

## 1. El problema

Un proyecto Python depende de un intérprete concreto y de paquetes de terceros en versiones concretas.

Si todos los proyectos comparten la misma instalación de Python, aparecen conflictos: el proyecto A necesita `requests 2.31` y el proyecto B necesita `requests 2.25`, y solo puede haber una versión instalada a la vez. Además, "en mi máquina funciona" deja de ser reproducible en otra.

Hacen falta dos cosas:

1. **Aislamiento:** cada proyecto con sus propios paquetes.
2. **Reproducibilidad:** poder reconstruir exactamente el mismo conjunto de paquetes en otro momento o en otra máquina.

## 2. Entorno virtual

Un entorno virtual es un directorio que contiene:

- Una referencia al intérprete de Python base (o una copia).
- Su propio directorio `site-packages`, donde se instalan los paquetes del proyecto.
- Scripts y ejecutables (en Windows, en `Scripts/`; en Linux y macOS, en `bin/`).
- Un fichero `pyvenv.cfg` que describe con qué intérprete se creó.

Los paquetes instalados dentro del entorno no afectan al Python del sistema ni a otros proyectos.

**Activar** un entorno solo modifica variables de la terminal (como `PATH`) para que `python` apunte al intérprete del entorno. No es obligatorio: también se puede invocar ese intérprete directamente.

### `.venv`

`.venv` es el nombre convencional del entorno virtual cuando vive dentro del propio proyecto.

- **No se versiona** en Git: contiene ficheros dependientes de la máquina y se puede regenerar.
- Es **desechable**: si se borra, se reconstruye a partir de la descripción del proyecto.

## 3. Declarar dependencias: `pyproject.toml`

`pyproject.toml` es el fichero estándar de configuración de un proyecto Python (PEP 518 y PEP 621). En su tabla `[project]` se declara, entre otras cosas:

- `name` y `version` del proyecto.
- `requires-python`: rango de versiones de Python compatibles (por ejemplo, `>=3.13`).
- `dependencies`: paquetes que el proyecto necesita, normalmente como **rangos** (por ejemplo, `typer>=0.12`).

Los rangos expresan qué versiones son *aceptables*, no cuál se instala exactamente.

## 4. Fijar versiones exactas: el lockfile

Un **lockfile** registra el resultado de resolver esos rangos: la versión **exacta** de cada paquete, incluidas las dependencias indirectas (las dependencias de tus dependencias), con hashes para verificar su integridad.

| | `pyproject.toml` | Lockfile |
|---|---|---|
| Lo escribe | La persona (o una herramienta a petición suya) | La herramienta, automáticamente |
| Contiene | Rangos de dependencias directas | Versiones exactas de todo el árbol |
| Propósito | Expresar intención | Garantizar reproducibilidad |
| ¿Se versiona? | Sí | Sí |
| ¿Se edita a mano? | Sí | No |

Analogía: `pyproject.toml` es la lista de la compra ("leche entera, cualquier marca"); el lockfile es el ticket ("Leche X, 1 L, lote 123").

## 5. uv

uv es una herramienta que reúne en un solo programa tareas que tradicionalmente se hacían con herramientas separadas (`venv`, `pip`, `pip-tools`, etc.):

- Crear y gestionar el entorno virtual del proyecto.
- Resolver dependencias y generar el lockfile (`uv.lock`).
- Instalar exactamente lo que indica el lockfile.
- Ejecutar comandos dentro del entorno.

`uv.lock` tiene un formato propio de uv, es multiplataforma y no debe editarse a mano.

### `uv sync`

Pone el entorno en el estado que describe el proyecto:

1. Crea `.venv` si no existe.
2. Comprueba que `uv.lock` es coherente con `pyproject.toml` y lo actualiza si es necesario.
3. Instala en `.venv` exactamente lo que indica el lockfile.

> **Verificado en la práctica (uv 0.13.9, propietario del proyecto):** tras borrar `.venv`, `uv sync` lo reconstruye correctamente a partir de `pyproject.toml` y `uv.lock`.

Es el comando para "dejar el entorno como debe estar", por ejemplo después de clonar el repositorio.

### `uv run <comando>`

Ejecuta un comando dentro del entorno del proyecto **sin necesidad de activarlo**. Antes de ejecutarlo, comprueba que el entorno está sincronizado con el lockfile.

Ejemplo: `uv run python --version` usa el intérprete de `.venv`, no el del sistema.

## 6. Flujo resumido

```
pyproject.toml  ──(resolución)──►  uv.lock  ──(uv sync)──►  .venv
 (intención)                        (exacto)                (instalado)
                                                              ▲
                                                 uv run ──────┘ (ejecuta dentro)
```

## 7. Ideas clave

- El entorno virtual aísla; el lockfile hace reproducible.
- `.venv` es desechable y no se versiona; `pyproject.toml` y `uv.lock` sí se versionan.
- No hace falta activar el entorno si se usa `uv run`.

## 8. Fuentes

- Python — `venv`: https://docs.python.org/3/library/venv.html
- PEP 621 — metadatos en `pyproject.toml`: https://peps.python.org/pep-0621/
- Documentación de uv: https://docs.astral.sh/uv/

## Aplicación en CompAI

- Versión de Python: [ADR-0001](../adr/0001-python-version.md). Uso de uv: [ADR-0002](../adr/0002-uv.md).
- Observación sobre el estado actual: `pyproject.toml` no tiene `[build-system]`. Por eso uv gestiona el entorno y las dependencias, pero no instala CompAI como paquete. Se estudiará al diseñar `src/`.
