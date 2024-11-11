import time

# ゲーム紹介
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
    print("3. ヤマザキジ")
    choice = input("誰を仲間にしますか？（1または2または3）: ")

    if choice == "1":
        print("\nだいす犬: きびだんご全部食ってやるよ！ガハハハッ！")
        print("GAMEOVER!だいす犬がきびだんごを全部食べてしまった！食糧がなくなった桃太郎は死んだ！")
        return
    elif choice == "2":
        print("\nモンキー泉水: 力がみなぎってきた...！ギアセカンド！")
        print("泉水は覚醒した！泉水と協力して鬼を蹴散らそう！")
        onitaiji_with_monkey()
    elif choice == "3":
        print("\nヤマザキジ: 鬼のデータは収集済みさ...！いつでも奇襲をかけて殺す準備はできてますよ。")
        print("ヤマザキジはサイコ感強めだが頼りになりそうだ。ヤマザキジと共に、鬼をぶっ〇しに行こう！")
        onitaiji_with_pheasant()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# キャバクラ
def go_to_kyabakura():
    print("\nまずはどの子と対峙するのか真剣に考えて決めよう！")
    time.sleep(1)
    print("どの子と遊ぼうかなぁ～")

    print("\n1. 日本一美人なキャバ嬢・かぐや")
    print("2. 東京を支配している伝説のキャバ嬢・ゆりこ")
    print("3.最年長キャバ嬢・泉ピン子")
    choice = input("どちらに行きますか？（1または2または3）: ")

    if choice == "1":
        print("\nかぐや: おい。鬼退治行ってこいや。キャバクラなんか来てる場合ちゃうぞ。")
        print("GAMEOVER!かぐやに竹でぶん殴られた！実は元ヤンだったかぐやは喧嘩最強だった！なにも抵抗できないまま桃太郎は死んだ！")
        return
    elif choice == "2":
        print("\nゆりこ: いつもは都民ファーストだけど、今夜はあなたファーストよ。")
        print("ゆりこはとてもやさしい女性のようだ。ゆりこと限られた時間を存分に楽しもう。")
        party_with_yuriko()
    elif choice == "3":
        print("\nピン子: 渡る世間は鬼ばかりだけど、鬼退治してる暇があるなら私ともっと楽しいことしよ？♥")
        print("まちがいない。ピン子は大当たりだ。今夜はピン子と素敵な夜を過ごそう。")
        party_with_pinko()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# 泉水と鬼退治
def onitaiji_with_monkey():
    print("\nどうやって鬼を倒すか決めよう！")
    time.sleep(1)
    print("さて、どうやって蹴散らすかな。")

    print("\n1.泉水と合体して倒す")
    print("2.泉水をおとりにして、おいしいところは全部自分がもっていく")
    print("3.シンプルに銃を使って仕留める")
    choice = input("どうやって倒す？（1または2または3):")

    if choice == "1":
        print("\nモンキー泉水: いくぜ桃太郎！フュージョン！はっ！")
        print("泉水と合体して「桃モンキー」となった！圧倒的なパワーで鬼を全滅させることに成功した！")
        zaihou_with_monkey()
    elif choice == "2":
        print("\nモンキー泉水: いや、ちょっ...おとりにするとか聞いてないって！")
        print("GAMEOVER!泉水は鬼にリンチにされた！仕方ないから一人で立ち向かった桃太郎は返り討ちにされて死んだ！")
        return
    elif choice == "3":
        print("\nモンキー泉水: ピストル使えば一発で仕留められるぜ？")
        print("普通に銃で撃ったら、鬼全員死んだ。")
        zaihou_with_monkey()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# 山崎と鬼退治
