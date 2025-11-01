#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para cambiar l_spanish: a l_english: en archivos YML
"""

import os
from pathlib import Path

def cambiar_idioma_yml(ruta_archivo):
    """Cambia l_spanish: a l_english: en la primera línea del archivo"""
    try:
        # Leer el archivo con UTF-8 BOM
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as f:
            lineas = f.readlines()
        
        # Cambiar la primera línea
        if lineas and 'l_spanish:' in lineas[0]:
            lineas[0] = lineas[0].replace('l_spanish:', 'l_english:')
            
            # Escribir de vuelta con UTF-8 BOM
            with open(ruta_archivo, 'w', encoding='utf-8-sig') as f:
                f.writelines(lineas)
            
            return True
        return False
    except Exception as e:
        print(f"Error procesando {ruta_archivo}: {e}")
        return False

if __name__ == "__main__":
    ruta_localization = Path(r"G:\Mi unidad\Coding\mods\Crusader Kings III\Traduccion Adoption Options al Español\localization\english")
    
    archivos_procesados = 0
    archivos_cambiados = 0
    
    for archivo in ruta_localization.glob("*.yml"):
        archivos_procesados += 1
        if cambiar_idioma_yml(archivo):
            print(f"✅ {archivo.name}: l_spanish: → l_english:")
            archivos_cambiados += 1
        else:
            print(f"⏭️  {archivo.name}: No requiere cambios")
    
    print(f"\n📊 Total: {archivos_procesados} archivos procesados, {archivos_cambiados} cambiados")
