import android_auto_play_opencv as am
import json

adbpath = 'C:\\Program Files\\Nox\\bin\\'
aapo = am.AapoManager(adbpath)
count = 0


# アカウントデータの読み込み
file = open('account.txt', 'r', encoding='utf-8')
account_data = json.load(file)
file.close()

# アカウント分繰り返し
for account in account_data:
    print('ID: {0}, PASSWORD:{1}'.format(account['id'], account['pwd']))

    # ID入力
    aapo.touchPos(250, 430)
    aapo.sleep(1)
    aapo.inputtext(account['id'])
    aapo.sleep(1)

    # パスワード入力
    aapo.touchPos(250, 560)
    aapo.sleep(1)
    aapo.inputtext(account['pwd'])
    aapo.sleep(1)

    # 何かスゴイ処理↓
    while True:
        print('何かスゴイ処理: {0}'.format(count))
        aapo.screencap()

        if count >= 10:
            # 何かスゴイ処理を抜ける
            print('何かスゴイ処理を抜ける')
            count = 0
            break
        else:
            # 何かスゴイ処理を続ける
            count += 1

        pass
    # 何かスゴイ処理↑

print('終了')
