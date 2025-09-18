Attribute VB_Name = "Module1"
Public Sub MirrorSortingData()
    Dim wsData As Worksheet, wsMain As Worksheet, wsBackup As Worksheet
    Dim lastRow As Long, lastCol As Long, i As Long
    Dim rowID As Long, tmpCol As Long
    Dim shp As Shape
    Dim dict As Object

    Application.EnableEvents = False
    Application.ScreenUpdating = False
    
    Set wsData = ThisWorkbook.Sheets("Sorting Data")
    Set wsMain = ThisWorkbook.Sheets("Solar System")
    
    ' Safety check: Require ResetSortingData between runs
    On Error Resume Next
    Set wsBackup = ThisWorkbook.Sheets("SolarSystem_BACKUP")
    On Error GoTo 0

    If Not wsBackup Is Nothing Then
        MsgBox "Reset Sorting Data before running Mirror Sorting Data again.", vbExclamation, "Action Required"
        Application.ScreenUpdating = True
        Application.EnableEvents = True
        Exit Sub
    End If
    
    ' Delete old backup if it exists
    On Error Resume Next
    Application.DisplayAlerts = False
    ThisWorkbook.Sheets("SolarSystem_BACKUP").Delete
    Application.DisplayAlerts = True
    On Error GoTo 0
    
    ' Create backup snapshot
    wsMain.Copy After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count)
    Set wsBackup = ActiveSheet
    wsBackup.Name = "SolarSystem_BACKUP"
    wsBackup.Visible = xlSheetHidden
    
    ' Original MirrorSortingData logic
    Set dict = CreateObject("Scripting.Dictionary")
    
    lastRow = wsData.Cells(wsData.Rows.Count, "L").End(xlUp).Row
    If lastRow < 2 Then GoTo CleanExit
    
    lastCol = wsMain.Cells.Find(what:="*", _
                                After:=wsMain.Cells(1, 1), _
                                LookIn:=xlFormulas, _
                                LookAt:=xlPart, _
                                SearchOrder:=xlByColumns, _
                                SearchDirection:=xlPrevious).Column
    
    For Each shp In wsMain.Shapes
        If Not shp.TopLeftCell Is Nothing Then
            dict(shp.Name) = shp.TopLeftCell.Row
        End If
    Next shp
    
    tmpCol = lastCol + 1
    For i = 2 To lastRow
        rowID = wsData.Cells(i, "L").Value
        wsMain.Cells(rowID, tmpCol).Value = i
    Next i
    
    With wsMain.Sort
        .SortFields.Clear
        .SortFields.Add Key:=wsMain.Range(wsMain.Cells(2, tmpCol), wsMain.Cells(lastRow, tmpCol)), _
                        SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
        .SetRange wsMain.UsedRange
        .Header = xlYes
        .Apply
    End With
    
    For Each shp In wsMain.Shapes
        If dict.Exists(shp.Name) Then
            Dim oldRow As Long, newRow As Long
            oldRow = dict(shp.Name)
            newRow = wsData.Columns("L").Find(what:=oldRow, LookAt:=xlWhole).Row
            shp.Top = wsMain.Cells(newRow, shp.TopLeftCell.Column).Top
            shp.Left = wsMain.Cells(newRow, shp.TopLeftCell.Column).Left
        End If
    Next shp
    
    wsMain.Columns(tmpCol).Delete
    
    ' Keep user on Solar System sheet, but only cell M8 selected
    wsMain.Activate
    wsMain.Range("M8").Select
    
CleanExit:
    Application.ScreenUpdating = True
    Application.EnableEvents = True
End Sub

' NOTE FOR FUTURE CHANGES:
' If new data columns are added to "Solar System" and "Sorting Data":
'   - Update the column letter for "ID_#" wherever "L" is used
'     (currently: lastRow = wsData.Cells(wsData.Rows.Count, "L").End(xlUp).Row
'      and rowID = wsData.Cells(i, "L").Value).


