#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require 'mysql'
require 'cgi/session'
cgi = CGI.new
session = CGI::Session.new(cgi)

connection = Mysql::connect("localhost" , "m_naito", nil,"m_naito_practice")

# 文字コードをUTF8に設定
connection.query("set character set utf8")
strdata = ""
stu_id = CGI.escapeHTML(cgi["s_id"])
stu_pass = CGI.escapeHTML(cgi["s_password"])
main_url = "main.cgi"
teacher_url = "teacher.cgi"


if !(stu_id.empty? || stu_pass.empty?)
	if stu_id == "99999" && stu_pass == "dR951kntq"
		print cgi.header({"status" => "REDIRECT", "location" => teacher_url})
	else
		login_id_mysql = connection.query("SELECT password FROM student_info WHERE student_id = #{stu_id}")
		#検索結果の個数（数値型）
		login_id = login_id_mysql.num_rows
		#検索したユーザのパスワード
		login_pass = login_id_mysql.fetch_row
		#login_pass = login_id_mysql.fetch_row.map(&:to_s)

		#検索結果によるエラー処理
		if login_id == 0
			strdata = '<p>学籍番号かパスワードが間違っています</p>'
		elsif login_id == 1

			if login_pass[0] == stu_pass
				print cgi.header({"status" => "REDIRECT", "location" => main_url})
			else
				strdata = '<p>学籍番号かパスワードが間違っています</p>'
			end

		else
			strdata = '<p>エラーです、管理者に連絡をしてください</p>'
		end
	end
end

print "Content-type: text/html\n\n"

print <<EOM
<!DOCTYPE html>

<html>
	<head>
	<meta http-equiv="Content-type" content="text/html; charset=UTF-8">
	 <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
	 <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
	 <script type="text/javascript" src="login.js"></script>
	<title>○○高校成績確認サイト</title>
	</head>
	<body>
		<h1>ログインフォーム</h1>
	  <div align="center">
			<table border="0">
				<form name = "stu_login" action="index.cgi" method="post">
	      	<tr>
					#{strdata}
	        	<th>
	            学籍番号
	          </th>
	          <td>
	          	<input type="text" id="s_id" name="s_id" value="" size="25">
							<span id="s_id_error" class="error_m"></span>
	          </td>
	        </tr>
	        <tr>
	          <th>
	         		パスワード 2516df1d1d
	          </th>
	          <td>
	            <input type="password" id="s_password" name="s_password" value="" size="24">
							<span id="s_password_error" class="error_m"></span>
	          </td>
	    		</tr>
	        <tr>
	        	<td colspan="2">
							<input type="button" value="ログイン" onclick="frameClick()">
	          </td>
	        </tr>
	      </form>
	  	</table>
	  </div>
	</body>
</html>
EOM

session['stu_id_session'] = stu_id
