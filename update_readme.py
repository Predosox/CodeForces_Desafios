import requests
from datetime import datetime

# Handle do Codeforces
handle = "Predosox"

# URL da API
url = f"https://codeforces.com/api/user.info?handles={handle}"
response = requests.get(url)
data = response.json()

# Extrair dados
user = data['result'][0]
rating = user.get('rating', 'N/A')
max_rating = user.get('maxRating', 'N/A')
rank = user.get('rank', 'N/A').title()
last_online = datetime.fromtimestamp(user['lastOnlineTimeSeconds']).strftime('%d/%m/%Y %H:%M:%S')
registration = datetime.fromtimestamp(user['registrationTimeSeconds']).strftime('%d/%m/%Y %H:%M:%S')
friends = user.get('friendOfCount', 0)
contribution = user.get('contribution', 0)
avatar = user.get('avatar')

# Submissões do usuário
status_url = f"https://codeforces.com/api/user.status?handle={handle}"
status_response = requests.get(status_url)
status_data = status_response.json()

# Verificar se a resposta foi bem-sucedida
if status_data["status"] == "OK":
    submissions = status_data["result"]
    accepted = [sub for sub in submissions if sub.get("verdict") == "OK"]

    # Criar conjunto de problemas únicos resolvidos
    unique_problems = set()
    for sub in accepted:
        problem = sub["problem"]
        contest_id = problem.get("contestId", "")
        index = problem.get("index", "")
        unique_problems.add(f"{contest_id}-{index}")

    total_unique_solved = len(unique_problems)
else:
    total_unique_solved = "Erro ao acessar API"

# Gerar conteúdo do README
readme_content = f"""## 👨‍💻 Perfil Codeforces: {handle}

- 📊 Rating: Ainda em construção 🚧
- 🏅 Rank: Em breve... 
- 🕒 Última vez online: `{last_online}`
- 📅 Registrado em: `{registration}`
- ✅ Problemas únicos resolvidos: `{total_unique_solved}`
"""

# Atualizar README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)