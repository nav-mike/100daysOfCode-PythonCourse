from bs4 import BeautifulSoup
import requests

# with open("website.html") as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.find_all(class_="heading"))
# print(soup.select_one(selector="p em a").get("href"))

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
stories = soup.select(selector=".titlelink")
upvotes = soup.select(selector=".score")

article_titles = [story.getText() for story in stories]
article_links = [story.get("href") for story in stories]
article_upvotes = [int(upvote.getText().split()[0]) for upvote in upvotes]

print(article_titles)
print(article_links)
print(article_upvotes)

# find highest upvote in the list with index
max_upvote = max(article_upvotes)
highest_index = article_upvotes.index(max_upvote)

# print the highest upvote article title and link
print("\nThe highest upvote is:")
print(article_titles[highest_index])
print(article_links[highest_index])
print(article_upvotes[highest_index])
