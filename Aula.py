resposta = {
    "Search": [
        {
            "Title": "Doctor Strange",
            "Year": "2016",
            "imdbID": "tt1211837",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/TE@._V1_SX300.jpg"
        },
        {
            "Title": "Strange Wilderness",
            "Year": "2008",
            "imdbID": "tt0489282",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MQQ@._V1_SX300.jpg"
        },
        {
            "Title": "Strange Brew",
            "Year": "1983",
            "imdbID": "tt0086373",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/A30A@._V1_SX300.jpg"
        },
        {
            "Title": "The Strange Love of Martha Ivers",
            "Year": "1946",
            "imdbID": "tt0038988",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MzNjA@._V1_SX300.jpg"
        }
    ],
    "totalResults": "761",
    "Response": "True"
}

# resposta é um dicionário com 3 chaves
# resposta[”Search”] é uma lista



dic = {
    "musicas": [
        {"nome": "Hey Jude", "banda": "Beatles"},
        {"nome": "November Rain", "banda": "Guns n' Roses"},
        {"nome": "How Deep Is Your Love", "banda": "Bee Gees"}
    ],
    "filmes": {
        "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira"],
        "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor"],
        "Star Wars": ["Luke", "Leia", "Darth Vader", "Chewbacca", "Han Solo"]
    }
}

def func1(a, b, c, d):
    for x in a:
        if x[b] == d:
            return x[c]
    return "naosei"


print(dic["filmes"][0][0] == "Wolverine")
# KeyError: 0
