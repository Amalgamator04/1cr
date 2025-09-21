# import requests
# import pandas as pd
# import time

# API_KEY = 'AIzaSyAHyusPnVOJ16wDVeniJv0cVQ1k35UYejw'

# def fetch_all_comments(video_id, api_key):
#     comments = []
#     url = "https://www.googleapis.com/youtube/v3/commentThreads"
#     params = {
#         'part': 'snippet,replies',
#         'videoId': video_id,
#         'maxResults': 100,
#         'textFormat': 'plainText',
#         'key': api_key
#     }

#     while True:
#         response = requests.get(url, params=params)
#         data = response.json()
        
#         for item in data.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']
#             comments.append({
#                 'text': comment['textDisplay'],
#             })
#             # Include replies if any
#             replies = item.get('replies', {}).get('comments', [])
#             for reply in replies:
#                 reply_snippet = reply['snippet']
#                 comments.append({
#                     'text': reply_snippet['textDisplay']
#                 })
        
#         if 'nextPageToken' in data:
#             params['pageToken'] = data['nextPageToken']
#             time.sleep(1)  
#         else:
#             break

#     return comments

# if __name__ == "__main__":
#     print("Fetching comments from YouTube video...")
#     all_comments = fetch_all_comments(VIDEO_ID, API_KEY)
#     print(f"Total comments fetched: {len(all_comments)}")

#     # Save to CSV for manual labeling
#     df = pd.DataFrame(all_comments)
#     df.to_csv('youtube_all_comments.csv', index=False, encoding='utf-8')
#     print("Comments saved to youtube_all_comments.csv")


import requests
import pandas as pd
import time

API_KEY = 'AIzaSyAHyusPnVOJ16wDVeniJv0cVQ1k35UYejw'

def fetch_all_comments(video_id, api_key):
    comments = []
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        'part': 'snippet,replies',
        'videoId': video_id,
        'maxResults': 100,
        'textFormat': 'plainText',
        'key': api_key
    }

    while True:
        response = requests.get(url, params=params)
        data = response.json()

        for item in data.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({'text': comment['textDisplay']})

            replies = item.get('replies', {}).get('comments', [])
            for reply in replies:
                reply_snippet = reply['snippet']
                comments.append({'text': reply_snippet['textDisplay']})

        if 'nextPageToken' in data:
            params['pageToken'] = data['nextPageToken']
            time.sleep(1)
        else:
            break

    return comments

if __name__ == "__main__":
    link_list=[''] #put video id here which is  after "v=" in youtube link
    for i in range(len(link_list)):
        print(f"Fetching data from YouTube video id...{i}")
        all_comments = fetch_all_comments(link_list[i], API_KEY)
        print(f"Fetched {len(all_comments)} comments.")

        df = pd.DataFrame(all_comments)
        df.to_csv(f'youtube_all_comments{i}.csv', index=False, encoding='utf-8')
        print(f"Saved comments to youtube_all_comments{i}.csv")


