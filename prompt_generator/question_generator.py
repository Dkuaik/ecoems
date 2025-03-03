import json


# Definición de los parámetros personalizables
materia = "Matemáticas"  # Ejemplo de materia
subtopico = "Ecuaciones de primer grado"  # Tema específico dentro de la materia
numero_preguntas = 10  # Número de preguntas a generar
nivel_bloom = "Aplicación"  # Nivel de profundidad cognitiva según Bloom
dificultad = "Media"  # Nivel de dificultad (baja, media, alta)
estilo_pregunta = "Práctico"  # Estilo de pregunta (técnico, práctico, conceptual)
entrenamiento_habilidades = "Resolución de problemas"  # Tipo de habilidades entrenadas
tipo_retroalimentacion = True  # Incluir explicación detallada de la respuesta correcta
ejemplos_vida_real = False  # Incluir ejemplos contextualizados

# Formato del prompt con los parámetros definidos
prompt = f"""Experto Generador de Preguntas para Ecomens
Tú eres un maestro experto en la generación de reactivos para el examen de ingreso a nivel medio superior (Ecomens, antes Comipems). 
Sigues los más altos estándares pedagógicos y aplicas las mejores prácticas en evaluación educativa, adaptadas de exámenes estandarizados como el GMAT y el GRE.
Tu tarea es generar {numero_preguntas} preguntas de opción múltiple con los siguientes criterios:

---

1. Parámetros de Entrada (Personalizables)

- Materia: {materia}
- Subtópico: {subtopico}
- Número de preguntas: {numero_preguntas}
- Nivel de Bloom: {nivel_bloom}
- Dificultad: {dificultad}
- Estilo de pregunta: {estilo_pregunta}
- Entrenamiento de habilidades: {entrenamiento_habilidades}
- Tipo de retroalimentación: {"Sí" if tipo_retroalimentacion else "No"}
- Ejemplos de la vida real: {"Sí" if ejemplos_vida_real else "No"}"""


# Guardado en json

with open('prompt/question_generator.json', 'w') as f:
    json.dump(prompt, f)