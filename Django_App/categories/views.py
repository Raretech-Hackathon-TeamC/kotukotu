from django.shortcuts import render

# TODO: ホーム画面にカテゴリー毎の累計活動時間の表示
    #* activity:HomeView内でimportする必要あり
    #* カテゴリーが削除済み(is_deleted = Ture)の場合は表示しない

# TODO: カテゴリー毎のhome画面
    #* カテゴリー毎の累計時間・累計日数の表示
    #* グラフの表示に必要なjson型データの送信

# TODO: カテゴリー作成機能
    #* activity:HomeViewでimportする必要あり
    #* home内でカテゴリー追加モーダルを表示(カテゴリー名・目標・色を選択)

# TODO: カテゴリーの編集
    #* カテゴリー毎のhome画面でモーダルで表示(カテゴリー名・目標・選択)

# TODO: カテゴリーの削除機能
    #* カテゴリー毎のhome画面で削除モーダルを表示し削除
    #* カテゴリー削除はis_deletedをtureに変更
