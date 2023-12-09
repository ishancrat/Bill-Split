df = pd.DataFrame(header)
df = df.reset_index()
check = input("create excel sheet? :")
path ="C://Users//Ishan//Desktop//" 
if (check.upper() == 'Y'):
    sheetNameAndPath = path+"trip_"+date+".xlsx"
    df.to_excel(sheetNameAndPath,header=False,index=False)
    print("Sheet saved to Desktop")
else:
    print("OK :)")
