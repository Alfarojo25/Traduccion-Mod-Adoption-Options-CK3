# Adoption Options - Traduccion al Espanol

## Descripcion

Traduccion completa al espanol del mod **Adoption Options** para Crusader Kings III.

## Requisitos

- Crusader Kings III version 1.18.0 o superior
- Mod original: [Adoption Options](https://steamcommunity.com/sharedfiles/filedetails/?id=2816662627)

## Instalacion

### Steam Workshop

1. Suscribete a este mod en Steam Workshop
2. Asegurate de tener instalado el mod original "Adoption Options"
3. Activa ambos mods en el launcher del juego
4. **Importante**: Este mod debe cargarse DESPUES del mod original

### Instalacion Manual

1. Descarga el mod desde GitHub
2. Copia la carpeta en: `Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Asegurate de tener instalado el mod original
4. Activa ambos mods en el launcher

## Caracteristicas

- ✅ Traduccion completa de todos los eventos
- ✅ Traduccion de la interfaz de usuario
- ✅ Traduccion de decisiones e interacciones
- ✅ **CORREGIDO:** Encoding UTF-8 con BOM (OBLIGATORIO para CK3)
- ✅ Mantiene compatibilidad con actualizaciones del mod original

## Encoding CORREGIDO (Importante)

**Fecha:** 1 de noviembre de 2025

Todos los archivos de localizacion (.yml) ahora usan **UTF-8 con BOM**, que es el encoding OBLIGATORIO para archivos de localizacion en CK3.

**Problema anterior:**

- Los archivos podian tener encoding incorrecto
- Caracteres espanoles (a, e, i, o, u, n, u, i, i) podian no mostrarse bien en el juego

**Solucion aplicada:**

- Todos los archivos .yml convertidos a UTF-8 con BOM
- Script `fix_encoding.py` incluido para futuras correcciones
- 6 archivos corregidos exitosamente

**Archivos corregidos:**

- ao_events_l_spanish.yml
- ao_gui_l_spanish.yml
- ao_common_l_spanish.yml
- ao_cc_common_l_spanish.yml
- ao_cc_gui_l_spanish.yml
- ao_ttd_common_l_spanish.yml

## Orden de Carga

Para que la traduccion funcione correctamente, asegurate de que el orden de carga sea:

1. Adoption Options (mod original)
2. Adoption Options - Spanish Translation (este mod)

## ⚠️ SOLUCION DE PROBLEMAS

### ¿Ves claves de texto en lugar de traducciones?

Si en el juego ves algo como `doctrine_ao_adoption_prevalence_illegitimate_name` en lugar del texto traducido:

**Causa:** Estructura incorrecta de archivos de localización

**Solución:** Actualiza a la version **1.0.3 o superior**. Esta version corrige:

1. ✅ Archivos en `localization/english/` (no spanish)
2. ✅ Nombres: `*_english.yml` (no *_spanish.yml)
3. ✅ Marcador: `l_english:` (no l_spanish:)
4. ✅ `replace_path="localization/english"` en descriptor.mod

**¿Por qué "english" si es traducción al español?**

Porque `replace_path` reemplaza los archivos ingleses del mod original con nuestras traducciones. El juego carga `localization/english/` y encuentra nuestro español dentro.

### Archivos actuales (v1.0.3):

```
localization/english/
├── ao_events_l_english.yml      # Contiene traducciones españolas
├── ao_gui_l_english.yml         # l_english: con texto en español
├── ao_common_l_english.yml      # UTF-8 con BOM
├── ao_cc_common_l_english.yml
├── ao_cc_gui_l_english.yml
└── ao_ttd_common_l_english.yml
```

Esto le indica a CK3 que debe reemplazar los archivos de localizacion en ingles con los archivos en espanol.

### Otros problemas comunes

- **Asegurate de cargar este mod DESPUES del mod original**
- **Verifica que ambos mods esten activos en el launcher**
- **Reinicia el juego completamente** despues de activar/actualizar los mods

## Contribuir

Si encuentras errores de traduccion o quieres mejorarla:

1. Reporta issues en GitHub
2. Envia pull requests con correcciones
3. Todas las contribuciones son bienvenidas

## Creditos

- **Mod Original**: Adoption Options
- **Traducción**: Alfarojo25
- **Versión del mod traducido**: 11.8

## Licencia

Esta traducción se proporciona gratuitamente para la comunidad de CK3.

## Changelog

### Versión 1.0 (2025-10-31)

- ✨ Traducción inicial completa al español
- 📝 Traducidos todos los archivos de localización
- 🎮 Compatible con versión 11.8 del mod original
