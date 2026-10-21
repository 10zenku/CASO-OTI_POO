# SISTEMA ACADEMICO OTI
# Programacion Orientada a Objetos (POO) - PRACTICA


# 1. CLASE CURSO
class Curso:
    def __init__(self, codigo, nombre, creditos,
                 teoricas, practicas, seminario, virtuales):
        self._codigo = codigo
        self._nombre = nombre
        self._creditos = creditos
        self._teoricas = teoricas
        self._practicas = practicas
        self._seminario = seminario
        self._virtuales = virtuales

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self._nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacio")

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, nuevos_creditos):
        if nuevos_creditos > 0:
            self._creditos = nuevos_creditos
        else:
            print("Los creditos deben ser mayores que cero")

    @property
    def teoricas(self):
        return self._teoricas

    @teoricas.setter
    def teoricas(self, horas):
        if horas >= 0:
            self._teoricas = horas
        else:
            print("Las horas no pueden ser negativas")

    @property
    def practicas(self):
        return self._practicas

    @practicas.setter
    def practicas(self, horas):
        if horas >= 0:
            self._practicas = horas
        else:
            print("Las horas no pueden ser negativas")

    @property
    def seminario(self):
        return self._seminario

    @seminario.setter
    def seminario(self, horas):
        if horas >= 0:
            self._seminario = horas
        else:
            print("Las horas no pueden ser negativas")

    @property
    def virtuales(self):
        return self._virtuales

    @virtuales.setter
    def virtuales(self, horas):
        if horas >= 0:
            self._virtuales = horas
        else:
            print("Las horas no pueden ser negativas")

    def total_horas(self):
        return (self._teoricas + self._practicas +
                self._seminario + self._virtuales)

    def validar_horas(self):
        print("Total de horas:", self.total_horas())

    def mostrar_datos(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Creditos:", self.creditos)
        print("Teoricas:", self.teoricas)
        print("Practicas:", self.practicas)
        print("Seminario:", self.seminario)
        print("Virtuales:", self.virtuales)
        print("Total de horas:", self.total_horas())


# 2. CLASE SECCION
class Seccion:
    def __init__(self, codigo, curso_codigo, periodo_codigo,
                 vacantes, matriculados):
        self._turno = codigo
        self._curso_codigo = curso_codigo
        self._periodo_codigo = periodo_codigo
        self._vacantes = vacantes
        self._matriculados = matriculados

    @property
    def codigo(self):
        return self._turno

    @property
    def curso_codigo(self):
        return self._curso_codigo

    @property
    def periodo_codigo(self):
        return self._periodo_codigo

    @property
    def vacantes(self):
        return self._vacantes

    @property
    def matriculados(self):
        return self._matriculados

    def disponibles(self):
        return self._vacantes - self._matriculados

    def matricular(self):
        if self.disponibles() > 0:
            self._matriculados += 1
            print("Matricula realizada correctamente")
        else:
            print("No hay vacantes disponibles")

    def mostrar_datos(self):
        print("Turno:", self.codigo)
        print("Codigo del curso:", self.curso_codigo)
        print("Codigo del periodo:", self.periodo_codigo)
        print("Vacantes:", self.vacantes)
        print("Matriculados:", self.matriculados)
        print("Disponibles:", self.disponibles())


# 3. CLASE PERIODO ACADEMICO
class PeriodoAcademico:
    def __init__(self, nombre, numero, año, inicio, fin,
                 matricula_inicio, matricula_fin, verano,
                 nota_minima, estado):
        self._nombre = nombre
        self._numero = numero
        self._año = año
        self._inicio = inicio
        self._fin = fin
        self._matricula_inicio = matricula_inicio
        self._matricula_fin = matricula_fin
        self._verano = verano
        self._nota_minima = nota_minima
        self._estado = estado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "" and len(nuevo_nombre) <= 45:
            self._nombre = nuevo_nombre
        else:
            print("Nombre vacio o demasiado largo")

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado in [1, 2, 3, 4]:
            self._estado = nuevo_estado
        else:
            print("Estado no valido")

    def cambiar_intervalo(self, nuevo_inicio, nuevo_fin):
        if nuevo_inicio <= nuevo_fin:
            self._matricula_inicio = nuevo_inicio
            self._matricula_fin = nuevo_fin
        else:
            print("Intervalo de matricula no valido")

    def validar_fechas(self):
        if self._inicio <= self._fin:
            print("Fechas del periodo correctas")
        else:
            print("La fecha final no puede ser anterior a la inicial")

    def mostrar_datos(self):
        print("Nombre:", self._nombre)
        print("Numero:", self._numero)
        print("Año:", self._año)
        print("Inicio:", self._inicio)
        print("Fin:", self._fin)
        print("Matricula inicio:", self._matricula_inicio)
        print("Matricula fin:", self._matricula_fin)
        print("Verano:", self._verano)
        print("Nota minima:", self._nota_minima)
        print("Estado:", self.estado)


# 4. CLASE PLAN DE ESTUDIO
class PlanEstudio:
    def __init__(self, nombre, año, obligatorios,
                 electivos, extracurriculares, vigente):
        self._nombre = nombre
        self._año = año
        self._obligatorios = obligatorios
        self._electivos = electivos
        self._extracurriculares = extracurriculares
        self._vigente = vigente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "" and len(nuevo_nombre) <= 36:
            self._nombre = nuevo_nombre
        else:
            print("Nombre vacio o demasiado largo")

    def total_creditos(self):
        return (self._obligatorios + self._electivos +
                self._extracurriculares)

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Año:", self._año)
        print("Obligatorios:", self._obligatorios)
        print("Electivos:", self._electivos)
        print("Extracurriculares:", self._extracurriculares)
        print("Total de creditos:", self.total_creditos())
        print("Vigente:", self._vigente)


# 5. CLASE ESCUELA PROFESIONAL
class EscuelaProfesional:
    def __init__(self, codigo, nombre, informacion_general,
                 perfil_egresado, director_codigo, secretario_codigo):
        self._codigo = codigo
        self._nombre = nombre
        self._informacion_general = informacion_general
        self._perfil_egresado = perfil_egresado
        self._director_codigo = director_codigo
        self._secretario_codigo = secretario_codigo

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self._nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacio")

    def mostrar_datos(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Informacion general:", self._informacion_general)
        print("Perfil del egresado:", self._perfil_egresado)
        print("Codigo del director:", self._director_codigo)
        print("Codigo del secretario:", self._secretario_codigo)


# 6. CLASE PERSONA
class Persona:
    def __init__(self, dni, nombres, apellidos):
        self._dni = dni
        self._nombres = nombres
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, nuevos_nombres):
        if nuevos_nombres != "":
            self._nombres = nuevos_nombres
        else:
            print("Los nombres no pueden estar vacios")

    @property
    def apellidos(self):
        return self._apellidos

    def nombre_completo(self):
        return self._nombres + " " + self._apellidos

    def mostrar_rol(self):
        raise NotImplementedError(
            "La clase hija debe indicar el rol"
        )

    def mostrar_datos(self):
        print("DNI:", self.dni)
        print("Nombres:", self.nombres)
        print("Apellidos:", self.apellidos)
        print("Nombre completo:", self.nombre_completo())
        print("Rol:", self.mostrar_rol())


# 7. CLASE ESTUDIANTE
class Estudiante(Persona):
    def __init__(self, dni, nombres, apellidos,
                 codigo_estudiante, escuela_codigo):
        super().__init__(dni, nombres, apellidos)
        self._codigo_estudiante = codigo_estudiante
        self._escuela_codigo = escuela_codigo

    def mostrar_rol(self):
        return "Estudiante"

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Codigo de estudiante:", self._codigo_estudiante)
        print("Codigo de escuela:", self._escuela_codigo)


# 8. CLASE DOCENTE
class Docente(Persona):
    def __init__(self, dni, nombres, apellidos, codigo_docente):
        super().__init__(dni, nombres, apellidos)
        self._codigo_docente = codigo_docente

    def mostrar_rol(self):
        return "Docente"

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Codigo de docente:", self._codigo_docente)


# CREACION DE OBJETOS

print("===== CURSO =====")
curso1 = Curso(
    "IS-282", "Programacion Orientada a Objetos",
    4, 2, 2, 1, 1
)
curso1.mostrar_datos()
curso1.validar_horas()

print("\n===== SECCION =====")
seccion1 = Seccion("A", "IS-282", "2026-II", 30, 10)
seccion1.matricular()
seccion1.mostrar_datos()

print("\n===== PERIODO ACADEMICO =====")
periodo1 = PeriodoAcademico(
    "2026-II", 2, 2026,
    "2026-08-01", "2026-12-20",
    "2026-07-01", "2026-08-31",
    0, 11.0, 1
)
periodo1.validar_fechas()
periodo1.mostrar_datos()

print("\n===== PLAN DE ESTUDIO =====")
plan1 = PlanEstudio(
    "Ingenieria de Sistemas", 2026, 100, 20, 5, True
)
plan1.mostrar_datos()

print("\n===== ESCUELA PROFESIONAL =====")
escuela1 = EscuelaProfesional(
    "EPIS_2026",
    "Ingenieria de Sistemas",
    "Formacion en computacion e informatica",
    "Profesional capaz de desarrollar y analizar software "
    "y sistemas informaticos",
    "27250001",
    "SEC22725"
)
escuela1.mostrar_datos()

print("\n===== ESTUDIANTE =====")
estudiante1 = Estudiante(
    "60257896", "Pauling", "Cconocc",
    "27253301", "EPIS_2026"
)
estudiante1.mostrar_datos()

print("\n===== DOCENTE =====")
docente1 = Docente(
    "70324565", "Cristian", "Loayza",
    "EPIS27251501"
)
docente1.mostrar_datos()
