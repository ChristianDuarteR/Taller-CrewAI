# Triage de tickets con CrewAI

El proyecto está separado en módulos pequeños:

- `models.py`: esquema de salida con Pydantic.
- `agent.py`: configuración del agente.
- `task.py`: prompt y reglas de negocio.
- `crew.py`: orquestación del crew.
- `tickets.py`: tickets de prueba.
- `main.py`: ejecución principal.
- `Taller.py`: punto de entrada compatible con el archivo original.

## Instalación en Windows

La versión actual del proyecto usa CrewAI `0.11.2`, que necesita dependencias
que no son compatibles con Python 3.14. Instala Python 3.12 y crea el entorno
virtual con ese intérprete:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Después ejecuta:

```powershell
python Taller.py
```

CrewAI también necesita las credenciales del proveedor LLM configurado antes de
kickoff, por ejemplo `OPENAI_API_KEY` si se usa el proveedor predeterminado.