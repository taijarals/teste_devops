import os

from notas import calcular_media, situacao

alunos = [
    ("Ana", 8, 9, 7),
    ("Bruno", 5, 6, 4),
    ("Carla", 3, 4, 5),
]

linhas = ""
for nome, av1, av2, av3 in alunos:
    media = calcular_media(av1, av2, av3)
    linhas += f"<tr><td>{nome}</td><td>{media}</td><td>{situacao(media)}</td></tr>\n"

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>Boletim da Turma</title></head>
<body>
  <h1>Boletim da Turma</h1>
  <table border="1" cellpadding="8">
    <tr><th>Aluno</th><th>Média</th><th>Situação</th></tr>
    {linhas}
  </table>
  <p>Publicado automaticamente pelo GitHub Actions.</p>
</body>
</html>"""

os.makedirs("site", exist_ok=True)
with open("site/index.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(html)

print("Site gerado em site/index.html")
