import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Función para cada sección
def bienestar_social():
    
    questions = [
        "Contribuyo con tiempo y/o dinero a proyectos sociales y comunitarios.",
        "Estoy comprometido con una vida de voluntariado.",
        "Demuestro imparcialidad y justicia al tratar con personas.",
        "Tengo una red de amigos cercanos y/o familiares.",
        "Me interesan los demás, incluso aquellos de diferentes antecedentes que el mío.",
        "Puedo equilibrar mis propias necesidades con las necesidades de los demás.",
        "Puedo comunicarme y llevarme bien con una gran variedad de personas.",
        "Obedezco las leyes y reglas de nuestra sociedad.",
        "Soy una persona compasiva y trato de ayudar a los demás cuando puedo.",
        "Apoyo y ayudo con las reuniones sociales de la familia, el vecindario y el trabajo."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])  # Selección de valores 0, 1 o 2
        values.append(value)
    return np.mean(values)  # Retornar el promedio de las respuestas

def bienestar_intelectual():
     
    questions = [
        "Estoy interesado en aprender cosas nuevas.",
        "Trato de mantenerme al tanto de los asuntos actuales a nivel local, nacional e internacional.",
        "Disfruto asistiendo a conferencias, obras de teatro, actuaciones musicales, museos, galerías y/o bibliotecas.",
        "Selecciono cuidadosamente películas y/o programas de televisión.",
        "Disfruto de actividades/juegos mentales creativos y estimulantes.",
        "Estoy contento con la cantidad y variedad que leo.",
        "Me esfuerzo por mejorar mis habilidades verbales y escritas.",
        "Un programa de educación continua es/será importante para mí en mi carrera.",
        "Puedo analizar, sintetizar y ver más de un lado de un problema.",
        "Me gusta participar en discusiones intelectuales."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_ocupacional():
    questions = [
        "Estoy contento con mi elección de carrera.",
        "Estoy buscando trabajar.",
        "Mis responsabilidades/obligaciones laborales/estudiantiles son consistentes con mis valores.",
        "Los pagos/ventajas en mi elección de campo profesional son consistentes con mis valores.",
        "Estoy contento con el equilibrio entre mi tiempo de trabajo y mi tiempo libre.",
        "Estoy contento con la cantidad de control que tengo en mi trabajo.",
        "Mi trabajo me da satisfacción y estimulación personal.",
        "Estoy contento con el crecimiento profesional que he tenido.",
        "Siento que mi trabajo me permite hacer una diferencia.",
        "Mi trabajo contribuye positivamente a mi bienestar."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_emocional():

    questions = [
        "Puedo desarrollar y mantener relaciones cercanas.",
        "Acepto la responsabilidad de mis acciones.",
        "Veo desafíos y cambios como oportunidades de crecimiento.",
        "Siento que tengo un control considerable sobre mí.",
        "Puedo reírme de la vida y de mí mismo.",
        "Me siento bien conmigo mismo.",
        "Soy capaz de lidiar adecuadamente con el estrés.",
        "Puedo reconocer mis deficiencias personales y trabajar en ellas.",
        "Tengo un fuerte sentido de optimismo de vida y uso mis pensamientos y actitudes en formas que afirmen la vida.",
        "Mi trabajo contribuye positivamente a mi bienestar general."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_espiritual():
    
    questions = [
        "Me siento cómodo con mi vida espiritual.",
        "Existe una relación directa entre mis valores y acciones.",
        "Cuando me deprimo o me frustro, mis creencias me ayudan.",
        "La oración, la meditación y/o reflexión son parte de mi vida.",
        "La vida es significativa para mí, y siento que tengo un propósito.",
        "Puedo hablar cómodamente de mis valores y creencias.",
        "Constantemente estoy tratando de crecer espiritualmente.",
        "Soy tolerante e intento aprender sobre las creencias de otros.",
        "Encuentro consuelo en la naturaleza y el entorno que me rodea.",
        "Practico gratitud regularmente en mi vida."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_financiero():
    
    questions = [
        "¿Tienes efectivo en tu bolsillo?",
        "¿Equilibras tu presupuesto?",
        "¿Conoces la cantidad total de la deuda que tienes?",
        "¿Administras bien tu tiempo?",
        "¿Tienes una cuenta propia de ahorro?",
        "¿Sabes cuánto hay en tu cuenta de ahorro?",
        "¿Tu situación financiera te genera estrés?",
        "¿Realizas alguna actividad que te genere ingresos?",
        "¿Tienes un plan financiero a largo plazo?",
        "¿Evalúas regularmente tu situación financiera?"
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_fisico():
    
    questions = [
        "Hago ejercicio aeróbico (vigoroso, continuo) durante 20 o 30 min. al menos 3 veces por semana.",
        "Como fruta, vegetales y granos integrales todos los días.",
        "Evito los productos de tabaco.",
        "Uso un cinturón de seguridad mientras viajo en o conduzco un automóvil.",
        "Minimizo deliberadamente mi ingesta de colesterol, grasas y aceites.",
        "Evito tomar bebidas alcohólicas o no consumo más de una bebida por día.",
        "Tengo una cantidad adecuada de agua.",
        "Tengo mecanismos adecuados para enfrentar el estrés.",
        "Mantengo un horario regular de inmunizaciones, exámenes físicos, chequeos dentales y autoexámenes.",
        "Mantengo un peso razonable, evitando los extremos de sobrepeso y bajo peso."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienvenida_encuesta():
    st.write("""
    Esta encuesta tiene como objetivo evaluar diferentes dimensiones de tu bienestar.
    A través de una serie de preguntas, podrás reflexionar sobre aspectos importantes de tu vida en las siguientes áreas:
    - Bienestar Social
    - Bienestar Intelectual
    - Bienestar Ocupacional
    - Bienestar Emocional
    - Bienestar Espiritual
    - Bienestar Financiero
    - Bienestar Físico

    Por favor, responde cada pregunta con sinceridad. Al final de la encuesta, podrás ver un gráfico que refleja tu bienestar en cada una de estas dimensiones.
    """)
    return 0

# Configuración de la aplicación Streamlit
def radar_chart(values):
    categories = ['Social', 'Intelectual', 'Ocupacional', 'Emocional', 'Espiritual', 'Financiero', 'Físico']
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='skyblue', alpha=0.4)
    ax.plot(angles, values, color='blue', linewidth=2, linestyle='solid')
    ax.set_yticks(np.arange(0, 3, 1))
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)

    return fig

def feedback(scores):
    feedbacks = []
    for score in scores:
        if score <= 0.5:
            feedbacks.append("Bajo: Considera estrategias para mejorar tu bienestar en esta área.")
        elif score <= 1.5:
            feedbacks.append("Medio: Estás en un buen camino, pero hay áreas que podrías fortalecer.")
        else:
            feedbacks.append("Alto: ¡Excelente! Estás haciendo un gran trabajo en esta área.")
    return feedbacks

def main():
    st.title('Bienvenido a la Rueda de la Vida')

    # Inicializa la sesión para el estado actual
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0  # Comienza en la página 0 (Bienvenida)

    # Inicializa las puntuaciones si no están definidas
    if 'scores' not in st.session_state:
        st.session_state.scores = [0] * 7  # Inicializa las puntuaciones a cero para 7 áreas

    # Define las páginas
    pages = [
        "Bienvenida",
        "Bienestar Social",
        "Bienestar Intelectual",
        "Bienestar Ocupacional",
        "Bienestar Emocional",
        "Bienestar Espiritual",
        "Bienestar Financiero",
        "Bienestar Físico",
        "Resultados"
    ]

    completed_sections = sum(1 for score in st.session_state.scores if score > 0)
    # Muestra el contenido de la página actual
    page = pages[st.session_state.current_page]

    if page == "Bienvenida":
        st.write("""
        Esta encuesta tiene como objetivo evaluar diferentes dimensiones de tu bienestar.
        A través de una serie de preguntas, podrás reflexionar sobre aspectos importantes de tu vida en las siguientes áreas:
        - Bienestar Social
        - Bienestar Intelectual
        - Bienestar Ocupacional
        - Bienestar Emocional
        - Bienestar Espiritual
        - Bienestar Financiero
        - Bienestar Físico

        Por favor, responde cada pregunta con sinceridad. Al final de la encuesta, podrás ver un gráfico que refleja tu bienestar en cada una de estas dimensiones.
        """)

    elif page == "Bienestar Social":
        st.header('Bienestar Social')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[0] = bienestar_social()

    elif page == "Bienestar Intelectual":
        st.header('Bienestar Intelectual')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[1] = bienestar_intelectual()

    elif page == "Bienestar Ocupacional":
        st.header('Bienestar Ocupacional')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[2] = bienestar_ocupacional()

    elif page == "Bienestar Emocional":
        st.header('Bienestar Emocional')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[3] = bienestar_emocional()

    elif page == "Bienestar Espiritual":
        st.header('Bienestar Espiritual')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[4] = bienestar_espiritual()

    elif page == "Bienestar Financiero":
        st.header('Bienestar Financiero')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[5] = bienestar_financiero()

    elif page == "Bienestar Físico":
        st.header('Bienestar Físico')
        st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
        st.session_state.scores[6] = bienestar_fisico()

    elif page == "Resultados":
        st.header('Resultados')
        if all(score > 0 for score in st.session_state.scores):
            st.pyplot(radar_chart(st.session_state.scores))
            feedback_scores = feedback(st.session_state.scores)
            for category, score in zip(['Social', 'Intelectual', 'Ocupacional', 'Emocional', 'Espiritual', 'Financiero', 'Físico'], feedback_scores):
                st.write(f"{category}: {score}")
        else:
            st.warning("Por favor, completa todas las secciones antes de ver los resultados.")

    # Botones de navegación
    col1, col2 = st.columns(2)

    # Botón "Página Anterior"
    if st.session_state.current_page > 0:
        with col1:
            if st.button('Página Anterior'):
                st.session_state.current_page -= 1
                st.rerun()


    # Botón "Siguiente Página"
    if st.session_state.current_page < len(pages) - 1:
        with col2:
            if st.button('Siguiente Página'):
                st.session_state.current_page += 1
                st.rerun()
    st.write(f"Sección actual: {pages[st.session_state.current_page]}")
    st.write(f"Secciones completadas: {completed_sections} de {len(pages) - 2}")  # Excluye 'Resultados'
if __name__ == '__main__':
    main()
