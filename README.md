# DavidSan

Base abierta de `DavidSan`: un agente construido sobre `Phi-4` para ayudarte a comunicar mejor tu valor, tu narrativa profesional y tu propuesta personal sin exponer datos privados.

Este repositorio publica la parte compartible del proyecto: estructura técnica inicial, paquete Python base, tests y lineamientos para crecer en abierto con sugerencias de la comunidad.

## Qué es hoy

`DavidSan` está en una fase temprana. Ahora mismo incluye:

- un paquete Python mínimo en `src/davidsan`
- configuración reproducible con `pyproject.toml`
- tests de humo para validar entorno
- carpetas preparadas para prompts, ejemplos, scripts, configs y documentación

No pretende ser una versión completa del agente todavía. Es una base pública y limpia para iterar en abierto.

## Enfoque del proyecto

La idea detrás de `DavidSan` es construir un asistente que:

- ayude a presentar mejor el valor de una persona o proyecto
- use `Phi-4` como motor base para generación y reformulación
- use contexto elegido de forma deliberada, no extracción indiscriminada de datos
- proteja información privada por defecto
- sea auditable, versionable y mejorable por comunidad

## Qué se publica y qué no

Este repo muestra trabajo real, pero solo la parte segura y compartible.

Sí se publica:

- código base del proyecto
- estructura del paquete y tests
- documentación pública
- prompts y configuraciones no sensibles
- ideas abiertas y dirección técnica

No se publica:

- datos personales reales
- historiales privados o conversaciones identificables
- secretos, tokens o `.env`
- configuraciones locales de uso personal
- memoria privada del agente o material sensible de operación

## Qué contiene el repo

| Carpeta | Propósito |
|---|---|
| `src/` | Código fuente principal del paquete |
| `tests/` | Tests básicos y validación inicial |
| `docs/` | Documentación técnica y funcional |
| `scripts/` | Utilidades de soporte y automatización |
| `prompts/` | Prompts y plantillas no sensibles |
| `configs/` | Configuraciones públicas y seguras |
| `examples/` | Ejemplos de uso y prototipos |

## Principios de publicación

Este repositorio está preparado para publicarse sin exponer datos sensibles:

- no incluye secretos, tokens ni claves
- no incluye datasets privados ni historiales personales
- no incluye variables de entorno reales
- no incluye salidas pesadas, artefactos o logs operativos

Si propones una contribución, por favor evita subir cualquier dato personal identificable.

## Instalación

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Verificación rápida

```bash
pytest
```

## Estado

Estado actual:

- paquete Python base creado
- estructura del proyecto definida
- tests de humo funcionando
- documentación pública inicial lista para revisión

Próximos pasos razonables:

- añadir módulos reales del asistente
- definir contratos de entrada y salida
- incorporar ejemplos de prompts seguros
- ampliar la integración operativa con `Phi-4`
- publicar una arquitectura inicial de privacidad y gobernanza ligera

## Comunidad

Las sugerencias son bienvenidas. Puedes abrir:

- `Issues` para bugs, ideas o preguntas
- `Pull Requests` para mejoras concretas

Revisa [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) y [SECURITY.md](SECURITY.md) antes de contribuir.

## Licencia

Este proyecto se publica bajo licencia MIT. Consulta [LICENSE](LICENSE).
