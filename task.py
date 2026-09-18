from crewai import Task

from agent import triage_agent
from models import TicketTriageResult


triage_task = Task(
    description="""
    Analiza detalladamente el siguiente ticket de soporte enviado por un usuario de Aurora SaaS:

    ---
    TICKET DE ENTRADA:
    "{ticket_text}"
    ---

    Usa ESTRICTAMENTE las siguientes tablas de negocio para determinar tu respuesta:

    TABLA 1 · Categorías y Equipo Destino:
    - Facturación -> Finanzas
    - Acceso y cuentas -> Identity
    - Rendimiento -> Plataforma
    - Integraciones -> Integraciones
    - Datos y reportes -> Datos
    - Interfaz / uso -> Producto
    - Fuera de alcance -> Ninguno (redirigir)

    TABLA 2 · Políticas de SLA por Severidad:
    - Crítica: Servicio caído o pérdida de datos para múltiples usuarios. (SLA Respuesta: 1 hora | SLA Resolución: 4 horas)
    - Alta: Función clave bloqueada, sin alternativa disponible. (SLA Respuesta: 4 horas | SLA Resolución: 24 horas)
    - Media: Función degradada, o bloqueada pero con alternativa. (SLA Respuesta: 8 horas | SLA Resolución: 72 horas)
    - Baja: Consulta, mejora o defecto menor. (SLA Respuesta: 24 horas | SLA Resolución: 10 días hábiles)
    - Fuera de alcance: No es un problema de la plataforma. (SLA Respuesta: Redirigir | SLA Resolución: No aplica)

    INSTRUCCIONES ADICIONALES:
    1. Determina la categoría y su equipo destino mapeado.
    2. Asigna la severidad evaluando el impacto real reportado en el ticket frente a la Tabla 2.
    3. Copia textualmente los tiempos de SLA de respuesta y resolución correspondientes a dicha severidad.
    4. Genera un borrador corto y empático de primera respuesta para informarle al usuario que su caso fue recibido y remitido al equipo correcto.
    """,
    expected_output="Un objeto estructurado con categoría, equipo_destino, severidad, sla_respuesta, sla_resolucion y borrador_respuesta.",
    agent=triage_agent,
    output_json=TicketTriageResult,
)