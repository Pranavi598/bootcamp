import requests

caption = "The expression of TP53 was elevated in lung cancer cells."

url = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/"
params = {
    "text": caption,
    "concepts": "gene,disease,chemical,species,mutation"
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(url, data=params, headers=headers)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
