# Adoption Options - Traducción al Español

## Descripción

Traducción completa al español del mod **Adoption Options** para Crusader Kings III.

## ⚠️ REQUISITOS OBLIGATORIOS

Para que este mod funcione correctamente:

1. ✅ **Crusader Kings III** versión 1.18.0 o superior
2. ✅ **Mod original:** [Adoption Options](https://steamcommunity.com/sharedfiles/filedetails/?id=2816662627) instalado y activo
3. ✅ **IDIOMA DEL JUEGO EN ESPAÑOL:**
   - Menú Principal → Opciones → Idioma → **Español**
   - **CRÍTICO**: Si el juego está en otro idioma, la traducción NO funcionará

## 📥 Instalación

### Steam Workshop (Recomendado)

1. Suscríbete al mod original: [Adoption Options](https://steamcommunity.com/sharedfiles/filedetails/?id=2816662627)
2. Suscríbete a este mod de traducción
3. Abre el launcher de CK3
4. Activa ambos mods:
   - ✅ Adoption Options
   - ✅ Adoption Options - Spanish Translation
5. **IMPORTANTE:** Configura CK3 en idioma español
6. Inicia el juego

### Instalación Manual

1. Descarga el mod desde [GitHub](https://github.com/Alfarojo25/Traduccion-Mod-Adoption-Options-CK3)
2. Extrae la carpeta en: `Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Instala el mod original [Adoption Options](https://steamcommunity.com/sharedfiles/filedetails/?id=2816662627)
4. Activa ambos mods en el launcher
5. **IMPORTANTE:** Configura CK3 en idioma español

## ✨ Características

- ✅ Traducción completa de todos los eventos (585 líneas)
- ✅ Traducción de la interfaz de usuario
- ✅ Traducción de decisiones e interacciones
- ✅ Traducción de doctrinas y tipos de adopción
- ✅ Encoding UTF-8 con BOM (obligatorio para CK3)
- ✅ Compatible con Crusader Kings III v1.18.0
- ✅ Compatible con Adoption Options v11.8

## 🔧 Estructura del Mod

```
localization/
└── spanish/
    ├── ao_events_l_spanish.yml      # Eventos de adopción
    ├── ao_gui_l_spanish.yml         # Interfaz gráfica
    ├── ao_common_l_spanish.yml      # Traducciones comunes (más extenso)
    ├── ao_cc_common_l_spanish.yml   # Contenido adicional
    ├── ao_cc_gui_l_spanish.yml      # GUI adicional
    └── ao_ttd_common_l_spanish.yml  # Contenido TTD
```

Todos los archivos usan:

- 📝 Encoding: **UTF-8 con BOM**
- 🏷️ Marcador: **l_spanish:**
- 🌐 Idioma: **Español**

## ⚠️ Solución de Problemas

### ❌ Veo claves de texto en lugar de traducciones

**Ejemplo:** `doctrine_ao_adoption_prevalence_illegitimate_name` en lugar de "Ilegítima"

**Causas posibles:**

1. **El idioma del juego NO está en español** ← Causa más común
   - Solución: Menú → Opciones → Idioma → Español → Reiniciar juego
2. **El mod original "Adoption Options" no está activo**
   - Solución: Activar en el launcher
3. **Orden de carga incorrecto**
   - Solución: "Adoption Options" debe cargarse ANTES que la traducción

### ❌ Los caracteres españoles (áéíóúñ) no se ven bien

**Causa:** Encoding incorrecto (esto YA está corregido en v1.0.4)

**Solución:** Actualiza a la versión 1.0.4 o superior

### ❌ El mod no aparece en el launcher

**Causa:** Archivos mal ubicados

**Solución Instalación Manual:**

```
Documents/
└── Paradox Interactive/
    └── Crusader Kings III/
        └── mod/
            └── Traduccion Adoption Options al Español/
                ├── descriptor.mod
                └── localization/
```

## 📝 Cómo Funciona

Este mod es una **traducción dependiente**. Funciona así:

1. **Adoption Options** (mod original) define:

   - Mecánicas del juego
   - Eventos
   - Decisiones
   - Doctrinas
   - Traits

2. **Este mod** (traducción) proporciona:

   - Textos en español para TODO lo anterior

3. **CK3** carga:
   - Primero el mod original (inglés)
   - Luego la traducción (español)
   - Cuando el idioma está en español, usa nuestros archivos

## 🎮 Contenido Traducido

- 📜 **Eventos de adopción:** 50+ eventos completos
- 🎭 **Interacciones:** Organizar adopción, adopciones compartidas
- ⚖️ **Doctrinas de fe:**
  - Prevalencia de adopción (Prohibida, Ilegítima, Rara, Poco Común, Común)
  - Tipos de adopción (Familial, Casta, Plebeyo, Cualquiera)
- 🏛️ **Decisiones:** Visitar orfanato, adoptar heredero
- 💭 **Tooltips y descripciones:** Completamente traducidos
- 🎨 **Interfaz gráfica:** Botones, opciones, menús

## 📊 Estadísticas

- **Archivos traducidos:** 6
- **Líneas de localización:** 585+
- **Claves traducidas:** 400+
- **Encoding:** UTF-8 con BOM ✅
- **Validado con:** CK3-Tiger v1.13.0

## 🤝 Contribuir

Si encuentras errores de traducción o quieres mejorarla:

1. Reporta issues en [GitHub](https://github.com/Alfarojo25/Traduccion-Mod-Adoption-Options-CK3/issues)
2. Envía pull requests con correcciones
3. Todas las contribuciones son bienvenidas

## 📜 Licencia

Esta traducción se proporciona gratuitamente para la comunidad de CK3.

## 🙏 Créditos

- **Mod Original:** [Adoption Options](https://steamcommunity.com/sharedfiles/filedetails/?id=2816662627)
- **Traducción:** Alfarojo25
- **Versión del mod original:** 11.8
- **Versión de la traducción:** 1.0.4

## 📚 Enlaces

- [GitHub del Proyecto](https://github.com/Alfarojo25/Traduccion-Mod-Adoption-Options-CK3)
- [Mod Original en Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=2816662627)
- [Changelog Completo](CHANGELOG.md)

---

**Última actualización:** 1 de noviembre de 2025 - v1.0.4
