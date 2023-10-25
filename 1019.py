tempo_duracao_em_segundos = int(input(""))
horas = tempo_duracao_em_segundos // 3600
minutos = (tempo_duracao_em_segundos % 3600) // 60
segundos = tempo_duracao_em_segundos % 60
print(f"{horas}:{minutos}:{segundos}")