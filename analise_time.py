
jogos = [
    {"adversario": "Universitario", "marcados": 2, "sofridos": 0},
    {"adversario": "River Plate", "marcados": 1, "sofridos": 1},
    {"adversario": "Boca Juniors", "marcados": 0, "sofridos": 3},
    {"adversario": "Penarol", "marcados": 3, "sofridos": 2},
    {"adversario": "Nacional", "marcados": 1, "sofridos": 0},
]
vitorias = 0
empates = 0
derrotas = 0

def resultado_jogo(marcados, sofridos):
    
    if marcados > sofridos:
        return "vitoria"
    elif marcados < sofridos:
        return "derrota"
    else:
        return "empate"

for jogo in jogos:
    
    adversario = jogo["adversario"]
    marcados =  jogo["marcados"]
    sofridos = jogo["sofridos"]
    
    resultado = resultado_jogo(marcados,sofridos)
    if resultado == "vitoria":
        print(f"Vitória contra {adversario} por: {marcados} x {sofridos}.")
        vitorias += 1
    elif resultado == "derrota":
        print(f"Derrota contra {adversario} por: {marcados} x {sofridos}.")
        derrotas += 1
        
    else:
        print(f"Empate contra {adversario} por: {marcados} x {sofridos}.")
        empates += 1
    
pontos_ganhos = (vitorias * 3) + empates 

pontos_possiveis = (len(jogos) * 3 )

aproveitamento = (pontos_ganhos / pontos_possiveis  ) * 100

print(f"Vitorias: {vitorias} | Derrotas: {derrotas} | Empates: {empates}")
print(f"Aproveitamento: {round(aproveitamento,1)}%")
    
