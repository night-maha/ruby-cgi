#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require 'mysql'
require 'cgi/session'
cgi = CGI.new
session = CGI::Session.new(cgi)

stu_id = session['stu_id_session']
form_year = CGI.escapeHTML(cgi["p_year"])
form_semester = CGI.escapeHTML(cgi["p_semester"])

connection = Mysql::connect("localhost" , "m_naito", nil,"m_naito_practice")

# 文字コードをUTF8に設定
connection.query("set character set utf8")

#ユーザの名前取得
login_id_stuname = connection.query("SELECT name FROM student_info WHERE student_id = #{stu_id}")
stuname = login_id_stuname.fetch_row

#データに存在する年度の取得
allseason_arr = []
allseason = connection.query("select year from record")
allseason.each do |toshi|
  allseason_arr.push(toshi)
end
allyears  =  allseason_arr.uniq!



#成績の情報抽出
result_show = []

if (form_year.empty? && form_semester.empty?)
  login_id_mysql = connection.query("SELECT jpn, math, eng, sci, soc, year, semester
    FROM record
    WHERE student_id = #{stu_id}
    ORDER BY year DESC, semester DESC")
elsif (form_semester.empty?)
  login_id_mysql = connection.query("SELECT jpn, math, eng, sci, soc, year, semester
    FROM record
    WHERE student_id = #{stu_id} AND year = #{form_year}
    ORDER BY semester desc")
elsif (form_year.empty?)
  login_id_mysql = connection.query("SELECT jpn, math, eng, sci, soc, year, semester
    FROM record
    WHERE student_id = #{stu_id} AND semester = #{form_semester}
    ORDER BY year desc")
else
  login_id_mysql = connection.query("SELECT jpn, math, eng, sci, soc, year, semester
    FROM record
    WHERE student_id = #{stu_id} AND year = #{form_year} AND semester = #{form_semester}")
end

#columnとrowの取得
column = login_id_mysql.num_fields()
row = login_id_mysql.num_rows()

#各データを配列に格納
if row == 0
  error_result = '<p>指定した期間では成績がありません</p>'
else
  login_id_mysql.each do |result_data|
     result_show.push(result_data)
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
	<title>生徒用</title>
	</head>
	<body>
    <h1>成績表示</h1>
    <br>
      <form name="semester" action="main.cgi" method="post">
      <select name="p_year" id="s_year">
      <option value="" selected>年度を選択してください。</option>
EOM

      y = 0
      while y < allyears.length
        print "<option value = "
        print allyears[y][0]
        print ">"
        print allyears[y][0]
        print "</option>"
        y += 1
      end

print <<EOM
      </select>
      <select name="p_semester" id="s_semester">
      <option value="" selected>学期を選択してください。</option>
      <option value="1">1学期</option>
      <option value="2">2学期</option>
      <option value="3">3学期</option>
      </select>
    <td colspan="2">
      <input type="submit" value="表示">

    </form>
    <div align="center">
      <table border="1">
      #{stuname[0]}さんの成績です
      #{error_result}

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
