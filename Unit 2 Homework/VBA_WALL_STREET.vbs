

Sub HW2_VBA_OF_WALL_STREET()


    ''''''''''''''''''''HOMEWORK 2 HARD-PART''''''''''''''''''''''''''''''
    
    
    ' --------------------------------------------
    ' LOOP THROUGH ALL SHEETS
    ' --------------------------------------------
    For Each ws In Worksheets
    
    
        Dim WorksheetName As String
        
        WorksheetName = ws.Name
        'MsgBox ("WorksheetName : " & WorksheetName)
    
        ''''Declaring Variables''''
        Dim i As Long
        Dim total_vol As Double
        Dim row As Integer
        total_vol = 0
        row = 2
        
        
        ''''Headers Name''''
        ws.Range("I" & 1).Value = "Ticker"
        ws.Range("J" & 1).Value = "Yearly Change"
        ws.Range("K" & 1).Value = "Percentage Change"
        ws.Range("L" & 1).Value = "Total Stock Volume"
        
        
        
        ''''Couting total non-blank rows in worksheet''''
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).row
        'MsgBox (LastRow)
        
        
        
         ''''LOOPING THROUGH EACH ROW''''
        For i = 2 To LastRow
        
                ''If cells value not equal''
                If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                    
                    
                    Ticker = ws.Cells(i, 1).Value
                    ws.Range("I" & row).Value = Ticker
                    
                    ''''YEARLY CHANGE''''
                    
                    Year_End_Value = ws.Cells(i, 6).Value
                    'MsgBox (Ticker & " : Year_End_Value :" & Year_End_Value)
                    'MsgBox (Cells(i, 1).Value & " AND " & Cells(i + 1, 1).Value)
                    
                    
                    
                    Yearly_Difference = Year_Start_Value - Year_End_Value
                    ws.Range("J" & row).Value = Yearly_Difference
                    'MsgBox (Ticker & " : Yearly_Difference : " & Yearly_Difference)
                    
                    
                    
                    ''''Conditional formatting that will highlight positive change in green and negative change in red.
                    If Yearly_Difference < 0 Then
                        ws.Range("J" & row).Interior.ColorIndex = 3
                    Else
                        ws.Range("J" & row).Interior.ColorIndex = 4
                    End If
                    
                    
                    
                    ''''PERCENTAGE CHANGE''''
                    If Year_Start_Value <> 0 Then
                        Percentage_Change = (Yearly_Difference / Year_Start_Value)
                        'MsgBox (Percentage_Change)
                        ws.Range("K" & row).Value = Percentage_Change
                        ws.Range("K" & row).NumberFormat = "0.00%"
                    End If
        
        
        
                     ''''Calculating Total Stock Volume''''
                    total_vol = total_vol + ws.Cells(i, 7).Value
                    ws.Range("L" & row).Value = total_vol
                    total_vol = 0
                                   
                                   
                    ''''Moving to next record in Summary''''
                    row = row + 1
                    
                    
                ''If cells value equal''
                Else
                
                    ''''Finding stock price at year start''''
                    
                    If ws.Cells(i, 2).Value = "20160101" Or ws.Cells(i, 2).Value = "20140101" Or ws.Cells(i, 2).Value = "20150101" Then
                    
                        Year_Start_Value = ws.Cells(i, 3).Value
                        Ticker = ws.Cells(i, 1).Value
                        'MsgBox (Ticker & " : Year_Start_Value :" & Year_Start_Value)
                    
                    End If
                    total_vol = total_vol + ws.Cells(i, 7).Value
                    
                End If
                
         
         
        Next i
        ''''End looping through each row''''
        
        
        
       '''''''''''''''''''''''''''''
       ''''Hard Part of Homework''''
       '''''''''''''''''''''''''''''
       
       ws.Range("O" & 2).Value = "Greatest % Increase"
       ws.Range("O" & 3).Value = "Greatest % Decrease"
       ws.Range("O" & 4).Value = "Greatest Total Volume"
       ws.Range("P" & 1).Value = "Ticker"
       ws.Range("Q" & 1).Value = "Value"
       
       Percentage_Min = 0
       Percentage_Max = 0
       
       
       
       ''''Greatest Percentage Increase and Decrease '''''
       
       Percentage_Min = Application.WorksheetFunction.Min(ws.Columns("K"))
       Percentage_Max = Application.WorksheetFunction.Max(ws.Columns("K"))
        
       ws.Range("Q" & 2).Value = Percentage_Max
       ws.Range("Q" & 3).Value = Percentage_Min
       ws.Range("Q" & 2).NumberFormat = "0.00%"
       ws.Range("Q" & 3).NumberFormat = "0.00%"
       'MsgBox ("Max : " & Percentage_Max & " Min : " & Percentage_Min)
        
       Dim j
       j = 2


        ''''Calculating Greatest % Increase, % Decrease and corresponding Ticker''''
       
       Do While ws.Cells(j, 11).Value <> ""
       
            If ws.Cells(j, 11).Value = Percentage_Max Then
                ws.Range("P" & 2).Value = ws.Cells(j, 9).Value
               
            ElseIf ws.Cells(j, 11).Value = Percentage_Min Then
                 ws.Range("P" & 3).Value = ws.Cells(j, 9).Value
            
            End If
            j = j + 1
            
       Loop
               
       
       ''''Calculating Greatest Total Stock Volume and corresponding Ticker''''
       Greatest_Total_Volume = 0
       
       Greatest_Total_Volume = Application.WorksheetFunction.Max(ws.Columns("L"))
       ws.Range("Q" & 4).Value = Greatest_Total_Volume
       
       Dim r As Integer
       r = 2
       Do While ws.Cells(r, 12).Value <> ""
       
            If ws.Cells(r, 12).Value = Greatest_Total_Volume Then
                ws.Range("P" & 4).Value = ws.Cells(r, 9).Value
            
            End If
            r = r + 1
            
       Loop
            
            
       
       
    Next ws
    ''''Loop through next worksheet''''

End Sub




