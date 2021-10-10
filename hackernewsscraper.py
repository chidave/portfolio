import requests
from bs4 import BeautifulSoup


def data_scraping():
    res = requests.get("https://news.ycombinator.com")
    soup = BeautifulSoup(res.text, 'html.parser')

    priority_dict = dict()  # dictionary for posts with more than 100 votes

    subtexts_list = list()  # list for tags with the class "subtext" (is a parent of the score class tags)
    counter = 0
    subtext = soup.select('.subtext')
    for line in subtext:
        subtexts_list.append(line.select('.score'))  # add the childen with the class "score" to the list

        counter += 1

    link_counter = 0
    story_links = soup.select('.itemlist .athing .storylink')
    for line in story_links:
        if len(subtexts_list[link_counter]) != 0:  # check if the subtext tag actually has "score" children
            score_line = subtexts_list[link_counter][0].contents[0]
            score = int(str(score_line).replace(" points", ""))

            if score > 100:
                # print(line.contents[0])
                story_title = line.contents[0]
                priority_dict[f'{story_title} ({score} points)'] = line['href']

        link_counter += 1

    # print(f'Scores num: {len(subtext)}')
    # print(f'Links num: {len(story_links)}')
    #
    # for key, value in priority_dict.items():
    #     print(f'{key}: {value}')

    return priority_dict