def onitaiji_with_pheasant():
    print("\nどうやって鬼を倒すか決めよう！")
    time.sleep(1)
    print("さて、どうやって蹴散らすかな。")

    print("\n1.鬼に睡眠薬が入ったエナジードリンクを飲ませて、眠らせてから倒す")
    print("2.ヤマザキジのデータを基に鬼の弱点をあぶりだして倒す")
    print("3.鬼にエロ本を与えて、鬼が読み始めたら一気に奇襲をかけて倒す")
    choice = input("どうやって倒す？（1または2または3):")

    if choice == "1":
        print("\nヤマザキジ: 鬼よ。永遠に眠れ。")
        print("鬼がぐっすり寝ている隙に、鬼をぶっ〇した。")
        zaihou_with_pheasant()
    elif choice == "2":
        print("\nヤマザキジ: 鬼の弱点は首です。首を切ってください。桃太郎さん？ちょっ...グハァ！")
        print("GAMEOVER!間違えてヤマザキジの首を切ってしまった！もう全部どうでもよくなった桃太郎は自分の首も切って死んだ！")
        return
    elif choice == "3":
        print("\nヤマザキジ: 鬼に金棒はもう古い。今の時代は「鬼にエロ本」ですよ。")
        print("エロ本に夢中なスケベ鬼を全員蹴散らした！")
        zaihou_with_pheasant()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return
    
# ゆりことパーリナイ
def party_with_yuriko():
    print("\nゆりこと最高の夜を楽しもう！")
    time.sleep(1)
    print("なにして遊ぼうかな。")

    print("\n1.「山手線の駅名」がお題のガチ山手線ゲームをする。")
    print("2.ゆりこと二人だけの秘密を共有して距離を縮める。")
    print("3.飲みのコールで盛り上がる。")
    choice = input("なにをする？（1または2または3):")

    if choice == "1":
        print("\nゆりこ: 山手線の駅名は全部覚えているわ。だってわたし東京を支配しているもの。")
        print("ゆりこはガチ山手線ゲーム激強だった。上機嫌になったゆりこからアフターのお誘いが来た！！")
        after_with_yuriko()
    elif choice == "2":
        print("\nゆりこ: 誰にも言わないでね。わたしれんほうちゃんのこと大嫌いなの。")
        print("GAMEOVER!なぜか隣のテーブルにいたれんほうちゃんにこの会話をきかれてしまった！あまりの気まずさに桃太郎は死んだ！")
        return
    elif choice == "3":
        print("\nゆりこ: どんぶらこ！どんぶらこ！ガンガン飲んでどんぶらこ！")
        print("ゆりこはコールがうまかった。このままゆりことアフターすることになった！！")
        after_with_yuriko()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# ピン子とパーリナイ
def party_with_pinko():
    print("\nピン子と最高の夜を楽しもう！")
    time.sleep(1)
    print("なにして遊ぼうかな。")

    print("\n1.トランプタワーを作る。")
    print("2.シャンパンタワーを作る。")
    print("3.きびだんごタワーを作る。")
    choice = input("なにをする？（1または2または3):")

    if choice == "1":
        print("\nピン子: ももちゃんトランプタワー作るのうま～い！♥")
        print("ピン子のご機嫌取りの方がうまい。このままピン子とアフターすることになった！")
        after_with_pinko()
    elif choice == "2":
        print("\nピン子: 素敵なシャンパンタワーね。一緒に乾杯しましょ！♥")
        print("GAMEOVER!なぜかシャンパンに毒が入っていた！桃太郎もピン子も死んだ！")
        return
    elif choice == "3":
        print("\nピン子: 立派なきびだんごタワーね！ももちゃん素敵！♥")
        print("ピン子を喜ばせることができた。その後、ピン子からアフターのお誘いが来た！！")
        after_with_pinko()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# 財宝出現！（泉水ver.）
def zaihou_with_monkey():
    print("\n鬼を倒したら財宝が出てきた！全部もらおう！")
    time.sleep(1)
    print("うひょー！財宝がいっぱいだー！")

    print("\n1.財宝を持ち帰って、村のみんなに分ける。")
    print("2.財宝は泉水と山分け。村のみんなのことなんか知るか。")
    print("3.泉水を倒して財宝を独占する。")
    choice = input("どうする？（1または2または3):")

    if choice == "1":
        print("\nモンキー泉水: 村のみんなに財宝分けすぎて、俺らの分なくなっちまった。")
        print("GAMEOVER！はいざんねーん！この世は弱肉強食～！村のみんなに優しくしすぎて力尽きた桃太郎は死んだ！")
        return
    elif choice == "2":
        print("\nモンキー泉水: これがひとつなぎの大財宝ってやつか。俺がいただくぜ！")
        print("GAMEOVER!実は海賊だった泉水に財宝を全部持ってかれた！なにもなくなった桃太郎は死んだ！")
        return
    elif choice == "3":
        print("\nモンキー泉水: うっ...！桃ちゃん...俺を仲間にしてくれてありがとよ...！")
        print("寝言は寝て言えよwww 邪魔者が消えた桃太郎は億万長者となった！GAMECLEAR!!!")
        ending()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# 財宝出現！（山崎ver.）
