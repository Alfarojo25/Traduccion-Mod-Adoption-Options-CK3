# Changelog - Adoption Options Spanish Translation

## [1.0.3] - 2025-11-01

### 🔧 Corregido

- **CRITICO:** Archivos movidos de `localization/spanish/` a `localization/english/`
- **CRITICO:** Nombres de archivos cambiados de `*_spanish.yml` a `*_english.yml`
- **CRITICO:** Primera línea cambiada de `l_spanish:` a `l_english:`
- Ahora los archivos reemplazan correctamente los archivos en inglés del mod original
- Las traducciones finalmente se cargan correctamente en el juego

### 📝 Explicación Técnica

El problema era que CK3 busca archivos de localización por idioma del juego. Aunque `replace_path="localization/english"` estaba configurado, nuestros archivos estaban en `localization/spanish/` con nombres `*_spanish.yml` y marcador `l_spanish:`.

**Solución aplicada:**

1. Carpeta renombrada: `spanish/` → `english/`
2. Archivos renombrados: `*_spanish.yml` → `*_english.yml`
3. Marcador cambiado: `l_spanish:` → `l_english:`

Ahora el mod reemplaza directamente los archivos ingleses con las traducciones españolas.

### 🎮 Compatible con

- Crusader Kings III version 1.18.0
- Adoption Options version 11.8

### 📝 Notas

- Hotfix CRITICO - Tercera corrección necesaria
- **Actualización OBLIGATORIA** para que funcione la traducción

## [1.0.2] - 2025-11-01

### 🔧 Corregido

- **CRITICO:** Agregado `replace_path="localization/english"` al descriptor.mod
- Las traducciones ahora se cargan correctamente en el juego
- Las doctrinas de fe reformadas ahora muestran texto en español en vez de las claves de localización

### 🎮 Compatible con

- Crusader Kings III version 1.18.0
- Adoption Options version 11.8

### 📝 Notas

- Version de hotfix CRITICA
- **Recomendado actualizar inmediatamente** si ves claves de texto en lugar de traducciones

## [1.0.1] - 2025-11-01

### 🔧 Corregido

- **CRITICO:** Encoding de todos los archivos .yml corregido a UTF-8 con BOM (obligatorio en CK3)
- Problema donde caracteres espanoles (a, e, i, o, u, n, u, i, i) podian no mostrarse correctamente
- 6 archivos de localizacion convertidos a UTF-8 con BOM:
  - ao_events_l_spanish.yml
  - ao_gui_l_spanish.yml
  - ao_common_l_spanish.yml
  - ao_cc_common_l_spanish.yml
  - ao_cc_gui_l_spanish.yml
  - ao_ttd_common_l_spanish.yml

### ✨ Agregado

- Script `fix_encoding.py` para futuras correcciones de encoding
- Documentacion sobre encoding correcto en README.md

### 🎮 Compatible con

- Crusader Kings III version 1.18.0
- Adoption Options version 11.8

### 📝 Notas

- Version de mantenimiento CRITICA
- **Recomendado actualizar inmediatamente** para evitar problemas de visualizacion
- El encoding UTF-8 con BOM es OBLIGATORIO para archivos de localizacion en CK3

---

## [1.0.0] - 2025-10-31

### ✨ Agregado

- Traduccion completa al espanol de todos los archivos de localizacion
- Archivo `ao_common_l_spanish.yml` - Textos comunes generales e interacciones (✅ 100%)
- Archivo `ao_events_l_spanish.yml` - Todos los eventos de adopcion y fertilidad compartida (✅ 100%)
- Archivo `ao_gui_l_spanish.yml` - Interfaz de usuario general (✅ 100%)
- Archivo `ao_cc_common_l_spanish.yml` - Textos comunes de contenido especial (✅ 100%)
- Archivo `ao_cc_gui_l_spanish.yml` - Interfaz de usuario especial (✅ 100%)
- Archivo `ao_ttd_common_l_spanish.yml` - Textos comunes adicionales (✅ 100%)
- README.md con instrucciones de instalacion
- LICENSE (MIT) - Alfarojo25
- Documentacion completa en carpeta Documentacion/

### 🎮 Compatible con

- Crusader Kings III version 1.17.\*
- Adoption Options version 11.8

### 📝 Notas

- Primera version publica
- Traduccion basada en los archivos de localizacion inglesa del mod original
- Requiere el mod original "Adoption Options" instalado

---

## Formato de versiones

Este proyecto usa [Semantic Versioning](https://semver.org/):

- MAJOR.MINOR.PATCH
- MAJOR: Cambios incompatibles
- MINOR: Nueva funcionalidad compatible
- PATCH: Correcciones de bugs
