ControlFocus("ѡ��Ҫ���ص��ļ�", "", "Edit1")

WinWait("[CLASS:#32770]", "", 10)

Dim $Files = ""
For $i = 1 to $CmdLine[0] Step 1
   ;MsgBox(0, "param", $CmdLine[$i])
   $Files = $Files & ' "' & $CmdLine[$i] & '"'
Next
;MsgBox(0, "files", $Files)
ControlSetText("ѡ��Ҫ���ص��ļ�" ,"", "Edit1", $Files)
Sleep(1000)

ControlClick("ѡ��Ҫ���ص��ļ�", "","Button1");