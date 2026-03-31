# DavidSan

`DavidSan` es un agente construido sobre `Phi-4` para ayudarte a convertir contexto personal y profesional en una narrativa más clara, útil y presentable, sin exponer datos privados.

La intención del proyecto es simple: usar IA para expresar mejor lo que una persona hace, cómo piensa y por qué aporta valor, pero sin convertir esa ayuda en una fuga de información.

Este repositorio contiene la parte pública y compartible del proyecto: base técnica, estructura inicial del paquete, tests, documentación y espacio para crecer en abierto con feedback de la comunidad.

## Por qué existe

Muchas herramientas ayudan a escribir mejor, pero pocas están pensadas para representar a una persona con criterio, contexto elegido y privacidad por defecto.

`DavidSan` nace para explorar justo eso:

- convertir experiencia y contexto en mensajes más claros
- ayudar a presentar valor sin exagerar ni sobreexponer
- usar IA como apoyo de formulación, no como sustituto de identidad
- construir una base técnica abierta que otros puedan revisar y mejorar

## Qué intenta resolver

`DavidSan` apunta a casos como:

- redactar una mejor presentación profesional
- reformular una propuesta de valor personal
- sintetizar experiencia en un tono más claro y sólido
- convertir contexto disperso en mensajes utilizables
- experimentar con asistentes personales que no dependan de publicar datos sensibles

## Qué es hoy

`DavidSan` está en una fase temprana. Ahora mismo incluye:

- un paquete Python mínimo en `src/davidsan`
- configuración reproducible con `pyproject.toml`
- tests de humo para validar entorno
- carpetas preparadas para prompts, ejemplos, scripts, configs y documentación

No es todavía una implementación completa del agente. Es una base pública, limpia y verificable para construir en abierto.

## Enfoque del proyecto

La dirección del proyecto hoy es construir un asistente que:

- ayude a presentar mejor el valor de una persona o proyecto
- use `Phi-4` como motor base para generación y reformulación
- use contexto elegido de forma deliberada, no extracción indiscriminada de datos
- proteja información privada por defecto
- sea auditable, versionable y mejorable por comunidad

## Qué hace interesante este repo

Aunque el proyecto esté en fase inicial, este repo ya muestra varias cosas útiles de cara a comunidad, colaboradores o recruiters:

- una idea concreta con criterio de producto
- una preocupación explícita por privacidad
- una base técnica reproducible
- intención de abrir diseño, no solo resultado final
- una forma seria de publicar trabajo en progreso

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

## Cómo correrlo localmente

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Principios de publicación

Este repositorio está preparado para publicarse sin exponer datos sensibles:

- no incluye secretos, tokens ni claves
- no incluye datasets privados ni historiales personales
- no incluye variables de entorno reales
- no incluye salidas pesadas, artefactos o logs operativos

Si propones una contribución, por favor evita subir cualquier dato personal identificable.

## Estado

Estado actual:

- paquete Python base creado
- estructura del proyecto definida
- tests de humo funcionando
- documentación pública inicial lista para revisión

Siguientes pasos razonables:

- añadir módulos reales del asistente
- definir contratos de entrada y salida
- incorporar ejemplos de prompts seguros
- ampliar la integración operativa con `Phi-4`
- publicar una arquitectura inicial de privacidad y gobernanza ligera

## Roadmap abierto

Busco especialmente sugerencias sobre:

- diseño del flujo del agente
- estructura de prompts y evaluación
- límites de privacidad y sanitización
- experiencia de uso para perfil profesional y storytelling
- empaquetado del proyecto como herramienta reusable

## Comunidad

Las sugerencias son bienvenidas. Puedes abrir:

- `Issues` para bugs, ideas o preguntas
- `Pull Requests` para mejoras concretas

Revisa [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) y [SECURITY.md](SECURITY.md) antes de contribuir.

## Licencia

Este proyecto se publica bajo licencia MIT. Consulta [LICENSE](LICENSE).
