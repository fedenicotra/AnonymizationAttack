import pandas as pd

def seekAlex(date1, date2):
       ## READ FILES ##
       lm = pd.read_csv("data/anonim_levi-montalcini.csv")
       cg = pd.read_csv("data/anonim_camillo-golgi.csv")
       uv = pd.read_csv("data/anonim_umberto-veronesi.csv")

       lm = lm.query("Age == '1*'")
       lm = lm.query("Gender == 'M'")

       lm.loc[:, ("Admission")] = pd.to_datetime(lm.loc[:, ("Admission")])
       lm.loc[:, ("Dimission")] = pd.to_datetime(lm.loc[:, ("Dimission")])

       lm.sort_values(by=['Admission', 'Dimission'], inplace=True)

       lm_final = lm[(lm['Admission'] >= date1) & (lm['Admission'] <= date2) & 
                     (lm['Dimission'] >= date1) & (lm['Dimission'] <= date2)]


       cg = cg.query("Age == '1*'")
       cg = cg.query("Gender == 'M'")

       cg["Admission"] = pd.to_datetime(cg.Admission)
       cg["Dimission"] = pd.to_datetime(cg.Dimission)

       cg.sort_values(by=['Admission', 'Dimission'], inplace=True)

       cg_final = cg[(cg['Admission'] >= date1) & (cg['Admission'] <= date2) & 
                     (cg['Dimission'] >= date1) & (cg['Dimission'] <= date2)]



       uv = uv.query("Age == '1*'")
       uv = uv.query("Gender == 'M'")

       uv["Admission"] = pd.to_datetime(uv.Admission)
       uv["Dimission"] = pd.to_datetime(uv.Dimission)

       uv.sort_values(by=['Admission', 'Dimission'], inplace=True)

       uv_final = uv[(uv['Admission'] >= date1) & (uv['Admission'] <= date2) & 
                     (uv['Dimission'] >= date1) & (uv['Dimission'] <= date2)]
       
       return lm_final, cg_final, uv_final


date1 = '2021-10-04'
date2 = '2021-10-06'

lm , cg , uv = seekAlex(date1, date2)

print("\nCENTRO DIAGNOSTICO RITA LEVI-MONTALCINI")
print(lm)
lm.to_csv("data/filtered_levi-montalcini.csv", index=False)

print("\nCENTRO DIAGNOSTICO CAMILLO GOLGI")
print(cg)
cg.to_csv("data/filtered_camillo-golgi.csv", index=False)

print("\nCENTRO DIAGNOSTICO UMBERTO VERONESI")
print(uv)
uv.to_csv("data/filtered_umberto-veronesi.csv", index=False)
