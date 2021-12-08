# test_flask-gunicorn-nginx
Flask, gunicorn, nginxの組み合わせで検証を行うためのリポジトリ
## nginxのログについて
`nginx.conf`にてhttpリクエスト及びレスポンスヘッダーをログ出力できるようにしてある。<br>
`/var/log/nginx/header_access.log`に出力される。
## 参考資料
### Locationヘッダー
https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Location
* Location レスポンスヘッダーはリダイレクト先の URL を示します。
### リダイレクト
* https://developer.mozilla.org/ja/docs/Web/HTTP/Redirections
### ログ
#### nginx
* https://siguniang.wordpress.com/2013/10/08/logging-request-response-headers-with-nginx/
* https://www.mk-mode.com/blog/2013/01/16/nginx-access-log/
* https://gato.intaa.net/archives/16110
##### 設定値のリスト
* http://www2.matsue-ct.ac.jp/home/kanayama/text/nginx/node18.html
#### gunicorn
* https://docs.gunicorn.org/en/stable/settings.html#access-log-format
* https://qiita.com/aqmr-kino/items/05ab0e003495d5196210
