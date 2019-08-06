ControlFocus("选择要加载的文件", "", "Edit1")

WinWait("[CLASS:#32770]", "", 10)

Dim $Files = ""
For $i = 1 to $CmdLine[0] Step 1
   ;MsgBox(0, "param", $CmdLine[$i])
   $Files = $Files & ' "' & $CmdLine[$i] & '"'
Next
;MsgBox(0, "files", $Files)
ControlSetText("选择要加载的文件" ,"", "Edit1", $Files)
Sleep(1000)

ControlClick("选择要加载的文件", "","Button1");