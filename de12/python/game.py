import time

# キャラクター紹介
def introduce_games():
    print("ぱっかーん！あなたは桃から生まれた桃太郎。早速世界平和のためにどこへ何をしに行くか決めよう！")
    print("1. 鬼ヶ島へ、鬼退治に行くぜ！")
    print("2. キャバクラで、キャバ嬢と対峙しにいくぜ！")

# ゲームスタート
def start_game():
    print("鬼退治orキャバ対峙！生きるか死ぬかの桃太郎デスゲーム開幕！")
    introduce_games()
    time.sleep(1)

    print("\nどちらに向かいますか？")
    choice = input("1. 鬼ヶ島\n2. キャバクラ\n選択してください（1または2）: ")

    if choice == "1":
        go_to_onigashima()
    elif choice == "2":
        go_to_kyabakura()
    else:
        print("無効な入力です。もう一度お試しください。")
        start_game()

# 鬼ヶ島
def go_to_onigashima():
    print("\nまずは鬼退治するための仲間集めだ！")
    time.sleep(1)
    print("きびだんごあげるから俺の下につけやコラ")
    
    print("\n1. 道用だいす犬")
    print("2. モンキー・D・泉水")
    print("3.ヤマザキジ")
    choice = input("誰を仲間にしますか？（1または2または3）: ")

    if choice == "1":
        print("\nだいす犬: きびだんご全部食ってやるよ！ガハハハッ！")
        print("だいす犬がきびだんごを全部食べてしまった！食糧がなくなった桃太郎は死んだ！")
        ending("good", "アカリ")
    elif choice == "2":
        print("\nモンキー泉水: 力がみなぎってきた...！ギアセカンド！")
        print("泉水は覚醒した！")
        ending("good", "アカリ")
    elif choice == "3":
        print("\nヤマザキジ: 鬼のデータは収集済みさ...！いつでも奇襲をかけて殺す準備はできてますよ。")
        print("ヤマザキジはサイコ感強めだが頼りになりそうだ。")
        ending("good", "アカリ")
    else:
        print("無効な入力です。デートが終了しました。")
        ending("bad", "アカリ")

# ユウとのデート
def go_to_kyabakura():
    print("\nユウと図書館デートに来ました！")
    time.sleep(1)
    print("ユウ: 静かでいい場所だね。")

    print("\n1. 一緒に本を読む")
    print("2. カフェでお茶をする")
    choice = input("どちらに行きますか？（1または2）: ")

    if choice == "1":
        print("\nユウ: この本、面白いね。")
        print("本について話しているうちに、二人の心が通じ合った！")
        ending("good", "ユウ")
    elif choice == "2":
        print("\nユウ: あなたと話すと、時間があっという間だね。")
        print("カフェでのんびりと会話を楽しみ、ユウとの距離が縮まった！")
        ending("good", "ユウ")
    else:
        print("無効な入力です。デートが終了しました。")
        ending("bad", "ユウ")

# エンディング
def ending(result, character):
    if result == "good":
        print(f"\n{character}と素敵な時間を過ごしました！")
        print(f"あなたと{character}は恋人同士になりました。おめでとう！")
    else:
        print(f"\nデートは上手くいきませんでした。次のチャンスに期待しましょう！")

# ゲーム実行
start_game()
