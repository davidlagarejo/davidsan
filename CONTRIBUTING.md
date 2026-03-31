# Contributing

Gracias por interesarte en mejorar `DavidSan`.

## Cómo contribuir

- abre un `issue` antes de hacer cambios grandes
- mantén los cambios pequeños y enfocados
- explica el problema, la decisión y el impacto esperado
- añade o actualiza tests cuando cambie el comportamiento
- evita incluir secretos, datos personales o material privado

## Tipos de contribución útiles

- mejoras en documentación
- propuestas de arquitectura
- tests y validaciones
- utilidades de desarrollo
- prompts y ejemplos no sensibles
- mejoras relacionadas con integraciones sobre `Phi-4`
- mejoras de privacidad y seguridad

## Setup local

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Estilo de cambios

- Python `3.12+`
- cambios claros, legibles y fáciles de revisar
- documentación alineada con el comportamiento real
- nada de datos personales reales en ejemplos o fixtures

## Pull requests

Incluye en tu PR:

- qué problema resuelve
- qué cambió exactamente
- cómo se verificó
- riesgos o límites conocidos

## Discusión abierta

Este proyecto está en etapa temprana. Las sugerencias sobre producto, privacidad, UX del asistente y diseño del repositorio son especialmente valiosas.
