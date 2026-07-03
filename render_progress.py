import re
import os

def fix_progress_bars():
    # Busca todos los archivos .md en tus notas
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'Apuntes Hacking')):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Si encuentra un bloque de dataviewjs de progreso
                if "dv.current().file.path" in content:
                    # Cuenta las tareas en el archivo actual
                    all_tasks = len(re.findall(r'^\s*-\s*\[[ xX]\]', content, re.MULTILINE))
                    completed_tasks = len(re.findall(r'^\s*-\s*\[[xX]\]', content, re.MULTILINE))
                    
                    percent = round((completed_tasks / all_tasks) * 100) if all_tasks > 0 else 0
                    
                    # Diseña la barra HTML estática idéntica a la tuya
                    html_bar = f"""
<strong>📊 Progreso del Módulo: {percent}% completado ({completed_tasks}/{all_tasks})</strong>
<progress value="{percent}" max="100" style="width: 100%; height: 18px; accent-color: #f38ba8; margin-top: 5px; margin-bottom: 20px;"></progress>
"""
                    # Reemplaza el bloque de código dataview por el HTML que la web sí entiende
                    new_content = re.sub(r'```dataviewjs.*?```', html_bar, content, flags=re.DOTALL)
                    
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_progress_bars()
