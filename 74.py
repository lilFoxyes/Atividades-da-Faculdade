total_candidatos = 0
maior_candidatos_por_vaga = 0
curso_maior_candidatos_por_vaga = None


cursos = {}

while True:
    
    entrada = input("Digite o código do curso, número de vagas, candidatos masculinos e candidatos femininos (ou 0 para encerrar): ")
    dados = entrada.split()
    
    
    if entrada == '0':
        break
    
    codigo_curso = dados[0]
    vagas = int(dados[1])
    candidatos_masculinos = int(dados[2])
    candidatos_femininos = int(dados[3])
    
    
    total_candidatos += candidatos_masculinos + candidatos_femininos
    candidatos_por_vaga = (candidatos_masculinos + candidatos_femininos) / vagas
    porcentagem_feminina = (candidatos_femininos / (candidatos_masculinos + candidatos_femininos)) * 100
    
    
    cursos[codigo_curso] = {
        'vagas': vagas,
        'candidatos_por_vaga': candidatos_por_vaga,
        'porcentagem_feminina': porcentagem_feminina
    }
    
   
    if candidatos_por_vaga > maior_candidatos_por_vaga:
        maior_candidatos_por_vaga = candidatos_por_vaga
        curso_maior_candidatos_por_vaga = codigo_curso


for codigo_curso, info_curso in cursos.items():
    print("Código do Curso: {}".format(codigo_curso))
    print("Número de Candidatos por Vaga: {:.2f}".format(info_curso['candidatos_por_vaga']))
    print("Porcentagem de Candidatos do Sexo Feminino: {:.2f}%".format(info_curso['porcentagem_feminina']))
    print()


print("Curso com mais candidatos por vaga: Código {} com {:.2f} candidatos por vaga".format(curso_maior_candidatos_por_vaga, maior_candidatos_por_vaga))

print("Total de Candidatos: {}".format(total_candidatos))