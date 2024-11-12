import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Spotify APIの認証情報を入力
client_id = 'fced629031ee4e6fa73ad81c818f1ea8'
client_secret = '244d13bde7fc40d29dd2e52d1f7683ba'

# Spotify APIクライアントの初期化
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 感情に対応するSpotifyの音楽特徴パラメータを定義
def get_emotion_params(emotion):
    if emotion == "joyful":
        return {"energy": 0.7, "valence": 0.8, "danceability": 0.7}
    elif emotion == "sad":
        return {"energy": 0.3, "valence": 0.2, "danceability": 0.3}
    elif emotion == "angry":
        return {"energy": 0.8, "valence": 0.4, "danceability": 0.6}
    elif emotion == "relaxed":
        return {"energy": 0.4, "valence": 0.6, "danceability": 0.5}
    else:
        return {"energy": 0.5, "valence": 0.5, "danceability": 0.5}

# 感情に合った音楽を提案する関数
def recommend_music(emotion):
    # 感情に対応する音楽特徴パラメータを取得
    params = get_emotion_params(emotion)
    
    # Spotify APIの曲検索
    results = sp.recommendations(
        seed_genres=["pop", "rock", "hip-hop", "jazz", "classical"],  # ジャンルを指定（調整可能）
        limit=10,
        target_energy=params["energy"],
        target_valence=params["valence"],
        target_danceability=params["danceability"]
    )
    
    # 曲のリストを表示
    if results and results['tracks']:
        print(f"Emotion: {emotion}")
        print("Recommended Tracks:")
        for track in results['tracks']:
            print(f"{track['name']} by {track['artists'][0]['name']}")
    else:
        print("No tracks found for this emotion.")

# 使用例
emotion = "sad"  # 'joyful', 'sad', 'angry', 'relaxed'のいずれか
recommend_music(emotion)
