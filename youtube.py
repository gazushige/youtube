from pytube import YouTube
import tkinter
import tkinter.filedialog as PATH


def movieCode():
    # Tkクラス生成
    root = tkinter.Tk()
    # 画面サイズ
    root.geometry('400x200')
    # 画面タイトル
    root.title('YouTubeダウンローダー')

    # ラベル
    lbl = tkinter.Label(text='動画URL：')
    lbl.place(x=20, y=70)

    # テキストボックス
    txt = tkinter.Entry(width=50)
    txt.place(x=80, y=70)

    # 説明
    description = tkinter.Label(text='YouTubeの動画URLをコピペして\nダウンロードボタンを押して下さい')
    description.place(x=120, y=100)
    # 決定ボタン
    btn = tkinter.Button(root, text='ダウンロード',
                         command=lambda: btnClick(txt.get()))
    btn.place(x=160, y=170)

    # 表示
    root.mainloop()
    return


def btnClick(url):
    yt = YouTube(url)

    # 最高画質のmp4形式でダウンロード
    stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    # デフォルトのファイル名を取得
    fn = stream.default_filename

    # 名前をつけて保存のダイアログボックスを表示
    savePath = PATH.asksaveasfilename(initialfile=fn, initialdir='./')

    # キャンセル時の処理
    if not savePath:
        print('キャンセルされたので処理を中断します')
        return

    # ダウンロード実施
    stream.download(savePath)
    return


if __name__ == '__main__':
    movieCode()
