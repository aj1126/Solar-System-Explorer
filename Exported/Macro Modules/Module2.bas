Attribute VB_Name = "Module2"
Public Sub ResetSortingData()
    Dim wsData As Worksheet, wsMain As Worksheet, wsBackup As Worksheet
    Dim lastRow As Long
    
    Application.EnableEvents = False
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    
    Set wsData = ThisWorkbook.Sheets("Sorting Data")
    Set wsMain = ThisWorkbook.Sheets("Solar System")
    
    ' Delete current Solar System sheet
    wsMain.Delete
    
    ' Restore Solar System from backup
    Set wsBackup = ThisWorkbook.Sheets("SolarSystem_BACKUP")
    wsBackup.Visible = xlSheetVisible
    wsBackup.Copy Before:=ThisWorkbook.Sheets(1)
    ActiveSheet.Name = "Solar System"
    
    ' Remove backup after restore
    wsBackup.Delete
    
    ' Reset Sorting Data by ID_#
    lastRow = wsData.Cells(wsData.Rows.Count, "L").End(xlUp).Row
    With wsData.Sort
        .SortFields.Clear
        .SortFields.Add Key:=wsData.Range("L2:L" & lastRow), _
                        SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
        .SetRange wsData.Range("A1:N" & lastRow)
        .Header = xlYes
        .Apply
    End With
    
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
    Application.EnableEvents = True
End Sub

' NOTE FOR FUTURE CHANGES:
' If new data columns are added to "Sorting Data":
'   - Update the column letter for "ID_#" wherever "L" is used
'     (currently: lastRow = wsData.Cells(wsData.Rows.Count, "L").End(xlUp).Row
'      and the SortFields.Add range "L2:L" & lastRow).
'   - Update the .SetRange line ("A1:N" & lastRow) so the sort range
'     extends to the new last column (e.g., change "N" to "O" if one new column is added).

