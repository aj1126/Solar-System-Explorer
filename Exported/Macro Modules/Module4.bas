Attribute VB_Name = "Module4"
Sub ColorizeOrbitalPlot()
    Dim wsData As Worksheet
    Dim wsPlot As Worksheet
    Dim ch As Chart
    Dim objName As String
    Dim colorHex As String
    Dim s As Series

    'Sheets
    Set wsData = ThisWorkbook.Sheets("Sorting Data")
    Set wsPlot = ThisWorkbook.Sheets("Orbital Plotter")
    Set ch = wsPlot.ChartObjects("Chart 1").Chart

    'Object name from the drop-down (C2 shows symbol version)
    objName = wsPlot.Range("C2").Value

    'Look up the matching color in Sorting Data, column AB = names w/ symbols, AC = Plot_color
    colorHex = Application.VLookup(objName, wsData.Range("AB2:AC1700"), 2, False)
    If IsError(colorHex) Or Len(colorHex) = 0 Then Exit Sub

    'Convert #RRGGBB to VBA color
    Dim r As Long, g As Long, b As Long
    r = CLng("&H" & Mid(colorHex, 2, 2))
    g = CLng("&H" & Mid(colorHex, 4, 2))
    b = CLng("&H" & Mid(colorHex, 6, 2))
    Dim rgbColor As Long
    rgbColor = RGB(r, g, b)

    'Apply to the series named exactly "Orbital Plot"
    Set s = ch.SeriesCollection("Orbital Plot")
    With s.Format
        'Outline/line color
        .Line.ForeColor.RGB = rgbColor
        'Marker interior (if a point marker is used)
        .Fill.ForeColor.RGB = rgbColor
    End With
    
    Call ResizeOrbitalPlot

End Sub

