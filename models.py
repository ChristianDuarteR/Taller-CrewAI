from pydantic import BaseModel, Field


class TicketTriageResult(BaseModel):
    categoria: str = Field(
        ...,
        description="Categoría elegida de Tabla 1 o 'Fuera de alcance'.",
    )
    equipo_destino: str = Field(
        ...,
        description="Equipo destino mapeado de Tabla 1 o 'Ninguno (redirigir)'.",
    )
    severidad: str = Field(
        ...,
        description="Severidad elegida de Tabla 2 (Crítica, Alta, Media, Baja, Fuera de alcance).",
    )
    sla_respuesta: str = Field(
        ..., description="Tiempo máximo de respuesta según la severidad."
    )
    sla_resolucion: str = Field(
        ..., description="Tiempo máximo de resolución según la severidad."
    )
    borrador_respuesta: str = Field(
        ...,
        description="Borrador opcional y amable de primera respuesta para el cliente.",
    )