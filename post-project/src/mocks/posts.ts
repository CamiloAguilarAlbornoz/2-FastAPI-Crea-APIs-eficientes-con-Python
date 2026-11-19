export interface Post {
  id: string;
  title: string;
  content: string;
  created_at: string;
}

export const mockPosts: Post[] = [
  {
    id: 'da7870b4-dc10-4ab1-b31c-cc965cc8d615',
    title: 'Bienvenidos a la aplicación de POSTS',
    content:
      'Este es el primer post de ejemplo. Aquí podrás leer artículos, noticias y contenido publicado por la comunidad. Cada tarjeta muestra el título y una parte del contenido, con la opción de expandirlo para leerlo completo usando el enlace de "ver más".',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: '4dc217c4-3199-4d10-8511-749bd1609834',
    title: 'Cómo organizar tus ideas antes de escribir',
    content:
      'Escribir un buen post comienza mucho antes de redactar la primera línea. Primero define el objetivo: ¿quieres informar, enseñar o entretener? Luego, enumera las ideas principales en una lista y ordénalas de manera lógica. Con esa estructura lista, redactar se vuelve mucho más fluido y el resultado final gana en claridad.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: '70950d96-e10e-4cbf-a2e5-a02002f7a459',
    title: 'Los beneficios de escribir con constancia',
    content:
      'Escribir con regularidad, aunque sea unos minutos al día, tiene efectos sorprendentes. Mejora la claridad de tus ideas, amplía tu vocabulario y te ayuda a organizar el pensamiento. Con el tiempo, notarás que los textos que antes te tomaban horas ahora salen con menos esfuerzo y mayor calidad.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: 'e9929e14-2b8b-4c29-b864-c5698380d00e',
    title: '5 consejos para mejorar tu redacción',
    content:
      '1) Lee mucho: la lectura alimenta la escritura. 2) Sé conciso: elimina las palabras que sobran. 3) Usa voz activa: tus frases ganarán fuerza. 4) Revisa siempre: una segunda pasada corrige la mayoría de los errores. 5) Pide opiniones: otros ojos detectan lo que tú ya no ves.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: '7b8d9063-f1d7-42c0-8fc3-8f8bb2dce64b',
    title: 'Qué hace que un contenido sea atractivo',
    content:
      'Un contenido atractivo combina un título claro, una introducción que engancha y un desarrollo que aporta valor real. Evita los rellenos y ve directo al grano. Además, el formato importa: párrafos cortos, subtítulos y listas facilitan la lectura y mantienen la atención del lector hasta el final.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: 'b542d757-2e3f-4bae-9160-aa7a3b263d8a',
    title: 'Errores comunes al publicar en línea',
    content:
      'Publicar sin releer, ignorar la ortografía, usar títulos engañosos o escribir párrafos interminables son errores frecuentes que alejan a los lectores. También es común olvidar el propósito del texto. Revisar con calma antes de publicar y pensar en quién te va a leer evita la mayoría de estos problemas.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: '45fa60c5-b160-4026-a837-10acff0710a2',
    title: 'La importancia de un buen título',
    content:
      'El título es la puerta de entrada a tu contenido. Un buen título promete algo concreto al lector: resolver un problema, explicar algo o contar una historia interesante. Debe ser honesto, breve y claro. Si el título cumple lo que promete y el contenido lo respalda, ganarás lectores fieles.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: 'a409094e-a0d6-4565-9645-ac563b099380',
    title: 'Cómo encontrar ideas para tus posts',
    content:
      'Las ideas están en todas partes: en las preguntas que te hacen, en los problemas que resuelves cada día y en los temas que te apasionan. Lleva una libreta o usa las notas del teléfono para anotarlas. Cuando tengas una lista suficiente, elige la idea que más te entusiasme y conviértela en tu próximo post.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: '60cce429-d265-4b8f-9f1d-a4657e41cdf3',
    title: 'Escribir para internet: claves del formato',
    content:
      'Leer en pantalla es distinto a leer en papel. Los textos para internet funcionan mejor con párrafos de dos o tres líneas, ideas una por una, y elementos visuales que den respiro. También ayuda anticipar la información importante al principio, porque muchos lectores solo recorren el texto en diagonal.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: 'f0f7f457-d4b4-4e53-93dc-cc5af8ff8951',
    title: 'La rutina de un escritor productivo',
    content:
      'Los escritores productivos no esperan la inspiración: crean rutinas. Eligen una hora fija, un lugar cómodo y una meta pequeña y alcanzable, como trescientas palabras al día. La constancia vence al talento sin disciplina. Empieza poco, pero empieza hoy, y el hábito hará el resto.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: '7f47d9da-241c-4edf-a77a-aadfe8e54701',
    title: 'Cómo conectar con tus lectores',
    content:
      'Escribir para la web no es hablar a la multitud, sino conversar con una persona. Usa un tono cercano, responde los comentarios y pregunta a tus lectores qué temas les interesan. Cuando alguien siente que escribes pensando en él, vuelve, comenta y comparte tu contenido.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
  {
    id: 'f00329c9-5c42-47a5-9fa1-a70591f9cd9a',
    title: 'El poder de revisar y editar tus textos',
    content:
      'Ningún buen texto sale perfecto a la primera. La revisión es donde ocurre la magia: se recortan las frases confusas, se reordenan las ideas y se pulen las palabras. Deja reposar el texto unas horas y vuélvelo a leer; verás errores y mejoras que antes pasaban desapercibidas.',
    created_at: '2026-11-13T15:48:46.202632+00:00',
  },
];
