Attribute VB_Name = "Module3"
Public Sub ColorizeSolarSystem()
    Dim wsSS As Worksheet, wsKey As Worksheet
    Dim lastRowSS As Long, lastColSS As Long
    Dim lastRowKey As Long
    Dim dictColors As Object
    Dim r As Long, domainID As Variant
    Dim clrPrimary As Long, clrSecondary As Long
    
    Application.ScreenUpdating = False
    Application.EnableEvents = False
    
    Set wsSS = ThisWorkbook.Sheets("Solar System")
    Set wsKey = ThisWorkbook.Sheets("Color Key")
    Set dictColors = CreateObject("Scripting.Dictionary")
    
    ' Build dictionary of Domain_ID ? (Primary, Secondary)
    lastRowKey = wsKey.Cells(wsKey.Rows.Count, "AA").End(xlUp).Row
    For r = 2 To lastRowKey
        domainID = wsKey.Cells(r, "AA").Value
        If Not dictColors.Exists(domainID) Then
            clrPrimary = wsKey.Cells(r, "C").Interior.Color
            clrSecondary = wsKey.Cells(r, "D").Interior.Color
            dictColors.Add domainID, Array(clrPrimary, clrSecondary)
        End If
    Next r
    
    ' Get last row and last used column in Solar System
    lastRowSS = wsSS.Cells(wsSS.Rows.Count, "A").End(xlUp).Row
    lastColSS = wsSS.Cells(1, wsSS.Columns.Count).End(xlToLeft).Column
    
    ' Loop through Solar System rows and colorize
    For r = 2 To lastRowSS
        domainID = wsSS.Cells(r, "X").Value
        If dictColors.Exists(domainID) Then
            ' Even rows = primary (darker), odd rows = secondary (lighter)
            If r Mod 2 = 0 Then
                wsSS.Range(wsSS.Cells(r, 1), wsSS.Cells(r, lastColSS)).Interior.Color = dictColors(domainID)(0)
            Else
                wsSS.Range(wsSS.Cells(r, 1), wsSS.Cells(r, lastColSS)).Interior.Color = dictColors(domainID)(1)
            End If
        End If
    Next r
    
    Application.EnableEvents = True
    Application.ScreenUpdating = True
    
    MsgBox "Solar System sheet has been successfully colorized.", vbInformation
End Sub

