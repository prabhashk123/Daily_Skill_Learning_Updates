
import pandas as pd
import win32com.client as win32
import open_files,offboarding

#Email 
outlook = win32.Dispatch('outlook.Application') # Create a Outlook Instance
mail = outlook.CreateItem(0) # Create Mail Message Item

too=pd.read_excel(open_files.to_cc_file_path,sheet_name="offboarding_to")
too = too["TO"]
list4 = []
for i in range(len(too)):
    rep = too[i]
    list4.append(rep)
list5= set(list4)
mail.To = ";".join(list5)

cc=pd.read_excel(open_files.to_cc_file_path, sheet_name="offboarding_cc")
cc = cc['CC'].values
list = []
for i in range(len(cc)):
    rep = cc[i]
    list.append(rep)
list1= set(list)
mail.CC = ";".join(list1)

mail.Subject = "IMPORTANT !!! Mandate to share Offboarding notifications 2 weeks prior to the end date"


body = '''<html>
<head>
<style>

</style>
</head>
<body>

Hi All, <br><br> As per the internal protocol all off-boarding notifications need to be sent to the central
team <b>2 WEEKS PRIOR TO THE END DATE</b>. However, only <mark>{:0.2f} %</mark> of notifications received with 
2 weeks of notice,<mark> {:0.2f} %</mark> of notifications received with 1 to 2 weeks of notice and 
<mark>{:0.2f} % </mark>of notifications received less than 1 week of notice. <br><br>
Bank is closely monitoring the offboarding projections and they are not able to report accurate numbers due
to short notice on notifications. <br><br><b>Going forward without proper justification and approval email 
from Rama / Raj, we will not close the work order without 2 weeks of notification. In such scenarios project
team will need to get a revised offboarding approval E-mail from ITP with 2 weeks of notice.</b> <br><br>Only 
exception can be consider for SOW movement, Onsite Quit and BGC/Compliance/HR actions cases. <br><br>Please 
notify the Onsite team accordingly.<br> <br> Please find below summary of last three months ({} – {}) excluding Admin Movement.  <br><br> 
<table>{}
</table><br><b>Thanks & Regards 
<br>
    BOFA Operations Team</br></b>
</body>
</html>
'''.format(offboarding.bet,offboarding.greter,offboarding.less,offboarding.last_last_month.strftime("%b"),offboarding.last_month.strftime("%b"),offboarding.dff.to_html().replace('<th>','<th style= "background-color:#90CAF9">' ).replace('<tr>','<tr style= "background-color:white">' ))
mail.HTMLBody = body 

# mail.HTMLBody = "Hi All, <br><br> As per the internal protocol all off-boarding notifications need to be sent to the central team <b>2 WEEKS PRIOR TO THE END DATE</b>. However, only <mark>12 %</mark> of notifications received with 2 weeks of notice,<mark> 24 %</mark> of notifications received with 1 to 2 weeks of notice and <mark>64 % </mark>of notifications received less than 1 week of notice. <br><br>Bank is closely monitoring the offboarding projections and they are not able to report accurate numbers due to short notice on notifications. <br><br><b>Going forward without proper justification and approval email from Rama / Raj, we will not close the work order without 2 weeks of notification. In such scenarios project team will need to get a revised offboarding approval E-mail from ITP with 2 weeks of notice.</b> <br><br>Only exception can be consider for SOW movement, Onsite Quit and BGC/Compliance/HR actions cases. <br><br>Please notify the Onsite team accordingly.<br> <br> Please find below summary of last three months (Feb – Apr) excluding Admin Movement.  <br><br>   " 
# attach=f"C:\\Users\\atharva.kabra\\OneDrive - Infosys Limited\Desktop\\ofboarding\\Attachment{datetime.datetime.now().date()}.xlsx"
mail.Attachments.Add(offboarding.output_file_path)
mail.Attachments.Add(offboarding.Pivot_file_path)
mail.Display()