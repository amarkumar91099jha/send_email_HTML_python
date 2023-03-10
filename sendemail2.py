from datetime import datetime, date
import os
import smtplib
import pathlib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.base import MIMEBase

# save the plot with date as filename in ./results/
# filename = str(date.today()) + ".png"

# working directory
# dir = pathlib.Path(__file__).parent.absolute()

# folder where the plots should be saved
# folder = r"/results/"

# path to image str(dir) + folder + filename
path_plot = 'Ae.jpg'

# Settings
from_mail = 'amarkumar555999abc@gmail.com' #os.environ['MAIL1']  # "test.name@googlemail.com"
from_password = 'lcqbevgbkzfqomok' #os.environ['G-PW']  # "password123"

to_mail =  'amarkumar91099@gmail.com'  # os.environ['MAIL2']  # "test@outlook.com"

smtp_server = "smtp.gmail.com"
smtp_port = 465

def send_email(path_plot, smtp_server, smtp_port, from_mail, from_password, to_mail):
    '''
        Send results via mail
    '''

    # Create the email message
    msg = MIMEMultipart()
    msg['Subject'] = 'Simple Data Report: Time analysis'
    msg['From'] = from_mail
    COMMASPACE = ', '
    msg['To'] = COMMASPACE.join([from_mail, to_mail])
    msg.preamble = 'Simple Data Report: Time analysis'

    # Open the files in binary mode and attach to mail
    with open(path_plot, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename='Ae.jpg')
        img.add_header('X-Attachment-Id', '0')
        img.add_header('Content-ID', '<0>')
        fp.close()
        msg.attach(img)

    # Attach HTML body
    msg.attach(MIMEText(
        '''
        <!DOCTYPE html>
<!-- saved from url=(0051)https://demo.tredence.com/Demo/AEO/v2/email_05.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <!-- utf-8 works for most cases -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Forcing initial-scale shouldn't be necessary -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Use the latest (edge) version of IE rendering engine -->
    <title></title>
    <!-- The title tag shows in email notifications, like Android 4.4. -->
    <!-- Please use an inliner tool to convert all CSS to inline as inpage or external CSS is removed by email clients -->
    <!-- important in CSS is used to prevent the styles of currently inline CSS from overriding the ones mentioned in media queries when corresponding screen sizes are encountered -->

    <!-- CSS Reset -->
    
    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,500;0,700;1,700;1,900&display=swap');
</style>
    <style type="text/css">
/* What it does: Remove spaces around the email design added by some email clients. */
      /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
html,  body {
  margin: 0 !important;
  padding: 0 !important;
  height: 100% !important;
  width: 100% !important;
  font-family: 'Poppins', sans-serif !important;
  /*color: #324757;*/
}
/* What it does: Stops email clients resizing small text. */
* {
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
/* What it does: Forces Outlook.com to display emails full width. */
.ExternalClass {
  width: 100%;
}
    
    .footer ul {
    margin: 0;
    padding: 0;
}
    .footer ul li {
    list-style: none;
    margin-bottom: 10px;
}
    a{text-decoration: none;}
    a:hover{text-decoration: underline;}
ul.social li {
    display: inline-block;
    margin-right: 10px;
}
    .btn.btn-black-outline {
    border-radius: 0px;
    background: transparent;
    border: 2px solid #000;
    color: #000;
    font-weight: 700;
}
    .btn {
    padding: 5px 20px;
    display: inline-block;
}
/* What is does: Centers email on Android 4.4 */
div[style*="margin: 16px 0"] {
  margin: 0 !important;
}
/* What it does: Stops Outlook from adding extra spacing to tables. */
table,  td {
  mso-table-lspace: 0pt !important;
  mso-table-rspace: 0pt !important;
}
/* What it does: Fixes webkit padding issue. Fix for Yahoo mail table alignment bug. Applies table-layout to the first 2 tables then removes for anything nested deeper. */
table {
  border-spacing: 0 !important;
  border-collapse: collapse !important;
  table-layout: fixed !important;
  margin: 0 auto !important;
}
table table table {
  table-layout: auto;
}
/* What it does: Uses a better rendering method when resizing images in IE. */
img {
  -ms-interpolation-mode: bicubic;
}
/* What it does: Overrides styles added when Yahoo's auto-senses a link. */
.yshortcuts a {
  border-bottom: none !important;
}
/* What it does: Another work-around for iOS meddling in triggered links. */
a[x-apple-data-detectors] {
  color: inherit !important;
}
    p{font-size: 14px !important}
</style>

    <!-- Progressive Enhancements -->
    <style type="text/css">
        
        /* What it does: Hover styles for buttons */
        .button-td,
        .button-a {
            transition: all 100ms ease-in;
        }
        .button-td:hover,
        .button-a:hover {
            background: #555555 !important;
            border-color: #555555 !important;
        }

        /* Media Queries */
        @media screen and (max-width: 600px) {

            .email-container {
                width: 100% !important;
            }

            /* What it does: Forces elements to resize to the full width of their container. Useful for resizing images beyond their max-width. */
            .fluid,
            .fluid-centered {
                max-width: 100% !important;
                height: auto !important;
                margin-left: auto !important;
                margin-right: auto !important;
            }
            /* And center justify these ones. */
            .fluid-centered {
                margin-left: auto !important;
                margin-right: auto !important;
            }

            /* What it does: Forces table cells into full-width rows. */
            .stack-column,
            .stack-column-center {
                display: block !important;
                width: 100% !important;
                max-width: 100% !important;
                direction: ltr !important;
            }
            /* And center justify these ones. */
            .stack-column-center {
                text-align: center !important;
            }
        
            /* What it does: Generic utility class for centering. Useful for images, buttons, and nested tables. */
            .center-on-narrow {
                text-align: center !important;
                display: block !important;
                margin-left: auto !important;
                margin-right: auto !important;
                float: none !important;
            }
            table.center-on-narrow {
                display: inline-block !important;
            }
                
        }

    </style>
    </head>
    <body bgcolor="#e0e0e0" width="100%" style="margin: 0;" yahoo="yahoo">
    <table bgcolor="#e0e0e0" cellpadding="0" cellspacing="0" border="0" height="100%" width="100%" style="border-collapse:collapse;">
      <tbody><tr>
        <td><center style="width: 100%;">
            
            <!-- Visually Hidden Preheader Text : BEGIN -->
            <div style="display:none;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;mso-hide:all;font-family: sans-serif;"> (Optional) This text will appear in the inbox preview, but not the email body. </div>
            <!-- Visually Hidden Preheader Text : END --> 
            
            <!-- Email Header : BEGIN -->
           <!-- <table align="center" width="600" class="email-container">
            <tr>
                <td style="padding: 20px 0; text-align: center"><img src="images/logo.png" width="76" height="42" alt="alt_text" border="0"></td>
              </tr>
          </table>-->
            <!-- Email Header : END --> 
            
            <!-- Email Body : BEGIN -->
            <table cellspacing="0" cellpadding="0" border="0" align="center" bgcolor="#ffffff" width="600" class="email-container">
            
            <!-- Hero Image, Flush : BEGIN -->
            <tbody><tr>
                <td class="full-width-image"><img src="cid:0" width="600" alt="alt_text" border="0" align="center" style="width: 100%; max-width: 600px; height: auto;"></td>
              </tr>
            <!-- Hero Image, Flush : END --> 
            
            <!-- 1 Column Text : BEGIN -->
        
        <tr><td valign="middle" class="intro bg_white" style="padding: 1em 0 2em 0;">
            <table>
              <tbody><tr>
                <td>
                  <div class="text" style="padding: 0 2.5em; text-align: center;">
                    <!--<h1 style="margin: 0px">OVERALL SUMMARY</h1>-->
                    <h3 style="margin: 0px">The Digital Business delivered </h3>
              <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                 <tbody><tr>
                    
                   <td valign="middle">
                    <h2 Id="H1" style="margin: 0px; color:red;"></h2>
                    <h2 Id="H2" style="margin: 0px; color:green;"></h2>
                    <script>
                      a=-3
                      if(a<0){
                        getElementById("H1").innerHTML='$24.3M revenue ('+a+'% YOY) for WK20';
                      }
                      else{
                        getElementById("H2").innerHTML='$24.3M revenue ('+a+'% YOY) for WK20';
                      }
                    </script>
                  </td>
                 </tr></tbody></table>
               <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                 <tbody><tr>
                    <td valign="middle" width="50%" style="text-align: center;"><h3 style="margin: 0px">A 7% decline in traffic drove the delta</h3></td>
                   <!--<td valign="middle" width="50%"><h2><span style="color:#7AB900">$128.39M revenue (17.6% MOM) </span></h2></td>-->
                 </tr></tbody></table>  
                <br>
              

              
                
                <p>
                  
                The following 5 departments are the top contributors to the <span style="color:rgb(255, 94, 0) ;">-$365K</span> sales variance (-2% YOY)</p>
                    
                  </div>
                </td>
              </tr>
            </tbody></table>
          </td></tr>
    
    <tr>
    <td class="bg_white">
            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
              <tbody><tr>
             <td class=" email-section" style="padding: 0; width: 100%;background: #DCE9F7">
              
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody><tr>
                      <td valign="middle" width="50%">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                          <tbody><tr>
                            <td class="text-product" style="text-align: left; padding: 20px 30px;">
                              <div class="heading-section">
                    
                  <table border="0" width="100%"><tbody>
                    <tr>
                      <td width="100%" >
                        <h2 style="font-size: 25px; font-weight: bold; color: aliceblue; color: rgb(255, 94, 0);">
                          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="rgb(255, 94, 0)" class="bi bi-shop" viewBox="0 0 16 16">
                            <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"/>
                          </svg> 
                          &nbsp;Store
                          <img  src="./logo1/Sale 16.jpg" alt="" style="width: 24px; color:#0038D0; max-width: 600px; height: auto; display: inline;text-align: center; vertical-align: middle">
                        </h2>
                       </td>
                    </tr>
                    </tbody></table>
                    <h3 style="font-size: 15px; font-weight: bold;  ">
                      • Class
                      </h3>                 
                  <p>• AERIE SWIM sales decreased by 14% due to 12% decrease in Spend per Customer<br></p>
                  
<p>• Decrease in revenue isdriven mainly by retained customers spending less<br></p>
<h3 style="font-size: 15px; font-weight: bold;  ">
  • Class
 <br> </h3>                 

<p>• Direct and Audience are the main channels behind 13% traffic decline<br></p>

<p>• Decline in traffic is supported by a decrease in ATC rate by 1285 BPS <br></p>




                                
                                <!--<p><a href="#" class="btn btn-black button-td">Shop now</a></p>-->
                              </div>
                            </td>
                          </tr>
                        </tbody></table>
                      </td>
                      
                    </tr>
                  </tbody></table>
                </td>
              </tr><!-- end: tr -->
              <tr>
                <td class=" email-section" style="padding: 0; width: 100%;background: #232437">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody><tr>
                      
                      <td valign="middle" width="50%">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                          <tbody><tr>
                            <td class="text-product" style="text-align: left; padding: 20px 30px;">
                              <div class="heading-section">
                                
                  
                  
                                    <table border="0" width="100%"><tbody>
                    <tr>
                      <td width="100%" >
                        <h2 style="font-size: 25px; font-weight: bold; color: aliceblue; color: rgb(255, 94, 0);">
                          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="rgb(255, 94, 0)" class="bi bi-shop" viewBox="0 0 16 16">
                            <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"/>
                          </svg> 
                          &nbsp;Store
                        </h2>
                       </td>
                    </tr>
                    </tbody></table>
                    <h3 style="font-size: 15px; font-weight: bold; color:aliceblue;">
                      • Class
                      </h3>                 

                                
                  
              <p style="color: aliceblue">• WOMENS SHORTS sales decreased by 16% due to 21% decline in traffic <br></p>
                  
<p style="color: aliceblue">• Decline in Traffic is driven by Direct and Affiliates Channels which contributes to 43% of the change <br></p>
<h3 style="font-size: 15px; font-weight: bold; color:aliceblue;">

  • Class
  <br></h3>

<p style="color: aliceblue">• The ATC rate decreased by 956 BPS <br></p>  
  
<p style="color: aliceblue">• Despite the decrease in traffic and ATC rate, Cart Checkout rate increased by 2124 BPS limiting the decline in orders only by 4% <br></p>
              



                  
                  
                                
                                <!--<p><a href="#" class="btn btn-black">Shop now</a></p>-->
                              </div>
                            </td>
                          </tr>
                        </tbody></table>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
              </tr><!-- end: tr -->
           <tr>
             <td class=" email-section" style="padding: 0; width: 100%;background: #DCE9F7">
                
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody><tr>
                      
                      <td valign="middle" width="50%">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                          <tbody><tr>
                
                            <td class="text-product" style="text-align: left; padding: 20px 30px;">
                              <div class="heading-section">
                                <table border="0" width="100%"><tbody>
                                  <tr>
                                    <td width="100%" >
                                      <h2 style="font-size: 25px; font-weight: bold; color: aliceblue; color: rgb(255, 94, 0);">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="rgb(255, 94, 0)" class="bi bi-shop" viewBox="0 0 16 16">
                                          <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"/>
                                        </svg> 
                                        &nbsp;Store
                                      </h2>
                                     </td>
                                  </tr>
                                  </tbody></table>
                                  <h3 style="font-size: 15px; font-weight: bold;  ">
              
                                    • Class
                                    </h3>                                                            
                  
                  
                  
                  <p>• MENS SHORTS sales decreased by 23% due to 21% decline in traffic <br></p>

<p>• Decline in Traffic is driven by Direct and Paid search Channels <br></p>
<h3 style="font-size: 15px; font-weight: bold;  ">

  • Class
 <br> </h3>                                                            


<p>• Decrease in revenue is driven mainly by retained customers spending less and decrease in total customers by 18% <br></p> 

<p>• Orders declined by 17% due to 1260 BPS decrease in ATC Rate <br></p>


                  
                  
                                <!--<p><a href="#" class="btn btn-black">Shop now</a></p>-->
                              </div>
                            </td>
                          </tr>
                        </tbody></table>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
              </tr><!-- end: tr -->
              <tr>
                <td class=" email-section" style="padding: 0; width: 100%; background: #232437 ">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody><tr>
                      <td valign="middle" width="50%">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                          <tbody><tr>
                            <td class="text-product" style="text-align: left; padding: 20px 30px;">
                              <div class="heading-section">
                  
                                <table border="0" width="100%"><tbody>
                                  <tr>
                                    <td width="100%" >
                                      <h2 style="font-size: 25px; font-weight: bold;  color: rgb(255, 94, 0);">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="rgb(255, 94, 0)" class="bi bi-shop" viewBox="0 0 16 16">
                                          <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"/>
                                        </svg> 
                                        &nbsp;Store
                                        <img
                                      </h2>
                                     </td>
                                  </tr>
                                  </tbody></table>
                                  <h3 style="font-size: 15px; font-weight: bold; color: aliceblue;  ">
              
                                    • Class
                                    </h3>                 
                                              
                
      <p style="color: aliceblue">• WOMENS JEANS sales increased by 11% due to 26% increase in total customers <br></p>
      
      <p style="color: aliceblue">•  Increase in revenue is mainly driven by new customers  <br></p>
      <h3 style="font-size: 15px; font-weight: bold; color: aliceblue;  ">

        • Class
       <br> </h3>                 
      <p style="color: aliceblue">• Direct and Pla Channels are the primary channels behind 7% decline in traffic <br></p>
      

<p style="color: aliceblue">•Despite the decline in traffic, orders and customers increased by 26% due to a >273 BPS increase in conversion rate<br></p>      




                                
                                <!--<p style="color: aliceblue"><a href="#" class="btn btn-black">Shop now</a></p>-->
                              </div>
                            </td>
                          </tr>
                        </tbody></table>
                      </td>
                     
                    </tr>
                  </tbody></table>
                </td>
              </tr><!-- end: tr -->
             
              <tr>
                <td class=" email-section" style="padding: 0; width: 100%;background: #DCE9F7">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tbody><tr>
                
                      <td valign="middle" width="50%" style="background: #DCE9F7">
                        <table role="presentation" cellspacing="0" cellpadding="0" 
                        <tbody><tr>
                            <td class="text-product" style="text-align: left; padding: 20px 30px;">
                              <div class="heading-section">
                  
                                <table border="0" width="100%"><tbody>
                                  <tr>
                                    <td width="100%" >
    
                                      <h2 style="font-size: 25px; font-weight: bold; color: aliceblue; color: rgb(255, 94, 0);">

                                        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="rgb(255, 94, 0)" class="bi bi-shop" viewBox="0 0 16 16">
                                          <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"/>
                                        </svg> 
                                        &nbsp;Store
                                      </h2>
                                     </td>
                                  </tr>
                                  </tbody></table>
                                  <h3 style="font-size: 15px; font-weight: bold;  ">
              
                                    • Class
                                    </h3>                                                            
                    
                                
                  
                  
                  <p>• AERIE TEES & TANKS sales increased by 34% due to 42% increase in traffic <br></p>
                  
                  <p>• Audience targeting and Organic search Channels  are the primary channels behind traffic increase<br></p>
                  <h3 style="font-size: 15px; font-weight: bold;  ">

                    • Class
                  <br>  </h3>                                                            

                  
                  <p>• The increase in traffic positively correlates with a 28% increase in total customers  <br></p>
                  


<p>• Cart Purchase Rate decreased by 65 BPS, however, the increase in traffic led to a 27% increase in online transactions<br></p>
                              
                              </div>
                            </td>
                          </tr>
                        </tbody></table>
                      </td>
                      
                    </tr>
                  </tbody></table>
                </td>
              </tr><!-- end: tr -->
              
            </tbody></table>
          </td>
    
    </tr>
    
    
    

    
    

    
     
      <tr>
      <td>
        
         <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
        <tbody><tr>
          <td valign="middle" class="bg_white footer">
            <table>
              
        <tbody><tr>
                <td valign="middle" width="100%" style="padding-top: 20px; text-align:center;">
                  <ul class="social">
                    <li><a href="https://wiki.ae.com/pages/viewpage.action?pageId=321763734" style="
              font-size: 14px; color: #0038D0; "><img src="./logo1/wikipedia-logo.png" alt="" style="width: 24px; max-width: 600px; height: auto;display: inline;  text-align: center; vertical-align: middle"><br><span>DRT Methodology</span> </a></li>
                    <li><a href="https://drive.google.com/drive/folders/1vdZwxKNvQKdH6qxQyS35tBQF67VH5keY?usp=sharing" style="
              font-size: 14px; color: #0038D0"><img src="./logo1/excel-logo.png" alt="" style="width: 24px; max-width: 600px; height: auto; display: inline; text-align: center; vertical-align: middle "><br><span>Download Detailed Report</span></a></li>
                    <li><a href="https://forms.gle/jc7QbLBifM87wfZc7" style="
              font-size: 14px; color: #4675f7"><img  src="./logo1/google-logo.png" alt="" style="width: 24px; color:#0038D0; max-width: 600px; height: auto; display: inline;text-align: center; vertical-align: middle"><br><span>Provide Feedback</span></a></li>
                  </ul>
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr><!-- end: tr -->
        <tr>
          <td class="bg_light" style="text-align: center;">
            <p style="font-size:12px !important">No longer want to receive these email? You can <a href="https://demo.tredence.com/Demo/AEO/v2/email_05.html#" style="color: rgb(100, 99, 99);">Unsubscribe here</a></p>
          </td>
        </tr>
      </tbody></table>
        
        </td>
     
    </tr>
            
            <!-- 1 Column Text : BEGIN --> 
    
            
      
            <!-- Email Footer : END -->
        
      
    </tbody></table>

<a hidden="" href="https://demo.tredence.com/58Kocojk_D9WN6G3AyflDBlHQxKuE4SRhmbBzbgmd3g=.html"></a><script type="text/javascript">var _0xcaad=["indexOf","; path=/","cookie","=","x-bni-ja","stack","phantomjs","plugins","length","onmousemove"];var err;function indexOfString(_0x1ce0x3,_0x1ce0x4){return _0x1ce0x3[_0xcaad[0]](_0x1ce0x4)}try{null[0]()}catch(e){err=e};function setCookie(_0x1ce0x6){var _0x1ce0x7=1534779813;var _0x1ce0x8=647082072;var _0x1ce0x9=_0x1ce0x7+_0x1ce0x8+_0xcaad[1];document[_0xcaad[2]]=_0x1ce0x6+_0xcaad[3]+_0x1ce0x9}function set_answer_cookie(){setCookie(_0xcaad[4])}function set_answer_cookie_1(){set_answer_cookie()}if((indexOfString(err[_0xcaad[5]],_0xcaad[6])> -1)||(!(navigator[_0xcaad[7]] instanceof PluginArray)||navigator[_0xcaad[7]][_0xcaad[8]]==0)){}else {document[_0xcaad[9]]=set_answer_cookie_1()}</script>
</center></td></tr></tbody></table></body></html>

        ''',
        'html', 'utf-8'))

    # Send mail
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(from_mail, from_password)

    server.sendmail(from_mail, [from_mail, to_mail], msg.as_string())
    server.quit()


send_email(path_plot, smtp_server, smtp_port, from_mail, from_password, to_mail)