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

# Gerar conteúdo do README
readme_content = f"""## 👨‍💻 Perfil Codeforces: {handle}

- 📊 Rating atual: `{rating}`
- 📈 Rating máximo: `{max_rating}`
- 🏅 Rank: `{rank}`
- 🕒 Última vez online: `{last_online}`
- 📅 Registrado em: `{registration}`
- 👥 Número de amigos: `{friends}`
- 🎖️ Contribuições: `{contribution}`
"""

# Atualizar README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
