import requests
import json


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = "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"
    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()#Bilgiyi json şeklinde geri döndürür

    def getRepositories(self, username):
        repo = requests.get(self.api_url + '/users/' + username + '/repos')
        return repo.json()

    def createRepositories(self, name):
        response = requests.post(self.api_url+'/user/repos?acces_token='+"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", json={
                "name": name,
                "description": "Test",
                "private": True
            })
        return response.json()


github = Github()

while True:
    print(' MENU '.center(50,'*'))
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nseciminiz: ')
    if secim == "4":
        break
    else:
        if secim == "1":
            username = input('Username: ').strip()
            result = github.getUser(username)
            print(f"name: {result['name']} || public repos: {result['public_repos']} || Followers: {result['followers']} || url: {result['html_url']} || bio: {result['bio']}")
        if secim == "2":
            username = input('Username: ').strip()
            result = github.getRepositories(username)
            for i in result:
                print(i['name'])
        if secim == "3":
            #token = input('Acces Key: ')
            name = input('Repositories ismi giriniz: ')
            result = github.createRepositories(name)
            print(result)

            pass