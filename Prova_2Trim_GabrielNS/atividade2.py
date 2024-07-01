
primavera_inicio = (9, 21)  
primavera_fim = (12, 20)    
verao_inicio = (12, 21)     
verao_fim = (3, 20)         
outono_inicio = (3, 21)     
outono_fim = (6, 20)        
inverno_inicio = (6, 21)    
inverno_fim = (9, 20)       


estacoes = [
    "Primavera",
    "Verão",
    "Outono",
    "Inverno"
]


dia = int(input("Digite o dia (1-31): "))
mes = int(input("Digite o mês (1-12): "))


nomes_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}


if (mes, dia) >= primavera_inicio and (mes, dia) <= primavera_fim:
    print(f"A data {dia} de {nomes_meses[mes]}  corresponde à estação {estacoes[0]}.")
elif (mes, dia) >= verao_inicio or (mes, dia) <= verao_fim:
    print(f"A data {dia} de {nomes_meses[mes]}  corresponde à estação {estacoes[1]}.")
elif (mes, dia) >= outono_inicio and (mes, dia) <= outono_fim:
    print(f"A data {dia} de {nomes_meses[mes]}  corresponde à estação {estacoes[2]}.")
else:
    print(f"A data {dia} de {nomes_meses[mes]}  corresponde à estação {estacoes[3]}.")

reiniciar = input("Deseja verificar outra data? (S/N): ")
if reiniciar.lower() == "s":
    print("\nReiniciando o programa...\n")
else:
    print("Programa encerrado!")

