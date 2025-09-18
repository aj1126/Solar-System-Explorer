Attribute VB_Name = "Module6"
'=== Unicode helper + macro ===
Private Function Uni(codepoint As Long) As String
    'Return a string for any Unicode code point
    If codepoint < &H10000 Then
        Uni = ChrW(codepoint)
    Else
        Dim hi As Long, lo As Long
        codepoint = codepoint - &H10000
        hi = (codepoint \ &H400) + &HD800
        lo = (codepoint Mod &H400) + &HDC00
        Uni = ChrW(hi) & ChrW(lo)
    End If
End Function

Public Sub FormatSpecialSymbol()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Orbital Plotter")

    Dim specials As Variant
    specials = Array( _
        Uni(&H1F77F), _
        Uni(&H1F77B), _
        Uni(&H1F77E), _
        Uni(&H1F77C), _
        Uni(&H1F77D), _
        Uni(&H2BF0), _
        Uni(&H2BF2))

    Dim val As String, i As Long
    val = ws.Range("C2").Value

    For i = LBound(specials) To UBound(specials)
        If InStr(val, specials(i)) > 0 Then
            ws.Range("C2").Font.Name = "Astromoony"
            Exit Sub
        End If
    Next i
    ws.Range("C2").Font.Name = "Aptos Display"
End Sub



