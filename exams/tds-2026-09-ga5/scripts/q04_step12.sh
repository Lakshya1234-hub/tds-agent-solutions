python3 -c "
import urllib.request, json
url = 'https://exam.sanand.workers.dev/check-status?quiz=tds-2026-09-ga5&email=rfvdv4896%40gmail.com&quizSign=v2.1794741841.DzsorxQsoENt45UkFEEHu33GO%2FBsMK4voSLXvDD%2BNL3NYRp4VR05LdY%2FQtk8Cj3O5pYQH6ZDU9%2FianFFGX6mwSHzNUNySVqjp2uypEfL38hkC5FVQ%2BTEuF2KEdQz0SE4b02z6xYiC85E0w%2FSxmbjdHKJ6pJVlJNJfQDX2hz5wNWT%2BEaMf%2BjxoYwYosGxP8Bs6njJZHXQ2VkL0lmz2Sj6Ok4%2FZFuYZiuFUFWNqQY0zvelqhjOBALPpI153unFqdcahdv%2FAgBoDQOU3Oiam8%2BdFFll%2Fod8iZFRY0Sqj0wpMOxA%2BLh%2Fl7y5zCKiAmfv28HWNc4XAT%2FQJl%2BclYnQqhwtew%3D%3D'
req = urllib.request.urlopen(url)
print(json.loads(req.read().decode('utf-8')))
"
