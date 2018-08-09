#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require 'mysql'
require 'cgi/session'
cgi = CGI.new
session = CGI::Session.new(cgi)

stu_id = session['stu_id_session']

connection = Mysql::connect("localhost" , "m_naito", nil,"m_naito_practice")

# 文字コードをUTF8に設定
connection.query("set character set utf8")
result_show = []
login_id_mysql = connection.query("SELECT jpn, math, eng, sci, soc, year, semester
  FROM record
  WHERE student_id = #{stu_id}
  ORDER BY year, semester")

column = login_id_mysql.num_fields()
row = login_id_mysql.num_rows()

login_id_mysql.each do |result_data|
   result_show.push(result_data)
   result_show.join ","
end

=begin
i = 0
while i < row
  result = result_show[i]
  result = '<tr>
              <td>#{result_show[i][0]}</td>
              <td>#{result_show[i][1]}</td>
              <td>#{result_show[i][2]}</td>
              <td>#{result_show[i][3]}</td>
              <td>#{result_show[i][4]}</td>
              <td>#{result_show[i][5]}</td>
              <td>#{result_show[i][6]}</td>
            </tr>'
  i += 1
end
=end

print "Content-type: text/html\n\n"

print <<EOM
<!DOCTYPE html>

<html>
	<head>
	<meta http-equiv="Content-type" content="text/html; charset=UTF-8">
	 <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
	 <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
	<title>生徒用</title>
	</head>
	<body>
    <h1>成績表示</h1>
    <div align="center">
      <table border="1">
        <tr>
          <th>国語</th>
          <th>数学</th>
          <th>英語</th>
          <th>理科</th>
          <th>社会</th>
          <th>年度</th>
          <th>学期</th>
        </tr>
EOM

        r = 0
        while r < row
          print '<tr>'
          c = 0
          while c < column
            print '<td>'
            print result_show[r][c]
            print '</td>'
            c += 1
          end
          print '</tr>'
          r += 1
        end

print <<EOM
      </table>
    </div>
	</body>
</html>
EOM

#コネクションを閉じる
connection.close
