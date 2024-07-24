#promedio de tiempo de duración con pacientes en consulta on-line
otras_sesiones_min = 20
otras_sesiones_max = 25
otras_sesiones_promedio = 23
sesiones_Linda = 45

sesion_promedio = 45

#Diferencias de duración
tiempo_promedio_vacio_min = 10 - otras_sesiones_min * 1000 // sesion_promedio / 10
tiempo_promedio_vacio_min_ = 100 - sesiones_Linda * 1000 // sesiones_Linda / 10
print(tiempo_promedio_vacio_min_)