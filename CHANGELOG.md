# Changelog - Adoption Options Spanish Translation

## [1.0.4] - 2025-11-01

### 🔧 Corregido - VERSIÓN FINAL CORRECTA

- **CRITICO:** Archivos movidos CORRECTAMENTE a `localization/spanish/` (estaban mal en `english/`)
- **CRITICO:** Nombres corregidos a `*_spanish.yml` (estaban mal como `*_english.yml`)
- **CRITICO:** Marcador corregido a `l_spanish:` (estaba mal como `l_english:`)
- **CRITICO:** Eliminado `replace_path` del descriptor.mod (no es necesario)
- Mod ahora funciona correctamente como traducción dependiente

### 📝 Explicación Técnica - ¿Qué estaba mal?

**Versiones 1.0.1 - 1.0.3: INCORRECTAS**

El error fue intentar "reemplazar" archivos ingleses. Las traducciones de CK3 NO funcionan así.

**Cómo funciona CORRECTAMENTE:**

CK3 carga archivos de localización según el idioma configurado:
- Idioma en Inglés → carga `localization/english/*_l_english.yml`
- Idioma en Español → carga `localization/spanish/*_l_spanish.yml`
- Idioma en Alemán → carga `localization/german/*_l_german.yml`

**Estructura CORRECTA (v1.0.4):**
```
localization/
└── spanish/              ← Carpeta del idioma español
    ├── ao_events_l_spanish.yml
    ├── ao_gui_l_spanish.yml
    ├── ao_common_l_spanish.yml
    ├── ao_cc_common_l_spanish.yml
    ├── ao_cc_gui_l_spanish.yml
    └── ao_ttd_common_l_spanish.yml
```

Cada archivo empieza con `l_spanish:` y contiene las traducciones españolas.

### ⚠️ REQUISITOS OBLIGATORIOS

Para que este mod funcione **DEBES**:

1. ✅ Tener instalado y activo: **Adoption Options** (mod original)
2. ✅ Tener instalado y activo: **Adoption Options - Spanish Translation** (este mod)
3. ✅ **CONFIGURAR CK3 EN IDIOMA ESPAÑOL:**
   - Menú Principal → Opciones → Idioma → **Español**
4. ✅ Reiniciar el juego después de cambiar el idioma

**SI NO CAMBIAS EL IDIOMA A ESPAÑOL, NO FUNCIONARÁ**

CK3 solo carga archivos `l_spanish:` cuando el idioma está en español.

### 🎮 Compatible con

- Crusader Kings III versión 1.18.0
- Adoption Options versión 11.8

### 📝 Notas Importantes

- Esta es la versión CORRECTA y FINAL
- Las versiones 1.0.1, 1.0.2 y 1.0.3 tenían la estructura INCORRECTA
- Validado con CK3-Tiger (los errores son normales en mods de traducción)
- Basado en la estructura del mod alemán (Ultimate German Translation Mod)

---

## [1.0.3] - 2025-11-01 ❌ VERSIÓN INCORRECTA

**NO USAR ESTA VERSIÓN** - Estructura incorrecta

---

## [1.0.2] - 2025-11-01 ❌ VERSIÓN INCORRECTA

**NO USAR ESTA VERSIÓN** - Estructura incorrecta

---

## [1.0.1] - 2025-11-01 ❌ VERSIÓN INCORRECTA

**NO USAR ESTA VERSIÓN** - Tenía problemas de encoding y espacios

---

## [1.0.0] - 2025-10-31 ❌ VERSIÓN INCORRECTA

**NO USAR ESTA VERSIÓN** - Primera versión con errores
