![](assets/header.png)

[![Centennial
College](https://img.shields.io/badge/-Centennial%20College-d4e039?style=flat&logo=Centennial-College&logoColor=white)](https://github.com/ttran375)
[![IU-VNU](https://img.shields.io/badge/-IU--VNU-198fd9?style=flat&logo=International-University&logoColor=white)](https://github.com/datttrian/iu-mafe)
[![LinkedIn
Learning](https://img.shields.io/badge/-LinkedIn%20Learning-0073B1?style=flat&logo=LinkedIn&logoColor=white)](https://github.com/datttrian/linkedin-learning)
[![DataCamp](https://img.shields.io/badge/-DataCamp-03EF62?style=flat&logo=DataCamp&logoColor=white)](https://github.com/datttrian/datacamp)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=flat&logo=LeetCode&logoColor=white)](https://github.com/datttrian/leetcode)
[![CS50X](https://img.shields.io/badge/-CS50X-e00000?style=flat&logo=CS50&logoColor=white)](https://github.com/datttrian/cs50x)
[![CS50P](https://img.shields.io/badge/-CS50P-e00000?style=flat&logo=CS50&logoColor=white)](https://github.com/datttrian/cs50p)
[![CS50AI](https://img.shields.io/badge/-CS50AI-e00000?style=flat&logo=CS50&logoColor=white)](https://github.com/datttrian/cs50ai)
[![Codecademy](https://img.shields.io/badge/-Codecademy-1F4056?style=flat&logo=Codecademy&logoColor=white)](https://github.com/datttrian/codecademy)

<p align="center">

<a href="https://github.com/datttrian">
<img src="https://github-stats-alpha.vercel.app/api?username=datttrian">
</a>

</p>

<p align="center">

<a href="https://github.com/datttrian">
<img src="https://github-readme-stats.vercel.app/api/top-langs?username=datttrian&&show_icons=true&locale=en&layout=compact&langs_count=10">
<img src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=datttrian">
</a>

</p>

<p align="center">

<a href="https://github.com/datttrian">
<img src="http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=datttrian">
</a>

</p>

``` python
import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Failed to fetch a quote."

print(get_random_quote())
```

    ## Quality means doing it right when no one is looking. - Henry Ford

![](assets/footer.svg)