def zaihou_with_pheasant():
    print("\n鬼を倒したら財宝が出てきた！全部もらおう！")
    time.sleep(1)
    print("うひょー！財宝がいっぱいだー！")

    print("\n1.財宝を持ち帰って、村のみんなに分ける。")
    print("2.財宝をデータ分析する。")
    print("3.ヤマザキジをぶっ〇す。")
    choice = input("どうする？（1または2または3):")

    if choice == "1":
        print("\nヤマザキジ: 村のみんなに財宝分けすぎて、我々の分の財宝がなくなりました。")
        print("GAMEOVER！はいざんねーん！この世は弱肉強食～！村のみんなに優しくしすぎて力尽きた桃太郎は死んだ！")
        return
    elif choice == "2":
        print("\nヤマザキジ: データ分析が完了しました。これは財宝ではありませんね。ただのゴミです。")
        print("GAMEOVER!どう見ても財宝だと思うが、ヤマザキジの分析によるとこれらはゴミらしい！なにもなくなった桃太郎は死んだ！")
        return
    elif choice == "3":
        print("\nヤマザキジ: 桃太郎さん...！あなたは私のデータ分析によると...100%地獄に落ちますよ...！")
        print("なにを言っているのかさっぱりわからなかったが、とりあえず邪魔者が消えた桃太郎は億万長者となった！GAMECLEAR!!!")
        ending()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# ゆりことアフター
def after_with_yuriko():
    print("\nゆりことデートスポットへ行こう！")
    time.sleep(1)
    print("どこに行こうかな。")

    print("\n1.東京スカイツリー")
    print("2.東京ディズニーリゾート")
    print("3.東京都庁")
    choice = input("どこに行く？（1または2または3):")

    if choice == "1":
        print("\nゆりこ: 高ーい！地上何メートルこれ？地面とソーシャルディスタンス取りすぎでしょ！")
        print("GAMEOVER!ゆりこは高所恐怖症だった。なにもできずに桃太郎は死んだ！")
        return
    elif choice == "2":
        print("\nゆりこ: ここは東京じゃない...！千葉よ！私の聖域ではないのよ！！")
        print("GAMEOVER!ゆりこは東京都の外に出てしまうと一気に弱体化してしまった。ちなみに桃太郎は死んだ！")
        return
    elif choice == "3":
        print("\nゆりこ: 都庁から見る夜景...素敵だわ。桃太郎さん。私ともっと「密」な関係になりませんか？")
        print("その後、僕とゆりこは都庁で結婚式を挙げ、いつまでも幸せに暮らした。GAMECLEAR!!!")
        ending()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return

# ピン子とアフター
def after_with_pinko():
    print("\nピン子とカラオケにきた！")
    time.sleep(1)
    print("何を歌えばピン子を喜ばせることができるかな。")

    print("\n1.back number「クリスマスソング」")
    print("2.ドリーミング「アンパンマンのマーチ」")
    print("3.マキシマム ザ ホルモン「メス豚のケツにビンタ（キックも）」")
    choice = input("どの曲を歌う？（1または2または3):")

    if choice == "1":
        print("\nピン子: back number歌ってる男は大体女々しい。")
        print("GAMEOVER!ピン子の偏りすぎている偏見が胸に刺さった。桃太郎は死んだ！")
        return
    elif choice == "2":
        print("\nピン子: わたしは「勇気りんりん」の方が好きだわ。")
        print("GAMEOVER!選挙ミス。愛と勇気すら友達にできなかった桃太郎は死んだ！")
        return
    elif choice == "3":
        print("\nピン子: メス！メス！メス豚のケツにビンタ！キックも～♪")
        print("ピン子はノリノリだ。その後、オールでカラオケした後に僕とピン子は結婚した。GAMECLEAR!!!")
        ending()
    else:
        print("無効な入力です。ゲームが終了しました。")
        return
    
# エンディング
def ending():
    print("お見事！このエンディングに到達しているということは、財宝もしくはキャバ嬢の桃をGETしてゲームをクリアしたということだ！おめでとう！")
   
# ゲーム実行
start_game()
