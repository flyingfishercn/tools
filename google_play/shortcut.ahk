; ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
; Hotkeys for JEFF at 20121010
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode 2    
 
Activate(t)
{
	IfWinActive,%t%
	{
		WinMinimize
		return
	}
	SetTitleMatchMode 2    
	DetectHiddenWindows,on
	IfWinExist,%t%
	{
		WinShow
		WinActivate           
		return 1
	}
	return 0
}
 
ActivateAndOpen(t,p)
{
	if Activate(t)==0
	{
		Run %p%
		WinActivate
		return
	}
}
 
; Program in common use
;s::ActivateAndOpen()
;w::ActivateAndOpen()
;a::ActivateAndOpen("Chrome","C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe")
;c::ActivateAndOpen("Picasa","D:\Program Files (x86)\Picasa\Picasa.exe")
;q::ActivateAndOpen("搜索Everything","C:\Program Files (x86)\Everything\Everything.exe")

;#h::
;Run Notepad
;WinWait, 无标题 - 记事本
;MsgBox 记事本窗口已被打开
;Return

;;按键定义
^Up::Send {PgDn}

 ;＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
;百度
#b::Run www.baidu.com

;谷歌
;#g::
 ;  Run http://203.208.46.148/search?q=%clipboard%
;Return

#g::
Run www.waaao.com
Return

#s::
Run C:\Program Files (x86)\Everything\Everything.exe
Return

;Notepad
#n::Run C:\Program Files (x86)\Notepad++\notepad++.exe

;OA
#o::Run C:\Program Files (x86)\lotus\notes\notes.exe

;adb_push .bat
#p::Run D:\Users\Administrator\Desktop\adb_push .bat

;lingoes
#t::Run C:\Users\Administrator\AppData\Local\Lingoes\Translator\lingoes-cn\Lingoes.exe

;eclipse
#j::Run D:\software\eclipse\eclipse.exe

;字符串替换
::'g::http://www.google.com{Left 2}

if (a_hour>10)    ; a_hour 是系统变量, 是当前系统时间中的小时
{
    
     Run C:\Program Files (x86)\Notepad++\notepad++.exe
    
}
