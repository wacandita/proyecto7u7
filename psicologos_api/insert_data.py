from database import SessionLocal
import Models

def ingreso():
    db = SessionLocal()

    # 🔥 limpiar (para evitar duplicados)
    db.query(Models.Psicologo).delete()

    psicologos = [
        Models.Psicologo(
            nombre="Dra. Ana",
            descripcion="Especialista en ansiedad",
            correo="ana@gmail.com",
            ubicacion="Santa Marta",
            imagen="https://images.unsplash.com/photo-1582750433449"
        ),
        Models.Psicologo(
            nombre="Dr. Carlos",
            descripcion="Terapia cognitivo-conductual",
            correo="carlos@gmail.com",
            ubicacion="Barranquilla",
            imagen="https://images.unsplash.com/photo-1508214751196"
        ),
        Models.Psicologo(
            nombre="Dra. Laura",
            descripcion="Depresión y estrés",
            correo="laura@gmail.com",
            ubicacion="Cartagena",
            imagen="https://images.unsplash.com/photo-1559839734"
        ),
        Models.Psicologo(
            nombre="Dra. María López",
            descripcion="Ansiedad y estrés laboral",
            correo="maria@gmail.com",
            ubicacion="Bogotá",
            imagen="https://randomuser.me/api/portraits/women/10.jpg"
        ),
        Models.Psicologo(
                nombre="Dr. Andrés Gómez",
                descripcion="Terapia familiar",
                correo="andres@gmail.com",
                ubicacion="Medellín",
                imagen="https://randomuser.me/api/portraits/men/11.jpg"
        ),
        Models.Psicologo(
                nombre="Dra. Sofía Martínez",
                descripcion="Depresión clínica",
                correo="sofia@gmail.com",
                ubicacion="Cali",
                imagen="https://randomuser.me/api/portraits/women/12.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Luis Torres",
            descripcion="Psicología infantil",
            correo="luis@gmail.com",
            ubicacion="Barranquilla",
            imagen="https://randomuser.me/api/portraits/men/13.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Camila Rojas",
            descripcion="Autoestima y desarrollo personal",
            correo="camila@gmail.com",
            ubicacion="Cartagena",
            imagen="https://randomuser.me/api/portraits/women/14.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Juan Pérez",
            descripcion="Adicciones",
            correo="juan@gmail.com",
            ubicacion="Santa Marta",
            imagen="https://randomuser.me/api/portraits/men/15.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Valentina Castro",
            descripcion="Relaciones de pareja",
            correo="valentina@gmail.com",
            ubicacion="Bogotá",
            imagen="https://randomuser.me/api/portraits/women/16.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Daniel Ruiz",
            descripcion="Trastornos emocionales",
            correo="daniel@gmail.com",
            ubicacion="Medellín",
            imagen="https://randomuser.me/api/portraits/men/17.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Laura Sánchez",
            descripcion="Terapia cognitiva",
            correo="laura2@gmail.com",
            ubicacion="Cali",
            imagen="https://randomuser.me/api/portraits/women/18.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Felipe Herrera",
            descripcion="Psicología deportiva",
            correo="felipe@gmail.com",
            ubicacion="Bucaramanga",
            imagen="https://randomuser.me/api/portraits/men/19.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Natalia Vega",
            descripcion="Manejo de emociones",
            correo="natalia@gmail.com",
            ubicacion="Pereira",
            imagen="https://randomuser.me/api/portraits/women/20.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Ricardo Díaz",
            descripcion="Ansiedad social",
            correo="ricardo@gmail.com",
            ubicacion="Manizales",
            imagen="https://randomuser.me/api/portraits/men/21.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Daniela Ortiz",
            descripcion="Coaching emocional",
            correo="daniela@gmail.com",
            ubicacion="Ibagué",
            imagen="https://randomuser.me/api/portraits/women/22.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Sebastián Cruz",
            descripcion="Psicología organizacional",
            correo="sebastian@gmail.com",
            ubicacion="Bogotá",
            imagen="https://randomuser.me/api/portraits/men/23.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Paula Moreno",
            descripcion="Terapia de duelo",
            correo="paula@gmail.com",
            ubicacion="Cartagena",
            imagen="https://randomuser.me/api/portraits/women/24.jpg"
        ),
        Models.Psicologo(
            nombre="Dr. Miguel Ángel",
            descripcion="Psicología clínica",
            correo="miguel@gmail.com",
            ubicacion="Cúcuta",
            imagen="https://randomuser.me/api/portraits/men/25.jpg"
        ),
        Models.Psicologo(
            nombre="Dra. Andrea Gil",
            descripcion="Salud mental juvenil",
            correo="andrea@gmail.com",
            ubicacion="Santa Marta",
            imagen="https://randomuser.me/api/portraits/women/26.jpg"
        )
    ]

    db.add_all(psicologos)
    db.commit()
    db.close()