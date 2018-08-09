#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
cgi = CGI.new

print "Content-type: text/html\n\n"

print <<EOM
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>○○のブログ</title>
</head>
<body>

<!-- ヘッダ -->
<header>
<h1><a href="http://www.htmq.com/blog/">○○のブログ</a></h1>
</header>

<!-- メインコンテンツ -->
<section>
<h2>はじめに</h2>
<p>初めての方はお読みください。</p>
<article>
<h3><a href= "entry1.html">ご挨拶</a></h3>
<p>いらっしゃいませ。○○と申します…</p>
</article>
<article>
<h3><a href= "entry21.html">お約束</a></h3>
<p>このブログをご覧になる際には…</p>
</article>
</section>

<section>
<h2>最近の投稿</h2>
<p>最近の投稿記事2件を表示します。</p>
<article>
<h3><a href= "entry99.html">買い物</a></h3>
<p>今日は買い物に出掛けた…</p>
</article>
<article>
<h3><a href= "entry98.html">読書</a></h3>
<p>今日は読書をして過ごした…</p>
</article>
<nav>
<a href="?p=2">次のページへ</a>
</nav>
</section>

<!--ナビゲーション -->
<nav>
<h2>カテゴリ</h2>
<ul>
<li><a href="category1.html">はじめに</a></li>
<li><a href="category2.html">日常</a></li>
<li><a href="category3.html">仕事</a></li>
</ul>
</nav>

<!-- フッタ -->
<footer>
<p>Copyright 2015</p>
</footer>

</body>
</html>
EOM
