for i in range(1,3): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！

# 出力結果
# 0 人目
# 1 人目
# 2 人目

for track in results['tracks']:
            print(f"{track['name']} by {track['artists'][0]['name']}")