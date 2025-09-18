Attribute VB_Name = "Module5"
Sub ResizeOrbitalPlot()
    Dim wsPlot As Worksheet
    Dim ch As Chart
    Dim q As Double
    Dim pad As Double
    Dim maxQ As Double
    
    Set wsPlot = ThisWorkbook.Sheets("Orbital Plotter")
    Set ch = wsPlot.ChartObjects("Chart 1").Chart
    
    ' Read the apsis value (H2) and add 10% margin
    q = wsPlot.Range("H2").Value
    If q <= 0 Then Exit Sub
    pad = q * 0.1
    maxQ = q + pad          ' single absolute limit used for all axes
    
    With ch
        ' X-axis
        With .Axes(xlCategory)
            .MinimumScale = -maxQ
            .MaximumScale = maxQ
            .MajorUnit = maxQ / 3   ' keeps grid spacing consistent
        End With
        
        ' Y-axis
        With .Axes(xlValue)
            .MinimumScale = -maxQ
            .MaximumScale = maxQ
            .MajorUnit = maxQ / 3   ' same spacing as X
        End With
    End With
End Sub


